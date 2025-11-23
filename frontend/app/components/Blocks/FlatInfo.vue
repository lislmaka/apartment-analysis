<script setup>
const props = defineProps(['title', 'list'])
</script>

<template>
    <div class="flex flex-col rounded-sm border border-gray-100">
        <div class="flex justify-between p-3 bg-gray-200 rounded-t-sm font-bold">
            <div>{{ props["title"] }}</div>
            <div class="bg-gray-100 px-3 rounded-sm">{{Object.keys(props['list']['list']).length}}</div>
        </div>
        <div class="flex flex-wrap justify-center gap-1 p-2">
            <div class="" v-for="value in props['list']['list']">
                <div class="p-2 rounded-sm text-nowrap text-sm" :class="props['list']['bgColor']">{{ value }}
                </div>
            </div>
        </div>
    </div>
</template>