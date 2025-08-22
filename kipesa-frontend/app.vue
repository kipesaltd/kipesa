<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template> 

<script setup lang="ts">
import { useAuthStore } from '~/stores/auth'
import { onMounted } from 'vue'

// Initialize auth store on app startup
const auth = useAuthStore()

// Only initialize on client side
onMounted(() => {
  auth.init()
})
</script> 

<style>
/* Archia Font Family */
@font-face {
  font-family: 'Archia';
  src: url('/fonts/Archia-Thin.otf') format('opentype');
  font-weight: 100;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Archia';
  src: url('/fonts/Archia-Light.otf') format('opentype');
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Archia';
  src: url('/fonts/Archia-Regular.otf') format('opentype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Archia';
  src: url('/fonts/Archia-Medium.otf') format('opentype');
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Archia';
  src: url('/fonts/Archia-SemiBold.otf') format('opentype');
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Archia';
  src: url('/fonts/Archia-Bold.otf') format('opentype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

/* Global Styles */
html {
  font-family: 'Archia', sans-serif;
}

body {
  font-family: 'Archia', sans-serif;
  line-height: 1.6;
  color: #333;
}

/* Custom utility classes */
.font-archia {
  font-family: 'Archia', sans-serif;
}
</style>
