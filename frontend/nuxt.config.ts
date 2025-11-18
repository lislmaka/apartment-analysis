// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devServer: {
    host: '0.0.0.0', // Принимать подключения со всех интерфейсов
    // port: 3000
  },
  // runtimeConfig: {
  //   app: {
  //     url: 'http://frontend-service:3000', // Docker service name
  //   },
  // },
  // app: {
  //   baseURL: '/',
  // },
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
  ],
  css: [
    'bootstrap/dist/css/bootstrap.min.css',
  ],
  plugins: [
    { src: 'plugins/bootstrap.js', mode: 'client' }, // load the plugin on client-side only
  ],
})
