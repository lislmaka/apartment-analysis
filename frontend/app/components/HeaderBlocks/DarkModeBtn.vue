<script setup>

const colorMode = useColorMode()

const isDark = computed(() => colorMode.value === 'dark')

function toggleDarkMode() {
  colorMode.preference = isDark.value ? 'light' : 'dark'
}
</script>

<template>
  <button @click="toggleDarkMode" class="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded-md flex items-center">
    <span v-if="!isDark">Dark</span>
    <span v-else>Light</span>
  </button>
</template>
