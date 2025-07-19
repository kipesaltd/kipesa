import { useRuntimeConfig } from '#app'
import { useAuthStore } from '~/stores/auth'
import { $fetch } from 'ofetch'

export function useApi() {
  const config = useRuntimeConfig()
  const auth = useAuthStore()

  function get(url: string, opts = {}) {
    console.log('useApi: Making GET request to', url)
    console.log('useApi: Auth token:', auth.token ? 'EXISTS' : 'NOT FOUND')
    
    return $fetch(url, {
    baseURL: config.public.apiBase,
      headers: auth.token ? { Authorization: `Bearer ${auth.token}` } : {},
      ...opts,
    })
  }

  function post(url: string, body: any, opts = {}) {
    console.log('useApi: Making POST request to', url)
    console.log('useApi: Auth token:', auth.token ? 'EXISTS' : 'NOT FOUND')
    console.log('useApi: Request body:', body)
    
    return $fetch(url, {
      method: 'POST',
      baseURL: config.public.apiBase,
      body,
      headers: auth.token ? { Authorization: `Bearer ${auth.token}` } : {},
      ...opts,
  })
  }

  return { get, post }
} 