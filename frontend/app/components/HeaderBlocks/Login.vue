<script setup>
const props = defineProps(['url'])
</script>

<template>
    <div class="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded-md flex items-center">
        <NuxtLink class="navbar-brand" :to="url['url']">Вход</NuxtLink>
    </div>
</template>