# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime
from django.utils.html import format_html

def image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "images/img_{0}.jpg".format(instance.id)

def video_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "video/video_{0}.mp4".format(instance.id)

class Avito(models.Model):
    DISTRICT_CHOICES = [
        ("Фокинский", "Фокинский"),
        ("Бежицкий", "Бежицкий"),
        ("Советский", "Советский"),
        ("Володарский", "Володарский"),
        ("", "Не указано"),
    ]

    TIP_DOMA_CHOICES = [
        ("кирпичный", "кирпичный"),
        ("панельный", "панельный"),
        ("монолитно-кирпичный", "монолитно-кирпичный"),
        ("", "Не указано"),
    ]

    RATING_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("", "Нет"),
    ]

    RECORD_STATUS_CHOICES = [
        ("1", "Новая"),
        ("2", "Капремонт"),
        ("3", "Дом"),     
        ("4", "Квартира"),  
        ("5", "Инфраструктура"), 
        ("6", "Все данные внесены"), 
    ]
    
    REVIEW_RESULTS_CHOICES = [
        ("1", "Осмотра не было"),
        ("2", "Осмотр был. Квартира подходит"),
        ("3", "Осмотр был. Квартира не подходит"),     
    ]

    RESEARCH_RESULTS_CHOICES = [
        ("1", "Пока не искали"),
        ("2", "Хорошо"),
        ("3", "Плохо"),
        ("4", "Информация не найдена"),  
    ]

    YESNO_RESULTS_CHOICES = [
        ("1", "Пока не искали"),
        ("2", "Да"),
        ("3", "Нет"),
        ("4", "Информация не найдена"),  
    ]

    # id = models.BigAutoField(primary_key=True)
    # id = models.CharField(blank=True, null=True, verbose_name="ID объявления")
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    url = models.TextField(blank=True, null=True, verbose_name="Url адрес")
    date_add = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="Дата добавления"
    )
    date_update = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="Дата обновления"
    )
    title = models.TextField(blank=True, null=True, verbose_name="Заголовок")
    description = models.TextField(
        blank=True, null=True, default="", verbose_name="Достоинства"
    )
    description_minus = models.TextField(
        blank=True, null=True, default="", verbose_name="Недостатки"
    )
    district = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=DISTRICT_CHOICES,
        default="",
        verbose_name="Район",
    )
    rating = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=RATING_CHOICES,
        default="",
        verbose_name="R",
    )

    record_status = models.CharField(
        # blank=True,
        # null=True,
        max_length=50,
        choices=RECORD_STATUS_CHOICES,
        default=1,
        verbose_name="Текущий статус записи",
    )

    review_results = models.CharField(
        # blank=True,
        # null=True,
        max_length=50,
        choices=REVIEW_RESULTS_CHOICES,
        default=1,
        verbose_name="Осмотр",
    )

    price = models.CharField(blank=True, null=True, max_length=20, verbose_name="Цена")
    address = models.TextField(blank=True, null=True, verbose_name="Адрес")
    seller = models.CharField(
        blank=True, null=True, max_length=250, verbose_name="Продавец"
    )
    kolichestvo_komnat = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Комнат"
    )
    obshchaya_ploshchad = models.FloatField(
        blank=True, null=True, verbose_name="Площадь"
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
    okna = models.CharField(blank=True, null=True, max_length=250, verbose_name="Окна")
    remont = models.TextField(blank=True, null=True)
    mebel = models.TextField(blank=True, null=True)
    sposob_prodazhi = models.TextField(blank=True, null=True)
    vid_sdelki = models.TextField(blank=True, null=True)
    # tip_doma = models.TextField(blank=True, null=True, verbose_name="Тип дома")
    tip_doma = models.CharField(
        max_length=50, choices=TIP_DOMA_CHOICES, default="", verbose_name="Тип дома"
    )
    god_postroyki = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Год постройки"
    )
    kapremont_date = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Дата капремонта"
    )
    kapremont_diff = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Кол-во лет до капремонта"
    )
    lift_diff = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Кол-во лет до замены лифта"
    )
    lift_date = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Дата замены лифта"
    )
    gkx_payments = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Стоимость комунальных платежей"
    )
    etazhey_v_dome = models.TextField(blank=True, null=True)
    passazhirskiy_lift = models.TextField(blank=True, null=True)
    gruzovoy_lift = models.TextField(blank=True, null=True)
    dvor = models.TextField(blank=True, null=True)
    parkovka = models.TextField(blank=True, null=True)
    etazh_val = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Этаж"
    )
    etazh_count = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Этажей"
    )
    to_magazin = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Магазин"
    )
    to_pyaterochka = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Пятерочка"
    )
    to_magnit = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Магнит"
    )
    to_bolnitsa = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Больница"
    )
    to_pochta = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Почта"
    )
    to_bank = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Банк"
    )
    to_apteka = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Аптека"
    )
    to_ozon = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Ozon"
    )
    to_wildberries = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Wildberries"
    )
    to_yandex = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Yandex"
    )
    to_bus_stop = models.CharField(
        blank=True, null=True, max_length=20, verbose_name="Остановка"
    )
    # status = models.CharField(
    #     blank=True, null=True, max_length=100, verbose_name="Статус"
    # )
    status = models.BooleanField(default=True, verbose_name="Статус")
    source_from = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="Источник"
    )
    tekhnika = models.TextField(blank=True, null=True)
    v_dome = models.TextField(blank=True, null=True)
    dopolnitelno = models.TextField(blank=True, null=True)
    teplyy_pol = models.TextField(blank=True, null=True)
    zaplanirovan_snos = models.TextField(blank=True, null=True)
    rating_infrastructure = models.FloatField(
        default=0, verbose_name="Рейтинг инфраструктуры"
    )
    rating_house = models.FloatField(
        default=0, verbose_name="Рейтинг дома"
    )
    rating_flat = models.FloatField(
        default=0, verbose_name="Рейтинг квартиры"
    )
    rating_all = models.FloatField(
        default=0, verbose_name="Суммарный рейтинг"
    )
    is_kapremont = models.BooleanField(default=False, verbose_name="Есть время до капремонта")
    is_no_stupenki = models.BooleanField(default=False, verbose_name="Нет ступенек перед входом в подьезд")
    is_musoroprovod = models.BooleanField(default=False, verbose_name="Есть мусоропровод")
    is_new_lift = models.BooleanField(default=False, verbose_name="Новый лифт")
    is_kuxnya = models.BooleanField(default=False, verbose_name="Нормальная кухня")
    is_tualet = models.BooleanField(default=False, verbose_name="Нормальный туалет")
    is_vana = models.BooleanField(default=False, verbose_name="Нормальная ванная")
    is_balkon = models.BooleanField(default=False, verbose_name="Нормальный балкон")
    is_neighbors_around = models.BooleanField(default=False, verbose_name="Нормальные соседи рядом")
    is_neighbors_top = models.BooleanField(default=False, verbose_name="Нормальные соседи сверху")
    is_door = models.BooleanField(default=False, verbose_name="Нормальная входня дверь")
    kuxnya = models.CharField(
        max_length=50, choices=RESEARCH_RESULTS_CHOICES, default="1", verbose_name="Кухня"
    )
    tualet = models.CharField(
        max_length=50, choices=RESEARCH_RESULTS_CHOICES, default="1", verbose_name="Туалет"
    )
    vana = models.CharField(
        max_length=50, choices=RESEARCH_RESULTS_CHOICES, default="1", verbose_name="Ванная комната"
    )
    balkon = models.CharField(
        max_length=50, choices=RESEARCH_RESULTS_CHOICES, default="1", verbose_name="Балкон"
    )

    door = models.CharField(
        max_length=50, choices=RESEARCH_RESULTS_CHOICES, default="1", verbose_name="Входная дверь"
    )
    neighbors_around = models.CharField(
        max_length=50, choices=RESEARCH_RESULTS_CHOICES, default="1", verbose_name="Соседи рядом"
    )
    neighbors_top = models.CharField(
        max_length=50, choices=RESEARCH_RESULTS_CHOICES, default="1", verbose_name="Соседи сверху"
    )
    tambur = models.CharField(
        max_length=50, choices=YESNO_RESULTS_CHOICES, default="1", verbose_name="Наличие тамбура"
    )
    no_stupenki = models.CharField(
        max_length=50, choices=YESNO_RESULTS_CHOICES, default="1", verbose_name="Наличие ступенек при входе в подьезд"
    )
    musoroprovod = models.CharField(
        max_length=50, choices=YESNO_RESULTS_CHOICES, default="1", verbose_name="Наличие мусоропровода в доме"
    )

    file_img = models.FileField(upload_to=image_path, null=True, blank=True, verbose_name="Фото")
    file_video = models.FileField(upload_to=video_path, null=True, blank=True, verbose_name="Видео")

    class Meta:
        managed = False
        db_table = "avito"
        verbose_name = "Квартиру"
        verbose_name_plural = "Квартиры"
        # ordering = ("-rating", "price", "-god_postroyki")

    @property
    def to_kapremont(self):
        if self.kapremont_date:
            return int(self.kapremont_date) - int(datetime.date.today().strftime("%Y"))
        # self.save()
        return None

    @property
    def url_to_img(self):
        return format_html("<img src='/static/flats/{}/main.jpg' height=200>", self.id)

    def __str__(self):
        return str(self.id)
