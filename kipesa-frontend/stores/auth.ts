import { defineStore } from 'pinia'
import { useApi } from '~/composables/useApi'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as null | Record<string, any>,
    token: null as null | string,
    loading: false,
    error: null as null | string,
  }),
  actions: {
    async login(email: string, password: string) {
      this.loading = true
      this.error = null
      try {
        const api = useApi()
        const response = await api.post('/auth/login', { email, password })
        this.token = response.access_token
        if (process.client && this.token) {
          localStorage.setItem('kipesa_token', this.token)
        }
        await this.fetchProfile()
      } catch (e: any) {
        this.error = e.response?.data?.detail || 'Login failed'
        this.token = null
        if (process.client) localStorage.removeItem('kipesa_token')
      } finally {
        this.loading = false
      }
    },
    async register(payload: Record<string, any>) {
      this.loading = true
      this.error = null
      try {
        const api = useApi()
        await api.post('/auth/register', payload)
      } catch (e: any) {
        this.error = e.response?.data?.detail || 'Registration failed'
      } finally {
        this.loading = false
      }
    },
    async fetchProfile() {
      if (!this.token) return
      try {
        const api = useApi()
        const response = await api.get('/auth/profile')
        this.user = response
      } catch (e: any) {
        this.user = null
        this.error = e.response?.data?.detail || 'Failed to fetch profile'
      }
    },
    logout() {
      this.user = null
      this.token = null
      if (process.client) localStorage.removeItem('kipesa_token')
    },
    init() {
      if (process.client) {
        const storedToken = localStorage.getItem('kipesa_token')
        if (storedToken) {
          this.token = storedToken
          this.fetchProfile()
        }
      }
    }
  },
}) 