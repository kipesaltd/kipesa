<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">{{ $t('dashboard') }}</h1>
    <p class="mb-6">{{ $t('welcome', { name: 'User' }) }}</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
      <NuxtLink to="/finance" class="bg-white dark:bg-gray-800 rounded shadow p-4 hover:shadow-lg transition-shadow cursor-pointer">
        <div class="flex justify-between items-start">
          <div>
            <div class="font-semibold">Income</div>
            <div class="text-2xl text-kipesa-green">TSh {{ totalIncome.toLocaleString() }}</div>
          </div>
          <div class="text-sm text-gray-500">→</div>
        </div>
      </NuxtLink>
      <div class="bg-white dark:bg-gray-800 rounded shadow p-4">
        <div class="font-semibold">Expenses</div>
        <div class="text-2xl text-red-500">TSh 0</div>
      </div>
      <div class="bg-white dark:bg-gray-800 rounded shadow p-4">
        <div class="font-semibold">Savings</div>
        <div class="text-2xl text-kipesa-blue">TSh 0</div>
      </div>
    </div>
    <section>
      <h2 class="text-xl font-semibold mb-2">Financial Health Overview</h2>
      <div class="bg-white dark:bg-gray-800 rounded shadow p-4">
        <p>Charts and analytics coming soon...</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { useFinanceStore } from '~/stores/finance'

const finance = useFinanceStore()

// Computed total income
const totalIncome = computed(() => {
  return finance.incomeSources.reduce((total, income) => {
    return total + income.amount
  }, 0)
})

// Load income sources on page mount
onMounted(() => {
  finance.fetchIncomeSources()
})
</script> 