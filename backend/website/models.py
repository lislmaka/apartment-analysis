# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Avito(models.Model):
    id = models.BigIntegerField(blank=False, null=False, unique=True, primary_key=True)
    url = models.TextField(blank=True, null=True, verbose_name="Url адрес")
    date_add = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="Дата добавления"
    )
    date_update = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="Дата обновления"
    )
    title = models.TextField(blank=True, null=True, verbose_name="Заголовок")
    price = models.BigIntegerField(blank=True, null=True, verbose_name="Цена")
    address = models.TextField(blank=True, null=True, verbose_name="Адрес")
    seller = models.CharField(
        blank=True, null=True, max_length=250, verbose_name="Продавец"
    )
    kolichestvo_komnat = models.IntegerField(
        blank=True, null=True, verbose_name="Кол-во комнат"
    )
    obshchaya_ploshchad = models.FloatField(
        blank=True, null=True, verbose_name="Общая площадь"
    )
    ploshchad_kukhni = models.FloatField(
        blank=True, null=True, verbose_name="Площадь кухни"
    )
    zhilaya_ploshchad = models.FloatField(
        blank=True, null=True, verbose_name="Жилая площадь"
    )
    etazh = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="Этаж и общее кол-во этажей в доме)",
    )
    balkon_ili_lodzhiya = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        verbose_name="Наличие балкона или лоджии",
    )
    tip_komnat = models.CharField(
        blank=True, null=True, max_length=250, verbose_name="Тип комнат"
    )
    vysota_potolkov = models.CharField(
        blank=True, null=True, max_length=10, verbose_name="Высота потолков"
    )
    sanuzel = models.CharField(
        blank=True, null=True, max_length=250, verbose_name="Санузел"
    )
    okna = models.CharField(
        blank=True, null=True, max_length=250, verbose_name="Окна"
    )
    remont = models.TextField(blank=True, null=True)
    mebel = models.TextField(blank=True, null=True)
    sposob_prodazhi = models.TextField(blank=True, null=True)
    vid_sdelki = models.TextField(blank=True, null=True)
    tip_doma = models.TextField(blank=True, null=True)
    god_postroyki = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="Год постройки дома"
    )
    kapremont_date = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="Дата капремонта"
    )
    etazhey_v_dome = models.TextField(blank=True, null=True)
    passazhirskiy_lift = models.TextField(blank=True, null=True)
    gruzovoy_lift = models.TextField(blank=True, null=True)
    dvor = models.TextField(blank=True, null=True)
    parkovka = models.TextField(blank=True, null=True)
    etazh_val = models.IntegerField(blank=True, null=True, verbose_name="Этаж")
    etazh_count = models.IntegerField(blank=True, null=True, verbose_name="Этажей")
    to_magazin = models.TextField(blank=True, null=True)
    to_pyaterochka = models.TextField(blank=True, null=True)
    to_magnit = models.TextField(blank=True, null=True)
    to_bolnitsa = models.TextField(blank=True, null=True)
    to_pochta = models.TextField(blank=True, null=True)
    to_bank = models.TextField(blank=True, null=True)
    to_apteka = models.TextField(blank=True, null=True)
    to_ozon = models.TextField(blank=True, null=True)
    to_wildberries = models.TextField(blank=True, null=True)
    to_yandex = models.TextField(blank=True, null=True)
    status = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="Статус"
    )
    source_from = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="Источник"
    )
    tekhnika = models.TextField(blank=True, null=True)
    v_dome = models.TextField(blank=True, null=True)
    dopolnitelno = models.TextField(blank=True, null=True)
    teplyy_pol = models.TextField(blank=True, null=True)
    zaplanirovan_snos = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "avito"
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    def __str__(self):
        return str(self.id)
