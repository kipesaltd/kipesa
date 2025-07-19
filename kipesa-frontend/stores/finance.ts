import { defineStore } from 'pinia'
import { useApi } from '~/composables/useApi'

export const useFinanceStore = defineStore('finance', {
  state: () => ({
    incomeSources: [] as any[],
    expenses: [] as any[],
    budgets: [] as any[],
    savingsGoals: [] as any[],
    loading: false,
    error: null as null | string,
  }),
  actions: {
    async fetchIncomeSources() {
      this.loading = true
      this.error = null
      try {
        const api = useApi()
        console.log('Finance store: Fetching income sources...')
        const response = await api.get('/finance/income-sources')
        console.log('Finance store: Income sources response:', response)
        this.incomeSources = response
        console.log('Finance store: Updated income sources:', this.incomeSources)
      } catch (e: any) {
        console.error('Finance store: Error fetching income sources:', e)
        this.error = e.response?.data?.detail || 'Failed to fetch income sources'
      } finally {
        this.loading = false
      }
    },
    async createIncomeSource(incomeData: {
      name: string
      amount: number
      frequency?: string
      description?: string
    }) {
      this.loading = true
      this.error = null
      console.log('Finance store: Creating income source with data:', incomeData)
      try {
        const api = useApi()
        const response = await api.post('/finance/income-sources', incomeData)
        console.log('Finance store: Create income source response:', response)
        // Refresh the income sources list
        console.log('Finance store: Refreshing income sources list...')
        await this.fetchIncomeSources()
        return response
      } catch (e: any) {
        this.error = e.response?.data?.detail || 'Failed to create income source'
        console.error('Create income source error:', e)
        throw e
      } finally {
        this.loading = false
      }
    },
    async fetchExpenses() {
      this.loading = true
      this.error = null
      try {
        const api = useApi()
        const response = await api.get('/finance/expenses')
        this.expenses = response
      } catch (e: any) {
        this.error = e.response?.data?.detail || 'Failed to fetch expenses'
      } finally {
        this.loading = false
      }
    },
    async fetchBudgets() {
      this.loading = true
      this.error = null
      try {
        const api = useApi()
        const response = await api.get('/finance/budgets')
        this.budgets = response
      } catch (e: any) {
        this.error = e.response?.data?.detail || 'Failed to fetch budgets'
      } finally {
        this.loading = false
      }
    },
    async fetchSavingsGoals() {
      this.loading = true
      this.error = null
      try {
        const api = useApi()
        const response = await api.get('/finance/savings-goals')
        this.savingsGoals = response
      } catch (e: any) {
        this.error = e.response?.data?.detail || 'Failed to fetch savings goals'
      } finally {
        this.loading = false
      }
    },
  },
}) 