import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from website.models import Avito
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html

import website.admin_helpers as myutils
from website.admin_ratings import (
    calculate_rating_infrastructure,
    calculate_rating_flat,
    calculate_rating_house,
)
import os
import shutil

# Register your models here.


class WebsiteAdmin(admin.ModelAdmin):
    list_display = [
        "show_info",
        # "description",
        # "description_minus",
        "price",
        # "district",
        # "etazh_val",
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
        # "show_map_to_main_objects",
        "show_img",
        # "url_to_img",
    ]
    save_on_top = True
    list_display_links = None
    # list_editable = (
    #     "price",
    #     "etazh_val",
    #     "kolichestvo_komnat",
    #     "obshchaya_ploshchad",
    #     "kapremont_date",
    #     "god_postroyki",
    #     "rating",
    #     "description",
    #     "description_minus",
    # )
    readonly_fields = [
        "is_kapremont",
        "is_new_lift",
        "kapremont_diff",
        "lift_diff",
        "address",
    ]
    actions = [
        "export_to_csv",
        "make_inactive",
        "make_active",
        # "delete_model",
        # "rating_infrastructure",
        # "rating_house",
        # "rating_flat",
        # "calculate_all_ratings",
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

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    # def delete_model(self, request, obj):
    #     # 7564501425
    #     for o in obj.all():
    #         path_file = f"/home/home/my/RepoCode/avito/parser/html/{o.source_from}_{o.pk}.html"
    #         path_dir = f"/home/home/my/RepoCode/avito/backend/website/static/flats/{o.pk}"
    #         print(f"{path_file=}")
    #         print(f"{path_dir=}")
    #         if os.path.exists(path_dir) and os.path.isdir(path_dir):
    #             print("Dir exist")
    #             shutil.rmtree(path_dir)
    #         if os.path.exists(path_file):
    #             print("File exist")
    #             shutil.rmtree(path_file)
    #         o.delete()

    # delete_model.short_description = 'Удалить выбранные записи'

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


    #obshchaya_ploshchad
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
        bg_color = ""
        if instance.review_results == "1":
            bg_color = "background-color: #e6e6e6;"
        elif instance.review_results == "2":
            bg_color = "background-color: #00e600;"
        elif instance.review_results == "3":
            bg_color = "background-color: #ffb3b3;"
        images_html_begin = '<div style="display: flex; justify-content: center; align-items: center; border-radius: 5px; {}">'.format(
            bg_color
        )
        images_html = '<img src="/static/flats/{}/main.jpg" width="200" height="200" style="padding: 10px; ">'.format(
            instance.id
        )
        #
        to_edit = format_html(
            """<a href="#"
        onclick="window.open('http://localhost:1337/admin/website/avito/{}/change/',
                            '_blank',
                            'width=1100,height=700');
                return false;"
    >{}</a>""",
            instance.id,
            format_html(images_html),
        )

        #
        images_html_end = "</div>"
        to_edit = images_html_begin + to_edit + images_html_end
        return format_html(to_edit)

    show_img.short_description = "Фото"

    # def show_img(self, instance):
    #     images_html_begin = '<div style="white-space: nowrap;">'
    #     images_html = '<img src="/static/flats/{}/main.jpg" width="100" height="100" style="padding-right: 3px;">'.format(instance.id)
    #     images_html_end = "</div>"
    #     # for i in range(1, 4):
    #     #     images_html += '<img src="/static/flats/{}/{}.jpg" width="100" height="100" style="padding-right: 3px;">'.format(
    #     #         instance.id, i
    #     #     )
    #     images_html = images_html_begin + images_html + images_html_end
    #     return format_html(images_html)
    # show_img.short_description = "Фото"

    # add extra data to template
    def changelist_view(self, request, extra_context=None):
        # Получаем агрегированные данные (подсчет новых подписчиков по дням)
        extra_context = extra_context or {}
        extra_context["chart_data"] = "Hello ^)"

        # Вызываем базовый метод с расширенным контекстом
        return super().changelist_view(request, extra_context=extra_context)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=avito.csv"
        writer = csv.writer(response)
        writer.writerow(
            [
                "Адрес",
                "Заголовок",
                "ID",
                "Цена",
                "Рейтинг инфраструктуры",
                "Рейтинг дома",
                "Рейтинг квартиры",
                "Рейтинг общий",
            ]
        )

        for flat in queryset:
            writer.writerow(
                [
                    flat.address,
                    flat.title,
                    flat.id,
                    flat.price,
                    flat.rating_infrastructure,
                    flat.rating_house,
                    flat.rating_flat,
                    flat.rating_all,
                ]
            )

        return response

    export_to_csv.short_description = "Экспорт CSV"

    def make_inactive(self, request, queryset):
        for flat in queryset:
            flat.status = False
            flat.save()

    make_inactive.short_description = "Сделать не активными"

    def make_active(self, request, queryset):
        for flat in queryset:
            flat.status = True
            flat.save()

    make_active.short_description = "Сделать активными"

    # def calculate_all_ratings(self, request, queryset):
    #     for flat in queryset:
    #         rating_infrastructure = calculate_rating_infrastructure(flat)
    #         rating_house = calculate_rating_house(flat)
    #         rating_flat = calculate_rating_flat(flat)
    #         flat.rating_infrastructure = rating_infrastructure
    #         flat.rating_house = rating_house
    #         flat.rating_flat = rating_flat
    #         flat.rating_all = rating_infrastructure + rating_house + rating_flat
    #         flat.save()

    # calculate_all_ratings.short_description = "Пересчитать все рейтинги"

    # def rating_infrastructure(self, request, queryset):
    #     for flat in queryset:
    #         flat.rating_infrastructure = calculate_rating_infrastructure(flat)
    #         flat.save()

    # rating_infrastructure.short_description = "Пересчитать рейтинг инфраструктуры"

    # def rating_house(self, request, queryset):
    #     for flat in queryset:
    #         flat.rating_house = calculate_rating_house(flat)
    #         flat.save()

    # rating_house.short_description = "Пересчитать рейтинг дома"

    # def rating_flat(self, request, queryset):
    #     for flat in queryset:
    #         flat.rating_flat = calculate_rating_flat(flat)
    #         flat.save()

    # rating_flat.short_description = "Пересчитать рейтинг квартиры"

    class Media:
        js = ("js/admin_overrides.js",)

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
