import { ref, computed } from 'vue'
import { useChatbotStore } from '~/stores/chatbot'
import type { ChatbotAnalytics } from '~/types/chatbot'

export function useChatAnalytics() {
  const chatbotStore = useChatbotStore()
  const analytics = ref<ChatbotAnalytics | null>(null)
  const loading = ref(false)

  const fetchAnalytics = async (startDate?: string, endDate?: string) => {
    loading.value = true
    try {
      analytics.value = await chatbotStore.getAnalytics(startDate, endDate)
    } catch (error) {
      console.error('Failed to fetch analytics:', error)
    } finally {
      loading.value = false
    }
  }

  const conversationMetrics = computed(() => {
    if (!analytics.value) return null

    return {
      totalConversations: analytics.value.total_conversations,
      totalMessages: analytics.value.total_messages,
      averageResponseTime: analytics.value.average_response_time,
      averageConfidence: analytics.value.average_confidence,
      messagesPerConversation: analytics.value.total_conversations > 0 
        ? (analytics.value.total_messages / analytics.value.total_conversations).toFixed(1)
        : '0'
    }
  })

  const languageDistribution = computed(() => {
    if (!analytics.value?.language_distribution) return []
    
    return Object.entries(analytics.value.language_distribution).map(([lang, count]) => ({
      language: lang === 'en' ? 'English' : 'Swahili',
      count,
      percentage: ((count / analytics.value!.total_conversations) * 100).toFixed(1)
    }))
  })

  const topIntents = computed(() => {
    return analytics.value?.top_intents || []
  })

  const sentimentDistribution = computed(() => {
    if (!analytics.value?.sentiment_distribution) return []
    
    return Object.entries(analytics.value.sentiment_distribution).map(([sentiment, count]) => ({
      sentiment,
      count,
      percentage: ((count / analytics.value!.total_messages) * 100).toFixed(1)
    }))
  })

  const performanceScore = computed(() => {
    if (!analytics.value) return 0
    
    const responseTimeScore = Math.max(0, 100 - (analytics.value.average_response_time * 10))
    const confidenceScore = analytics.value.average_confidence * 100
    
    return Math.round((responseTimeScore + confidenceScore) / 2)
  })

  const getPerformanceColor = (score: number) => {
    if (score >= 80) return 'text-green-600'
    if (score >= 60) return 'text-yellow-600'
    return 'text-red-600'
  }

  const getPerformanceLabel = (score: number) => {
    if (score >= 80) return 'Excellent'
    if (score >= 60) return 'Good'
    if (score >= 40) return 'Fair'
    return 'Poor'
  }

  return {
    analytics,
    loading,
    fetchAnalytics,
    conversationMetrics,
    languageDistribution,
    topIntents,
    sentimentDistribution,
    performanceScore,
    getPerformanceColor,
    getPerformanceLabel
  }
} 