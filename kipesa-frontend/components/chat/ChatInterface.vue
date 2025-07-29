<template>
  <div class="flex flex-col h-full bg-gray-50">
    <!-- Header -->
    <div class="bg-white border-b border-gray-200 px-6 py-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center">
            <span class="text-white font-bold text-lg">K</span>
          </div>
          <div>
            <h1 class="text-lg font-semibold text-gray-900">Kipesa Chat</h1>
            <p class="text-sm text-gray-500">
              {{ isConversationStarted ? 'Active conversation' : 'Start a conversation' }}
            </p>
          </div>
        </div>
        
        <div class="flex items-center gap-2">
          <!-- Health Status -->
          <div class="flex items-center gap-1">
            <div class="w-2 h-2 rounded-full" :class="healthStatus.color"></div>
            <span class="text-xs text-gray-500">{{ healthStatus.text }}</span>
          </div>
          
          <!-- Actions -->
          <button
            @click="clearConversation"
            class="text-gray-400 hover:text-gray-600 transition-colors"
            title="Clear conversation"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Messages Container -->
    <div 
      ref="messagesContainer"
      class="flex-1 overflow-y-auto px-4 py-2 space-y-2"
      :class="{ 'opacity-50': loading }"
    >
      <!-- Welcome Message -->
      <div v-if="!isConversationStarted && messages.length === 0" class="text-center py-8">
        <div class="max-w-md mx-auto">
          <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg class="w-8 h-8 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
            </svg>
          </div>
          <h2 class="text-xl font-semibold text-gray-900 mb-2">Welcome to Kipesa AI</h2>
          <p class="text-gray-600 mb-6">
            I'm here to help you with financial advice, budgeting, investments, and more. 
            Ask me anything about personal finance!
          </p>
          
          <!-- Quick Start Buttons -->
          <div class="grid grid-cols-1 gap-3">
            <button
              v-for="starter in starterMessages"
              :key="starter.message"
              @click="startConversation(starter.message)"
              :disabled="loading"
              class="text-left p-4 bg-white border border-gray-200 rounded-lg hover:border-blue-300 hover:bg-blue-50 transition-colors disabled:opacity-50"
            >
              <div class="font-medium text-gray-900">{{ starter.title }}</div>
              <div class="text-sm text-gray-500">{{ starter.message }}</div>
            </button>
          </div>
        </div>
      </div>

      <!-- Messages -->
      <template v-else>
        <ChatMessage
          v-for="message in messages"
          :key="`${message.timestamp}-${message.content.substring(0, 10)}`"
          :message="message"
        />
      </template>

      <!-- Typing Indicator -->
      <TypingIndicator v-if="typing" />
    </div>

    <!-- Error Banner -->
    <div v-if="error" class="bg-red-50 border-t border-red-200 px-6 py-3">
      <div class="flex items-center gap-2">
        <svg class="w-5 h-5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        <span class="text-sm text-red-700">{{ error }}</span>
        <button @click="clearError" class="ml-auto text-red-500 hover:text-red-700">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- Message Input -->
    <MessageInput
      :disabled="loading"
      :loading="loading"
      :error="error"
      @send="handleSendMessage"
      @language-change="handleLanguageChange"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, nextTick, watch } from 'vue'
import { Language } from '~/types/chatbot'
import { useChatbotStore } from '~/stores/chatbot'
import ChatMessage from './ChatMessage.vue'
import TypingIndicator from './TypingIndicator.vue'
import MessageInput from './MessageInput.vue'

const chatbotStore = useChatbotStore()
const messagesContainer = ref<HTMLDivElement>()

// Computed properties
const messages = computed(() => chatbotStore.messages)
const loading = computed(() => chatbotStore.loading)
const error = computed(() => chatbotStore.error)
const typing = computed(() => chatbotStore.typing)
const isConversationStarted = computed(() => chatbotStore.isConversationStarted)

const healthStatus = computed(() => {
  // This would be updated based on actual health check
  return { color: 'bg-green-500', text: 'Connected' }
})

const starterMessages = [
  {
    title: '💰 Budget Planning',
    message: 'Help me create a monthly budget for my income and expenses'
  },
  {
    title: '💳 Investment Advice',
    message: 'What are the best investment options for a beginner in Tanzania?'
  },
  {
    title: '🏦 Banking Questions',
    message: 'Explain the different types of bank accounts available in Tanzania'
  },
  {
    title: '📊 Financial Analysis',
    message: 'How can I analyze my spending patterns and improve my finances?'
  }
]

// Methods
const startConversation = async (message: string) => {
  try {
    await chatbotStore.startConversation(message, chatbotStore.language)
    scrollToBottom()
  } catch (err) {
    console.error('Failed to start conversation:', err)
  }
}

const handleSendMessage = async (message: string, language: Language) => {
  try {
    if (!isConversationStarted.value) {
      await startConversation(message)
    } else {
      await chatbotStore.sendMessage(message)
    }
    scrollToBottom()
  } catch (err) {
    console.error('Failed to send message:', err)
  }
}

const handleLanguageChange = (language: Language) => {
  chatbotStore.setLanguage(language)
}

const clearConversation = () => {
  chatbotStore.clearConversation()
}

const clearError = () => {
  chatbotStore.setError(null)
}

const scrollToBottom = () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}

// Watch for new messages and scroll to bottom
watch(messages, () => {
  scrollToBottom()
}, { deep: true })

// Health check on mount
onMounted(async () => {
  try {
    await chatbotStore.checkHealth()
  } catch (err) {
    console.error('Health check failed:', err)
  }
})
</script> 