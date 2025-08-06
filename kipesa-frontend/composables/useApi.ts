import { useRuntimeConfig } from '#app'
import { useAuthStore } from '~/stores/auth'
import { $fetch } from 'ofetch'

// Request debouncing
const pendingRequests = new Map<string, Promise<any>>()

export function useApi() {
  const config = useRuntimeConfig()
  const auth = useAuthStore()

  function get(url: string, opts = {}) {
    console.log('useApi: Making GET request to', url)
    console.log('useApi: Auth token:', auth.token ? 'EXISTS' : 'NOT FOUND')
    
    // Check for pending request
    const requestKey = `GET:${url}`
    if (pendingRequests.has(requestKey)) {
      return pendingRequests.get(requestKey)!
    }
    
    const request = $fetch(url, {
      baseURL: config.public.apiBase,
      headers: auth.token ? { Authorization: `Bearer ${auth.token}` } : {},
      timeout: 10000, // 10 second timeout
      ...opts,
    }).finally(() => {
      pendingRequests.delete(requestKey)
    })
    
    pendingRequests.set(requestKey, request)
    return request
  }

  function post(url: string, body: any, opts = {}) {
    console.log('useApi: Making POST request to', url)
    console.log('useApi: Auth token:', auth.token ? 'EXISTS' : 'NOT FOUND')
    console.log('useApi: Request body:', body)
    
    // Check for pending request
    const requestKey = `POST:${url}:${JSON.stringify(body)}`
    if (pendingRequests.has(requestKey)) {
      return pendingRequests.get(requestKey)!
    }
    
    const request = $fetch(url, {
      method: 'POST',
      baseURL: config.public.apiBase,
      body,
      headers: auth.token ? { Authorization: `Bearer ${auth.token}` } : {},
      timeout: 30000, // 30 second timeout for POST requests
      ...opts,
    }).finally(() => {
      pendingRequests.delete(requestKey)
    })
    
    pendingRequests.set(requestKey, request)
    return request
  }

  return { get, post }
} 