import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  css: ['~/assets/css/tailwind.css'],
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
    '@nuxtjs/i18n',
    '@vite-pwa/nuxt',
  ],
  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE_URL || 'http://localhost:8000',
    },
  },
  pwa: {
    registerType: 'autoUpdate',
    manifest: {
      name: 'Kipesa',
      short_name: 'Kipesa',
      theme_color: '#1db954',
      background_color: '#fff',
      display: 'standalone',
      lang: 'en',
    },
  },
  typescript: {
    strict: true,
    shim: false,
  },
}) 