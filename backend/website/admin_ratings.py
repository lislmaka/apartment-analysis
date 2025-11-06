

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
    return round(sum(rls), 2)


def calculate_rating_infrastructure(flat):
    """
    Расчет рейтинга инфраструктуры
    """
    rls = []

    # Есть ли рядом магазин
    distance = 500
    flag_magazin = False
    distance_mags_lst = []
    if flat.to_magazin and int(flat.to_magazin) <= distance:
        distance_mags_lst.append(int(flat.to_magazin))
        flag_magazin = True
    if flat.to_pyaterochka and int(flat.to_pyaterochka) <= distance:
        distance_mags_lst.append(int(flat.to_pyaterochka))
        flag_magazin = True
    if flat.to_magnit and int(flat.to_magnit) <= distance:
        distance_mags_lst.append(int(flat.to_magnit))
        flag_magazin = True

    if flag_magazin:
        rls.append(sum([formula_morma(i, distance) for i in distance_mags_lst]))
    else:
        rls.append(0)

    # Есть ли рядом остановка
    flag_bus_stop = False
    if flat.to_bus_stop and int(flat.to_bus_stop) <= distance:
        rls.append(formula_morma(int(flat.to_bus_stop), distance))
        flag_bus_stop = True
    else:
        rls.append(0)


    # Есть ли рядом какой-то пункт выдачи товаров
    flag_delivery = False
    distance_delivery_lst = []
    if flat.to_ozon and int(flat.to_ozon) <= distance:
        distance_delivery_lst.append(int(flat.to_ozon))
        flag_delivery = True
    if flat.to_wildberries and int(flat.to_wildberries) <= distance:
        distance_delivery_lst.append(int(flat.to_wildberries))
        flag_delivery = True
    if flat.to_yandex and int(flat.to_yandex) <= distance:
        distance_delivery_lst.append(int(flat.to_yandex))
        flag_delivery = True

    if flag_delivery:
        rls.append(sum([formula_morma(i, distance) for i in distance_delivery_lst]))
    else:
        rls.append(0)

    # # Учет не основных показетелей
    # if flat.to_apteka and int(flat.to_apteka) <= distance:
    #     rls.append(formula_morma(int(flat.to_apteka), distance))
    # else:
    #     rls.append(0)

    # # to_bolnitsa 
    # if flat.to_bolnitsa and int(flat.to_bolnitsa) <= distance:
    #     rls.append(formula_morma(int(flat.to_bolnitsa), distance))
    # else:
    #     rls.append(0)

    # # to_pochta 
    # if flat.to_pochta and int(flat.to_pochta) <= distance:
    #     rls.append(formula_morma(int(flat.to_pochta), distance))
    # else:
    #     rls.append(0)

    # # to_bank 
    # if flat.to_bank and int(flat.to_bank) <= distance:
    #     rls.append(formula_morma(int(flat.to_bank), distance))
    # else:
    #     rls.append(0)


    if flag_magazin and flag_delivery and flag_bus_stop:
        # Учет не обяхательных гаправлений только при условии что все обязательные есть
        # Есть ли рядом аптека
        if flat.to_apteka and int(flat.to_apteka) <= distance:
            rls.append(formula_morma(int(flat.to_apteka), distance))
        else:
            rls.append(0)

        # to_bolnitsa 
        if flat.to_bolnitsa and int(flat.to_bolnitsa) <= distance:
            rls.append(formula_morma(int(flat.to_bolnitsa), distance))
        else:
            rls.append(0)

        # to_pochta 
        if flat.to_pochta and int(flat.to_pochta) <= distance:
            rls.append(formula_morma(int(flat.to_pochta), distance))
        else:
            rls.append(0)

        # to_bank 
        if flat.to_bank and int(flat.to_bank) <= distance:
            rls.append(formula_morma(int(flat.to_bank), distance))
        else:
            rls.append(0)

    return round(sum(rls), 2)
