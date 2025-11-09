import csv
from django.http import HttpResponse

from website.admin_ratings import (
    calculate_rating_flat,
    calculate_rating_house,
    calculate_rating_infrastructure2,
)


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
                round(flat.rating_infrastructure),
                round(flat.rating_house),
                round(flat.rating_flat),
                round(flat.rating_all),
            ]
        )

    return response

def action_export_info(queryset):
    """Action export to csv"""
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=avito_info.csv"
    writer = csv.writer(response)
    # writer.writerow(
    #     [
    #         "Адрес",
    #         "Заголовок",
    #         "Цена",
    #         "URL"
    #     ]
    # )

    for flat in queryset:
        writer.writerow(
            [
                # flat.address,
                # flat.title,
                # flat.price,
                flat.url,
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


def action_recalc_all_ratings(queryset):
    for flat in queryset:
        rating_infrastructure = calculate_rating_infrastructure2(flat)
        rating_house = calculate_rating_house(flat)
        rating_flat = calculate_rating_flat(flat)
        flat.rating_infrastructure = rating_infrastructure
        flat.rating_house = rating_house
        flat.rating_flat = rating_flat
        flat.rating_all = round(rating_infrastructure + rating_house + rating_flat, 2)

        flat.save()
