<template>
  <div class="flex gap-3 p-4">
    <div class="flex flex-col items-start max-w-[80%]">
      <div class="bg-gray-100 text-gray-900 rounded-2xl rounded-bl-md px-4 py-3 shadow-sm">
        <div class="flex items-center gap-1">
          <div class="flex space-x-1">
            <div 
              v-for="i in 3" 
              :key="i"
              class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
              :style="{ animationDelay: `${(i - 1) * 0.1}s` }"
            ></div>
          </div>
          <span class="text-xs text-gray-500 ml-2">Kipesa is typing...</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// No props needed for this component
</script> 