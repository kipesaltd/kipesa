<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <Navigation />
    <main class="container mx-auto py-8">
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
import Navigation from '~/components/molecules/Navigation.vue';
</script> 