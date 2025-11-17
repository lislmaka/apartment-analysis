<script setup lang="ts">
import AppLeftSide from '~/components/AppLeftSide.vue';
import AppRightSide from '~/components/AppRightSide.vue';

// const { data, pending, error } = await useFetch('http://service.backend:8000/api/list/')
// const { data, pending, error } = await useFetch('https://fakeapi.extendsclass.com/books')


</script>

<template>
    <div class="">
        <div class="row">
            <!-- <div class="col-3">
                <AppLeftSide/>
            </div> -->
            <div class="col-9">
                <AppData/>
            </div>
            <div class="col-3">
                <AppRightSide/>
            </div>
        </div>
    </div>
</template>
