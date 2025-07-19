<template>
  <button
    :type="type"
    class="px-4 py-2 rounded font-semibold focus:outline-none focus:ring-2 focus:ring-kipesa-green bg-kipesa-green text-white hover:bg-kipesa-blue transition disabled:opacity-50"
    :disabled="disabled"
    v-bind="$attrs"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps({
  type: { type: String, default: 'submit' }, // Default to 'submit' for forms
  disabled: { type: Boolean, default: false },
})
</script> 