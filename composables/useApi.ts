import { useRuntimeConfig } from '#app'
import { useAuthStore } from '~/stores/auth'
import { $fetch } from 'ofetch'

export function useApi() {
  const config = useRuntimeConfig()
  const auth = useAuthStore()

  function get(url: string, opts = {}) {
    return $fetch(url, {
      baseURL: config.public.apiBase,
      headers: auth.token ? { Authorization: `Bearer ${auth.token}` } : {},
      ...opts,
    })
  }

  function post(url: string, body: any, opts = {}) {
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