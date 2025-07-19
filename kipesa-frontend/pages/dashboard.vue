<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">{{ $t('dashboard') }}</h1>
    <p class="mb-6">{{ $t('welcome', { name: 'User' }) }}</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
      <div class="bg-white dark:bg-gray-800 rounded shadow p-4">
        <div class="font-semibold">Income</div>
        <div class="text-2xl text-kipesa-green">TSh 0</div>
      </div>
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