<script setup>
const props = defineProps(['list'])
</script>

<template>

    <div class="flex justify-center m-2 w-full gap-2">
        <div class="" v-for="value in props['list']['list']">
            <div class="p-2 rounded-sm text-nowrap text-sm" :class="props['list']['bgColor']">{{ value["label"] }}</div>
        </div>
    </div>

</template>