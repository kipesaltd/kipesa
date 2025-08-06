<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">{{ $t('finance') }}</h1>
    <p class="mb-6">Manage your income, expenses, budgets, and savings goals here.</p>
    
    <!-- Add Income Source Form -->
    <div class="bg-white dark:bg-gray-800 rounded shadow p-6 mb-6">
      <h2 class="text-xl font-semibold mb-4">Add Income Source</h2>
      <form @submit.prevent="addIncomeSource" class="space-y-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <KInput 
            v-model="newIncome.name" 
            type="text" 
            placeholder="Income Source Name" 
            required 
          />
          <KInput 
            v-model="newIncome.amount" 
            type="number" 
            placeholder="Amount (TSh)" 
            required 
          />
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <KInput 
            v-model="newIncome.frequency" 
            type="text" 
            placeholder="Frequency (e.g., Monthly, Weekly)" 
          />
          <KInput 
            v-model="newIncome.description" 
            type="text" 
            placeholder="Description (optional)" 
          />
        </div>
        <KButton type="submit" :disabled="loading">
          {{ loading ? 'Adding...' : 'Add Income Source' }}
      </KButton>
      </form>
    </div>

    <!-- Income Sources List -->
    <div class="bg-white dark:bg-gray-800 rounded shadow p-6">
      <h2 class="text-xl font-semibold mb-4">Income Sources</h2>
      <div v-if="loading" class="text-center py-4">
        <p>Loading income sources...</p>
      </div>
      <div v-else-if="error" class="text-red-500 py-4">
        {{ error }}
      </div>
      <div v-else-if="incomeSources.length === 0" class="text-gray-500 py-4">
        <p>No income sources found. Add your first income source above.</p>
      </div>
      <ul v-else class="space-y-4">
        <li v-for="income in incomeSources" :key="income.id" class="border border-gray-200 dark:border-gray-700 rounded p-4">
          <div class="flex justify-between items-start">
            <div class="flex-1">
              <div class="font-semibold text-lg">{{ income.name }}</div>
              <div class="text-2xl font-bold text-kipesa-green">TSh {{ income.amount.toLocaleString() }}</div>
              <div v-if="income.frequency" class="text-sm text-gray-500 mt-1">
                Frequency: {{ income.frequency }}
              </div>
              <div v-if="income.description" class="text-sm text-gray-600 mt-1">
                {{ income.description }}
              </div>
            </div>
            <div class="text-xs text-gray-400">
              {{ new Date(income.created_at).toLocaleDateString() }}
            </div>
          </div>
      </li>
    </ul>
      
      <!-- Total Income Summary -->
      <div v-if="incomeSources.length > 0" class="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700">
        <div class="text-lg font-semibold">
          Total Monthly Income: 
          <span class="text-kipesa-green">
            TSh {{ totalMonthlyIncome.toLocaleString() }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useFinanceStore } from '~/stores/finance'
import KButton from '~/components/atoms/KButton.vue'
import KInput from '~/components/atoms/KInput.vue'

const finance = useFinanceStore()
const { incomeSources, loading, error, fetchIncomeSources, createIncomeSource } = finance

// Form data for new income source
const newIncome = ref({
  name: '',
  amount: '',
  frequency: '',
  description: ''
})

// Computed total monthly income
const totalMonthlyIncome = computed(() => {
  return incomeSources.reduce((total, income) => {
    // Simple calculation - assumes all amounts are monthly
    // In a real app, you'd want to convert different frequencies to monthly
    return total + income.amount
  }, 0)
})

// Add new income source
const addIncomeSource = async () => {
  try {
    console.log('Adding income source:', newIncome.value)
    await createIncomeSource({
      name: newIncome.value.name,
      amount: parseFloat(newIncome.value.amount),
      frequency: newIncome.value.frequency || undefined,
      description: newIncome.value.description || undefined
    })
    
    // Reset form
    newIncome.value = {
      name: '',
      amount: '',
      frequency: '',
      description: ''
    }
    console.log('Income source added successfully')
  } catch (error) {
    console.error('Failed to add income source:', error)
    // Don't reset form on error so user can fix and retry
  }
}

// Load income sources on page mount
onMounted(() => {
  fetchIncomeSources()
})
</script> 