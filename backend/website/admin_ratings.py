def calculate_rating_house(flat):
    """
    Расчет рейтинга дома
    """
    rls = []
    if flat.is_kapremont:
        rls.append(1)
    if flat.is_no_stupenki:
        rls.append(1)
    if flat.is_musoroprovod:
        rls.append(1)
    if flat.is_new_lift:
        rls.append(1)
    return sum(rls)


def calculate_rating_flat(flat):
    """
    Расчет рейтинга квартиры
    """
    rls = []
    if flat.is_kuxnya:
        rls.append(1)
    if flat.is_tualet:
        rls.append(1)
    if flat.is_vana:
        rls.append(1)
    if flat.is_balkon:
        rls.append(1)
    return sum(rls)


def calculate_rating_infrastructure(flat):
    """
    Расчет рейтинга инфраструктуры
    """
    rls = []

    # Есть ли рядом магазин
    distance = 500
    flag_magazin = False
    if flat.to_magazin and int(flat.to_magazin) <= distance:
        flag_magazin = True
    if flat.to_pyaterochka and int(flat.to_pyaterochka) <= distance:
        flag_magazin = True
    if flat.to_magnit and int(flat.to_magnit) <= distance:
        flag_magazin = True

    if flag_magazin:
        rls.append(1)
    else:
        rls.append(0)

    # Есть ли рядом аптека
    if flat.to_apteka and int(flat.to_apteka) <= distance:
        rls.append(1)
    else:
        rls.append(0)

    # Есть ли рядом какой-то пункт выдачи товаров
    flag_delivery = False
    if flat.to_ozon and int(flat.to_ozon) <= distance:
        flag_delivery = True
    if flat.to_wildberries and int(flat.to_wildberries) <= distance:
        flag_delivery = True
    if flat.to_yandex and int(flat.to_yandex) <= distance:
        flag_delivery = True

    if flag_delivery:
        rls.append(1)
    else:
        rls.append(0)

    return sum(rls)
