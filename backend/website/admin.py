from django.contrib import admin
from website.models import Avito
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html

import website.admin_helpers as myutils

# Register your models here.


class WebsiteAdmin(admin.ModelAdmin):
    list_display = [
        # "id",
        # "title",
        # "address",
        "show_info",
        "price",
        "etazh_val",
        "etazh_count",
        "kolichestvo_komnat",
        "obshchaya_ploshchad",
        # "short_god_postroyki",
        "god_postroyki",
        # "short_kapremont_date",
        "kapremont_date",
        "show_map_to_main_objects",
        "show_img",
    ]
    save_on_top = True

    list_editable = (
        "price",
        "etazh_val",
        "etazh_count",
        "kolichestvo_komnat",
        "obshchaya_ploshchad",
        "kapremont_date",
        "god_postroyki",
    )
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": "5"})},
        models.FloatField: {"widget": TextInput(attrs={"size": "5"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 4, "cols": 40})},
    }
    # list_filter = ["status", "source_from"]
    search_fields = ["id", "address"]

    # god_postroyki
    def short_god_postroyki(self, instance):
        return instance.god_postroyki

    short_god_postroyki.short_description = "Год"
    short_god_postroyki.admin_order_field = "god_postroyki"

    # kapremont_date
    def short_kapremont_date(self, instance):
        return instance.kapremont_date

    short_kapremont_date.short_description = "Капремонт"
    short_kapremont_date.admin_order_field = "kapremont_date"

    # show links to maps
    def show_map_to_main_objects(self, instance):
        return myutils.maps(instance=instance)

    show_map_to_main_objects.short_description = "Расстояния"

    def show_info(self, instance):
        return myutils.show_info(instance=instance)

    show_info.short_description = "Информация"

    def show_img(self, instance):
        images_html_begin = '<div style="white-space: nowrap;">'
        images_html = ""
        images_html_end = "</div>"
        for i in range(1, 4):
            images_html += '<img src="/static/{}/{}.jpg" width="100" height="100" style="padding-right: 3px;">'.format(
                instance.id, i
            )
        images_html = images_html_begin + images_html + images_html_end
        return format_html(images_html)
    
admin.site.register(Avito, WebsiteAdmin)
# Register your models here.
