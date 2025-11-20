<script setup>
const props = defineProps(['item'])

const fields = {
   "price": "Цена",
   "address": "Адрес",
   "kolichestvo_komnat": "Кол-во комнат",
   "obshchaya_ploshchad": "Общая площадь",
   "god_postroyki": "Год постройки",
   "kapremont_date": "Дата капремонта",
   "etazh_val": "Этаж",
   "etazh_count": "Этажей",
}
const kapremontColor = computed(() => {
   let cls = ""
   // console.log(props["item"]["kapremont_date"])
   if ((props["item"]["kapremont_date"] - 2025) <= 5) {
      cls = "bg-danger-subtle"
   }
   return cls
})

</script>


<template>
   <UPageCard 
      :title=item.title
      :description=item.address
      orientation="horizontal">

      <img v-bind:src="'/public/images/' + item['id'] + '/main.jpg'" class="w-50" alt="...">
      <!-- <img src="/tailwindcss-v4.svg" alt="Tailwind CSS" class="w-full" /> -->
   </UPageCard>
</template>

<!-- <template>
   <div class="card mb-3">
      <div class="row g-0">
         <div class="col-md-9">
            <div class="card-body">
               <h5 class="card-title"><span class="badge text-bg-secondary">{{ item["id"] }}</span> {{ item["title"] }}
               </h5>
               <h5 class="card-title">{{ item["address"] }}</h5>
               <p class="card-text"></p>

               <div class="d-block">
                  <div class="d-inline-flex p-2 m-1 border">
                     {{ fields["price"] }}
                     <span class="badge text-bg-light">{{ item["price"] }}</span>
                  </div>
                  <div class="d-inline-flex p-2 m-1 border">
                     {{ fields["god_postroyki"] }}
                     <span class="badge text-bg-light">{{ item["god_postroyki"] }}</span>
                  </div>
                  <div class="d-inline-flex p-2 m-1 border">
                     {{ fields["kolichestvo_komnat"] }}
                     <span class="badge text-bg-light">{{ item["kolichestvo_komnat"] }}</span>
                  </div>
                  <div class="d-inline-flex p-2 m-1 border">
                     {{ fields["obshchaya_ploshchad"] }}
                     <span class="badge text-bg-light">{{ item["obshchaya_ploshchad"] }}</span>
                  </div>
                  <div class="d-inline-flex p-2 m-1 border" :class="kapremontColor">
                     {{ fields["kapremont_date"] }}
                     <span class="badge text-bg-light" >{{ item["kapremont_date"] }}</span>
                  </div>
                  <div class="d-inline-flex p-2 m-1 border">
                     {{ fields["etazh_val"] }}
                     <span class="badge text-bg-light">{{ item["etazh_val"] }}</span>
                  </div>
                  <div class="d-inline-flex p-2 m-1 border">
                     {{ fields["etazh_count"] }}
                     <span class="badge text-bg-light">{{ item["etazh_count"] }}</span>
                  </div>
               </div>



            </div>
         </div>
         <div class="col-md-3 d-flex justify-content-end">
            <img v-bind:src="'/public/images/' + item['id'] + '/main.jpg'" class="img-fluid rounded-end" width="250"
               alt="...">
         </div>
      </div>
   </div>
</template> -->