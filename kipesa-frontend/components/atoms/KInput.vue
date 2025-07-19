<template>
  <input
    v-bind="$attrs"
    :type="type"
    :placeholder="placeholder"
    :value="modelValue"
    @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    class="block w-full px-3 py-2 border border-gray-300 rounded focus:ring-kipesa-green focus:border-kipesa-green dark:bg-gray-800 dark:text-white"
  />
</template>

<script setup lang="ts">
defineProps({
  type: { type: String, default: 'text' },
  placeholder: { type: String, default: '' },
  modelValue: { type: String, default: '' },
})

defineEmits(['update:modelValue'])
</script> 