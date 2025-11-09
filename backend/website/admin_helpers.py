from django.utils.html import format_html


colors = {
    "1": "#f2f2f2",
    "2": "#00e600",
    "3": "#ffb3b3",
    "4": "#e6e600",
}


def show_info33(instance):
    record_status = show_record_status(instance)
    infrastructure_info = show_infrastructure_info(instance)
    house_info = show_house_info(instance)
    flat_info = show_house_flat(instance)
    descriptions = show_description(instance)
    general_info = show_general_info(instance)
    lmaps = maps(instance)

    # display: inline-block; background-color: #f2f2f2; font-size: 12px;
    to_obj = """<div style="">{} {} {} {} {} {} {}</div>""".format(
        lmaps,
        record_status,
        general_info,
        house_info,
        flat_info,
        infrastructure_info,
        descriptions,
    )
    to_obj_html = format_html(to_obj)
    return to_obj_html


def show_item(background_color, title, value, is_copy=False):
    rez = """<span style="
    display: inline-block; 
    background-color: {}; 
    color: black; 
    padding: 3px; 
    margin: 3px;">
    {} {}
    </span>""".format(background_color, title, value)
    if is_copy:
        rez = """<span style="
        display: inline-block; 
        background-color: {}; 
        color: black; 
        padding: 3px; 
        margin: 3px; cursor:pointer;" onclick="copyToClipboard('{}')">
        {} {}
        </span>""".format(background_color, title, title, value)

    return rez


def show_description(instance):
    html_desc = ""
    html_desc_minus = ""
    if instance.description and len(instance.description) > 10:
        html_desc = format_html(
            """<div style="border-left: 5px solid #ccffcc; padding: 5px; margin-bottom:3px;">{}</div>""",
            # """<div style="width: 250px;">{}</div>""",
            format_html(instance.description),
        )

    if instance.description_minus and len(instance.description_minus) > 10:
        html_desc_minus = format_html(
            """<div style="border-left: 5px solid #ffe6e6; padding: 5px;">{}</div>""",
            # """<div style="width: 250px;">{}</div>""",
            format_html(instance.description_minus),
        )
    return format_html("{} {}", html_desc, html_desc_minus)


def calc_item_infrastructure(
    obj,
    title,
    rating_infrastructure,
    rating_infrastructure_deliveris,
    rating_infrastructure_mags,
    distance=500,
):
    background_color = ""
    if obj:
        if int(obj) <= distance and (title in rating_infrastructure):
            background_color = "#00e600"
        elif int(obj) > distance and (title in rating_infrastructure):
            background_color = "#ffb3b3"
        elif int(obj) <= distance:
            background_color = "#b3b3ff"
        else:
            background_color = "#ffe0b3"
        return show_item(background_color, title, obj)
    else:
        if (
            title in rating_infrastructure
            and title not in rating_infrastructure_deliveris
            and title not in rating_infrastructure_mags
        ):
            background_color = "#ffb3b3"
            return show_item(background_color, title, "")
        # elif (
        #     title in rating_infrastructure
        #     and title not in rating_infrastructure_mags
        # ):
        #     background_color = "#ffb3b3"
        #     return show_item(background_color, title, "")
        else:
            return ""


def calc_item_house(obj, title, val):
    text = ""
    if val is not None:
        text = val
    background_color = ""
    if obj:
        background_color = "#00e600"
    else:
        background_color = "#ffb3b3"
    return show_item(background_color, title, text)


def calc_item_flat(obj, title):
    background_color = ""
    if obj:
        background_color = "#00e600"
    else:
        background_color = "#ffb3b3"
    return show_item(background_color, title, "")


def show_house_flat(instance):
    d = {
        "is_kuxnya": {
            "title": "Кухня",
            "instance": instance.kuxnya,
            "rez": None,
        },
        "is_tualet": {
            "title": "Туалет",
            "instance": instance.tualet,
            "rez": None,
        },
        "is_vana": {
            "title": "Ванна",
            "instance": instance.vana,
            "rez": None,
        },
        "is_balkon": {
            "title": "Балкон",
            "instance": instance.balkon,
            "rez": None,
        },
        "is_neighbors_around": {
            "title": "Соседи &#8660;",
            "instance": instance.neighbors_around,
            "rez": None,
        },
        "is_neighbors_top": {
            "title": "Соседи &#8657;",
            "instance": instance.neighbors_top,
            "rez": None,
        },
        "is_door": {
            "title": "Дверь",
            "instance": instance.door,
            "rez": None,
        },
    }
    for item in d:
        # d[item]["rez"] = calc_item_flat(d[item]["instance"], d[item]["title"])
        if d[item]["instance"]:
            d[item]["rez"] = show_item(
                colors[d[item]["instance"]], d[item]["title"], ""
            )
        else:
            d[item]["rez"] = show_item(colors["1"], d[item]["title"], "")

    to_obj = """<div style="">{} {} {} {} {} {} {} {}</div>""".format(
        show_item("#cccccc", "Квартира", ""),
        d["is_kuxnya"]["rez"],
        d["is_tualet"]["rez"],
        d["is_vana"]["rez"],
        d["is_balkon"]["rez"],
        d["is_neighbors_around"]["rez"],
        d["is_neighbors_top"]["rez"],
        d["is_door"]["rez"],
    )
    to_obj_html = format_html(to_obj)

    return format_html(to_obj_html)


def show_house_info(instance):
    d = {
        "is_kapremont": {
            "title": "Капремонт",
            "instance": instance.is_kapremont,
            "val": instance.kapremont_diff,
            "rez": None,
        },
        "is_new_lift": {
            "title": "Лифт",
            "instance": instance.is_new_lift,
            "val": instance.lift_diff,
            "rez": None,
        },
        "is_no_stupenki": {
            "title": "Ступеньки",
            "instance": instance.no_stupenki,
            "val": None,
            "rez": None,
        },
        "is_musoroprovod": {
            "title": "Мусоропровод",
            "instance": instance.musoroprovod,
            "val": None,
            "rez": None,
        },
    }
    for item in d:
        if item == "is_kapremont":
            if d[item]["instance"]:
                d[item]["rez"] = show_item(
                    colors["2"], d[item]["title"], d[item]["val"]
                )
            elif not d[item]["instance"] and instance.kapremont_date:
                d[item]["rez"] = show_item(
                    colors["3"], d[item]["title"], d[item]["val"]
                )
            elif (
                not d[item]["instance"]
                and not instance.kapremont_date
                and instance.record_status != "1"
            ):
                d[item]["rez"] = show_item(colors["4"], d[item]["title"], "")
            else:
                d[item]["rez"] = show_item(colors["1"], d[item]["title"], "")

        elif item == "is_new_lift":
            if d[item]["instance"]:
                d[item]["rez"] = show_item(
                    colors["2"], d[item]["title"], d[item]["val"]
                )
            elif not d[item]["instance"] and instance.lift_date:
                d[item]["rez"] = show_item(
                    colors["3"], d[item]["title"], d[item]["val"]
                )
            elif (
                not d[item]["instance"]
                and not instance.lift_date
                and instance.record_status != "1"
            ):
                d[item]["rez"] = show_item(colors["4"], d[item]["title"], "")
            else:
                d[item]["rez"] = show_item(colors["1"], d[item]["title"], "")
        else:
            # d[item]["rez"] = calc_item_house(
            #     d[item]["instance"], d[item]["title"], d[item]["val"]
            # )
            if d[item]["instance"]:
                d[item]["rez"] = show_item(
                    colors[d[item]["instance"]], d[item]["title"], ""
                )
            else:
                d[item]["rez"] = show_item(colors["1"], d[item]["title"], "")

    to_obj = """<div style="">{} {} {} {} {}</div>""".format(
        show_item("#cccccc", "Дом", ""),
        d["is_kapremont"]["rez"],
        d["is_new_lift"]["rez"],
        d["is_no_stupenki"]["rez"],
        d["is_musoroprovod"]["rez"],
    )
    to_obj_html = format_html(to_obj)

    return format_html(to_obj_html)


def show_infrastructure_info(instance):
    distance = 500
    rating_infrastructure = [
        # "Магазин",
        "Пятерочка",
        "Магнит",
        # "Аптека",
        # "Остановка",
        "Ozon",
        "WB",
        "YM",
    ]
    rating_infrastructure_deliveris = [
        "Ozon",
        "WB",
        "YM",
    ]
    rating_infrastructure_mags = [
        "Пятерочка",
        "Магнит",
    ]
    d = {
        "to_magazin": {
            "title": "Магазин",
            "instance": instance.to_magazin,
            "rez": None,
        },
        "to_pyaterochka": {
            "title": "Пятерочка",
            "instance": instance.to_pyaterochka,
            "rez": None,
        },
        "to_magnit": {
            "title": "Магнит",
            "instance": instance.to_magnit,
            "rez": None,
        },
        "to_bus_stop": {
            "title": "Остановка",
            "instance": instance.to_bus_stop,
            "rez": None,
        },
        "to_bolnitsa": {
            "title": "Больница",
            "instance": instance.to_bolnitsa,
            "rez": None,
        },
        "to_pochta": {
            "title": "Почта",
            "instance": instance.to_pochta,
            "rez": None,
        },
        "to_bank": {
            "title": "Банк",
            "instance": instance.to_bank,
            "rez": None,
        },
        "to_apteka": {
            "title": "Аптека",
            "instance": instance.to_apteka,
            "rez": None,
        },
        "to_ozon": {
            "title": "Ozon",
            "instance": instance.to_ozon,
            "rez": None,
        },
        "to_wildberries": {
            "title": "WB",
            "instance": instance.to_wildberries,
            "rez": None,
        },
        "to_yandex": {
            "title": "YM",
            "instance": instance.to_yandex,
            "rez": None,
        },
    }

    mags_sum = []
    mags_avg = ""
    if d["to_pyaterochka"]["instance"]:
        mags_sum.append(int(d["to_pyaterochka"]["instance"]))
    if d["to_magnit"]["instance"]:
        mags_sum.append(int(d["to_magnit"]["instance"]))
    if mags_sum:
        mags_avg = int(sum(mags_sum) / len(mags_sum))

    delivery_sum = []
    delivery_avg = ""
    if d["to_ozon"]["instance"]:
        delivery_sum.append(int(d["to_ozon"]["instance"]))
    if d["to_wildberries"]["instance"]:
        delivery_sum.append(int(d["to_wildberries"]["instance"]))
    if d["to_yandex"]["instance"]:
        delivery_sum.append(int(d["to_yandex"]["instance"]))
    if delivery_sum:
        delivery_avg = int(sum(delivery_sum) / len(delivery_sum))

    if instance.record_status == "1":
        deliverys_item = show_item(colors["1"], "Доставка", delivery_avg)
        mags_item = show_item(colors["1"], "Сетевые", mags_avg)
        for item in d:
            d[item]["rez"] = calc_item_infrastructure(
                d[item]["instance"],
                d[item]["title"],
                rating_infrastructure,
                rating_infrastructure_deliveris,
                rating_infrastructure_mags,
                distance,
            )
            if (
                d[item]["title"] in rating_infrastructure_deliveris
                and d[item]["rez"]
                and int(d[item]["instance"]) <= distance
            ):
                deliverys_item = show_item("#00e600", "Доставка", delivery_avg)
            if (
                d[item]["title"] in rating_infrastructure_mags
                and d[item]["rez"]
                and int(d[item]["instance"]) <= distance
            ):
                mags_item = show_item("#00e600", "Сетевые", mags_avg)
    elif instance.record_status == "2":
        deliverys_item = show_item(colors["4"], "Доставка", delivery_avg)
        mags_item = show_item(colors["4"], "Сетевые", mags_avg)
        for item in d:
            d[item]["rez"] = calc_item_infrastructure(
                d[item]["instance"],
                d[item]["title"],
                rating_infrastructure,
                rating_infrastructure_deliveris,
                rating_infrastructure_mags,
                distance,
            )
            if (
                d[item]["title"] in rating_infrastructure_deliveris
                and d[item]["rez"]
                and int(d[item]["instance"]) <= distance
            ):
                deliverys_item = show_item("#00e600", "Доставка", delivery_avg)
            if (
                d[item]["title"] in rating_infrastructure_mags
                and d[item]["rez"]
                and int(d[item]["instance"]) <= distance
            ):
                mags_item = show_item("#00e600", "Сетевые", mags_avg)
    else:
        deliverys_item = show_item("#ffb3b3", "Доставка", delivery_avg)
        mags_item = show_item("#ffb3b3", "Сетевые", mags_avg)
        for item in d:
            d[item]["rez"] = calc_item_infrastructure(
                d[item]["instance"],
                d[item]["title"],
                rating_infrastructure,
                rating_infrastructure_deliveris,
                rating_infrastructure_mags,
                distance,
            )
            if (
                d[item]["title"] in rating_infrastructure_deliveris
                and d[item]["rez"]
                and int(d[item]["instance"]) <= distance
            ):
                deliverys_item = show_item("#00e600", "Доставка", delivery_avg)
            if (
                d[item]["title"] in rating_infrastructure_mags
                and d[item]["rez"]
                and int(d[item]["instance"]) <= distance
            ):
                mags_item = show_item("#00e600", "Сетевые", mags_avg)

    to_obj_main = """<div style="">{} {} {}</div>""".format(
        show_item("#cccccc", "Инфраструктура", ""),
        mags_item,
        deliverys_item,
    )
    to_obj_seccond = """<div style="">{} {} {} {} {} {}</div>""".format(
        d["to_magazin"]["rez"],
        d["to_bolnitsa"]["rez"],
        d["to_pochta"]["rez"],
        d["to_bank"]["rez"],
        d["to_apteka"]["rez"],
        d["to_bus_stop"]["rez"],
    )
    to_obj_html = format_html(
        "{} {}", format_html(to_obj_main), format_html(to_obj_seccond)
    )

    return format_html(to_obj_html)


def show_record_status(instance):
    bg_color = "#e6e6e6"
    if instance.record_status == "2":
        bg_color = "#00e600"

    status = show_item(bg_color, instance.get_record_status_display(), "")
    bg_color = "#e6e6e6"
    if instance.review_results == "2":
        bg_color = "#00e600"
    elif instance.review_results == "3":
        bg_color = "#ffb3b3"

    review_results = show_item(bg_color, instance.get_review_results_display(), "")
    return format_html(
        "<div>{} {}</div>", format_html(status), format_html(review_results)
    )


def show_general_info(instance):
    dop_info = []
    dop_info.append(show_item("#e6e6e6", instance.id, "", True))

    address = instance.address.split(",")
    if instance.source_from == "avito":
        dop_info.append(
            # show_item("#e6e6e6", f"{address[-3]}, {address[-2]}, {address[-1]}", "")
            show_item("#e6e6e6", f"{address[-2]}, {address[-1]}", "", True)
        )
    if instance.source_from == "cian":
        dop_info.append(
            # show_item("#e6e6e6", f"{address[2]}, {address[0]}, {address[1]}", "")
            show_item("#e6e6e6", f"{address[0]}, {address[1]}", "", True)
        )

    if instance.district:
        dop_info.append(show_item("#e6e6e6", instance.district, ""))
    if instance.tip_doma:
        dop_info.append(show_item("#e6e6e6", instance.tip_doma.capitalize(), ""))

    if instance.etazh_val:
        dop_info.append(show_item("#e6e6e6", "Этаж", instance.etazh_val))
    if instance.etazh_count:
        dop_info.append(show_item("#e6e6e6", "Этажей", instance.etazh_count))
    if instance.obshchaya_ploshchad:
        dop_info.append(show_item("#e6e6e6", "Площадь", instance.obshchaya_ploshchad))
    if instance.god_postroyki:
        dop_info.append(show_item("#e6e6e6", "Год постройки", instance.god_postroyki))
    return format_html("<div>{}</div>", format_html("".join(map(str, dop_info))))


def show_info(instance):
    html_desc = ""
    html_desc_minus = ""
    dop_info = [instance.id]
    if instance.district:
        dop_info.append(f"р-н {instance.district}")
    if instance.tip_doma:
        dop_info.append(f"{instance.tip_doma.capitalize()}")

    if instance.description and len(instance.description) > 10:
        html_desc = format_html(
            """<div style="border-left: 5px solid #00e600; padding: 5px; margin-bottom:3px;">{}</div>""",
            # """<div style="width: 250px;">{}</div>""",
            instance.description,
        )

    if instance.description_minus and len(instance.description_minus) > 10:
        html_desc_minus = format_html(
            """<div style="border-left: 5px solid #ff944d; padding: 5px;">{}</div>""",
            # """<div style="width: 250px;">{}</div>""",
            instance.description_minus,
        )

    # ------------------------
    to_obj = ""
    to_obj_begin = """<div style="display: flex;">"""

    if instance.to_magazin:
        if int(instance.to_magazin) <= 500:
            to_magazin = f'<span style="background-color: green; color: white; padding: 3px; margin-right: 3px;">Магазин {instance.to_magazin}</span>'
        else:
            to_magazin = f'<span style="background-color: #ffb3b3; color: black; padding: 3px; margin-right: 3px;">Магазин {instance.to_magazin}</span>'
    else:
        to_magazin = ""

    if instance.to_pyaterochka:
        if int(instance.to_pyaterochka) <= 500:
            to_pyaterochka = f'<span style="background-color: green; color: white; padding: 3px; margin-right: 3px;">Пятерочка {instance.to_pyaterochka}</span>'
        else:
            to_pyaterochka = f'<span style="background-color: #ffb3b3; color: black; padding: 3px; margin-right: 3px;">Пятерочка {instance.to_pyaterochka}</span>'
    else:
        to_pyaterochka = ""

    if instance.to_magnit:
        if int(instance.to_magnit) <= 500:
            to_magnit = f'<span style="background-color: green; color: white; padding: 3px; margin-right: 3px;">Магнит {instance.to_magnit}</span>'
        else:
            to_magnit = f'<span style="background-color: #ffb3b3; color: black; padding: 3px; margin-right: 3px;">Магнит {instance.to_magnit}</span>'
    else:
        to_magnit = ""

    if instance.to_bolnitsa:
        if int(instance.to_bolnitsa) <= 500:
            to_bolnitsa = f'<span style="background-color: green; color: white; padding: 3px; margin-right: 3px;">Больница {instance.to_bolnitsa}</span>'
        else:
            to_bolnitsa = f'<span style="background-color: #ffb3b3; color: black; padding: 3px; margin-right: 3px;">Больница {instance.to_bolnitsa}</span>'
    else:
        to_bolnitsa = ""

    if instance.to_pochta:
        if int(instance.to_pochta) <= 500:
            to_pochta = f'<span style="background-color: green; color: white; padding: 3px; margin-right: 3px;">Почта {instance.to_pochta}</span>'
        else:
            to_pochta = f'<span style="background-color: #ffb3b3; color: black; padding: 3px; margin-right: 3px;">Почта {instance.to_pochta}</span>'
    else:
        to_pochta = ""

    if instance.to_bank:
        if int(instance.to_bank) <= 500:
            to_bank = f'<span style="background-color: green; color: white; padding: 3px; margin-right: 3px;">Банк {instance.to_bank}</span>'
        else:
            to_bank = f'<span style="background-color: #ffb3b3; color: black; padding: 3px; margin-right: 3px;">Банк {instance.to_bank}</span>'
    else:
        to_bank = ""

    if instance.to_apteka:
        if int(instance.to_apteka) <= 500:
            to_apteka = f'<span style="background-color: green; color: white; padding: 3px; margin-right: 3px;">Аптека {instance.to_apteka}</span>'
        else:
            to_apteka = f'<span style="background-color: #ffb3b3; color: black; padding: 3px; margin-right: 3px;">Аптека {instance.to_apteka}</span>'
    else:
        to_apteka = ""

    to_obj_end = """</div>"""
    to_obj = (
        to_obj_begin
        + to_magazin
        + to_pyaterochka
        + to_magnit
        + to_bolnitsa
        + to_pochta
        + to_bank
        + to_apteka
        + to_obj_end
    )
    to_obj_html = format_html(to_obj)
    # ------------------------
    to_hospital = format_html(
        """<a href="#"
    onclick="window.open('https://yandex.ru/maps/?rtext={}~{}&rtt=mt',
                         'newwindow',
                         'width=1100,height=700');
              return false;"
 >Больница</a>""",
        instance.address,
        "Брянск, проспект Станке Димитрова, 96",
    )

    to_vokzal = format_html(
        """<a href="#"
    onclick="window.open('https://yandex.ru/maps/?rtext={}~{}&rtt=mt',
                         'newwindow',
                         'width=1100,height=700');
              return false;"
 >До ЖД</a>""",
        instance.address,
        "Брянск, Речная улица, 2А",
    )

    to_address_on_map = format_html(
        """<a href="#"
    onclick="window.open('https://yandex.ru/maps/?text={}',
                         'newwindow',
                         'width=1100,height=700');
              return false;"
 >На карте</a>""",
        instance.address,
    )

    to_avito = format_html(
        """<a href="#"
    onclick="window.open('{}',
                         'newwindow',
                         'width=1100,height=700');
              return false;"
 >На {}</a>""",
        instance.url,
        instance.source_from,
    )
    to_gkh = format_html(
        """<a href="#"
    onclick="window.open('https://my-gkh.ru/houses/searchhouses',
                         'newwindow',
                         'width=1100,height=700');
              return false;"
 >ЖКХ</a>"""
    )
    # ------------------------
    return format_html(
        """<div>{} {} <br> &#8250; {} <br> &#8250; {} &#8250; {} &#8250; {} &#8250; {} &#8250; {} <br> {} {}</div>""",
        # """<div>{} <br> &#8250; {} <br> &#8250; {} &#8250; {} &#8250; {} &#8250; {} &#8250; {}</div>""",
        to_obj_html,
        format_html(" &#8250; ".join(map(str, dop_info))),
        instance.address,
        # district,
        to_hospital,
        to_vokzal,
        to_address_on_map,
        to_avito,
        to_gkh,
        #
        html_desc,
        html_desc_minus,
    )


def maps(instance):
    to_hospital = format_html(
        """<a href="#"
    onclick="window.open('https://yandex.ru/maps/?rtext={}~{}&rtt=mt',
                         '_blank',
                         'width=1100,height=700');
              return false;"
 >Больница</a>""",
        instance.address,
        "Брянск, проспект Станке Димитрова, 96",
    )

    to_vokzal = format_html(
        """<a href="#"
    onclick="window.open('https://yandex.ru/maps/?rtext={}~{}&rtt=mt',
                         '_blank',
                         'width=1100,height=700');
              return false;"
 >ЖД</a>""",
        instance.address,
        "Брянск, Речная улица, 2А",
    )

    to_address_on_map = format_html(
        """<a href="#"
    onclick="window.open('https://yandex.ru/maps/?text={}',
                         '_blank',
                         'width=1100,height=700');
              return false;"
 >Yandex</a>""",
        instance.address,
    )

    to_address_on_map_google = format_html(
        """<a href="#"
    onclick="window.open('https://www.google.com/maps/place/{}',
                         '_blank',
                         'width=1100,height=700');
              return false;"
 >Google</a>""",
        instance.address,
    )

    #     to_address_on_map_google_all = format_html(
    #         """<a href="#"
    #     onclick="window.open('https://www.google.com/maps/d/edit?mid=1CqEeIWmaLPMRzZq0li8Mv9vylvzM9YY&usp=sharing',
    #                          '_blank',
    #                          'width=1100,height=700');
    #               return false;"
    #  >GoogleAll</a>"""
    #     )

    to_avito = format_html(
        """<a href="#"
    onclick="window.open('{}',
                         '_blank',
                         'width=1100,height=700');
              return false;"
 >{}</a>""",
        instance.url,
        instance.source_from.capitalize(),
    )

    to_2gis = format_html(
        """<a href="#"
    onclick="window.open('https://2gis.ru/bryansk/search/{}',
                         '_blank',
                         'width=1100,height=700');
              return false;"
 >2GIS</a>""",
        instance.address,
    )

    #     to_edit = format_html(
    #         """<a href="#"
    #     onclick="window.open('http://localhost:1337/admin/website/avito/{}/change/',
    #                          '_blank',
    #                          'width=1100,height=700');
    #               return false;"
    #  >Edit</a>""",
    #         instance.id,
    #     )

    return format_html(
        """<div>{} {} {} {} {} {}</div>""",
        format_html(show_item("#e6e6e6", to_hospital, "")),
        format_html(show_item("#e6e6e6", to_vokzal, "")),
        format_html(show_item("#e6e6e6", to_avito, "")),
        format_html(show_item("#e6e6e6", to_2gis, "")),
        format_html(show_item("#e6e6e6", to_address_on_map, "")),
        format_html(show_item("#e6e6e6", to_address_on_map_google, "")),
        # format_html(show_item("#e6e6e6", to_address_on_map_google_all, "")),
    )


def show_flat_image(instance):
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

    file_name = f"images/{instance.id}/main.jpg"
    if instance.file_img:
        file_name = instance.file_img
    images_html = '<img src="/public/{}" width="150" height="150" style="padding-bottom: 10px; ">'.format(
        file_name
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
    #     video = format_html(
    #       """<div><a href="#"
    #     onclick="window.open('http://localhost:1337/static/video/video.html',
    #                         '_blank',
    #                         'width=500,height=300');
    #             return false;"
    # >{}</a></div>""",
    #         "Видео",
    #     )
    video = ""
    if instance.file_video:
        video = format_html(
            """<a href="http://localhost:1337/public/{}" target="_blank"">Видео отчет</>""",
            instance.file_video,
        )
    #
    images_html_end = "</div>"
    to_edit = images_html_begin + to_edit + images_html_end + video
    return format_html(to_edit)
