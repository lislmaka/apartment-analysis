<script setup>
definePageMeta({
    layout: 'empty',
})
</script>
<template>
    <div class="flex items-center justify-center h-screen">
        <div class="flex flex-col rounded-sm border border-gray-200 w-1/3">
            <div class="bg-gray-200 p-3 rounded-t-sm font-normal text-xl">Добро пожаловать</div>
            <div class="p-5 space-y-5">

                <label for="first_name" class="block mb-2.5 text-sm font-medium text-heading">Имя пользвателя</label>
                <input type="text" id="first_name"
                    class="bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand block w-full px-3 py-2.5 shadow-xs placeholder:text-body"
                    placeholder="John" required />

                <label for="first_name" class="block mb-2.5 text-sm font-medium text-heading">Пароль</label>
                <input type="text" id="first_name"
                    class="bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand block w-full px-3 py-2.5 shadow-xs placeholder:text-body"
                    placeholder="John" required />
            </div>
            <div class="flex p-3 rounded-b-sm border-t border-gray-200 justify-center items-center gap-3">
                <button class="bg-green-400 rounded-sm px-3 py-2 text-white">Регистрация</button>
                <button class="bg-green-400 rounded-sm px-3 py-2 text-white">Вход</button>
            </div>
            <div class="flex p-3 rounded-b-sm border-t border-gray-200 justify-center items-center gap-3">
                <NuxtLink class="navbar-brand" to="/">На главную</NuxtLink>
            </div>
            
        </div>
    </div>
</template>