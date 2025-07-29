export enum Language {
  ENGLISH = "en",
  SWAHILI = "sw"
}

export enum MessageRole {
  USER = "user",
  ASSISTANT = "assistant",
  SYSTEM = "system"
}

export interface Message {
  role: MessageRole
  content: string
  timestamp: string
  metadata?: Record<string, any>
}

export interface ChatRequest {
  message: string
  conversation_id?: string
  language: Language
  user_id?: string
  context?: Record<string, any>
}

export interface ChatResponse {
  conversation_id: string
  message: string
  language: Language
  confidence: number
  intent?: string
  entities?: Array<Record<string, any>>
  sentiment?: string
  response_time: number
  metadata?: Record<string, any>
}

export interface ConversationCreate {
  initial_message: string
  language: Language
  user_id?: string
  context?: Record<string, any>
}

export interface ConversationResponse {
  conversation_id: string
  messages: Message[]
  language: Language
  created_at: string
  updated_at: string
  user_id?: string
  metadata?: Record<string, any>
}

export interface ConversationHistory {
  conversation_id: string
  messages: Message[]
  total_messages: number
  created_at: string
  updated_at: string
}

export interface ChatbotFeedback {
  conversation_id: string
  message_id: string
  rating: number
  feedback?: string
  helpful: boolean
}

export interface ChatbotAnalytics {
  total_conversations: number
  total_messages: number
  average_response_time: number
  average_confidence: number
  language_distribution: Record<string, number>
  top_intents: Array<Record<string, any>>
  sentiment_distribution: Record<string, number>
}

export interface ChatState {
  conversation_id?: string
  messages: Message[]
  language: Language
  loading: boolean
  error: string | null
  typing: boolean
} 