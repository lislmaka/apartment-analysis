import os
import sqlite3


def sqlite3_check_if_exist(id):
    connection = sqlite3.connect("db/my_database.db")
    cursor = connection.cursor()

    id = cursor.execute("SELECT id FROM avito WHERE id=?", (id,)).fetchone()

    connection.commit()
    connection.close()

    return bool(id)


def copy_data_row_to_row(id_from, id_to):
    list_fields = [
        "is_no_stupenki",
        "no_stupenki",
        "musoroprovod",
        "is_musoroprovod",
        "kapremont_date",
        "kapremont_diff",
        "is_kapremont",
        "lift_date",
        "lift_diff",
        "is_new_lift",
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
        "to_bus_stop",
    ]

    connection = sqlite3.connect("db/my_database.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    if sqlite3_check_if_exist(id_from):
        fields = ", ".join(list_fields)
        sql = f"select {fields} from avito where id=?"
        fields = cursor.execute(sql, (id_from,)).fetchone()
        fields = dict(fields)
        fields["copy_from_done"] = id_from

        columns = ", ".join([f"{k} = ?" for k in fields.keys()])
        values = list(fields.values())
        values.append(id_to)
        sql = f"UPDATE avito SET {columns} WHERE id = ?"
        # print(sql)
        # print(values)

        cursor.execute(sql, values)
        connection.commit()
    else:
        # print(f"{id=} not exist")
        pass

    connection.close()


def dublicate(dublicate_id, flat):
    if sqlite3_check_if_exist(dublicate_id):
        flat.dublicat_status = "1"
        flat.save()

        
def copy_data_row_to_row2(id_from, id_to, flat):
    list_fields = [
        "is_no_stupenki",
        "no_stupenki",
        "musoroprovod",
        "is_musoroprovod",
        "kapremont_date",
        "kapremont_diff",
        "is_kapremont",
        "lift_date",
        "lift_diff",
        "is_new_lift",
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
        "to_bus_stop",
    ]

    connection = sqlite3.connect("db/my_database.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    if sqlite3_check_if_exist(id_from):
        fields = ", ".join(list_fields)
        sql = f"select {fields} from avito where id=?"
        fields = cursor.execute(sql, (id_from,)).fetchone()
        fields = dict(fields)

        if fields["is_no_stupenki"] and fields["is_no_stupenki"] is not None:
            flat.is_no_stupenki = fields["is_no_stupenki"]
        if fields["no_stupenki"] and fields["no_stupenki"] is not None:
            flat.no_stupenki = fields["no_stupenki"]
        if fields["musoroprovod"] and fields["musoroprovod"] is not None:
            flat.musoroprovod = fields["musoroprovod"]
        if fields["is_musoroprovod"] and fields["is_musoroprovod"] is not None:
            flat.is_musoroprovod = fields["is_musoroprovod"]
        if fields["kapremont_date"] and fields["kapremont_date"] is not None:
            flat.kapremont_date = fields["kapremont_date"]
        if fields["kapremont_diff"] and fields["kapremont_diff"] is not None:
            flat.kapremont_diff = fields["kapremont_diff"]
        if fields["is_kapremont"] and fields["is_kapremont"] is not None:
            flat.is_kapremont = fields["is_kapremont"]
        if fields["lift_date"] and fields["lift_date"] is not None:
            flat.lift_date = fields["lift_date"]
        if fields["lift_diff"] and fields["lift_diff"] is not None:
            flat.lift_diff = fields["lift_diff"]
        if fields["is_new_lift"] and fields["is_new_lift"] is not None:
            flat.is_new_lift = fields["is_new_lift"]
        if fields["to_magazin"] and fields["to_magazin"] is not None:
            flat.to_magazin = fields["to_magazin"]
        if fields["to_pyaterochka"] and fields["to_pyaterochka"] is not None:
            flat.to_pyaterochka = fields["to_pyaterochka"]
        if fields["to_magnit"] and fields["to_magnit"] is not None:
            flat.to_magnit = fields["to_magnit"]
        if fields["to_bolnitsa"] and fields["to_bolnitsa"] is not None:
            flat.to_bolnitsa = fields["to_bolnitsa"]
        if fields["to_pochta"] and fields["to_pochta"] is not None:
            flat.to_pochta = fields["to_pochta"]
        if fields["to_bank"] and fields["to_bank"] is not None:
            flat.to_bank = fields["to_bank"]
        if fields["to_apteka"] and fields["to_apteka"] is not None:
            flat.to_apteka = fields["to_apteka"]
        if fields["to_ozon"] and fields["to_ozon"] is not None:
            flat.to_ozon = fields["to_ozon"]
        if fields["to_wildberries"] and fields["to_wildberries"] is not None:
            flat.to_wildberries = fields["to_wildberries"]
        if fields["to_yandex"] and fields["to_yandex"] is not None:
            flat.to_yandex = fields["to_yandex"]
        if fields["to_bus_stop"] and fields["to_bus_stop"] is not None:
            flat.to_bus_stop = fields["to_bus_stop"]
        flat.copy_from = None
        flat.copy_from_done = id_from
        flat.save()

    connection.close()