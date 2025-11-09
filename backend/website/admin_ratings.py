

def formula_morma(value, distance):
    return 1 - ((value - 0) / (distance - 0))

def formula_morma2(value, mmin=1970, mmax=2025):
    return (value - mmin) / (mmax - mmin)

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
    if flat.god_postroyki:
        rls.append(formula_morma2(int(flat.god_postroyki)))

    # print("rating house")
    return round(sum(rls), 2)


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
    if flat.is_neighbors_around:
        rls.append(1)
    if flat.is_neighbors_top:
        rls.append(1)
    if flat.is_door:
        rls.append(1)

    # print("rating flat")
    return round(sum(rls), 2)


def calculate_rating_infrastructure2(flat):
    """
    Расчет рейтинга инфраструктуры
    """
    rls = []
    # print("to_magazin= ", flat.to_magazin)
    # print("to_pyaterochka=", flat.to_pyaterochka)
    # print("to_magnit= ", flat.to_magnit)
    # print("to_ozon= ", flat.to_ozon)
    # print("to_wildberries= ", flat.to_wildberries)
    # print("to_yandex= ", flat.to_yandex)
    # print("to_apteka= ", flat.to_apteka)
    # print("to_bolnitsa= ", flat.to_bolnitsa)
    # print("to_pochta= ", flat.to_pochta)
    # print("to_bank= ", flat.to_bank)
    # print("to_bus_stop= ", flat.to_bus_stop)

    # Есть ли рядом магазин
    distance = 500
    flag_magazin = False
    distance_mags_lst = []
    # if int(flat.to_magazin) >= 0 and int(flat.to_magazin) <= distance:
    #     distance_mags_lst.append(int(flat.to_magazin))
    #     flag_magazin = True
    if flat.to_pyaterochka is not None and int(flat.to_pyaterochka) >= 0 and int(flat.to_pyaterochka) <= distance:
        distance_mags_lst.append(int(flat.to_pyaterochka))
        flag_magazin = True
    if flat.to_magnit is not None and int(flat.to_magnit) >= 0 and int(flat.to_magnit) <= distance:
        distance_mags_lst.append(int(flat.to_magnit))
        flag_magazin = True

    if flag_magazin:
        rls.append(sum([formula_morma(i, distance) for i in distance_mags_lst]))
    else:
        rls.append(0)

    print(rls)
    # Есть ли рядом какой-то пункт выдачи товаров
    flag_delivery = False
    distance_delivery_lst = []
    if flat.to_ozon is not None and int(flat.to_ozon) >= 0 and int(flat.to_ozon) <= distance:
        distance_delivery_lst.append(int(flat.to_ozon))
        flag_delivery = True
    if flat.to_wildberries is not None and int(flat.to_wildberries) >= 0 and int(flat.to_wildberries) <= distance:
        distance_delivery_lst.append(int(flat.to_wildberries))
        flag_delivery = True
    if flat.to_yandex is not None and int(flat.to_yandex) >= 0 and int(flat.to_yandex) <= distance:
        distance_delivery_lst.append(int(flat.to_yandex))
        flag_delivery = True

    if flag_delivery:
        rls.append(sum([formula_morma(i, distance) for i in distance_delivery_lst]))
    else:
        rls.append(0)

    print(rls)

    if flag_magazin and flag_delivery:
        # Учет не обяхательных гаправлений только при условии что все обязательные есть
        # Есть ли рядом аптека
        if flat.to_apteka is not None and int(flat.to_apteka) >= 0 and int(flat.to_apteka) <= distance:
            rls.append(formula_morma(int(flat.to_apteka), distance))
        else:
            rls.append(0)

        # to_bolnitsa 
        if flat.to_bolnitsa is not None and int(flat.to_bolnitsa) >= 0 and int(flat.to_bolnitsa) <= distance:
            rls.append(formula_morma(int(flat.to_bolnitsa), distance))
        else:
            rls.append(0)

        # to_pochta 
        if flat.to_pochta is not None and int(flat.to_pochta) >= 0 and int(flat.to_pochta) <= distance:
            rls.append(formula_morma(int(flat.to_pochta), distance))
        else:
            rls.append(0)

        # to_bank 
        if flat.to_bank is not None and int(flat.to_bank) >= 0 and int(flat.to_bank) <= distance:
            rls.append(formula_morma(int(flat.to_bank), distance))
        else:
            rls.append(0)

        # to_bus_stop
        if flat.to_bus_stop is not None and int(flat.to_bus_stop) >= 0 and int(flat.to_bus_stop) <= distance:
            rls.append(formula_morma(int(flat.to_bus_stop), distance))
        else:
            rls.append(0)

    print(f"rating1 = {round(sum(rls), 2)}")
    return round(sum(rls), 2)
