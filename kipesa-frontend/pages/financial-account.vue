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
    <div class="relative z-10 px-4 md:px-8 lg:px-16 xl:px-32">
      <!-- Page Header -->
      <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4 pt-16 pb-8 max-w-7xl mx-auto">
        <div>
          <h1 class="text-2xl md:text-3xl font-semibold text-[#332C21]">Financial Account</h1>
          <p class="text-base md:text-lg text-[#332C21] opacity-80">List of your linked financial accounts</p>
        </div>
        <button class="bg-[#309F50] text-white rounded-full px-5 py-4 flex items-center justify-center hover:bg-[#2A8A45] transition-colors">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
          </svg>
        </button>
      </div>

      <!-- Account Types -->
      <div class="flex gap-10 mb-10 max-w-7xl mx-auto">
        <div class="text-xl font-semibold text-[#332C21]">Bank account</div>
        <div class="text-xl font-semibold text-[#332C21] ml-10">Mobile money</div>
      </div>

      <!-- Account Cards Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6 mb-10 max-w-7xl mx-auto">
        <!-- M-PESA -->
        <div class="bg-white rounded-lg p-5 shadow-sm hover:shadow-md transition-shadow account-card">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#00A651] rounded flex items-center justify-center">
                <span class="text-white font-semibold text-sm">MP</span>
              </div>
              <div>
                <div class="text-xl font-medium text-[#332C21]">M-PESA</div>
              </div>
            </div>
            <div class="flex items-center gap-5">
              <div class="text-xl font-semibold text-[#332C21]">TZS 20,000</div>
              <button class="text-[#332C21] p-1 hover:bg-gray-100 rounded">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Halopesa -->
        <div class="bg-white rounded-lg p-5 shadow-sm hover:shadow-md transition-shadow account-card">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#F57921] rounded flex items-center justify-center">
                <span class="text-white font-semibold text-sm">HP</span>
              </div>
              <div>
                <div class="text-xl font-medium text-[#332C21]">Halopesa</div>
              </div>
            </div>
            <div class="flex items-center gap-5">
              <div class="text-xl font-semibold text-[#332C21]">TZS 100,000</div>
              <button class="text-[#332C21] p-1 hover:bg-gray-100 rounded">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Azania Bank -->
        <div class="bg-white rounded-lg p-5 shadow-sm hover:shadow-md transition-shadow account-card">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#E4F7FF] rounded flex items-center justify-center">
                <span class="text-[#0095DA] font-semibold text-sm">AZ</span>
              </div>
              <div>
                <div class="text-xl font-medium text-[#332C21]">Azania</div>
              </div>
            </div>
            <div class="flex items-center gap-5">
              <div class="text-xl font-semibold text-[#332C21]">TZS 750,000</div>
              <button class="text-[#332C21] p-1 hover:bg-gray-100 rounded">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- DTB Bank -->
        <div class="bg-white rounded-lg p-5 shadow-sm hover:shadow-md transition-shadow account-card">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#EB204B] rounded flex items-center justify-center">
                <span class="text-white font-semibold text-sm">DT</span>
              </div>
              <div>
                <div class="text-xl font-medium text-[#332C21]">DTB</div>
              </div>
            </div>
            <div class="flex items-center gap-5">
              <div class="text-xl font-semibold text-[#332C21]">TZS 300,000</div>
              <button class="text-[#332C21] p-1 hover:bg-gray-100 rounded">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Absa Bank -->
        <div class="bg-white rounded-lg p-5 shadow-sm hover:shadow-md transition-shadow">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#005B82] rounded flex items-center justify-center">
                <span class="text-white font-semibold text-sm">AB</span>
              </div>
              <div>
                <div class="text-xl font-medium text-[#332C21]">Absa</div>
              </div>
            </div>
            <div class="flex items-center gap-5">
              <div class="text-xl font-semibold text-[#332C21]">TZS 605,000</div>
              <button class="text-[#332C21] p-1 hover:bg-gray-100 rounded">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- CRDB Bank -->
        <div class="bg-white rounded-lg p-5 shadow-sm hover:shadow-md transition-shadow">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#E2FFE1] rounded flex items-center justify-center">
                <span class="text-[#30A050] font-semibold text-sm">CR</span>
              </div>
              <div>
                <div class="text-xl font-medium text-[#332C21]">CRDB</div>
              </div>
            </div>
            <div class="flex items-center gap-5">
              <div class="text-xl font-semibold text-[#332C21]">TZS 400,000</div>
              <button class="text-[#332C21] p-1 hover:bg-gray-100 rounded">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- NCBA Bank -->
        <div class="bg-white rounded-lg p-5 shadow-sm hover:shadow-md transition-shadow">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#EAEAEA] rounded flex items-center justify-center">
                <span class="text-[#666666] font-semibold text-sm">NC</span>
              </div>
              <div>
                <div class="text-xl font-medium text-[#332C21]">NCBA</div>
              </div>
            </div>
            <div class="flex items-center gap-5">
              <div class="text-xl font-semibold text-[#332C21]">TZS 82,000</div>
              <button class="text-[#332C21] p-1 hover:bg-gray-100 rounded">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Ecobank -->
        <div class="bg-white rounded-lg p-5 shadow-sm hover:shadow-md transition-shadow">
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#005B82] rounded flex items-center justify-center">
                <span class="text-white font-semibold text-sm">EC</span>
              </div>
              <div>
                <div class="text-xl font-medium text-[#332C21]">Ecobank</div>
              </div>
            </div>
            <div class="flex items-center gap-5">
              <div class="text-xl font-semibold text-[#332C21]">TZS 848,000</div>
              <button class="text-[#332C21] p-1 hover:bg-gray-100 rounded">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Net Worth Section -->
      <div class="bg-white rounded-lg p-5 shadow-sm mb-10 max-w-7xl mx-auto hover:shadow-md transition-shadow">
        <div class="flex flex-col lg:flex-row gap-8">
          <!-- Chart Section -->
          <div class="flex-1">
            <h2 class="text-xl font-semibold text-[#332C21] mb-6">Net Worth</h2>
            
            <!-- Pie Chart Container -->
            <div class="relative w-80 h-80 mx-auto">
              <!-- Pie Chart -->
              <div class="w-full h-full rounded-full bg-conic-gradient relative">
                <!-- Chart segments using CSS conic-gradient -->
                <div class="absolute inset-0 rounded-full" style="background: conic-gradient(#5D9EEB 0deg 60deg, #63CDD3 60deg 120deg, #C292FF 120deg 180deg, #ECB359 180deg 240deg, #607799 240deg 300deg, #E276CA 300deg 360deg);"></div>
                
                <!-- Center cutout -->
                <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-32 h-32 bg-white rounded-full flex items-center justify-center">
                  <div class="text-center">
                    <div class="text-3xl font-semibold text-[#332C21] leading-tight">Total</div>
                    <div class="text-3xl font-semibold text-[#332C21] leading-tight">TZS</div>
                    <div class="text-3xl font-semibold text-[#332C21] leading-tight">3,105,000</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Percentage Indicators -->
            <div class="flex justify-center gap-5 mt-6">
              <div class="text-sm text-[#332C21] bg-gray-100 px-3 py-2 rounded">16.10%</div>
              <div class="text-sm text-[#332C21] bg-gray-100 px-3 py-2 rounded">24.15%</div>
              <div class="text-sm text-[#332C21] bg-gray-100 px-3 py-2 rounded">26.40%</div>
            </div>
          </div>

          <!-- Legend Section -->
          <div class="flex-1">
            <div class="grid grid-cols-2 gap-4">
              <!-- Left Column -->
              <div class="space-y-4">
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#5D9EEB] rounded-full"></div>
                  <span class="text-sm text-[#332C21]">Fixed</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#63CDD3] rounded-full"></div>
                  <span class="text-sm text-[#332C21]">Savings</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#C292FF] rounded-full"></div>
                  <span class="text-sm text-[#332C21]">Salary</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#ECB359] rounded-full"></div>
                  <span class="text-sm text-[#332C21]">Current</span>
                </div>
              </div>

              <!-- Right Column -->
              <div class="space-y-4">
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#607799] rounded-full"></div>
                  <span class="text-sm text-[#332C21]">Term</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#E276CA] rounded-full"></div>
                  <span class="text-sm text-[#332C21]">Mobile Money</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#72C5B1] rounded-full"></div>
                  <span class="text-sm text-[#332C21]">Card</span>
                </div>
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
// Financial Account page logic
</script>

<style scoped>
/* Custom styles for financial account page */
.bg-conic-gradient {
  background: conic-gradient(
    #5D9EEB 0deg 60deg,
    #63CDD3 60deg 120deg,
    #C292FF 120deg 180deg,
    #ECB359 180deg 240deg,
    #607799 240deg 300deg,
    #E276CA 300deg 360deg
  );
}

/* Improved alignment and spacing */
.account-card {
  min-height: 93px;
  display: flex;
  align-items: center;
}

.net-worth-section {
  min-height: 593px;
}

.pie-chart-container {
  aspect-ratio: 1;
  max-width: 336px;
  max-height: 336px;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .account-cards {
    @apply grid-cols-1;
  }
}

@media (max-width: 768px) {
  .net-worth-section {
    @apply flex-col;
  }
  
  .pie-chart-container {
    @apply w-64 h-64;
  }
}
</style>
