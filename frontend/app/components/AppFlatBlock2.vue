<script setup>
const props = defineProps(['item'])
let image_danger_class = ref("bg-gray-100")
let isUnsuitable = ref(false)

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

// const chackIsUnsutable = computed(() => {
//     if (index === "kapremont_date" && (props["item"]["kapremont_date"] - 2025) <= 5) {
//         cls = "bg-black"
//     }
//     return cls
// })

function kapremontColor(index) {
    let cls = ""
    if (index === "kapremont_date" && (props["item"]["kapremont_date"] - 2025) <= 5) {
        cls = "bg-red-100"
        image_danger_class = "bg-red-200"
        isUnsuitable = true
    }
    return cls
}

function priceColor(index) {
    let cls = ""
    if (index === "price" && props["item"]["price"] > 5000000) {
        cls = "bg-red-100"
        image_danger_class = "bg-red-200"
        isUnsuitable = true
    }
    return cls
}


const classObject = reactive({
  'bg-black': true
})
</script>


<template>
    <div class="grid grid-cols-12 gap-1 border border-gray-100 p-3 mb-5 rounded">

        <div class="col-span-9">
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
        <div class="col-span-3 justify-items-center">
            <div v-if="isUnsuitable" class="block bg-red-300 p-1 m-1 px-3 rounded">Квартира не подходит</div>
            <img class="size-52 shrink-0 p-3 rounded-2xl mb-1" :class="image_danger_class" v-bind:src="'/public/images/' + item['id'] + '/main.jpg'" />
        </div>
        
    </div>
</template>

<!-- <template>
    <UPageCard :title=item.title :description=item.address orientation="horizontal">

        <img v-bind:src="'/public/images/' + item['id'] + '/main.jpg'" class="w-50" alt="...">
    </UPageCard>
</template> -->