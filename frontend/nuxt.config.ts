// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devServer: {
    port: 5173,
    host: '0.0.0.0'  // Разрешить подключения из Docker
  },
  // vite: {
  //   server: {
  //     hmr: {
  //       protocol: 'ws',
  //       host: 'service.frontend',           // Имя сервиса Docker
  //       port: 5173,
  //       clientPort: 1337         // Порт прокси (NGINX)
  //     }
  //   }
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
