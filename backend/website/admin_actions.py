import csv
from django.http import HttpResponse


def action_export_csv(queryset):
    """Action export to csv"""
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


def action_make_active(queryset):
    """Make flat active"""
    for flat in queryset:
        flat.status = True
        flat.save()


def action_make_inactive(queryset):
    """Make flat inactive"""
    for flat in queryset:
        flat.status = False
        flat.save()
