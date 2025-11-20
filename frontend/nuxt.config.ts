// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devServer: {
    host: '0.0.0.0', // Принимать подключения со всех интерфейсов
    // port: 3000
  },
  runtimeConfig: {
    baseURL: 'http://service.backend:8000/api/list/',
    public: {
      // baseURL: 'http://frontend-service:3000',
    },
  },
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: [
    // '@nuxtjs/tailwindcss',
    '@nuxt/ui',
  ],
  css: [
    // 'bootstrap/dist/css/bootstrap.min.css',
    '~/assets/css/main.css',
  ],
  plugins: [
    // { src: 'plugins/bootstrap.js', mode: 'client' }, 
  ],
})
