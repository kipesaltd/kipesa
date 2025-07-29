import { defineStore } from 'pinia'
import { useApi } from '~/composables/useApi'
import type { 
  ChatState, 
  Message, 
  ChatRequest, 
  ConversationCreate, 
  ChatResponse,
  ConversationResponse,
  ChatbotFeedback,
  ChatbotAnalytics
} from '~/types/chatbot'
import { Language, MessageRole } from '~/types/chatbot'

export const useChatbotStore = defineStore('chatbot', {
  state: (): ChatState => ({
    conversation_id: undefined,
    messages: [],
    language: Language.ENGLISH,
    loading: false,
    error: null,
    typing: false
  }),

  getters: {
    isConversationStarted: (state) => !!state.conversation_id,
    lastMessage: (state) => state.messages[state.messages.length - 1],
    userMessages: (state) => state.messages.filter(msg => msg.role === MessageRole.USER),
    assistantMessages: (state) => state.messages.filter(msg => msg.role === MessageRole.ASSISTANT),
    totalMessages: (state) => state.messages.length
  },

  actions: {
    async startConversation(initialMessage: string, language: Language = Language.ENGLISH) {
      this.loading = true
      this.error = null
      
      try {
        const api = useApi()
        const payload: ConversationCreate = {
          initial_message: initialMessage,
          language,
          context: {
            user_agent: navigator.userAgent,
            timestamp: new Date().toISOString()
          }
        }

        const response: ConversationResponse = await api.post('/chatbot/conversation', payload)
        
        this.conversation_id = response.conversation_id
        this.messages = response.messages
        this.language = response.language
        
        return response
      } catch (error: any) {
        this.error = error.response?.data?.detail || 'Failed to start conversation'
        throw error
      } finally {
        this.loading = false
      }
    },

    async sendMessage(message: string) {
      if (!message.trim()) return
      
      this.loading = true
      this.error = null
      this.typing = true

      // Add user message immediately
      const userMessage: Message = {
        role: MessageRole.USER,
        content: message,
        timestamp: new Date().toISOString()
      }
      this.messages.push(userMessage)

      try {
        const api = useApi()
        const payload: ChatRequest = {
          message,
          conversation_id: this.conversation_id,
          language: this.language,
          context: {
            user_agent: navigator.userAgent,
            timestamp: new Date().toISOString()
          }
        }

        const response: ChatResponse = await api.post('/chatbot/chat', payload)
        
        // Update conversation ID if this is a new conversation
        if (!this.conversation_id) {
          this.conversation_id = response.conversation_id
        }

        // Add assistant response
        const assistantMessage: Message = {
          role: MessageRole.ASSISTANT,
          content: response.message,
          timestamp: new Date().toISOString(),
          metadata: {
            confidence: response.confidence,
            intent: response.intent,
            sentiment: response.sentiment,
            response_time: response.response_time
          }
        }
        this.messages.push(assistantMessage)

        return response
      } catch (error: any) {
        this.error = error.response?.data?.detail || 'Failed to send message'
        // Remove the user message if the request failed
        this.messages.pop()
        throw error
      } finally {
        this.loading = false
        this.typing = false
      }
    },

    async loadConversationHistory(conversationId: string) {
      this.loading = true
      this.error = null
      
      try {
        const api = useApi()
        const response = await api.get(`/chatbot/conversation/${conversationId}`)
        
        this.conversation_id = response.conversation_id
        this.messages = response.messages
        
        return response
      } catch (error: any) {
        this.error = error.response?.data?.detail || 'Failed to load conversation history'
        throw error
      } finally {
        this.loading = false
      }
    },

    async submitFeedback(messageId: string, rating: number, feedback?: string, helpful: boolean = true) {
      if (!this.conversation_id) return
      
      try {
        const api = useApi()
        const payload: ChatbotFeedback = {
          conversation_id: this.conversation_id,
          message_id: messageId,
          rating,
          feedback,
          helpful
        }

        await api.post('/chatbot/feedback', payload)
      } catch (error: any) {
        console.error('Failed to submit feedback:', error)
      }
    },

    async getAnalytics(startDate?: string, endDate?: string): Promise<ChatbotAnalytics | null> {
      try {
        const api = useApi()
        const params = new URLSearchParams()
        if (startDate) params.append('start_date', startDate)
        if (endDate) params.append('end_date', endDate)
        
        const url = `/chatbot/analytics${params.toString() ? `?${params.toString()}` : ''}`
        return await api.get(url)
      } catch (error: any) {
        console.error('Failed to get analytics:', error)
        return null
      }
    },

    async getSupportedLanguages() {
      try {
        const api = useApi()
        return await api.get('/chatbot/languages')
      } catch (error: any) {
        console.error('Failed to get supported languages:', error)
        return []
      }
    },

    async getSupportedIntents() {
      try {
        const api = useApi()
        return await api.get('/chatbot/intents')
      } catch (error: any) {
        console.error('Failed to get supported intents:', error)
        return []
      }
    },

    async checkHealth() {
      try {
        const api = useApi()
        return await api.get('/chatbot/health')
      } catch (error: any) {
        console.error('Chatbot health check failed:', error)
        return false
      }
    },

    setLanguage(language: Language) {
      this.language = language
    },

    clearConversation() {
      this.conversation_id = undefined
      this.messages = []
      this.error = null
      this.loading = false
      this.typing = false
    },

    addMessage(message: Message) {
      this.messages.push(message)
    },

    setTyping(typing: boolean) {
      this.typing = typing
    },

    setError(error: string | null) {
      this.error = error
    }
  }
}) 