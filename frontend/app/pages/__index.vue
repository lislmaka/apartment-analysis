<script setup lang="ts">
const { data, pending, error } = await useFetch('http://service.backend:8000/api/list/')
// const { data, pending, error } = await useFetch('https://fakeapi.extendsclass.com/books')

const fields = {
   id: "id",
   // title: "Название",
   // url: "",
   // address: "Адрес",
   price: "Цена",
   kolichestvo_komnat: "Кол-во комнат",
   etazh_val: "Этаж",
   etazh_count: "Этажей",
   obshchaya_ploshchad: "Площадь",
   god_postroyki: "Год постройки",
   kapremont_date: "Капремонт",
   // images: "Фото",
};
</script>

<template>

   <div class="grid grid-cols-8 gap-1 bg-gray-500">
      <div v-for="field in fields" class="px-6 py-1 bg-gray-700 text-left text-gray-50">{{ field }}</div>
   </div>

   <div v-for="item in data" class="grid grid-cols-8 gap-1 border border-gray-500">
      <div class="col-span-8 px-6 py-1 text-left text-gray-900 bg-gray-200">
         {{ item.title }}
         <br>
         {{ item.address }}
      </div>
      <div class="px-6 py-3 text-left text-gray-900">{{ item.id }}</div>
      <div class="px-6 py-3 text-left text-gray-900">{{ item.price }}</div>
      <div class="px-6 py-3 text-left text-gray-900">{{ item.kolichestvo_komnat }}</div>
      <div class="px-6 py-3 text-left text-gray-900">{{ item.etazh_val }}</div>
      <div class="px-6 py-3 text-left text-gray-900">{{ item.etazh_count }}</div>
      <div class="px-6 py-3 text-left text-gray-900">{{ item.obshchaya_ploshchad }}</div>
      <div class="px-6 py-3 text-left text-gray-900">{{ item.god_postroyki }}</div>
      <div class="px-6 py-3 text-left text-gray-900">{{ item.kapremont_date }}</div>

      <div class="col-span-8 px-6 py-3 text-left text-gray-900">
         <div class="grid grid-cols-10 gap-1">
            <div><img src="/flats/7609817498/1.jpg"></div>
            <div><img src="/flats/7609817498/2.jpg"></div>
            <div><img src="/flats/7609817498/3.jpg"></div>
            <div><img src="/flats/7609817498/4.jpg"></div>
            <div><img src="/flats/7609817498/5.jpg"></div>
            <div><img src="/flats/7609817498/6.jpg"></div>
            <div><img src="/flats/7609817498/7.jpg"></div>
            <div><img src="/flats/7609817498/8.jpg"></div>
            <div><img src="/flats/7609817498/9.jpg"></div>
            <div><img src="/flats/7609817498/10.jpg"></div>
         </div>
      </div>
   </div>

</template>