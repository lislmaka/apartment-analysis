import { ref, computed } from 'vue'

// Reactive global state
const globalCounter = ref(0)
const globalCounter1 = ref(0)
// const theme = ref('light')

export function useGlobalData() {
    //   const increment = () => {
    //     globalCounter.value++
    //   }

    //   const toggleTheme = () => {
    //     theme.value = theme.value === 'light' ? 'dark' : 'light'
    //   }
    const fields_general = {
        "price": "Цена",
        // "address": "Адрес",
        "kolichestvo_komnat": "Кол-во комнат",
        "obshchaya_ploshchad": "Общая площадь",
        "god_postroyki": "Год постройки",
        // "kapremont_date": "Дата капремонта",
        "etazh_val": "Этаж",
        "etazh_count": "Этажей",
        "district": "Район",
    }
    const fields_ratings = {
        "rating_all": "Суммарный",
        "rating_house": "Дом",
        "rating_flat": "Квартира",
        "rating_infrastructure": "Инфраструктура",
    }
    const fields_house = {
        "kapremont_date": "Дата капремонта",
        "kapremont_diff": "Сколько до капремонта",
        "is_new_lift": "Новый лифт",
        "is_musoroprovod": "Есть ли мусоропровод"
    }

    const fields_district = {
        "to_pyaterochka": "Пятерочка",
        "to_magnit": "Магнит",
        "to_bolnitsa": "Больница",
        "to_pochta": "Почта",
        "to_bank": "Банк",
        "to_apteka": "Аптека",
        "to_ozon": "Ozon",
        "to_wildberries": "WB",
        "to_bus_stop": "Остановка",
    }

    const main = {
        "ratings": {
            "label": "Рейтинг",
            "data": fields_ratings,
        },
        "general": {
            "label": "Информация",
            "data": fields_general,
        },
        "house": {
            "label": "Дом",
            "data": fields_house,
        },
        "district": {
            "label": "Инфраструктура (метры)",
            "data": fields_district,
        },
    }
    return {
        fields_general: fields_general,
        fields_ratings: fields_ratings,
        fields_house: fields_house,
        fields_district: fields_district,
        main: main,
        globalCounter: computed(() => globalCounter.value),
        globalCounter1: globalCounter1,
        //     theme: computed(() => theme.value),
        //     increment,
        //     toggleTheme
    }
}