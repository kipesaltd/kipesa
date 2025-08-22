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
        <div class="relative bg-white rounded-full shadow-sm w-full max-w-lg h-16">
          <div class="absolute right-6 top-1/2 transform -translate-y-1/2">
            <svg class="w-6 h-6 text-[#309F50]" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <circle cx="11" cy="11" r="8" stroke-width="2"/>
              <path d="m21 21-4.35-4.35" stroke-width="2"/>
            </svg>
          </div>
          <input 
            type="text" 
            placeholder="Can we help you with your search?"
            class="w-full h-full pl-8 pr-16 rounded-full text-lg md:text-xl font-normal text-[#309F50] placeholder:text-[#309F50] placeholder:opacity-80 focus:outline-none focus:ring-2 focus:ring-[#309F50]/20 border-0"
          />
        </div>
      </div>

      <!-- Header Section -->
      <div class="flex flex-col lg:flex-row lg:justify-between lg:items-center gap-6 pb-8">
        <!-- Title and Subtitle -->
        <div class="flex flex-col gap-1">
          <h1 class="text-2xl font-semibold text-[#332C21]">Bill Centre</h1>
          <p class="text-base font-normal text-[#332C21] opacity-80">List of your linked bills</p>
        </div>

        <!-- Status Legend and Add Button -->
        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4 lg:gap-5">
          <!-- Status Legend -->
          <div class="flex flex-wrap items-center gap-4">
            <div class="flex items-center gap-2">
              <div class="w-2.5 h-2.5 bg-[#F35252] rounded-full"></div>
              <span class="text-sm text-[#332C21]">Overdue</span>
            </div>
            <div class="flex items-center gap-2">
              <div class="w-2.5 h-2.5 bg-[#EC923F] rounded-full"></div>
              <span class="text-sm text-[#332C21]">Due</span>
            </div>
            <div class="flex items-center gap-2">
              <div class="w-2.5 h-2.5 bg-[#1B7EDA] rounded-full"></div>
              <span class="text-sm text-[#332C21]">Upcoming</span>
            </div>
          </div>
          
          <!-- Add Button -->
          <button class="flex items-center justify-center w-13 h-13 bg-[#309F50] rounded-full hover:bg-[#2A8B47] transition-colors">
            <svg class="w-3 h-3 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v14m7-7H5"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Bills Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6 pb-16">
        <!-- Insurance Bill Card -->
        <div class="relative bg-white rounded-lg shadow-sm overflow-hidden">
          <!-- Background Decorative Elements -->
          <div class="absolute top-0 right-0">
            <div class="relative">
              <!-- Main blue circles -->
              <div class="absolute -top-9 -right-2">
                <div class="w-[219px] h-[132px] rounded-full bg-[rgba(27,126,218,0.1)] absolute top-0"></div>
                <div class="w-[200px] h-[187px] rounded-full bg-[rgba(27,126,218,0.1)] absolute top-2 -right-8"></div>
              </div>
              <!-- Status dot -->
              <div class="absolute top-5 right-9 w-2.5 h-2.5 bg-[#1B7EDA] rounded-full"></div>
            </div>
          </div>

          <!-- Card Content -->
          <div class="relative z-10 p-5">
            <div class="flex gap-3">
              <!-- Icon -->
              <div class="w-16 h-16 bg-white border border-[#149647] rounded-lg flex items-center justify-center flex-shrink-0">
                <img src="/icons/insurance.svg" alt="Insurance" class="w-10 h-10" />
              </div>
              
              <!-- Content -->
              <div class="flex flex-col justify-between min-h-[66px]">
                <div class="flex flex-col gap-1">
                  <p class="text-sm font-normal text-[#332C21]">Insurance</p>
                  <p class="text-base font-medium text-[#332C21]">TZS 100,000</p>
                </div>
                <p class="text-sm font-normal text-[#332C21]">Due date: 30/09/23</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Investment Bill Card -->
        <div class="relative bg-white rounded-lg shadow-sm overflow-hidden">
          <!-- Background Decorative Elements -->
          <div class="absolute top-0 right-0">
            <div class="relative">
              <!-- Red circles -->
              <div class="absolute -top-9 -right-2">
                <div class="w-[219px] h-[132px] rounded-full bg-[rgba(243,82,82,0.1)] absolute top-0"></div>
                <div class="w-[200px] h-[187px] rounded-full bg-[rgba(243,82,82,0.1)] absolute top-2 -right-8"></div>
              </div>
              <!-- Status dot -->
              <div class="absolute top-5 right-9 w-2.5 h-2.5 bg-[#F35252] rounded-full"></div>
            </div>
          </div>

          <!-- Card Content -->
          <div class="relative z-10 p-5">
            <div class="flex gap-3">
              <!-- Icon -->
              <div class="w-16 h-16 bg-white border border-[#41B8B1] rounded-lg flex items-center justify-center flex-shrink-0">
                <img src="/icons/investment.svg" alt="Investment" class="w-8 h-8" />
              </div>
              
              <!-- Content -->
              <div class="flex flex-col justify-between min-h-[66px]">
                <div class="flex flex-col gap-1">
                  <p class="text-sm font-normal text-[#332C21]">Investment</p>
                  <p class="text-base font-medium text-[#332C21]">TZS 450,000</p>
                </div>
                <p class="text-sm font-normal text-[#332C21]">Due date: 01/09/23</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Netflix Bill Card -->
        <div class="relative bg-white rounded-lg shadow-sm overflow-hidden">
          <!-- Background Decorative Elements -->
          <div class="absolute top-0 right-0">
            <div class="relative">
              <!-- Orange circles -->
              <div class="absolute -top-9 -right-2">
                <div class="w-[219px] h-[132px] rounded-full bg-[rgba(236,146,63,0.1)] absolute top-0"></div>
                <div class="w-[200px] h-[187px] rounded-full bg-[rgba(236,146,63,0.1)] absolute top-2 -right-8"></div>
              </div>
              <!-- Status dot -->
              <div class="absolute top-5 right-9 w-2.5 h-2.5 bg-[#EC923F] rounded-full"></div>
            </div>
          </div>

          <!-- Card Content -->
          <div class="relative z-10 p-5">
            <div class="flex gap-3">
              <!-- Icon -->
              <div class="w-16 h-16 bg-white border border-[#E50914] rounded-lg flex items-center justify-center flex-shrink-0">
                <div class="w-6 h-11 bg-[#E50914] rounded flex items-center justify-center">
                  <span class="text-white font-bold text-lg">N</span>
                </div>
              </div>
              
              <!-- Content -->
              <div class="flex flex-col justify-between min-h-[66px]">
                <div class="flex flex-col gap-1">
                  <p class="text-sm font-normal text-[#332C21]">Netflix</p>
                  <p class="text-base font-medium text-[#332C21]">TZS 20,000</p>
                </div>
                <p class="text-sm font-normal text-[#332C21]">Due date: 22/09/23</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Taifa Gas Bill Card -->
        <div class="relative bg-white rounded-lg shadow-sm overflow-hidden">
          <!-- Background Decorative Elements -->
          <div class="absolute top-0 right-0">
            <div class="relative">
              <!-- Red circles -->
              <div class="absolute -top-9 -right-2">
                <div class="w-[219px] h-[132px] rounded-full bg-[rgba(243,82,82,0.1)] absolute top-0"></div>
                <div class="w-[200px] h-[187px] rounded-full bg-[rgba(243,82,82,0.1)] absolute top-2 -right-8"></div>
              </div>
              <!-- Status dot -->
              <div class="absolute top-5 right-9 w-2.5 h-2.5 bg-[#F35252] rounded-full"></div>
            </div>
          </div>

          <!-- Card Content -->
          <div class="relative z-10 p-5">
            <div class="flex gap-3">
              <!-- Icon -->
              <div class="w-16 h-16 bg-white border border-[#70C054] rounded-lg flex items-center justify-center flex-shrink-0">
                <img src="/icons/taifa-gas.svg" alt="Taifa Gas" class="w-10 h-10" />
              </div>
              
              <!-- Content -->
              <div class="flex flex-col justify-between min-h-[66px]">
                <div class="flex flex-col gap-1">
                  <p class="text-sm font-normal text-[#332C21]">Taifa Gas</p>
                  <p class="text-base font-medium text-[#332C21]">TZS 50,000</p>
                </div>
                <p class="text-sm font-normal text-[#332C21]">Due date: 05/09/23</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Healthcare Bill Card -->
        <div class="relative bg-white rounded-lg shadow-sm overflow-hidden">
          <!-- Background Decorative Elements -->
          <div class="absolute top-0 right-0">
            <div class="relative">
              <!-- Orange circles -->
              <div class="absolute -top-9 -right-2">
                <div class="w-[219px] h-[132px] rounded-full bg-[rgba(236,146,63,0.1)] absolute top-0"></div>
                <div class="w-[200px] h-[187px] rounded-full bg-[rgba(236,146,63,0.1)] absolute top-2 -right-8"></div>
              </div>
              <!-- Status dot -->
              <div class="absolute top-5 right-9 w-2.5 h-2.5 bg-[#EC923F] rounded-full"></div>
            </div>
          </div>

          <!-- Card Content -->
          <div class="relative z-10 p-5">
            <div class="flex gap-3">
              <!-- Icon -->
              <div class="w-16 h-16 bg-white border border-[#0095DA] rounded-lg flex items-center justify-center flex-shrink-0">
                <img src="/icons/healthcare.svg" alt="Healthcare" class="w-10 h-10" />
              </div>
              
              <!-- Content -->
              <div class="flex flex-col justify-between min-h-[66px]">
                <div class="flex flex-col gap-1">
                  <p class="text-sm font-normal text-[#332C21]">Healthcare</p>
                  <p class="text-base font-medium text-[#332C21]">TZS 50,000</p>
                </div>
                <p class="text-sm font-normal text-[#332C21]">Due date: 22/09/23</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Vacation Bill Card -->
        <div class="relative bg-white rounded-lg shadow-sm overflow-hidden">
          <!-- Background Decorative Elements -->
          <div class="absolute top-0 right-0">
            <div class="relative">
              <!-- Red circles -->
              <div class="absolute -top-9 -right-2">
                <div class="w-[219px] h-[132px] rounded-full bg-[rgba(243,82,82,0.1)] absolute top-0"></div>
                <div class="w-[200px] h-[187px] rounded-full bg-[rgba(243,82,82,0.1)] absolute top-2 -right-8"></div>
              </div>
              <!-- Status dot -->
              <div class="absolute top-5 right-9 w-2.5 h-2.5 bg-[#F35252] rounded-full"></div>
            </div>
          </div>

          <!-- Card Content -->
          <div class="relative z-10 p-5">
            <div class="flex gap-3">
              <!-- Icon -->
              <div class="w-16 h-16 bg-white border border-[#8662D3] rounded-lg flex items-center justify-center flex-shrink-0">
                <img src="/icons/vacation.svg" alt="Vacation" class="w-10 h-8" />
              </div>
              
              <!-- Content -->
              <div class="flex flex-col justify-between min-h-[66px]">
                <div class="flex flex-col gap-1">
                  <p class="text-sm font-normal text-[#332C21]">Vacation</p>
                  <p class="text-base font-medium text-[#332C21]">TZS 100,000</p>
                </div>
                <p class="text-sm font-normal text-[#332C21]">Due date: 05/09/23</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
// Bill Center page logic
</script>

<style scoped>
/* Custom styles for bill center */
.font-archia {
  font-family: 'Archia', sans-serif;
}
</style>

