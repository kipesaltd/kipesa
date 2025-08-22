<template>
  <div class="flex h-screen bg-gray-50">
    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-lg">
      <!-- Logo Section -->
      <div class="p-6 border-b border-gray-200">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center">
            <span class="text-white font-bold text-lg">K</span>
          </div>
          <h1 class="text-xl font-semibold text-gray-900">Kipesa</h1>
        </div>
      </div>

      <!-- Navigation -->
      <nav class="p-4">
        <ul class="space-y-2">
          <li>
            <a href="#" class="flex items-center px-4 py-3 text-gray-700 bg-blue-50 border-r-2 border-blue-600 rounded-lg">
              <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/>
              </svg>
              Dashboard
            </a>
          </li>
          <li>
            <a href="#" class="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-50 rounded-lg">
              <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              Transactions
            </a>
          </li>
          <li>
            <a href="#" class="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-50 rounded-lg">
              <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 20 20">
                <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3z"/>
              </svg>
              Users
            </a>
          </li>
          <li>
            <a href="#" class="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-50 rounded-lg">
              <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 20 20">
                <path d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zM3 10a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zM14 9a1 1 0 00-1 1v6a1 1 0 001 1h2a1 1 0 001-1v-6a1 1 0 00-1-1h-2z"/>
              </svg>
              Analytics
            </a>
          </li>
          <li>
            <a href="#" class="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-50 rounded-lg">
              <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"/>
              </svg>
              Settings
            </a>
          </li>
        </ul>
      </nav>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 overflow-hidden">
      <!-- Header -->
      <header class="bg-white shadow-sm border-b border-gray-200">
        <div class="flex items-center justify-between px-6 py-4">
          <div>
            <h2 class="text-2xl font-semibold text-gray-900">Dashboard</h2>
            <p class="text-gray-600">Welcome back, Admin</p>
          </div>
          <div class="flex items-center space-x-4">
            <!-- Notifications -->
            <button class="p-2 text-gray-400 hover:text-gray-600">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-5 5v-5z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
              </svg>
            </button>
            <!-- Profile -->
            <div class="flex items-center space-x-3">
              <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" 
                   alt="Profile" 
                   class="w-8 h-8 rounded-full">
              <span class="text-sm font-medium text-gray-700">Admin User</span>
            </div>
          </div>
        </div>
      </header>

      <!-- Page Content -->
      <div class="p-6 overflow-y-auto h-full">
        <slot />
      </div>
      <Footer />
    </main>
  </div>
</template>

<script setup>
// Default layout
</script>
