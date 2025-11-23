<script setup>
const colorMode = useColorMode()

const isDark = computed(() => colorMode.value === 'dark')

function toggleDarkMode() {
  colorMode.preference = isDark.value ? 'light' : 'dark'
}
</script>

<template>
  <button @click="toggleDarkMode" class="p-2 bg-gray-200 dark:bg-gray-700 rounded-md flex items-center">
    <span v-if="!isDark">Dark</span>
    <span v-else>Light</span>
  </button>
</template>
