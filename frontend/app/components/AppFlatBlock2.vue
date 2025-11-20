<script setup>
const props = defineProps(['item'])

const fields_general = {
    "price": "Цена",
    // "address": "Адрес",
    "kolichestvo_komnat": "Кол-во комнат",
    "obshchaya_ploshchad": "Общая площадь",
    "god_postroyki": "Год постройки",
    "kapremont_date": "Дата капремонта",
    "etazh_val": "Этаж",
    "etazh_count": "Этажей",
}
const fields_ratings = {
    "rating_all": "Суммарный рейтинг",
    "rating_house": "Рейтинг дома",
    "rating_flat": "Рейтинг квартиры",
    "rating_flat": "Рейтинг квартиры",
    "rating_infrastructure": "Рейтинг инфраструктыры",
}
// const kapremontColor = computed((index) => {
//     let cls = ""
//     // console.log(props["item"]["kapremont_date"])
//     if (index === "kapremont_date" && (props["item"]["kapremont_date"] - 2025) <= 5) {
//         cls = "bg-black"
//     }
//     return cls
// })
function kapremontColor(index) {
    let cls = ""
    if (index === "kapremont_date" && (props["item"]["kapremont_date"] - 2025) <= 5) {
        cls = "bg-red-100"
    }
    return cls
}

function priceColor(index) {
    let cls = ""
    if (index === "price" && props["item"]["price"] > 5000000) {
        cls = "bg-red-100"
    }
    return cls
}


const classObject = reactive({
  'bg-black': true
})
</script>


<template>
    <div
        class="mx-auto flex flex-row justify-between items-start mb-2 gap-x-4 rounded-xl bg-white p-6 outline outline-black/5 dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10">

        <div class="">
            <div class="text-xl font-medium text-black dark:text-white">{{ item.title }}</div>
            <p class="text-gray-500 dark:text-gray-400">{{ item.address }}</p>
            <!-- Ratings -->
            <div class="flex flex-wrap gap-1">
                <div class="flat_items_label">Рейтинг</div>
                <div class="flat_items_wrapper" v-for="(value, index) in fields_ratings">
                    <div class="flat_items_text">{{ value }}</div>
                    <div class="flat_items_value">
                        {{ item[index] }}
                    </div>
                </div>
            </div>
            <!-- General -->
            <div class="flex flex-wrap gap-1">
                <div class="flat_items_label">Общая информация</div>
                <div class="flat_items_wrapper" :class="kapremontColor(index), priceColor(index)" v-for="(value, index) in fields_general">
                    <div class="flat_items_text">{{ value }}</div>
                    <div class="flat_items_value">
                        {{ item[index] }}
                    </div>
                </div>
            </div>
        </div>

        <img class="size-52 shrink-0" v-bind:src="'/public/images/' + item['id'] + '/main.jpg'" />
    </div>
</template>

<!-- <template>
    <UPageCard :title=item.title :description=item.address orientation="horizontal">

        <img v-bind:src="'/public/images/' + item['id'] + '/main.jpg'" class="w-50" alt="...">
    </UPageCard>
</template> -->