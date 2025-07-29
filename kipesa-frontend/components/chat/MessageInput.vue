<template>
  <div class="border-t border-gray-200 bg-white p-4">
    <div class="flex items-end gap-3">
      <!-- Language Selector -->
      <div class="flex-shrink-0">
        <select 
          v-model="selectedLanguage"
          @change="onLanguageChange"
          class="text-xs border border-gray-300 rounded-md px-2 py-1 bg-white"
        >
          <option value="en">🇺🇸 English</option>
          <option value="sw">🇹🇿 Swahili</option>
        </select>
      </div>

      <!-- Message Input -->
      <div class="flex-1 relative">
        <textarea
          ref="textareaRef"
          v-model="message"
          @keydown="handleKeydown"
          @input="autoResize"
          placeholder="Type your message here..."
          class="w-full border border-gray-300 rounded-lg px-4 py-3 pr-12 resize-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          :class="{ 'opacity-50': disabled }"
          :disabled="disabled"
          rows="1"
          maxlength="2000"
        ></textarea>
        
        <!-- Character Count -->
        <div class="absolute bottom-2 right-2 text-xs text-gray-400">
          {{ message.length }}/2000
        </div>
      </div>

      <!-- Send Button -->
      <button
        @click="sendMessage"
        :disabled="!canSend || disabled"
        class="flex-shrink-0 bg-blue-500 text-white rounded-lg p-3 hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        :class="{ 'animate-pulse': loading }"
      >
        <svg v-if="!loading" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
        </svg>
        <div v-else class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
      </button>
    </div>

    <!-- Error Message -->
    <div v-if="error" class="mt-2 text-sm text-red-600 bg-red-50 border border-red-200 rounded-md p-2">
      {{ error }}
    </div>

    <!-- Quick Actions -->
    <div class="mt-3 flex flex-wrap gap-2">
      <button
        v-for="suggestion in quickSuggestions"
        :key="suggestion"
        @click="sendQuickMessage(suggestion)"
        :disabled="disabled"
        class="text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 px-3 py-1 rounded-full transition-colors disabled:opacity-50"
      >
        {{ suggestion }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, nextTick } from 'vue'
import { Language } from '~/types/chatbot'
import { useChatbotStore } from '~/stores/chatbot'

interface Props {
  disabled?: boolean
  loading?: boolean
  error?: string | null
}

const props = withDefaults(defineProps<Props>(), {
  disabled: false,
  loading: false,
  error: null
})

const emit = defineEmits<{
  send: [message: string, language: Language]
  languageChange: [language: Language]
}>()

const chatbotStore = useChatbotStore()
const message = ref('')
const selectedLanguage = ref<Language>(Language.ENGLISH)
const textareaRef = ref<HTMLTextAreaElement>()

const canSend = computed(() => message.value.trim().length > 0 && !props.disabled)

const quickSuggestions = computed(() => {
  const suggestions = {
    [Language.ENGLISH]: [
      "How can I save money?",
      "What are the best investment options?",
      "Help me create a budget",
      "Explain tax deductions"
    ],
    [Language.SWAHILI]: [
      "Ninawezaje kuweka pesa?",
      "Nini chaguo bora za uwekezaji?",
      "Nisaidie kutengeneza bajeti",
      "Elezea punguzo la kodi"
    ]
  }
  return suggestions[selectedLanguage.value]
})

const autoResize = () => {
  if (textareaRef.value) {
    textareaRef.value.style.height = 'auto'
    textareaRef.value.style.height = `${textareaRef.value.scrollHeight}px`
  }
}

const handleKeydown = (event: KeyboardEvent) => {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault()
    sendMessage()
  }
}

const sendMessage = async () => {
  if (!canSend.value) return
  
  const trimmedMessage = message.value.trim()
  message.value = ''
  
  // Reset textarea height
  if (textareaRef.value) {
    textareaRef.value.style.height = 'auto'
  }
  
  emit('send', trimmedMessage, selectedLanguage.value)
}

const sendQuickMessage = (suggestion: string) => {
  message.value = suggestion
  sendMessage()
}

const onLanguageChange = () => {
  emit('languageChange', selectedLanguage.value)
}

// Auto-resize on mount
nextTick(() => {
  autoResize()
})
</script> 