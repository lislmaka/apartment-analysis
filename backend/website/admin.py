from django.contrib import admin
from website.models import Avito
from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.


class WebsiteAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "address",
        "price",
        "etazh_val",
        "etazh_count",
        "kolichestvo_komnat",
        "obshchaya_ploshchad",
        "short_god_postroyki",
        "short_kapremont_date",
    ]

    formfield_overrides = {
        # models.CharField: {"widget": TextInput(attrs={"size": "5"})},
        # models.IntegerField: {"widget": TextInput(attrs={"size": "10"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 4, "cols": 40})},
    }
    list_filter = ["status", "source_from"]
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


admin.site.register(Avito, WebsiteAdmin)
# Register your models here.
