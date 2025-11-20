<script setup>
import AppLeftSide from '~/components/AppLeftSide.vue';
import AppRightSide from '~/components/AppRightSide.vue';

const runtimeConfig = useRuntimeConfig()
const message = ref("")
const paginationPageNumber = ref(1)
const countProjects = ref(0)

let url = "baseURL" in runtimeConfig ? runtimeConfig.baseURL : 'http://localhost:1337/api/list/'

const { data, status, error } = await useFetch(url, {
    query: {
        page: paginationPageNumber,
    },
    // lazy: true,
})


const filteredProjects = computed(() => {
    if (!message.value) {
        countProjects.value = data.value["count"]
        return data.value["results"];
    }
    const lowerCaseSearchText = message.value.toLowerCase();
    const d = data.value["results"].filter(user => user.id.toString().includes(message.value));
    countProjects.value = d.length
    console.log("--->>>", countProjects.value)
    return d
})

function filtersEvents(val) {
    alert(val)
}
function getPaginationPageNumber(page) {
    paginationPageNumber.value = page
}

</script>

<template>
    <div class="block my-3">
        <UPagination v-model:page="paginationPageNumber" :total="countProjects" />
    </div>
    <div class="grid grid-cols-12 gap-4">

        <div v-if="data" class="col-span-9">
            <AppFlatBlock2 v-for="item in filteredProjects" :key="item.id" :item="item" />
        </div>
        <div class="col-span-3">
            <AppRightSide @filters="filtersEvents" />
        </div>
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
