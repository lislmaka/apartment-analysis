<script setup>
const { globalCounter1 } = useGlobalData()

const urls = {
    main: {
        url: "/",
        label: "LOGO",
        icon: "",
    },
    flats: {
        url: "/flats",
        label: "Квартиры",
        icon: "i-lucide-book-open",
    },
    about: {
        url: "/about",
        label: "About",
        icon: "lucide:info",
    },
}

</script>
<template>
    <div class="flex justify-between sticky top-0 z-50 bg-white py-5">
        <div class="flex space-x-5 justify-start">
            <div class="flex items-center space-x-1 font-normal text-xl" v-for="url in urls">
                <template v-if="url['url'] == '/flats'">
                    <NuxtLink class="navbar-brand flex items-center space-x-1" :to="url['url']">
                        <div>{{ url['label'] }}</div>
                        <div class="bg-gray-400 text-white px-2 rounded-sm text-sm">{{ globalCounter1 }}</div>
                    </NuxtLink>
                </template>
                <template v-else>
                    <NuxtLink class="navbar-brand" :to="url['url']">{{ url['label'] }}</NuxtLink>
                </template>
            </div>
        </div>
        <div>
            <HeaderBlocksDarkModeBtn />
        </div>
    </div>
</template>