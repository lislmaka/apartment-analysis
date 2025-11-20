<script setup>
const emit = defineEmits(['filters'])
// const emit = defineEmits(['enlarge-text'])
// const isChecked = computed(() => {
//     if (!message.value) {
//         countProjects.value = data.value.length
//         return data.value;
//     }
//     const lowerCaseSearchText = message.value.toLowerCase();
//     const d = data.value.filter(user => user.id.toString().includes(message.value));
//     countProjects.value = d.length
//     return d
// })

function isChecked(event) {
    if (event.target.checked) {
        emit('filters', '111')
    }
}

</script>
<template>
    <div class="flex flex-col rounded-xl bg-white outline outline-black/5  dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10">
        <div class="block bg-gray-50 p-3 text-xl font-medium text-black dark:text-white dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10">Фильтры</div>
        <div class="block p-3">
            <a href="#" @click="$emit('filters', 'pizza1')">Тестовый фильтр</a>
        </div>
    </div>
    <!-- <div class="card">
        <div class="card-header">
            Фильтры
        </div>
        <ul class="list-group list-group-flush">
            <a href="#" class="list-group-item list-group-item-action">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="checkDefault"
                        @click="isChecked($event)">
                    <label class="form-check-label" for="checkDefault">
                        Default checkbox
                    </label>
                </div>
            </a>
            <a href="#" class="list-group-item list-group-item-action">A second link item</a>
            <a href="#" class="list-group-item list-group-item-action">A third link item</a>
            <a href="#" class="list-group-item list-group-item-action">A fourth link item</a>
            <li class="list-group-item">A second item</li>
            <li class="list-group-item">A third item</li>
        </ul>
        <button @click="$emit('filters', 'pizza1')" type="button" class="btn btn-primary">Primary</button>
    </div> -->
</template>