<template>
  <nav class="flex items-center justify-between px-4 py-2 bg-kipesa-green text-white">
    <div class="flex items-center gap-4">
      <NuxtLink to="/dashboard" class="font-bold text-lg">Kipesa</NuxtLink>
      <NuxtLink to="/finance" class="hover:underline">{{ t('finance') }}</NuxtLink>
      <NuxtLink to="/chatbot" class="hover:underline">{{ t('chatbot') }}</NuxtLink>
      <NuxtLink to="/calculators" class="hover:underline">{{ t('calculators') }}</NuxtLink>
    </div>
    <div class="flex items-center gap-2">
      <NuxtLink to="/profile" class="hover:underline">{{ t('profile') }}</NuxtLink>
      <NuxtLink to="/settings" class="hover:underline">{{ t('settings') }}</NuxtLink>
      <button 
        v-if="auth.token"
        @click="handleLogout" 
        class="hover:underline text-white bg-transparent border-none cursor-pointer"
      >
        {{ t('logout') }}
      </button>
      <select v-model="locale" class="ml-2 rounded text-black px-2 py-1">
        <option value="en">EN</option>
        <option value="sw">SW</option>
      </select>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import { useAuthStore } from '~/stores/auth'
import { useRouter } from 'vue-router'

const { t, locale } = useI18n()
const auth = useAuthStore()
const router = useRouter()

const handleLogout = () => {
  auth.logout()
  router.push('/login')
}
</script> 