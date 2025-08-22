<template>
  <div class="min-h-screen bg-[#F5FAF6]">
    <!-- Navigation -->
    <Navigation />
    
    <!-- Background Decorative Elements -->
    <div class="relative">
      <img src="/icons/leaf-pattern-1.svg" alt="" class="absolute top-0 left-0 w-48 h-32 opacity-10 z-0 hidden lg:block" />
      <img src="/icons/leaf-pattern-2.svg" alt="" class="absolute top-8 right-0 w-48 h-32 opacity-10 z-0 hidden lg:block" />
      <img src="/icons/leaf-pattern-3.svg" alt="" class="absolute top-12 right-12 w-48 h-32 opacity-10 z-0 hidden xl:block" />
    </div>

    <!-- Main Content -->
    <div class="relative z-10 max-w-7xl mx-auto px-4 md:px-8 lg:px-16 xl:px-32">
      <!-- Search Bar -->
      <div class="flex justify-center py-8">
        <div class="relative bg-white rounded-full shadow-sm w-full max-w-[609px] h-16">
          <div class="absolute right-6 top-1/2 transform -translate-y-1/2">
            <svg class="w-7 h-7 text-[#309F50]" viewBox="0 0 28 28" fill="none" stroke="currentColor">
              <circle cx="11" cy="11" r="8" stroke-width="2"/>
              <path d="m21 21-4.35-4.35" stroke-width="2"/>
            </svg>
          </div>
          <input 
            type="text" 
            placeholder="Can we help you with your search?"
            class="w-full h-full pl-8 pr-16 rounded-full text-xl font-normal text-[#309F50] placeholder:text-[#309F50] placeholder:opacity-80 focus:outline-none focus:ring-2 focus:ring-[#309F50]/20 border-0"
          />
        </div>
      </div>

      <!-- Controls Section -->
      <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4 mb-8">
        <!-- Back Button -->
        <button class="flex items-center gap-2.5 px-4 py-3.5 border border-[#309F50] rounded-lg text-[#309F50] font-medium text-lg hover:bg-[#309F50]/5 transition-colors w-fit">
          <img src="/icons/back-arrow.svg" alt="Back" class="w-2 h-3.5" />
          <span>View Budget</span>
        </button>

        <!-- Toggle Tabs -->
        <div class="flex">
          <!-- Expected Income Tab (Active) -->
          <div class="bg-[#309F50] rounded-l-full px-5 py-4">
            <span class="text-white font-medium text-lg">Expected Income</span>
          </div>
          <!-- Expected Spend Tab -->
          <div class="bg-white border border-[#309F50] rounded-r-full px-5 py-4 shadow-sm">
            <span class="text-[#332C21] font-normal text-lg">Expected Spend</span>
          </div>
        </div>

        <!-- Date Filter -->
        <div class="bg-[#F5FAF6] border border-[rgba(51,44,33,0.3)] rounded-lg px-3 py-2 w-fit">
          <div class="flex items-center justify-between gap-2 min-w-[140px]">
            <span class="text-xs font-normal text-[#332C21]">September 2023</span>
            <svg class="w-5 h-5 text-[#332C21]" viewBox="0 0 20 20" fill="none" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 8l4 4 4-4"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Header Section with Total and Add Button -->
      <div class="bg-white rounded-lg shadow-sm p-5 mb-8">
        <div class="flex justify-between items-center">
          <div class="flex items-center gap-2.5">
            <div class="flex flex-col">
              <span class="text-2xl font-normal text-[#332C21]">Total expected income:</span>
              <span class="text-2xl font-semibold text-[#332C21]">TZS 1,474,700</span>
            </div>
          </div>
          <button class="bg-[#309F50] rounded-full w-[52px] h-[52px] flex items-center justify-center hover:bg-[#309F50]/90 transition-colors">
            <img src="/icons/add-icon.svg" alt="Add" class="w-3 h-3" />
          </button>
        </div>
      </div>

      <!-- Income Items Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6 mb-8">
        <!-- Salary Item -->
        <div class="bg-white rounded-lg shadow-sm p-5">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <!-- Salary Icon Container -->
              <div class="w-[60px] h-[60px] border border-[#7BC282] rounded-lg flex items-center justify-center">
                <img src="/icons/salary-icon.svg" alt="Salary" class="w-8 h-8" />
              </div>
              <div class="flex flex-col gap-1">
                <span class="text-lg font-normal text-[#332C21]">Salary</span>
                <span class="text-2xl font-semibold text-[#332C21]">TZS 1,000,000</span>
              </div>
            </div>
            <div class="relative w-10 h-10">
              <button class="w-6 h-6 flex items-center justify-center absolute top-2 right-2">
                <img src="/icons/delete-icon.svg" alt="Delete" class="w-3.5 h-4" />
              </button>
              <div class="w-10 h-10 border border-[#309F50] rounded-full"></div>
            </div>
          </div>
        </div>

        <!-- Business Item -->
        <div class="bg-white rounded-lg shadow-sm p-5">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <!-- Business Icon Container -->
              <div class="w-[60px] h-[60px] border border-[#ECB359] rounded-lg flex items-center justify-center">
                <img src="/icons/business-icon.svg" alt="Business" class="w-10 h-10" />
              </div>
              <div class="flex flex-col gap-1">
                <span class="text-lg font-normal text-[#332C21]">Business</span>
                <span class="text-2xl font-semibold text-[#332C21]">TZS 9,700</span>
              </div>
            </div>
            <div class="relative w-10 h-10">
              <button class="w-6 h-6 flex items-center justify-center absolute top-2 right-2">
                <img src="/icons/delete-icon.svg" alt="Delete" class="w-3.5 h-4" />
              </button>
              <div class="w-10 h-10 border border-[#309F50] rounded-full"></div>
            </div>
          </div>
        </div>

        <!-- Investment Item -->
        <div class="bg-white rounded-lg shadow-sm p-5">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <!-- Investment Icon Container -->
              <div class="w-[60px] h-[60px] border border-[#5D9EEB] rounded-lg flex items-center justify-center">
                <img src="/icons/investment-icon.svg" alt="Investment" class="w-10 h-10" />
              </div>
              <div class="flex flex-col gap-1">
                <span class="text-lg font-normal text-[#332C21]">Investment</span>
                <span class="text-2xl font-semibold text-[#332C21]">TZS 465,000</span>
              </div>
            </div>
            <div class="relative w-10 h-10">
              <button class="w-6 h-6 flex items-center justify-center absolute top-2 right-2">
                <img src="/icons/delete-icon.svg" alt="Delete" class="w-3.5 h-4" />
              </button>
              <div class="w-10 h-10 border border-[#309F50] rounded-full"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Income Flow Chart -->
      <div class="bg-white rounded-lg shadow-sm p-8 mb-16">
        <!-- Chart Header -->
        <div class="flex flex-col lg:flex-row lg:justify-between lg:items-center gap-4 mb-8">
          <h2 class="text-2xl font-semibold text-[#332C21]">Income flow</h2>
          <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4">
            <!-- Legend -->
            <div class="flex flex-wrap items-center gap-5">
              <div class="flex items-center gap-2">
                <div class="w-2.5 h-2.5 bg-[#7BC282] rounded-full"></div>
                <span class="text-sm text-[#332C21]">Salary</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-2.5 h-2.5 bg-[#ECB359] rounded-full"></div>
                <span class="text-sm text-[#332C21]">Business</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-2.5 h-2.5 bg-[#5D9EEB] rounded-full"></div>
                <span class="text-sm text-[#332C21]">Investment</span>
              </div>
            </div>
            <!-- Date Filter -->
            <div class="bg-white border border-[rgba(51,44,33,0.3)] rounded-lg px-3 py-2">
              <div class="flex items-center justify-between gap-2 min-w-[140px]">
                <span class="text-xs font-normal text-[#332C21]">Last 3 months</span>
                <svg class="w-5 h-5 text-[#332C21]" viewBox="0 0 20 20" fill="none" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 8l4 4 4-4"/>
                </svg>
              </div>
            </div>
          </div>
        </div>

        <!-- Chart Container -->
        <div class="relative">
          <!-- Y-axis Labels -->
          <div class="absolute left-0 top-0 h-full flex flex-col justify-between text-xs text-[#332C21] opacity-80 py-2">
            <span>1000</span>
            <span>800</span>
            <span>600</span>
            <span>400</span>
            <span>200</span>
            <span>0</span>
          </div>
          
          <!-- Chart Area -->
          <div class="ml-16 relative h-80">
            <!-- Grid Lines -->
            <div class="absolute inset-0">
              <div class="h-full flex flex-col justify-between">
                <div class="border-b border-[#332C21] opacity-10"></div>
                <div class="border-b border-[#332C21] opacity-10"></div>
                <div class="border-b border-[#332C21] opacity-10"></div>
                <div class="border-b border-[#332C21] opacity-10"></div>
                <div class="border-b border-[#332C21] opacity-10"></div>
                <div class="border-b border-[#332C21] opacity-10"></div>
              </div>
            </div>
            
            <!-- Chart Lines and Points -->
            <div class="relative h-full">
              <!-- Salary Line (Green) -->
              <svg class="absolute inset-0 w-full h-full" preserveAspectRatio="none" viewBox="0 0 1000 320">
                <path d="M 50 280 Q 350 200 500 240 T 950 190" stroke="#7BC282" stroke-width="3" fill="none"/>
              </svg>
              
              <!-- Business Line (Orange) -->
              <svg class="absolute inset-0 w-full h-full" preserveAspectRatio="none" viewBox="0 0 1000 320">
                <path d="M 50 310 Q 350 290 500 280 T 950 270" stroke="#ECB359" stroke-width="3" fill="none"/>
              </svg>
              
              <!-- Investment Line (Blue) -->
              <svg class="absolute inset-0 w-full h-full" preserveAspectRatio="none" viewBox="0 0 1000 320">
                <path d="M 50 250 Q 350 160 500 180 T 950 140" stroke="#5D9EEB" stroke-width="3" fill="none"/>
              </svg>
              
              <!-- Data Points -->
              <div class="absolute bottom-12 left-12 w-1.5 h-1.5 bg-[#7BC282] rounded-full"></div>
              <div class="absolute bottom-8 left-12 w-1.5 h-1.5 bg-[#ECB359] rounded-full"></div>
              <div class="absolute bottom-16 left-12 w-1.5 h-1.5 bg-[#5D9EEB] rounded-full"></div>
              
              <div class="absolute bottom-20 left-1/2 w-1.5 h-1.5 bg-[#7BC282] rounded-full"></div>
              <div class="absolute bottom-10 left-1/2 w-1.5 h-1.5 bg-[#ECB359] rounded-full"></div>
              <div class="absolute bottom-32 left-1/2 w-1.5 h-1.5 bg-[#5D9EEB] rounded-full"></div>
              
              <div class="absolute bottom-36 right-12 w-1.5 h-1.5 bg-[#7BC282] rounded-full"></div>
              <div class="absolute bottom-14 right-12 w-1.5 h-1.5 bg-[#ECB359] rounded-full"></div>
              <div class="absolute bottom-44 right-12 w-1.5 h-1.5 bg-[#5D9EEB] rounded-full"></div>
            </div>
          </div>
          
          <!-- X-axis Labels -->
          <div class="flex justify-between mt-4 ml-16">
            <span class="text-xs text-[#332C21] opacity-80">July</span>
            <span class="text-xs text-[#332C21] opacity-80">August</span>
            <span class="text-xs text-[#332C21] opacity-80">September</span>
          </div>
          
          <!-- Chart Label -->
          <div class="absolute left-2 top-1/2 transform -translate-y-1/2 -rotate-90">
            <span class="text-xs text-[#332C21] opacity-80 whitespace-nowrap">Amount in thousands and TZS</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
// Page meta
definePageMeta({
  title: 'Expected Income - Kipesa'
})
</script>

