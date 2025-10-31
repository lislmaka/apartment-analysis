from django.utils.html import format_html


def show_info(instance):
    return format_html(
        """<div>{}<br>{}<br>{}</div>""",
        instance.id,
        instance.title,
        instance.address
    )


def maps(instance):
    to_hospital = format_html(
        """<a href="#"
    onclick="window.open('https://yandex.ru/maps/?rtext={}~{}&rtt=mt',
                         'newwindow',
                         'width=1100,height=700');
              return false;"
 >&rarr; Больница</a>""",
        instance.address,
        "Брянск, проспект Станке Димитрова, 96",
    )

    to_vokzal = format_html(
        """<a href="#"
    onclick="window.open('https://yandex.ru/maps/?rtext={}~{}&rtt=mt',
                         'newwindow',
                         'width=1100,height=700');
              return false;"
 >&rarr; До ЖД</a>""",
        instance.address,
        "Брянск, Речная улица, 2А",
    )

    to_address_on_map = format_html(
        """<a href="#"
    onclick="window.open('https://yandex.ru/maps/?text={}',
                         'newwindow',
                         'width=1100,height=700');
              return false;"
 >&rarr; На карте</a>""",
        instance.address,
    )

    to_avito = format_html(
        """<a href="#"
    onclick="window.open('{}',
                         'newwindow',
                         'width=1100,height=700');
              return false;"
 >&rarr; На Avito</a>""",
        instance.url,
    )
    return format_html(
        """<div>{}<br>{}<br>{}<br>{}</div>""",
        to_hospital,
        to_vokzal,
        to_address_on_map,
        to_avito,
    )
