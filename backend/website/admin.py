import csv
import datetime
import json
from django.contrib import admin
from django.http import HttpResponse
from website.serializers import WebsiteSerializer
from website.models import Avito
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html

import website.admin_helpers as myutils
import website.admin_actions as aa
from website.admin_ratings import (
    calculate_rating_infrastructure,
    calculate_rating_flat,
    calculate_rating_house,
)
from django.contrib.admin.models import LogEntry
from django.db.models import Count
from django.contrib.admin import DateFieldListFilter


class LinkTypeFilter(admin.SimpleListFilter):
    title = ""
    parameter_name = "link_type"
    template = "admin/hidden_filter.html"

    def lookups(self, request, model_admin):
        return ((request.GET.get(self.parameter_name), ""),)

    def queryset(self, request, queryset):
        return queryset


class WebsiteAdmin(admin.ModelAdmin):
    # class Media:
    #     js = ("js/admin_overrides.js",)
    class Media:
        js = ("js/copy.js",)

    show_facets = admin.ShowFacets.ALWAYS
    list_display = [
        "show_info",
        "price",
        # "show_etazh_val",
        # "show_kolichestvo_komnat",
        # "show_obshchaya_ploshchad",
        # "show_god_postroyki",
        # "short_kapremont_date",
        # "show_to_kapremont",
        # "show_rating_infrastructure",
        # "show_rating_house",
        # "show_rating_flat",
        "show_rating_all",
        "is_active",
        # "date_update",
        "show_img",
    ]
    save_on_top = True
    list_display_links = None
    readonly_fields = [
        "is_kapremont",
        "is_new_lift",
        "is_kuxnya",
        "is_tualet",
        "is_vana",
        "is_balkon",
        "is_neighbors_around",
        "is_neighbors_top",
        "is_door",
        "is_no_stupenki",
        "is_musoroprovod",
        "kapremont_diff",
        "lift_diff",
        "address",
        "rating_infrastructure",
        "rating_house",
        "rating_flat",
        "rating_all",
        "url",
    ]
    actions = [
        "action_export_csv",
        "action_export_info",
        "make_inactive",
        "make_active",
        "recalc_all_ratings",
    ]

    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": "10"})},
        models.FloatField: {"widget": TextInput(attrs={"size": "10"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 5, "cols": 30})},
    }
    list_filter = [
        "status",
        "record_status",
        "review_results",
        "district",
        "source_from",
        LinkTypeFilter,
        ("date_update", DateFieldListFilter),
    ]
    search_fields = ["id", "address"]

    fieldsets = [
        (
            "Общяя информация",
            {
                "fields": [
                    ("address",),
                    ("url",),
                    (
                        "rating_infrastructure",
                        "rating_house",
                        "rating_flat",
                        "rating_all",
                    ),
                    (
                        "review_results",
                        "record_status",
                    ),
                    ("price", "god_postroyki", "gkx_payments", ),
                    ("file_img", "file_video")
                ],
            },
        ),
        (
            "Дом (рейтинг)",
            {
                "fields": [
                    (
                        # "is_kapremont",
                        # "is_new_lift",
                        "is_no_stupenki",
                        "is_musoroprovod",
                    ),
                    ("no_stupenki", "musoroprovod"),
                    # ("god_postroyki", "gkx_payments"),
                    (
                        "is_kapremont",
                        "kapremont_date",
                        "kapremont_diff",
                    ),
                    (
                        "is_new_lift",
                        "lift_date",
                        "lift_diff",
                    ),
                ],
            },
        ),
        (
            "Квартира (рейтинг)",
            {
                "fields": [
                    (
                        "is_kuxnya",
                        "is_tualet",
                        "is_vana",
                        "is_balkon",
                        "is_neighbors_around",
                        "is_neighbors_top",
                        "is_door",
                    ),
                    ("neighbors_around", "neighbors_top", "tambur", "door"),
                    ("kuxnya", "tualet", "vana", "balkon"),
                ],
            },
        ),
        (
            "Инфраструктура (рейтинг)",
            {
                "fields": [
                    (
                        "to_magazin",
                        "to_pyaterochka",
                        "to_magnit",
                        "to_bus_stop",
                        "to_ozon",
                        "to_wildberries",
                        "to_yandex",
                    ),
                    (
                        # "to_magazin",
                        # "to_pyaterochka",
                        # "to_magnit",
                        "to_bolnitsa",
                        "to_pochta",
                        "to_bank",
                        "to_apteka",
                        # "to_bus_stop",
                        # "to_ozon",
                        # "to_wildberries",
                        # "to_yandex",
                    ),
                ],
            },
        ),
        (
            "Дополения и замечания в свободной форме",
            {
                "fields": [
                    ("description", "description_minus"),
                ],
            },
        ),
        (
            "Информация о квартире",
            {
                "fields": [
                    (
                        "district",
                        "tip_doma",
                        # "price",
                        "kolichestvo_komnat",
                        "obshchaya_ploshchad",
                        "etazh_val",
                        "etazh_count",
                        # "god_postroyki",
                        # "kapremont_date",
                    ),
                ],
            },
        ),
    ]

    #
    def changelist_view(self, request, extra_context=None):
        # queryset = Avito.objects.all()
        # serializer = WebsiteSerializer(queryset, many=True)

        # # Serialize and attach the chart data to the template context
        # as_json = json.dumps(list(serializer.data))
        status = Avito.objects.values("record_status").annotate(
            count=Count("record_status")
        )

        status_labels = dict(Avito.RECORD_STATUS_CHOICES)
        status_data = [["Status", "Count", {"role": "style"}]]

        for row in status:
            status_data_color = "#e6e6e6"
            if row["record_status"] == "6":
                status_data_color = "#00e600"
            status_data.append(
                [status_labels[row["record_status"]], row["count"], status_data_color]
            )
        status_data = json.dumps(status_data)

        link_type = request.GET.get("link_type", "")
        history = LogEntry.objects.order_by("-action_time").distinct()[:20]
        history_lst = []
        for row in history:
            if row.object_id not in history_lst:
                history_lst.append(row.object_id)

        extra_context = extra_context or {
            "link_type": link_type,
            "history": history_lst[:5],
            "status": status_data,
        }

        return super().changelist_view(
            request,
            extra_context=extra_context,
        )

    # Удалить sction delete selected
    # Потом можно вернуть
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def show_god_postroyki(self, instance):
        return instance.god_postroyki

    show_god_postroyki.short_description = "Год"
    show_god_postroyki.admin_order_field = "god_postroyki"

    # def show_rating_infrastructure(self, instance):
    #     return instance.rating_infrastructure

    # show_rating_infrastructure.short_description = "R(И)"
    # show_rating_infrastructure.admin_order_field = "rating_infrastructure"

    # def show_rating_house(self, instance):
    #     return instance.rating_house

    # show_rating_house.short_description = "R(Д)"
    # show_rating_house.admin_order_field = "rating_house"

    # def show_rating_flat(self, instance):
    #     return instance.rating_flat

    # show_rating_flat.short_description = "R(К)"
    # show_rating_flat.admin_order_field = "rating_flat"

    def show_rating_all(self, instance):
        return instance.rating_all

    show_rating_all.short_description = "Рейтинг"
    show_rating_all.admin_order_field = "rating_all"

    def show_url(self, instance):
        return format_html(instance.url)

    def show_to_kapremont(self, instance):
        return instance.kapremont_diff

    show_to_kapremont.short_description = "КЛет"
    show_to_kapremont.admin_order_field = "kapremont_diff"

    def show_kolichestvo_komnat(self, instance):
        return instance.kolichestvo_komnat

    show_kolichestvo_komnat.short_description = "К"
    show_kolichestvo_komnat.admin_order_field = "kolichestvo_komnat"

    # etazh_val
    def show_etazh_val(self, instance):
        return instance.etazh_val

    show_etazh_val.short_description = "Э"
    show_etazh_val.admin_order_field = "etazh_val"

    # obshchaya_ploshchad
    def show_obshchaya_ploshchad(self, instance):
        return instance.obshchaya_ploshchad

    show_obshchaya_ploshchad.short_description = "S"
    show_obshchaya_ploshchad.admin_order_field = "obshchaya_ploshchad"

    #
    def is_active(self, instance):
        return instance.status == 1

    is_active.boolean = True
    is_active.short_description = ""

    # god_postroyki
    def short_god_postroyki(self, instance):
        return instance.god_postroyki

    short_god_postroyki.short_description = "Год"
    short_god_postroyki.admin_order_field = "god_postroyki"

    # kapremont_date
    def short_kapremont_date(self, instance):
        return instance.kapremont_date

    short_kapremont_date.short_description = "КГод"
    short_kapremont_date.admin_order_field = "kapremont_date"

    # show links to maps
    def show_map_to_main_objects(self, instance):
        return myutils.maps(instance=instance)

    show_map_to_main_objects.short_description = "Расстояния"

    def show_info(self, instance):
        return myutils.show_info33(instance=instance)

    show_info.short_description = "Информация"

    def show_img(self, instance):
        return myutils.show_flat_image(instance)

    show_img.short_description = "Фото"

    def action_export_csv(self, request, queryset):
        return aa.action_export_csv(queryset)

    action_export_csv.short_description = "Экспорт CSV Google   "

    def action_export_info(self, request, queryset):
        return aa.action_export_info(queryset)

    action_export_info.short_description = "Экспорт CSV INFO   "

    # Make flat inactive
    def make_inactive(self, request, queryset):
        aa.action_make_inactive(queryset)

    make_inactive.short_description = "Сделать не активными"

    # Make flat active
    def make_active(self, request, queryset):
        aa.action_make_active(queryset)

    make_active.short_description = "Сделать активными"

    # Make flat active
    def recalc_all_ratings(self, request, queryset):
        aa.action_recalc_all_ratings(queryset)

    recalc_all_ratings.short_description = "Пересчитать все рейтинги"

    # class Media:
    #     js = ("js/admin_overrides.js",)

    def save_model(self, request, obj, form, change):
        years = 5
        # kapremont
        if "kapremont_date" in request.POST and request.POST["kapremont_date"]:
            ddiff = int(request.POST["kapremont_date"]) - int(
                datetime.date.today().strftime("%Y")
            )
            obj.kapremont_diff = ddiff
            if ddiff >= years:
                obj.is_kapremont = True
            else:
                obj.is_kapremont = False
        else:
            obj.kapremont_diff = None
            obj.is_kapremont = False

        # lift
        if "lift_date" in request.POST and request.POST["lift_date"]:
            ddiff = int(request.POST["lift_date"]) - int(
                datetime.date.today().strftime("%Y")
            )
            obj.lift_diff = ddiff
            if ddiff >= years or ddiff < 0:
                obj.is_new_lift = True
            else:
                obj.is_new_lift = False
        else:
            obj.lift_diff = None
            obj.is_new_lift = False

        # kuxnya
        if "kuxnya" in request.POST and request.POST["kuxnya"] == "2":
            obj.is_kuxnya = True
        else:
            obj.is_kuxnya = False
        # tualet
        if "tualet" in request.POST and request.POST["tualet"] == "2":
            obj.is_tualet = True
        else:
            obj.is_tualet = False
        # vana
        if "vana" in request.POST and request.POST["vana"] == "2":
            obj.is_vana = True
        else:
            obj.is_vana = False
        # balkon
        if "balkon" in request.POST and request.POST["balkon"] == "2":
            obj.is_balkon = True
        else:
            obj.is_balkon = False
        # neighbors_around
        if (
            "neighbors_around" in request.POST
            and request.POST["neighbors_around"] == "2"
        ):
            obj.is_neighbors_around = True
        else:
            obj.is_neighbors_around = False
        # neighbors_top
        if "neighbors_top" in request.POST and request.POST["neighbors_top"] == "2":
            obj.is_neighbors_top = True
        else:
            obj.is_neighbors_top = False
        # door
        if "door" in request.POST and request.POST["door"] == "2":
            obj.is_door = True
        else:
            obj.is_door = False

        # musoroprovod
        if "musoroprovod" in request.POST and request.POST["musoroprovod"] == "2":
            obj.is_musoroprovod = True
        else:
            obj.is_musoroprovod = False

        # no_stupenki
        if "no_stupenki" in request.POST and request.POST["no_stupenki"] == "3":
            obj.is_no_stupenki = True
        else:
            obj.is_no_stupenki = False

        # calculate rating
        rating_infrastructure = calculate_rating_infrastructure(obj)
        rating_house = calculate_rating_house(obj)
        rating_flat = calculate_rating_flat(obj)
        obj.rating_infrastructure = rating_infrastructure
        obj.rating_house = rating_house
        obj.rating_flat = rating_flat
        obj.rating_all = round(rating_infrastructure + rating_house + rating_flat, 2)

        super().save_model(request, obj, form, change)


admin.site.register(Avito, WebsiteAdmin)
admin.site.site_header = "Анализ квартир"
# Register your models here.
