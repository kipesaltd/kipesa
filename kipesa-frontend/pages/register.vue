<template>
  <div class="max-w-md mx-auto mt-12 bg-white dark:bg-gray-800 p-8 rounded shadow">
    <h1 class="text-2xl font-bold mb-4">Register</h1>
    <form @submit.prevent="onRegister">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <KInput v-model="email" type="email" placeholder="Email" required />
        <KInput v-model="password" type="password" placeholder="Password" required />
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <KInput v-model="fullName" type="text" placeholder="Full Name" required />
        <KInput v-model="phoneNumber" type="tel" placeholder="Phone Number" required />
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <select v-model="ageGroup" class="block w-full px-3 py-2 border border-gray-300 rounded focus:ring-kipesa-green focus:border-kipesa-green dark:bg-gray-800 dark:text-white" required>
          <option value="">Select Age Group</option>
          <option value="18-25">18-25</option>
          <option value="26-35">26-35</option>
          <option value="36-45">36-45</option>
          <option value="46-55">46-55</option>
          <option value="56-65">56-65</option>
          <option value="65+">65+</option>
        </select>
        <select v-model="gender" class="block w-full px-3 py-2 border border-gray-300 rounded focus:ring-kipesa-green focus:border-kipesa-green dark:bg-gray-800 dark:text-white" required>
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>
      <div class="mb-4">
        <KInput v-model="location" type="text" placeholder="Location (City, Country)" required />
      </div>
      <KButton type="submit" :disabled="loading">{{ loading ? 'Registering...' : 'Register' }}</KButton>
      <div v-if="formError" class="text-red-500 mt-2">{{ formError }}</div>
      <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
    </form>
    
    <!-- Login link -->
    <div class="mt-6 text-center">
      <p class="text-gray-600 dark:text-gray-400">
        Already have an account? 
        <NuxtLink to="/login" class="text-kipesa-green hover:underline font-medium">
          Login here
        </NuxtLink>
      </p>
    </div>
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
const phoneNumber = ref('')
const ageGroup = ref('')
const gender = ref('')
const location = ref('')
const formError = ref('')
const auth = useAuthStore()
const router = useRouter()

const schema = z.object({
  email: z.string().trim().email('Invalid email address'),
  password: z.string().trim().min(6, 'Password must be at least 6 characters'),
  full_name: z.string().trim().min(2, 'Full name must be at least 2 characters'),
  phone_number: z.string().trim().min(1, 'Phone number is required'),
  age_group: z.string().trim().min(1, 'Age group is required'),
  gender: z.string().trim().min(1, 'Gender is required'),
  location: z.string().trim().min(1, 'Location is required')
})

const onRegister = async () => {
  formError.value = ''
  const result = schema.safeParse({ 
    email: email.value.trim(), 
    password: password.value.trim(), 
    full_name: fullName.value.trim(),
    phone_number: phoneNumber.value.trim(),
    age_group: ageGroup.value.trim(),
    gender: gender.value.trim(),
    location: location.value.trim()
  })
  if (!result.success) {
    formError.value = result.error.issues.map(e => e.message).join(', ')
    return
  }
  await auth.register({ 
    email: email.value, 
    password: password.value, 
    full_name: fullName.value,
    phone_number: phoneNumber.value,
    age_group: ageGroup.value,
    gender: gender.value,
    location: location.value
  })
  if (!auth.error) {
    router.push('/dashboard')
  }
}

const { loading, error } = auth
</script> 