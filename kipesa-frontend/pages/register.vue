<template>
  <div class="max-w-md mx-auto mt-12 bg-white dark:bg-gray-800 p-8 rounded shadow">
    <h1 class="text-2xl font-bold mb-4">Register</h1>
    <form @submit.prevent="onRegister">
      <KInput v-model="email" type="email" placeholder="Email" class="mb-4" />
      <KInput v-model="password" type="password" placeholder="Password" class="mb-4" />
      <KInput v-model="fullName" type="text" placeholder="Full Name" class="mb-4" />
      <KButton type="submit" :disabled="loading">{{ loading ? 'Registering...' : 'Register' }}</KButton>
      <div v-if="formError" class="text-red-500 mt-2">{{ formError }}</div>
      <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '~/stores/auth'
import KInput from '~/components/atoms/KInput.vue'
import KButton from '~/components/atoms/KButton.vue'
import { useRouter } from 'vue-router'
import { z } from 'zod'

const email = ref('')
const password = ref('')
const fullName = ref('')
const formError = ref('')
const auth = useAuthStore()
const router = useRouter()

const schema = z.object({
  email: z.string().trim().email('Invalid email address'),
  password: z.string().trim().min(6, 'Password must be at least 6 characters'),
  full_name: z.string().trim().min(2, 'Full name must be at least 2 characters')
})

const onRegister = async () => {
  formError.value = ''
  const result = schema.safeParse({ 
    email: email.value.trim(), 
    password: password.value.trim(), 
    full_name: fullName.value.trim() 
  })
  if (!result.success) {
    formError.value = result.error.issues.map(e => e.message).join(', ')
    return
  }
  await auth.register({ email: email.value, password: password.value, full_name: fullName.value })
  if (!auth.error) {
    router.push('/login')
  }
}

const { loading, error } = auth
</script> 