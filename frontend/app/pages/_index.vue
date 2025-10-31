<script setup lang="ts">
const { data, pending, error } = await useFetch('http://service.backend:8000/api/list/')
// const { data, pending, error } = await useFetch('https://fakeapi.extendsclass.com/books')

const fields = {
   id: "id",
   title: "Название",
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
function getImg(id, number) {
   return "flats/" + id + "/" + number + ".jpg"
}
</script>

<template>


   <div class="relative overflow-x-auto">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
         <thead class="text-xs text-gray-50 uppercase bg-gray-700">
            <tr>
               <th v-for="field in fields" scope="col" class="px-6 py-3">
                  {{ field }}
               </th>
            </tr>
         </thead>
      </table>   
      <table v-for="item in data" class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
         <!-- <thead class="text-xs text-gray-50 uppercase bg-gray-700">
            <tr>
               <th v-for="field in fields" scope="col" class="px-6 py-3">
                  {{ field }}
               </th>
            </tr>
         </thead> -->
         <tbody>
            <tr class="bg-gray-100 border-b border-gray-300 text-gray-900">
               <td class="px-6 py-4">
                  <a :href="item.url" target="_blank">{{ item.id }}</a>
               </td>
               <td class="px-6 py-4" width="300px">
                  {{ item.title }}
                  <br class="border-b border-gray-500">
                  {{ item.address }}
               </td>
               <!-- <td class="px-6 py-4">
                  {{ item.address }}
               </td> -->
               <td class="px-6 py-4">
                  {{ item.price }}
               </td>
               <td class="px-6 py-4">
                  {{ item.kolichestvo_komnat }}
               </td>
               <td class="px-6 py-4">
                  {{ item.etazh_val }}
               </td>
               <td class="px-6 py-4">
                  {{ item.etazh_count }}
               </td>
               <td class="px-6 py-4">
                  {{ item.obshchaya_ploshchad }}
               </td>
               <td class="px-6 py-4">
                  {{ item.god_postroyki }}
               </td>
               <td class="px-6 py-4">
                  {{ item.kapremont_date }}
               </td>
               <!-- <td colspan="10">
                  <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                     <tr>
                        
                     </tr>
                     <tr class="bg-gray-100 border-b border-gray-500 text-gray-900">
                        <td colspan="10" class="px-6 py-4">
                           111
                        </td>
                     </tr>
                  </table>
               </td> -->
            </tr>
            <tr>
               <td colspan="10">122313</td>
            </tr>
         </tbody>
      </table>
   </div>

</template>
<!-- <template>  
   <div>  
      <h1 v-if="data">{{ data }}</h1>  
         <p v-if="pending">Loading...</p>  
      <p v-if="error">{{ error.message }}</p>  
   </div>  
</template>  -->
