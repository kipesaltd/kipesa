<template>
  <div 
    :class="[
      'flex gap-3 p-4 transition-all duration-200',
      message.role === 'user' ? 'justify-end' : 'justify-start'
    ]"
  >
    <!-- User Message -->
    <div v-if="message.role === 'user'" class="flex flex-col items-end max-w-[80%]">
      <div class="bg-blue-500 text-white rounded-2xl rounded-br-md px-4 py-2 shadow-sm">
        <p class="text-sm whitespace-pre-wrap">{{ message.content }}</p>
      </div>
      <span class="text-xs text-gray-500 mt-1">
        {{ formatTime(message.timestamp) }}
      </span>
    </div>

    <!-- Assistant Message -->
    <div v-else-if="message.role === 'assistant'" class="flex flex-col items-start max-w-[80%]">
      <div class="bg-gray-100 text-gray-900 rounded-2xl rounded-bl-md px-4 py-2 shadow-sm">
        <div class="text-sm whitespace-pre-wrap" v-html="formatAssistantMessage(message.content)"></div>
        
        <!-- Message Metadata -->
        <div v-if="message.metadata" class="mt-2 pt-2 border-t border-gray-200">
          <div class="flex flex-wrap gap-2 text-xs text-gray-500">
            <span v-if="message.metadata.confidence" class="flex items-center gap-1">
              <span class="w-2 h-2 rounded-full" 
                :class="getConfidenceColor(message.metadata.confidence)">
              </span>
              {{ Math.round(message.metadata.confidence * 100) }}% confidence
            </span>
            <span v-if="message.metadata.intent" class="bg-blue-100 text-blue-700 px-2 py-1 rounded">
              {{ message.metadata.intent }}
            </span>
            <span v-if="message.metadata.sentiment" class="bg-green-100 text-green-700 px-2 py-1 rounded">
              {{ message.metadata.sentiment }}
            </span>
            <span v-if="message.metadata.response_time" class="text-gray-400">
              {{ formatResponseTime(message.metadata.response_time) }}
            </span>
          </div>
        </div>
      </div>
      
      <!-- Feedback Buttons -->
      <div class="flex gap-1 mt-2">
        <button 
          @click="submitFeedback(5, true)"
          class="text-xs text-gray-400 hover:text-green-500 transition-colors"
          title="Very helpful"
        >
          👍
        </button>
        <button 
          @click="submitFeedback(1, false)"
          class="text-xs text-gray-400 hover:text-red-500 transition-colors"
          title="Not helpful"
        >
          👎
        </button>
      </div>
      
      <span class="text-xs text-gray-500 mt-1">
        {{ formatTime(message.timestamp) }}
      </span>
    </div>

    <!-- System Message -->
    <div v-else class="flex justify-center w-full">
      <div class="bg-yellow-50 border border-yellow-200 text-yellow-800 rounded-lg px-3 py-2 text-xs">
        {{ message.content }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Message } from '~/types/chatbot'
import { useChatbotStore } from '~/stores/chatbot'

interface Props {
  message: Message
}

const props = defineProps<Props>()
const chatbotStore = useChatbotStore()

const formatTime = (timestamp: string) => {
  const date = new Date(timestamp)
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
}

const formatResponseTime = (time: number) => {
  return `${time.toFixed(1)}s`
}

const getConfidenceColor = (confidence: number) => {
  if (confidence >= 0.8) return 'bg-green-500'
  if (confidence >= 0.6) return 'bg-yellow-500'
  return 'bg-red-500'
}

const formatAssistantMessage = (content: string) => {
  return content
    // Replace markdown headers with HTML
    .replace(/^### (.*$)/gim, '<h3 class="font-semibold text-lg mb-2 text-gray-800">$1</h3>')
    .replace(/^## (.*$)/gim, '<h2 class="font-bold text-xl mb-3 text-gray-900">$1</h2>')
    .replace(/^# (.*$)/gim, '<h1 class="font-bold text-2xl mb-4 text-gray-900">$1</h1>')
    // Replace bold markdown with HTML
    .replace(/\*\*(.*?)\*\*/g, '<strong class="font-semibold">$1</strong>')
    // Replace italic markdown with HTML
    .replace(/\*(.*?)\*/g, '<em class="italic">$1</em>')
    // Replace code blocks
    .replace(/```([\s\S]*?)```/g, '<pre class="bg-gray-800 text-green-400 p-3 rounded-md text-xs overflow-x-auto my-2"><code>$1</code></pre>')
    // Replace inline code
    .replace(/`([^`]+)`/g, '<code class="bg-gray-200 text-gray-800 px-1 py-0.5 rounded text-xs">$1</code>')
    // Handle bullet lists more robustly
    .replace(/^[\s]*\- (.*$)/gim, '<li class="ml-4 mb-1">$1</li>')
    // Handle numbered lists
    .replace(/^[\s]*\d+\. (.*$)/gim, '<li class="ml-4 mb-1">$1</li>')
    // Wrap consecutive list items in ul tags
    .replace(/(<li.*<\/li>)+/g, (match) => `<ul class="list-disc space-y-1 my-2">${match}</ul>`)
    // Replace line breaks with proper spacing
    .replace(/\n\n/g, '</p><p class="my-2">')
    .replace(/\n/g, '<br>')
    // Wrap in paragraph tags for non-list content
    .replace(/^([^<].*)$/gm, '<p class="mb-2">$1</p>')
    // Clean up empty paragraphs
    .replace(/<p class="mb-2"><\/p>/g, '')
    // Clean up consecutive p tags
    .replace(/<\/p><p class="mb-2">/g, '</p><p class="mb-2">')
    // Remove extra paragraph tags around headers and lists
    .replace(/<p class="mb-2">(<h[1-6].*<\/h[1-6]>)<\/p>/g, '$1')
    .replace(/<p class="mb-2">(<ul.*<\/ul>)<\/p>/g, '$1')
    .replace(/<p class="mb-2">(<pre.*<\/pre>)<\/p>/g, '$1')
}

const submitFeedback = (rating: number, helpful: boolean) => {
  // Generate a simple message ID for feedback
  const messageId = `${props.message.timestamp}-${props.message.content.substring(0, 10)}`
  chatbotStore.submitFeedback(messageId, rating, undefined, helpful)
}
</script> 