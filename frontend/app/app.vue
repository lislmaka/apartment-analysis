<script setup lang="ts">
const { data } = await useFetch('http://service.backend:8000/api/')
// const { data } = await useFetch('https://fakeapi.extendsclass.com/books')

</script>

<template>
  <p>Page visits: {{ data }}</p>
</template>
