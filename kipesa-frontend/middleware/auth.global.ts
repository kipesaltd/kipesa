import { useAuthStore } from '~/stores/auth'
import { defineNuxtRouteMiddleware, navigateTo } from '#app'

export default defineNuxtRouteMiddleware((to) => {
  // Skip middleware for login and register pages
  if (['/login', '/register'].includes(to.path)) {
    return
  }
  
  // Only run auth checks on client side
  if (!process.client) {
    return
  }
  
  const auth = useAuthStore()
  
  // Check localStorage for token
  const storedToken = localStorage.getItem('kipesa_token')
  
  if (storedToken && !auth.token) {
    auth.token = storedToken
  }
  
  if (!auth.token) {
    return navigateTo('/login')
  }
}) 