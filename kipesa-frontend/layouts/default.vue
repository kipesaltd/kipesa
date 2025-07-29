<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <KNavBar />
    <main class="max-w-4xl mx-auto py-8 px-4">
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
import KNavBar from '~/components/molecules/KNavBar.vue'
</script> 