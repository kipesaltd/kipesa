<template>
  <div class="max-w-md mx-auto mt-12 bg-white dark:bg-gray-800 p-8 rounded shadow">
    <h1 class="text-2xl font-bold mb-4">Login</h1>
    <form @submit.prevent="onLogin">
      <KInput v-model="email" type="email" placeholder="Email" class="mb-4" />
      <KInput v-model="password" type="password" placeholder="Password" class="mb-4" />
      <KButton type="submit" :disabled="loading">{{ loading ? 'Logging in...' : 'Login' }}</KButton>
      <div v-if="formError" class="text-red-500 mt-2">{{ formError }}</div>
      <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
    </form>
    
    <!-- Register link -->
    <div class="mt-6 text-center">
      <p class="text-gray-600 dark:text-gray-400">
        Don't have an account? 
        <NuxtLink to="/register" class="text-kipesa-green hover:underline font-medium">
          Register here
        </NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { useAuthStore } from '~/stores/auth'
import KInput from '~/components/atoms/KInput.vue'
import KButton from '~/components/atoms/KButton.vue'
import { useRouter } from 'vue-router'
import { z } from 'zod'

const email = ref('')
const password = ref('')
const formError = ref('')
const auth = useAuthStore()
const router = useRouter()

const schema = z.object({
  email: z.string().trim().email('Invalid email address'),
  password: z.string().trim().min(6, 'Password must be at least 6 characters')
})

const onLogin = async () => {
  formError.value = ''
  const emailValue = email.value.trim()
  const passwordValue = password.value.trim()
  
  console.log('Email value:', emailValue)
  console.log('Password value:', passwordValue)
  
  const result = schema.safeParse({ 
    email: emailValue, 
    password: passwordValue 
  })
  if (!result.success) {
    formError.value = result.error.issues.map(e => e.message).join(', ')
    console.log('Validation error:', formError.value)
    console.log('Validation issues:', result.error.issues)
    return
  }
  console.log('Attempting login...')
  try {
    await auth.login(emailValue, passwordValue)
  if (!auth.error && auth.token && auth.user) {
    router.push('/dashboard')
    }
  } catch (error) {
    console.error('Login error:', error)
    formError.value = 'Login failed: ' + (error as any)?.message || 'Unknown error'
  }
}

// Optionally, watch for error and show a toast or alert
watch(() => auth.error, (err) => {
  if (err) {
    alert(err) // or use a toast library
  }
})

const { loading, error } = auth
</script> 