<script setup>
const props = defineProps(['count'])
const emit = defineEmits(['getpaginationPageNumber'])

function onNextPage(event, page) {
    emit('getpaginationPageNumber', page)
}


</script>
<template>
    {{ props["count"] }}
    <nav aria-label="...">
        <ul class="pagination">
            <li class="page-item disabled">
                <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item active" aria-current="page">
                <a class="page-link" href="#" @click="onNextPage($event, 2)">2</a>
            </li>
            <li class="page-item"><a class="page-link" href="#" @click="onNextPage($event, 3)">3</a></li>
            <li class="page-item">
                <a class="page-link" href="#">Next</a>
            </li>
        </ul>
    </nav>
</template>