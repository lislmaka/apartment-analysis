<script setup>
import { tr } from '@nuxt/ui/runtime/locale/index.js'

const emit = defineEmits(['filters'])
const props = defineProps(['sortOrder', 'districs'])
let iconPricesSort = ref("&#8659;")

function isChecked(event, val) {
    iconPricesSort.value = iconPricesSort.value == "&#8659;" ? "&#8657;" : "&#8659;"
    emit(event, '111')
}

// function showOrderIcon() {
//     if (props["sortOrder"] == "DESC") {
//         iconPricesSort.value = "i-lucide-arrow-down-1-0"
//     } else {
//         iconPricesSort.value = "i-lucide-arrow-down-0-1"
//     }
// }

</script>
<template>
    <div class="flex flex-col space-y-5">
        <div class="flex flex-col rounded-sm border border-gray-300">
            <div class="bg-gray-100 p-3 text-xl font-medium text-black">Фильтры / Сортировка</div>
            <!-- <div class="block p-3">
            <a href="#" @click="$emit('filters', 'pizza1')">Сортировка по рейтингу {{ props["sortOrder"] }}</a>
        </div> -->
            <div class="flex flex-col">
                <div class="p-2">
                    <a href="#" @click="isChecked('filters', props['sortOrder'])">Сортировка по рейтингу <span
                            v-html="iconPricesSort"></span>
                        <!-- Сортировка по цене <UIcon :name="iconPricesSort" class="size-5" />
                <span v-if="iconPricesSortFlag"><UIcon name="i-lucide-arrow-down-1-0" class="size-5" /></span>
                <span v-else="iconPricesSortFlag"><UIcon name="i-lucide-arrow-down-0-1" class="size-5" /></span> -->
                    </a>
                </div>
                <!-- <div class="p-2">
                    <a href="#" @click="isChecked('filters', props['sortOrder'])">Сортировка по рейтингу <span
                            v-html="iconPricesSort"></span>
                    </a>
                </div> -->

            </div>
        </div>

        <div class="flex flex-col rounded-sm border border-gray-300">
            <div class="bg-gray-100 p-3 text-xl font-medium text-black">Районы</div>
            <div class="flex justify-between" v-for="(count, district) in props['districs']">
                <div class="p-2">{{ district }}</div>
                <div class="bg-gray-200 m-2 px-2 rounded-sm">
                    {{ count }}
                </div>
            </div>
        </div>

    </div>


</template>