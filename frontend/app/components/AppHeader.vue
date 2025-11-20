<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'

const route = useRoute()

const items = computed<NavigationMenuItem[]>(() => [{
    label: 'Main',
    to: '/',
    icon: 'i-lucide-book-open',
    active: route.path.startsWith('/docs/getting-started')
}, {
    label: 'About',
    to: '/about',
    icon: 'i-lucide-box',
    active: route.path.startsWith('/docs/components')
}, 
// {
//     label: 'Figma',
//     icon: 'i-simple-icons-figma',
//     to: 'https://go.nuxt.com/figma-ui',
//     target: '_blank'
// }, {
//     label: 'Releases',
//     icon: 'i-lucide-rocket',
//     to: 'https://github.com/nuxt/ui/releases',
//     target: '_blank'
// }
])
</script>

<template>
    <UHeader>
        <template #left>
            <NuxtLink to="/">
                LOGO
            </NuxtLink>

            <UNavigationMenu :items="items" />
        </template>


        <template #right>
            <UColorModeButton />

            <!-- <UTooltip text="Open on GitHub" :kbds="['meta', 'G']">
                <UButton color="neutral" variant="ghost" to="https://github.com/nuxt/ui" target="_blank"
                    icon="i-simple-icons-github" aria-label="GitHub" />
            </UTooltip> -->
        </template>

        <template #body>
            <UNavigationMenu :items="items" orientation="vertical" class="-mx-2.5" />
        </template>
    </UHeader>
</template>

<!-- <template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <NuxtLink class="navbar-brand" to="/">Apartment Analysis</NuxtLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/">Home</a>
                    </li>
                    <li class="nav-item">
                        <NuxtLink class="nav-link" to="/about">About</NuxtLink>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template> -->