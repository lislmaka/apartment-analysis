<script setup lang="ts">
const { data, pending, error } = await useFetch('http://service.backend:8000/api/')
</script>

<template>  
   <div>  
      <h1 v-if="data">{{ data }}</h1>  
         <p v-if="pending">Loading...</p>  
      <p v-if="error">{{ error.message }}</p>  
   </div>  
</template> 