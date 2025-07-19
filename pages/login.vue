<template>
  <div class="max-w-md mx-auto mt-12 bg-white dark:bg-gray-800 p-8 rounded shadow">
    <h1 class="text-2xl font-bold mb-4">Login</h1>
    <form @submit.prevent="onLogin">
      <KInput v-model="email" type="email" placeholder="Email" class="mb-4" />
      <KInput v-model="password" type="password" placeholder="Password" class="mb-4" />
      <KButton :disabled="loading" @click="onLogin">
        {{ loading ? 'Logging in...' : 'Login' }}
      </KButton>
      <div v-if="formError" class="text-red-500 mt-2">{{ formError }}</div>
      <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
    </form>
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
  email: z.string().email(),
  password: z.string().min(6)
})

const onLogin = async () => {
  formError.value = ''
  const result = schema.safeParse({ email: email.value, password: password.value })
  if (!result.success) {
    formError.value = result.error.issues.map(e => e.message).join(', ')
    console.log('Validation error:', formError.value)
    return
  }
  console.log('Attempting login...')
  await auth.login(email.value, password.value)
  console.log('token:', auth.token)
  console.log('user:', auth.user)
  console.log('error:', auth.error)
  if (!auth.error && auth.token && auth.user) {
    router.push('/dashboard')
  }
}

watch(() => auth.error, (err) => {
  if (err) {
    alert(err)
  }
})

const { loading, error } = auth
</script> 