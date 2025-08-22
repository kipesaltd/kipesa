<template>
  <div class="min-h-screen bg-[#F5FAF6]">
    <!-- Navigation -->
    <Navigation />
    
    <!-- Currency Exchange Rates Strip -->
    <div class="bg-white shadow-sm">
      <div class="">
        <!-- Main Rates Row with Marquee -->
        <div class="overflow-hidden py-2.5">
          <div class="marquee-container">
            <div class="marquee-content flex items-center gap-8 text-sm whitespace-nowrap">
              <!-- First set of rates -->
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">USD:</span>
                <span class="font-light text-[#332C21]">Buy 2469- Sell 2494</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">EUR:</span>
                <span class="font-light text-[#332C21]">Buy 2583 - Sell 2610</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">GBP:</span>
                <span class="font-light text-[#332C21]">Buy 2980- Sell 3010</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">AED:</span>
                <span class="font-light text-[#332C21]">Buy 672.33 - Sell 679.02</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">KES:</span>
                <span class="font-light text-[#332C21]">Buy 16.64 - Sell 16.78</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">UGX:</span>
                <span class="font-light text-[#332C21]">Buy 0.63 - Sell 0.66</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">CNY:</span>
                <span class="font-light text-[#332C21]">Buy 0.63 - Sell 0.66</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">INR:</span>
                <span class="font-light text-[#332C21]">Buy 29.72 - Sell 30.02</span>
              </div>
              
              <!-- Duplicate set for seamless loop -->
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">USD:</span>
                <span class="font-light text-[#332C21]">Buy 2469- Sell 2494</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">EUR:</span>
                <span class="font-light text-[#332C21]">Buy 2583 - Sell 2610</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">GBP:</span>
                <span class="font-light text-[#332C21]">Buy 2980- Sell 3010</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">AED:</span>
                <span class="font-light text-[#332C21]">Buy 672.33 - Sell 679.02</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">KES:</span>
                <span class="font-light text-[#332C21]">Buy 16.64 - Sell 16.78</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">UGX:</span>
                <span class="font-light text-[#332C21]">Buy 0.63 - Sell 0.66</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">CNY:</span>
                <span class="font-light text-[#332C21]">Buy 0.63 - Sell 0.66</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="font-medium text-[#332C21]">INR:</span>
                <span class="font-light text-[#332C21]">Buy 29.72 - Sell 30.02</span>
              </div>
            </div>
          </div>
        </div>
        
        
      </div>
    </div>

    <!-- Background Decorative Elements -->
    <div class="relative">
      <img src="/icons/leaf-pattern-1.svg" alt="" class="absolute top-0 left-0 w-48 h-32 opacity-10 z-0 hidden lg:block" />
      <img src="/icons/leaf-pattern-2.svg" alt="" class="absolute top-8 right-0 w-48 h-32 opacity-10 z-0 hidden lg:block" />
      <img src="/icons/leaf-pattern-3.svg" alt="" class="absolute top-12 right-12 w-48 h-32 opacity-10 z-0 hidden xl:block" />
    </div>

    <!-- Main Content -->
    <div class="relative z-10">
      <!-- Welcome Section -->
      <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4 pt-16 pb-8">
        <h1 class="text-xl md:text-2xl font-normal text-[#332C21]">Welcome Paul Mandele,</h1>
        <div class="bg-[#F5FAF6] border border-[rgba(51,44,33,0.3)] rounded-lg px-3 py-2 w-fit">
          <div class="flex items-center justify-between gap-2 min-w-[140px]">
            <span class="text-xs font-normal text-[#332C21]">September 2023</span>
            <svg class="w-4 h-4 text-[#332C21]" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Search Bar -->
      <div class="flex justify-center pb-8">
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

      <!-- Statistics Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 pb-8">
        <!-- Financial Account Card -->
        <div class="bg-white rounded-lg p-4 relative overflow-hidden shadow-sm min-h-[132px]">
          <!-- Background circles -->
          <div class="absolute -top-9 -right-2">
            <div class="w-28 h-28 rounded-full bg-[#74D9C7] absolute top-0.5 left-0"></div>
            <div class="w-32 h-32 rounded-full bg-[rgba(116,217,199,0.2)] absolute top-0 left-0.5"></div>
            <!-- Icon container -->
            <div class="absolute top-12 left-8 w-9 h-9 bg-white rounded-lg flex items-center justify-center">
              <img src="/icons/bank.svg" alt="Bank" class="w-8 h-8" />
            </div>
          </div>
          <div class="relative z-10 h-full flex flex-col justify-between">
            <div class="pt-4">
              <p class="text-base md:text-lg font-medium text-[#332C21] opacity-90">Financial account</p>
              <p class="text-xl md:text-2xl font-semibold text-[#332C21]">TZS 3,105,000</p>
            </div>
            <p class="text-sm text-[#332C21] opacity-70 mt-auto">Total available balance</p>
          </div>
        </div>

        <!-- Bill Center Card -->
        <div class="bg-white rounded-lg p-4 relative overflow-hidden shadow-sm min-h-[132px]">
          <!-- Background circles -->
          <div class="absolute -top-9 -right-2">
            <div class="w-28 h-28 rounded-full bg-[#FFCC7C] absolute top-0.5 left-0"></div>
            <div class="w-32 h-32 rounded-full bg-[rgba(255,204,124,0.2)] absolute top-0 left-0.5"></div>
            <!-- Icon container -->
            <div class="absolute top-12 left-8 w-9 h-9 bg-white rounded-lg flex items-center justify-center">
              <img src="/icons/bill.svg" alt="Bill" class="w-8 h-8" />
            </div>
          </div>
          <div class="relative z-10 h-full flex flex-col justify-between">
            <div class="pt-4">
              <p class="text-base md:text-lg font-medium text-[#332C21] opacity-90">Bill center</p>
              <p class="text-xl md:text-2xl font-semibold text-[#332C21]">6</p>
            </div>
            <p class="text-sm text-[#332C21] opacity-70 mt-auto">Total bills</p>
          </div>
        </div>

        <!-- Budget Center Card -->
        <div class="bg-white rounded-lg p-4 relative overflow-hidden shadow-sm min-h-[132px]">
          <!-- Background circles -->
          <div class="absolute -top-9 -right-2">
            <div class="w-28 h-28 rounded-full bg-[#FF9999] absolute top-0.5 left-0"></div>
            <div class="w-32 h-32 rounded-full bg-[rgba(255,153,153,0.2)] absolute top-0 left-0.5"></div>
            <!-- Icon container -->
            <div class="absolute top-12 left-8 w-9 h-9 bg-white rounded-lg flex items-center justify-center">
              <img src="/icons/pie-chart.svg" alt="Budget" class="w-8 h-8" />
            </div>
          </div>
          <div class="relative z-10 h-full flex flex-col justify-between">
            <div class="pt-4">
              <p class="text-base md:text-lg font-medium text-[#332C21] opacity-90">Budget center</p>
              <p class="text-xl md:text-2xl font-semibold text-[#332C21]">TZS 240,000</p>
              <div class="flex items-center gap-1 mt-2">
                <p class="text-sm text-[#F35252]">TZS 530,000</p>
                <svg class="w-4 h-4 text-[#F35252]" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/>
                </svg>
              </div>
            </div>
            <p class="text-sm text-[#332C21] opacity-70 mt-auto">Budgeted available balance</p>
          </div>
        </div>

        <!-- Calendar Card -->
        <div class="bg-white rounded-lg p-4 relative overflow-hidden shadow-sm min-h-[132px]">
          <!-- Background circles -->
          <div class="absolute -top-9 -right-2">
            <div class="w-28 h-28 rounded-full bg-[#92C4FF] absolute top-0.5 left-0"></div>
            <div class="w-32 h-32 rounded-full bg-[rgba(146,196,255,0.2)] absolute top-0 left-0.5"></div>
            <!-- Icon container -->
            <div class="absolute top-12 left-8 w-9 h-9 bg-white rounded-lg flex items-center justify-center">
              <img src="/icons/calendar.svg" alt="Calendar" class="w-8 h-8" />
            </div>
          </div>
          <div class="relative z-10 h-full flex flex-col justify-between">
            <div class="pt-4">
              <p class="text-base md:text-lg font-medium text-[#332C21] opacity-90">Calendar</p>
              <p class="text-xl md:text-2xl font-semibold text-[#332C21]">3</p>
            </div>
            <p class="text-sm text-[#332C21] opacity-70 mt-auto">Total overdue bills</p>
          </div>
        </div>
      </div>

      <!-- Content Grid -->
      <div class="grid grid-cols-1 xl:grid-cols-2 gap-6 md:gap-8">
        <!-- Your Spending Widget -->
        <div class="bg-white rounded-lg shadow-sm">
          <div class="p-4 md:p-6">
            <!-- Spending Header -->
            <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4 pb-6">
              <h3 class="text-lg md:text-xl font-semibold text-[#332C21]">Your spending</h3>
              <div class="bg-white border border-[rgba(51,44,33,0.3)] rounded-lg px-3 py-2 w-fit">
                <div class="flex items-center justify-between gap-2 min-w-[140px]">
                  <span class="text-xs font-normal text-[#332C21]">September 2023</span>
                  <svg class="w-4 h-4 text-[#332C21]" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                  </svg>
                </div>
              </div>
            </div>

            <!-- Spending Content -->
            <div class="grid grid-cols-2 gap-4 md:gap-8 pb-6">
              <!-- Legend Column 1 -->
              <div class="space-y-2">
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#5D9EEB] rounded-full flex-shrink-0"></div>
                  <span class="text-sm text-[#332C21]">Water bill</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#D67DCD] rounded-full flex-shrink-0"></div>
                  <span class="text-sm text-[#332C21]">Food</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#607799] rounded-full flex-shrink-0"></div>
                  <span class="text-sm text-[#332C21]">Gym</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#F89B67] rounded-full flex-shrink-0"></div>
                  <span class="text-sm text-[#332C21]">Home</span>
                </div>
              </div>

              <!-- Legend Column 2 -->
              <div class="space-y-2">
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#63CDD3] rounded-full flex-shrink-0"></div>
                  <span class="text-sm text-[#332C21]">Phone bill</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#ECB359] rounded-full flex-shrink-0"></div>
                  <span class="text-sm text-[#332C21]">House Help</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#7BC282] rounded-full flex-shrink-0"></div>
                  <span class="text-sm text-[#332C21]">Shopping</span>
                </div>
              </div>
            </div>

            <!-- Pie Chart Section -->
            <div class="relative w-full max-w-[270px] aspect-square mx-auto">
              <!-- Pie Chart -->
              <svg class="w-full h-full" viewBox="0 0 270 270">
                <!-- Water bill slice (largest) -->
                <path d="M 135 135 L 135 35 A 100 100 0 0 1 196.06 57.32 Z" fill="#5D9EEB" />
                <!-- Phone bill slice -->
                <path d="M 135 135 L 196.06 57.32 A 100 100 0 0 1 212.68 73.94 Z" fill="#63CDD3" stroke="#F35252" stroke-width="2" />
                <!-- Food slice -->
                <path d="M 135 135 L 212.68 73.94 A 100 100 0 0 1 235 135 Z" fill="#D67DCD" />
                <!-- House Help slice -->
                <path d="M 135 135 L 235 135 A 100 100 0 0 1 212.68 196.06 Z" fill="#ECB359" />
                <!-- Gym slice -->
                <path d="M 135 135 L 212.68 196.06 A 100 100 0 0 1 135 235 Z" fill="#607799" />
                <!-- Shopping slice -->
                <path d="M 135 135 L 135 235 A 100 100 0 0 1 57.32 212.68 Z" fill="#7BC282" stroke="#F35252" stroke-width="2" />
                <!-- Home slice -->
                <path d="M 135 135 L 57.32 212.68 A 100 100 0 0 1 35 135 Z" fill="#F89B67" />
              </svg>
              
              <!-- Center Total -->
              <div class="absolute inset-0 flex items-center justify-center">
                <div class="text-center">
                  <p class="text-2xl md:text-3xl font-semibold leading-tight text-[#332C21]">Total</p>
                  <p class="text-2xl md:text-3xl font-semibold leading-tight text-[#332C21]">TZS</p>
                  <p class="text-2xl md:text-3xl font-semibold leading-tight text-[#332C21]">900,000</p>
                </div>
              </div>
            </div>

            <!-- Gym percentage highlight -->
            <div class="text-center md:text-right pt-4">
              <p class="text-sm font-medium text-[#332C21]">3.Gym 11.11%</p>
            </div>
          </div>
        </div>

        <!-- Calendar Widget -->
        <div class="bg-white rounded-lg shadow-sm">
          <div class="p-4 md:p-6">
            <!-- Calendar Header -->
            <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4 pb-6">
              <h3 class="text-lg md:text-xl font-semibold text-[#332C21]">Payment reminders</h3>
              <div class="flex items-center gap-3">
                <svg class="w-5 h-5 text-[#332C21]" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
                </svg>
                <span class="text-sm text-[#332C21]">Sept 2023</span>
                <svg class="w-5 h-5 text-[#332C21]" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
              </div>
            </div>

            <!-- Calendar Grid -->
            <div class="grid grid-cols-7 gap-1 mb-4 max-w-sm mx-auto">
              <!-- Day Headers -->
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm md:text-base font-medium text-[#332C21]">Mo</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm md:text-base font-medium text-[#332C21]">Tu</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm md:text-base font-medium text-[#332C21]">We</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm md:text-base font-medium text-[#332C21]">Th</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm md:text-base font-medium text-[#332C21]">Fri</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm md:text-base font-medium text-[#332C21]">Sa</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm md:text-base font-medium text-[#332C21]">Su</span>
              </div>

              <!-- Previous month days -->
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">27</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">28</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">29</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">30</span>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">31</span>
              </div>
              <div class="h-10 flex items-center justify-center relative">
                <span class="text-sm font-medium text-[#332C21]">1</span>
                <div class="absolute bottom-1 w-1.5 h-1.5 bg-[#F35252] rounded-full"></div>
              </div>
              <div class="h-10 flex items-center justify-center">
                <span class="text-sm font-medium text-[#332C21]">2</span>
              </div>

              <!-- Calendar days grid continues with simplified responsive layout -->
              <!-- Week 1 -->
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">3</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">4</span></div>
              <div class="h-10 flex items-center justify-center relative"><span class="text-sm font-medium text-[#332C21]">5</span><div class="absolute bottom-1 w-1.5 h-1.5 bg-[#F35252] rounded-full"></div></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">6</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">7</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">8</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">9</span></div>
              
              <!-- Week 2 -->
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">10</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">11</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">12</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">13</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">14</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">15</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">16</span></div>

              <!-- Week 3 -->
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">17</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">18</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">19</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">20</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">21</span></div>
              <div class="h-10 flex items-center justify-center relative bg-[rgba(48,159,80,0.1)] rounded-full"><span class="text-sm font-medium text-[#332C21] relative z-10">22</span><div class="absolute bottom-1 w-2 h-2 bg-[#EC923F] rounded-full"></div></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">23</span></div>

              <!-- Week 4 -->
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">24</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">25</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">26</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">27</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">28</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[#332C21]">29</span></div>
              <div class="h-10 flex items-center justify-center relative"><span class="text-sm font-medium text-[#332C21]">30</span><div class="absolute bottom-1 w-1.5 h-1.5 bg-[#1B7EDA] rounded-full"></div></div>

              <!-- Next month -->
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">1</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">2</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">3</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">4</span></div>
              <div class="h-10 flex items-center justify-center"><span class="text-sm font-medium text-[rgba(51,44,33,0.6)]">5</span></div>
            </div>

            <!-- Payment Items -->
            <div class="space-y-3">
              <!-- Healthcare Payment -->
              <div class="border border-[rgba(48,159,80,0.3)] rounded-lg p-3">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 border border-[#0095DA] rounded-lg flex items-center justify-center flex-shrink-0">
                      <img src="/icons/medical-services.svg" alt="Healthcare" class="w-6 h-6" />
                    </div>
                    <div>
                      <p class="text-sm text-[#332C21]">Healthcare</p>
                      <p class="text-base font-medium text-[#332C21]">TZS 50,000</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="flex items-center gap-1">
                      <div class="w-2 h-2 bg-[#F35252] rounded-full"></div>
                      <span class="text-sm text-[#332C21] hidden sm:inline">Overdue</span>
                    </div>
                    <svg class="w-5 h-5 text-[#332C21]" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                    </svg>
                  </div>
                </div>
              </div>

              <!-- Netflix Payment -->
              <div class="border border-[rgba(48,159,80,0.3)] rounded-lg p-3">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 border border-[#E50914] rounded-lg flex items-center justify-center flex-shrink-0">
                      <img src="/icons/netflix.svg" alt="Netflix" class="w-6 h-6" />
                    </div>
                    <div>
                      <p class="text-sm text-[#332C21]">Netflix</p>
                      <p class="text-base font-medium text-[#332C21]">TZS 20,000</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="flex items-center gap-1">
                      <div class="w-2 h-2 bg-[#F35252] rounded-full"></div>
                      <span class="text-sm text-[#332C21] hidden sm:inline">Overdue</span>
                    </div>
                    <svg class="w-5 h-5 text-[#332C21]" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                    </svg>
                  </div>
                </div>
              </div>

              <!-- Legend -->
              <div class="flex flex-wrap items-center gap-4 pt-2">
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
// Dashboard page logic
</script>

<style scoped>
/* Custom styles for dashboard */
.font-archia {
  font-family: 'Archia', sans-serif;
}

/* Marquee animation styles */
.marquee-container {
  width: 100%;
}

.marquee-content {
  animation: marquee 30s linear infinite;
  will-change: transform;
}

@keyframes marquee {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}

/* Pause animation on hover for better UX */
.marquee-content:hover {
  animation-play-state: paused;
}
</style>

