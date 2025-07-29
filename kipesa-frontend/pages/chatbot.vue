<template>
  <div class="min-h-screen bg-gray-50">
    
    <!-- Main Content -->
    <div class="flex h-[calc(100vh-64px)]">
      <!-- Chat Interface -->
      <div class="flex-1">
        <ChatInterface />
      </div>
      
      <!-- Sidebar (Optional - for future features) -->
      <div class="hidden lg:block w-80 bg-white border-l border-gray-200 p-6">
        <div class="space-y-6">
          <!-- Conversation Info -->
          <div v-if="isConversationStarted">
            <h3 class="text-lg font-semibold text-gray-900 mb-3">Conversation Info</h3>
            <div class="space-y-2 text-sm">
              <div class="flex justify-between">
                <span class="text-gray-500">Messages:</span>
                <span class="font-medium">{{ totalMessages }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-500">Language:</span>
                <span class="font-medium">{{ languageLabel }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-500">Started:</span>
                <span class="font-medium">{{ conversationStartTime }}</span>
              </div>
            </div>
          </div>
          
          <!-- Quick Actions -->
          <div>
            <h3 class="text-lg font-semibold text-gray-900 mb-3">Quick Actions</h3>
            <div class="space-y-2">
              <button
                @click="exportConversation"
                :disabled="!isConversationStarted"
                class="w-full text-left p-3 text-sm bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors disabled:opacity-50"
              >
                📄 Export Conversation
              </button>
              <button
                @click="shareConversation"
                :disabled="!isConversationStarted"
                class="w-full text-left p-3 text-sm bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors disabled:opacity-50"
              >
                🔗 Share Conversation
              </button>
            </div>
          </div>
          
          <!-- Help -->
          <div>
            <h3 class="text-lg font-semibold text-gray-900 mb-3">Help</h3>
            <div class="space-y-2 text-sm text-gray-600">
              <p>💡 You can ask me about:</p>
              <ul class="list-disc list-inside space-y-1 ml-2">
                <li>Budget planning</li>
                <li>Investment advice</li>
                <li>Banking services</li>
                <li>Tax information</li>
                <li>Financial goals</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { Language } from '~/types/chatbot'
import { useChatbotStore } from '~/stores/chatbot'
import ChatInterface from '~/components/chat/ChatInterface.vue'

const chatbotStore = useChatbotStore()

// Computed properties
const isConversationStarted = computed(() => chatbotStore.isConversationStarted)
const totalMessages = computed(() => chatbotStore.totalMessages)
const languageLabel = computed(() => {
  return chatbotStore.language === Language.ENGLISH ? 'English' : 'Swahili'
})
const conversationStartTime = computed(() => {
  if (!chatbotStore.messages.length) return 'N/A'
  const firstMessage = chatbotStore.messages[0]
  return firstMessage ? new Date(firstMessage.timestamp).toLocaleTimeString() : 'N/A'
})

// Methods
const exportConversation = () => {
  if (!isConversationStarted.value) return
  
  const conversationText = chatbotStore.messages
    .map(msg => `${msg.role === 'user' ? 'You' : 'Kipesa'}: ${msg.content}`)
    .join('\n\n')
  
  const blob = new Blob([conversationText], { type: 'text/plain' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `kipesa-conversation-${new Date().toISOString().split('T')[0]}.txt`
  a.click()
  URL.revokeObjectURL(url)
}

const shareConversation = () => {
  if (!isConversationStarted.value) return
  
  const conversationText = chatbotStore.messages
    .map(msg => `${msg.role === 'user' ? 'You' : 'Kipesa'}: ${msg.content}`)
    .join('\n\n')
  
  if (navigator.share) {
    navigator.share({
      title: 'Kipesa Conversation',
      text: conversationText
    })
  } else {
    // Fallback to clipboard
    navigator.clipboard.writeText(conversationText)
    alert('Conversation copied to clipboard!')
  }
}

// Set page title
useHead({
  title: 'Chatbot - Kipesa'
})
</script> 