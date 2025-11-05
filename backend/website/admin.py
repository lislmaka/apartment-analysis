import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
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


class WebsiteAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/admin_overrides.js",)
        
    list_display = [
        "show_info",
        "price",
        "show_etazh_val",
        "show_kolichestvo_komnat",
        "show_obshchaya_ploshchad",
        "show_god_postroyki",
        "short_kapremont_date",
        "show_to_kapremont",
        # "show_rating_infrastructure",
        # "show_rating_house",
        # "show_rating_flat",
        "show_rating_all",
        "is_active",
        "show_img",
    ]
    save_on_top = True
    list_display_links = None
    readonly_fields = [
        "is_kapremont",
        "is_new_lift",
        "kapremont_diff",
        "lift_diff",
        "address",
    ]
    actions = [
        "action_export_csv",
        "make_inactive",
        "make_active",
    ]

    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": "5"})},
        models.FloatField: {"widget": TextInput(attrs={"size": "5"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 5, "cols": 30})},
    }
    list_filter = [
        "status",
        "record_status",
        "review_results",
        "district",
        "source_from",
    ]
    search_fields = ["id", "address"]

    fieldsets = [
        (
            "Общяя информация",
            {
                "fields": [
                    ("address",),
                    (
                        "review_results",
                        "record_status",
                    ),
                ],
            },
        ),
        (
            "Дом (рейтинг)",
            {
                "fields": [
                    (
                        "is_kapremont",
                        "is_new_lift",
                        "is_no_stupenki",
                        "is_musoroprovod",
                    ),
                    (
                        "god_postroyki",
                        "kapremont_date",
                        "kapremont_diff",
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
                    ),
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
                        "to_bolnitsa",
                        "to_pochta",
                        "to_bank",
                        "to_apteka",
                        "to_ozon",
                        "to_wildberries",
                        "to_yandex",
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
                        "price",
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

    def show_rating_infrastructure(self, instance):
        return instance.rating_infrastructure

    show_rating_infrastructure.short_description = "R(И)"
    show_rating_infrastructure.admin_order_field = "rating_infrastructure"

    def show_rating_house(self, instance):
        return instance.rating_house

    show_rating_house.short_description = "R(Д)"
    show_rating_house.admin_order_field = "rating_house"

    def show_rating_flat(self, instance):
        return instance.rating_flat

    show_rating_flat.short_description = "R(К)"
    show_rating_flat.admin_order_field = "rating_flat"

    def show_rating_all(self, instance):
        return instance.rating_all

    show_rating_all.short_description = "R(О)"
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

    short_kapremont_date.short_description = "КР"
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

    action_export_csv.short_description = "Экспорт CSV"

    # Make flat inactive
    def make_inactive(self, request, queryset):
        aa.action_make_inactive(queryset)

    make_inactive.short_description = "Сделать не активными"

    # Make flat active
    def make_active(self, request, queryset):
        aa.action_make_active(queryset)

    make_active.short_description = "Сделать активными"


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

        # lift
        if "lift_date" in request.POST and request.POST["lift_date"]:
            ddiff = int(request.POST["lift_date"]) - int(
                datetime.date.today().strftime("%Y")
            )
            obj.lift_diff = ddiff
            if ddiff >= years:
                obj.is_new_lift = True
            else:
                obj.is_new_lift = False

        # calculate rating
        rating_infrastructure = calculate_rating_infrastructure(obj)
        rating_house = calculate_rating_house(obj)
        rating_flat = calculate_rating_flat(obj)
        obj.rating_infrastructure = rating_infrastructure
        obj.rating_house = rating_house
        obj.rating_flat = rating_flat
        obj.rating_all = rating_infrastructure + rating_house + rating_flat

        super().save_model(request, obj, form, change)


admin.site.register(Avito, WebsiteAdmin)
# Register your models here.
