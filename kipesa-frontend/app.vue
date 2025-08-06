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