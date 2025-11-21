<script setup>
import AppLeftSide from '~/components/AppLeftSide.vue';
import AppRightSide from '~/components/AppRightSide.vue';

const runtimeConfig = useRuntimeConfig()
const message = ref("")
const paginationPageNumber = ref(1)
// const countProjects = ref(0)
let sortPriceOrder = ref("DESC")

let url = "baseURL" in runtimeConfig ? runtimeConfig.baseURL : 'http://localhost:1337/api/list/'

const { data, status, error } = await useFetch(url, {
    query: {
        page: paginationPageNumber,
        sort_price_order: sortPriceOrder,
    },
    // lazy: true,
})

// countProjects.value = data.value["count"]

// const filteredProjects = computed(() => {
//     if (!message.value) {
//         countProjects.value = data.value["count"]
//         return data.value["results"];
//     }
//     const lowerCaseSearchText = message.value.toLowerCase();
//     const d = data.value["results"].filter(user => user.id.toString().includes(message.value));
//     countProjects.value = d.length
//     console.log("--->>>", countProjects.value)
//     data.value = d
//     return data.value
// })

const countFlats = computed(() => {
    if (status.value == "success") {
        return data.value["count"]
    }
})

const countDistrics = computed(() => {
    let districs = {}
    if (status.value == "success") {
        for (let flat in data.value['results']) {
            districs[data.value['results'][flat]["district"]] = districs[data.value['results'][flat]["district"]] ? districs[data.value['results'][flat]["district"]] + 1 : 1
            //     if (flat["district"] in districs) {
            //         districs[flat["district"]] += 1
            //     } else {
            //         districs[flat["district"]] = 1
            //     }
        }
    }

    return districs
})

let compare = (a, b) => {

}
function filtersEvents(val) {
    // if (sortPriceOrder == "DESC") {
    //     data.value['results'].sort((a, b) => b.rating_all - a.rating_all)
    // } else {
    //     data.value['results'].sort((a, b) => a.rating_all - b.rating_all)
    // }
    // // data.value['results'].sort(compare)
    // // console.log("sortPrice = ", sortPrice.value)

    // // console.log("sortPrice = ", sortPrice.value)
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
    <div class="grid grid-cols-12 gap-4">

        <div v-if="data" class="col-span-9">
            <AppFlatBlock v-for="item in data['results']" :key="item.id" :item="item" />
        </div>
        <div class="col-span-3">
            <AppRightSide @filters="filtersEvents" :sortOrder="sortPriceOrder" :districs="countDistrics" />
        </div>
    </div>
    <div class="block my-3">
        <UPagination v-model:page="paginationPageNumber" :total="countFlats" />
    </div>
    <!-- <p v-if="status === 'pending'">Loading...</p>
    <p v-if="error">{{ error.message }}</p> -->
    <!-- <div class="">
        <div>
            {{ paginationPageNumber }}
            <AppPagination :count="countProjects" @getpaginationPageNumber="getPaginationPageNumber" />

        </div>
        <div class="row">
            <div class="col-9">
                <div v-if="data">
                    <AppFlatBlock2 v-for="item in filteredProjects" :key="item.id" :item="item" />
                </div>
                <p v-if="pending">Loading...</p>
                <p v-if="error">{{ error.message }}</p>

            </div>
            <div class="col-3">
                <div class="row  mb-1">
                    <div class="col-10">
                        <input v-model="message" class="form-control" type="text">
                    </div>
                    <div class="col-2">
                        <h4><span class="badge text-bg-secondary">{{ countProjects }}</span></h4>
                    </div>
                </div>
                <AppRightSide @filters="filtersEvents" />
            </div>
        </div>
    </div>
 -->
</template>
