<script setup>
import AppLeftSide from '~/components/AppLeftSide.vue';
import AppRightSide from '~/components/AppRightSide.vue';

const runtimeConfig = useRuntimeConfig()

// const { data, pending, error } = await useFetch('http://service.backend:8000/api/list/')
// const { data, pending, error } = await useFetch('http://localhost:1337/api/list/')
let url = "baseURL" in runtimeConfig ? runtimeConfig.baseURL  : 'http://localhost:1337/api/list/'

const { data, pending, error } = await useFetch(url)
const message = ref("")
const countProjects = ref("0")

const filteredProjects = computed(() => {
    if (!message.value) {
        countProjects.value = data.value["results"].length
        return data.value["results"];
    }
    const lowerCaseSearchText = message.value.toLowerCase();
    const d = data.value["results"].filter(user => user.id.toString().includes(message.value));
    countProjects.value = d.length
    return d
})

function filtersEvents(val) {
    alert(val)
}

</script>

<template>
    <div class="">
        <div class="row">
            <div class="col-9">
                <div v-if="data">
                    <AppFlatBlock v-for="item in filteredProjects" :key="item.id" :item="item"/>
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
</template>
