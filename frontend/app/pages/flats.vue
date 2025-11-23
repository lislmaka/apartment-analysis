<script setup>
const { globalCounter, globalCounter1 } = useGlobalData()
const runtimeConfig = useRuntimeConfig()
const message = ref("")
const paginationPageNumber = ref(1)
let sortPriceOrder = ref("DESC")

let url = "baseURL" in runtimeConfig ? runtimeConfig.baseURL : 'http://localhost:1337/api/list/'

const { data, status, error } = await useFetch(url, {
    query: {
        page: paginationPageNumber,
        sort_price_order: sortPriceOrder,
    },
    // lazy: true,
})

const countFlats = computed(() => {
    if (status.value == "success") {
        globalCounter1.value = data.value["count"]
        return data.value["count"]
    }
})

const countDistrics = computed(() => {
    let districs = {}
    if (status.value == "success") {
        for (let flat in data.value['results']) {
            districs[data.value['results'][flat]["district"]] = districs[data.value['results'][flat]["district"]] ? districs[data.value['results'][flat]["district"]] + 1 : 1
        }
    }

    return districs
})

function filtersEvents(val) {
    sortPriceOrder.value = sortPriceOrder.value == "DESC" ? "ASC" : "DESC"
}

function getPaginationPageNumber(page) {
    paginationPageNumber.value = page
}

</script>

<template>
    <div class="block my-3">
        <UPagination v-model:page="paginationPageNumber" :total="countFlats" />
    </div>
    <div class="grid grid-cols-12 gap-5">

        <div v-if="data" class="col-span-9">
            <FlatBlock v-for="item in data['results']" :key="item.id" :item="item" />
        </div>
        <div class="col-span-3">
            <RightSide @filters="filtersEvents" :sortOrder="sortPriceOrder" :districs="countDistrics" />
        </div>
    </div>
    <div class="block my-3">
        <UPagination v-model:page="paginationPageNumber" :total="countFlats" />
    </div>
</template>
