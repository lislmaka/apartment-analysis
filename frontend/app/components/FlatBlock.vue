<script setup>
const { fields_general, fields_ratings, fields_house, fields_district, main } = useGlobalData()

const props = defineProps(['item'])
let isUnsuitable = ref(false)


const badElementColor = "bg-red-100"
const goodElementColor = "bg-green-100"
const warnigElementColor = "bg-orange-100"
const hideElement = "hidden"

function checkElement(index) {
    if (index === "kapremont_date") {
        if ((props["item"]["kapremont_date"] - 2025) <= 5) {
            isUnsuitable = true
            return badElementColor
        } else {
            return goodElementColor
        }
    }
    else if (index === "kapremont_diff") {
        if (props["item"]["kapremont_diff"] > 0 && props["item"]["kapremont_diff"] <= 5) {
            isUnsuitable = true
            return badElementColor
        } else {
            return goodElementColor
        }
    }
    else if (index === "price") {
        if (props["item"]["price"] > 6000000) {
            isUnsuitable = true
            return badElementColor
        } else {
            return goodElementColor
        }
    }
    // is_musoroprovod
    else if (index === "is_musoroprovod") {
        if (props["item"]["is_musoroprovod"] === false) {
            props["item"]["is_musoroprovod"] = "Нет"
            isUnsuitable = true
            return badElementColor
        } else {
            props["item"]["is_musoroprovod"] = "Да"
            return goodElementColor
        }
    }
    else if (index === "is_new_lift") {
        if (props["item"]["is_new_lift"] === false) {
            props["item"]["is_new_lift"] = "Нет"
            isUnsuitable = true
            return badElementColor
        } else {
            props["item"]["is_new_lift"] = "Да"
            return goodElementColor
        }
    }
    else if (index in fields_district) {
        if (props["item"][index] === null) {
            return hideElement
        }
        if (parseInt(props["item"][index]) <= 500) {
            return goodElementColor
        } else {
            return warnigElementColor
        }
    }
    return ""
}
</script>


<template>
    <div class="flex border border-gray-300 p-3 mb-5 rounded-sm">
        <div class="flex flex-col flex-nowrap w-3/4 gap-1">
            <div class="text-xl font-medium text-black dark:text-white">{{ item.title }}</div>
            <p class="text-gray-500 dark:text-gray-400">{{ item.address }}</p>
            <!-- Ratings -->
            <div class="flex flex-wrap gap-1 text-gray-700" v-for="cat in main">
                <div class="bg-gray-500 text-white border-gray-500 rounded-sm text-sm px-2 py-1">{{ cat.label }}</div>
                <div class="flex justify-between border border-gray-300 rounded-sm text-sm space-x-1"
                    :class="checkElement(index)" v-for="(value, index) in cat.data">
                    <div class="px-2 py-1">{{ value }}</div>
                    <div class="bg-gray-300 rounded-r-sm px-2 py-1">
                        {{ item[index] }}
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col w-1/4">
            <div v-if="isUnsuitable" class="bg-red-300 p-1 m-1 px-3 rounded text-center font-bold">Квартира не подходит
            </div>
            <img class="w-full shrink-0 p-3 rounded-2xl mb-1 bg-gray-100" :class="{ 'bg-red-100': isUnsuitable }"
                v-bind:src="'/public/images/' + item['id'] + '/main.jpg'" />
        </div>

    </div>
</template>