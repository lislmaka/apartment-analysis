<script setup>
// const { data, pending, error } = await useFetch('http://service.backend:8000/api/')
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

// const countProjects = computed(() => {
//    return data.value.length > 0 ? data.value.length : 0
// })
// function sortedData1() {
//    if (!data?.value) return []
//    return [data.value].sort((a: any, b: any) => {
//       console.log(a.price, b.price)
//       // Пример: сортировка по полю `name` (алфавитно)
//       return parseFloat(a.price) - parseFloat(b.price);
//    })
// }
// function sortedData2() {
//    if (!data?.value) return []
//    console.log("sdfsffdf222")
//    return [data.value].sort((a: any, b: any) => {
//       // Пример: сортировка по полю `name` (алфавитно)
//       return parseFloat(b.price) - parseFloat(a.price);
//    })
// }
</script>

<template>

   <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">Serch text:({{ countProjects }}) {{ message }}</label>
      <input v-model="message" type="text" class="form-control" id="exampleFormControlInput1" placeholder="">
   </div>

   <div v-if="data">
      <div class="card mb-3" v-for="item in filteredProjects" :key="item['id']">
         <!-- {{ data }} -->
         <div class="row g-0">
            <div class="col-md-9">
               <div class="card-body">
                  <h5 class="card-title">{{ item["id"] }} {{ item["title"] }}</h5>
                  <p class="card-text">Price {{ item["price"] }}</p>
                  <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
                  <!-- <a href="#" @click="sortedData1" class="list-group-item list-group-item-action">Sort1</a>
                  <a href="#" @click="sortedData2" class="list-group-item list-group-item-action">Sort2</a> -->
               </div>
            </div>
            <div class="col-md-3 d-flex justify-content-end">
               <img v-bind:src="'/public/images/' + item['id'] + '/main.jpg'" class="img-fluid rounded-end" width="250"
                  alt="...">
            </div>
         </div>
      </div>
   </div>
   <p v-if="pending">Loading...</p>
   <p v-if="error">{{ error.message }}</p>

</template>