<template>
  <nav class="bg-[#F5FAF6] px-4 py-8 lg:px-32 lg:py-8">
    <div class="max-w-7xl mx-auto">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4 lg:gap-8">
        <!-- Logo Section -->
        <div class="flex items-center justify-center lg:justify-start">
          <div class="p-4 rounded-lg">
            <img 
              src="/kipesa-logo.svg" 
              alt="Kipesa Logo" 
              class="h-12 w-auto"
            />
          </div>
        </div>

        <!-- Navigation Menu -->
        <div class="flex flex-col lg:flex-row items-center gap-4 lg:gap-8">
          <!-- Menu Items -->
          <div class="flex flex-col lg:flex-row items-center gap-2 lg:gap-8">
            <NuxtLink 
              to="/" 
              class="text-[#332C21] font-medium text-lg hover:text-[#309F50] transition-colors"
              :class="{ 'text-[#309F50] font-semibold': $route.path === '/' }"
            >
              Dashboard
            </NuxtLink>
            <NuxtLink 
              to="/financial-account" 
              class="text-[#332C21] font-medium text-lg hover:text-[#309F50] transition-colors"
              :class="{ 'text-[#309F50] font-semibold': $route.path === '/financial-account' }"
            >
              Financial Account
            </NuxtLink>
            <NuxtLink 
              to="/bill-centre" 
              class="text-[#309F50] font-semibold text-lg"
            >
              Bill Centre
            </NuxtLink>
            <NuxtLink 
              to="/budget-center" 
              class="text-[#332C21] font-medium text-lg hover:text-[#309F50] transition-colors"
              :class="{ 'text-[#309F50] font-semibold': $route.path === '/budget-center' }"
            >
              Budget Center
            </NuxtLink>
            <NuxtLink 
              to="/calendar" 
              class="text-[#332C21] font-medium text-lg hover:text-[#309F50] transition-colors"
              :class="{ 'text-[#309F50] font-semibold': $route.path === '/calendar' }"
            >
              Calendar
            </NuxtLink>
          </div>

          <!-- Language Selector -->
          <div class="flex items-center gap-2 px-3 py-3.5 bg-white rounded-lg">
            <div class="flex items-center gap-2">
              <img 
                src="/uk-flag.png" 
                alt="UK Flag" 
                class="w-5 h-5 rounded"
              />
              <span class="text-[#332C21] font-medium text-lg">EN</span>
            </div>
            <button class="flex items-center justify-center w-6 h-6">
              <img 
                src="/expand-more.svg" 
                alt="Expand" 
                class="w-3 h-3"
              />
            </button>
          </div>

          <!-- User Profile -->
          <div class="flex items-center gap-1">
            <div class="flex items-center gap-1 px-3 py-3.5">
              <img 
                src="/user-avatar.png" 
                alt="User Avatar" 
                class="w-12 h-12 rounded-full object-cover"
              />
              <button class="flex items-center justify-center w-6 h-6">
                <img 
                  src="/expand-more.svg" 
                  alt="Expand" 
                  class="w-3 h-3"
                />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
// Component logic can be added here if needed
</script>

<style scoped>
/* Custom styles for the navigation component */
.nuxt-link-active {
  @apply text-[#309F50] font-semibold;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .nav-container {
    @apply flex-col;
  }
  
  .nav-menu {
    @apply flex-col gap-4;
  }
  
  .nav-items {
    @apply flex-col gap-2;
  }
}
</style>
