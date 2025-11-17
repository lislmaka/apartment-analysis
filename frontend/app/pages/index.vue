<script setup>
import AppLeftSide from '~/components/AppLeftSide.vue';
import AppRightSide from '~/components/AppRightSide.vue';

const { data, pending, error } = await useFetch('http://service.backend:8000/api/list/')
const message = ref("")
const countProjects = ref("0")

const filteredProjects = computed(() => {
    if (!message.value) {
        return data.value;
    }
    const lowerCaseSearchText = message.value.toLowerCase();
    const d = data.value.filter(user => user.id.toString().includes(message.value));
    countProjects.value = d.length
    return d
})

</script>

<template>
    <div class="">
        <div class="row">
            <!-- <div class="col-3">
                <AppLeftSide/>
            </div> -->
            <div class="col-9">
                <!-- <AppData v-bind:data="data"/> -->
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Serch text:({{ countProjects }}) {{ message
                        }}</label>
                    <input v-model="message" type="text" class="form-control" id="exampleFormControlInput1"
                        placeholder="">
                </div>
                <div v-if="data">
                    <AppFlatBlock v-for="item in filteredProjects" :key="item.id" :item="item"/>
                    <!-- <div class="card mb-3" v-for="item in filteredProjects" :key="item['id']">
                        <div class="row g-0">
                            <div class="col-md-9">
                                <div class="card-body">
                                    <h5 class="card-title">{{ item["id"] }} {{ item["title"] }}</h5>
                                    <p class="card-text">Price {{ item["price"] }}</p>
                                    <p class="card-text"><small class="text-body-secondary">Last updated 3 mins
                                            ago</small></p>
                                </div>
                            </div>
                            <div class="col-md-3 d-flex justify-content-end">
                                <img v-bind:src="'/public/images/' + item['id'] + '/main.jpg'"
                                    class="img-fluid rounded-end" width="250" alt="...">
                            </div>
                        </div>
                    </div> -->
                </div>
                <p v-if="pending">Loading...</p>
                <p v-if="error">{{ error.message }}</p>

            </div>
            <div class="col-3">
                <AppRightSide />
            </div>
        </div>
    </div>
</template>
