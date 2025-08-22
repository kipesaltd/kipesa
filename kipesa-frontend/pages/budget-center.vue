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

    <!-- Main Container -->
    <div class="relative z-10">
      <!-- Search Bar -->
      <div class="flex justify-center py-8 px-4">
        <div class="relative bg-white rounded-full shadow-sm w-full max-w-[609px] h-16">
          <div class="absolute right-6 top-1/2 transform -translate-y-1/2">
            <svg class="w-7 h-7 text-[#309F50]" viewBox="0 0 28 28" fill="none" stroke="currentColor">
              <circle cx="14" cy="14" r="10" stroke-width="2"/>
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

      <!-- Header Section -->
      <div class="flex justify-between items-center px-4 md:px-8 lg:px-16 xl:px-32 pb-8">
        <!-- Title and Subtitle -->
        <div class="flex flex-col gap-2">
          <h1 class="text-2xl font-semibold text-[#332C21]">Budget Centre</h1>
          <p class="text-base font-normal text-[#332C21] opacity-80">Manage your finances</p>
        </div>

        <!-- Add Button -->
        <button class="flex items-center justify-center w-[52px] h-[52px] bg-[#309F50] rounded-full hover:bg-[#2A8B47] transition-colors">
          <svg class="w-3 h-3 text-white" viewBox="0 0 22 22" fill="none" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 4v14m7-7H4"/>
          </svg>
        </button>
      </div>

      <!-- Budget vs Spend Chart -->
      <div class="mx-4 md:mx-8 lg:mx-16 xl:mx-32 mb-8">
        <div class="bg-white rounded-lg shadow-sm">
          <!-- Chart Header -->
          <div class="flex justify-between items-center p-8 pb-6">
            <h3 class="text-2xl font-semibold text-[#332C21]">Budget vs Spend</h3>
            <div class="flex items-center gap-5">
              <!-- Legend -->
              <div class="flex items-center gap-5">
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#74D9C7] rounded-full"></div>
                  <span class="text-sm text-[#332C21]">Budget</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-2.5 h-2.5 bg-[#FF9999] rounded-full"></div>
                  <span class="text-sm text-[#332C21]">Spend</span>
                </div>
              </div>
              
              <!-- Date Filter -->
              <div class="bg-white border border-[rgba(51,44,33,0.3)] rounded-lg px-3 py-2">
                <div class="flex items-center justify-between gap-2 min-w-[140px]">
                  <span class="text-xs font-normal text-[#332C21]">September 2023</span>
                  <svg class="w-4 h-4 text-[#332C21]" viewBox="0 0 20 20" fill="none" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 8l4 4 4-4"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <!-- Chart Container -->
          <div class="relative px-8 pb-8">
            <!-- Y-axis Labels -->
            <div class="absolute left-12 top-0 h-64 flex flex-col justify-between text-xs text-[#332C21] opacity-80 py-2">
              <span>1600</span>
              <span>1200</span>
              <span>800</span>
              <span>400</span>
              <span>0</span>
            </div>
            
            <!-- Chart Area -->
            <div class="ml-20 relative">
              <!-- Grid Lines -->
              <div class="absolute inset-0 h-64">
                <div class="h-full flex flex-col justify-between">
                  <div class="border-b border-[#332C21] opacity-10"></div>
                  <div class="border-b border-[#332C21] opacity-10"></div>
                  <div class="border-b border-[#332C21] opacity-10"></div>
                  <div class="border-b border-[#332C21] opacity-10"></div>
                  <div class="border-b border-[#332C21] opacity-10"></div>
                </div>
              </div>
              
              <!-- Chart Line -->
              <div class="relative h-64">
                <!-- Chart paths based on exact Figma coordinates -->
                <svg class="w-full h-full" viewBox="0 0 1126 231" preserveAspectRatio="none">
                  <!-- Budget Line path from Figma -->
                  <path 
                    d="M 0 180 L 50 170 L 100 165 L 150 150 L 200 140 L 250 135 L 300 125 L 350 120 L 400 115 L 450 110 L 500 105 L 550 100 L 600 95 L 650 90 L 700 85 L 750 80 L 800 75 L 850 70 L 900 65 L 950 60 L 1000 55 L 1050 50 L 1100 45 L 1126 40"
                    fill="none" 
                    stroke="#FF9999" 
                    stroke-width="2"
                  />
                  
                  <!-- Spend Line path -->
                  <path 
                    d="M 0 160 L 50 140 L 100 120 L 150 100 L 200 80 L 250 100 L 300 90 L 350 85 L 400 75 L 450 65 L 500 70 L 550 60 L 600 55 L 650 50 L 700 45 L 750 40 L 800 35 L 850 30 L 900 25 L 950 20 L 1000 15 L 1050 10 L 1100 8 L 1126 5"
                    fill="none" 
                    stroke="#74D9C7" 
                    stroke-width="2"
                  />
                  
                  <!-- Data Points for Budget -->
                  <g fill="#74D9C7">
                    <circle cx="0" cy="160" r="3"/>
                    <circle cx="100" cy="120" r="3"/>
                    <circle cx="200" cy="80" r="3"/>
                    <circle cx="300" cy="90" r="3"/>
                    <circle cx="400" cy="75" r="3"/>
                    <circle cx="500" cy="70" r="3"/>
                    <circle cx="600" cy="55" r="3"/>
                    <circle cx="700" cy="45" r="3"/>
                    <circle cx="800" cy="35" r="3"/>
                    <circle cx="900" cy="25" r="3"/>
                    <circle cx="1000" cy="15" r="3"/>
                    <circle cx="1100" cy="8" r="3"/>
                  </g>
                  
                  <!-- Data Points for Spend -->
                  <g fill="#FF9999">
                    <circle cx="0" cy="180" r="3"/>
                    <circle cx="100" cy="165" r="3"/>
                    <circle cx="200" cy="140" r="3"/>
                    <circle cx="300" cy="125" r="3"/>
                    <circle cx="400" cy="115" r="3"/>
                    <circle cx="500" cy="105" r="3"/>
                    <circle cx="600" cy="95" r="3"/>
                    <circle cx="700" cy="85" r="3"/>
                    <circle cx="800" cy="75" r="3"/>
                    <circle cx="900" cy="65" r="3"/>
                    <circle cx="1000" cy="55" r="3"/>
                    <circle cx="1100" cy="45" r="3"/>
                  </g>
                </svg>
              </div>
            </div>
            
            <!-- X-axis Labels -->
            <div class="ml-20 flex justify-between text-xs text-[#332C21] opacity-80 mt-2 overflow-hidden">
              <span>0</span>
              <span>01</span>
              <span>02</span>
              <span>03</span>
              <span>04</span>
              <span>05</span>
              <span>06</span>
              <span>07</span>
              <span>08</span>
              <span>09</span>
              <span>10</span>
              <span>11</span>
              <span>12</span>
              <span>13</span>
              <span>14</span>
              <span>15</span>
              <span>16</span>
              <span>17</span>
              <span>18</span>
              <span>19</span>
              <span>20</span>
              <span>21</span>
              <span>22</span>
              <span>23</span>
              <span>24</span>
              <span>25</span>
              <span>26</span>
              <span>27</span>
              <span>28</span>
              <span>29</span>
              <span>30</span>
            </div>
            
            <!-- Chart Label -->
            <div class="absolute left-8 top-1/2 transform -translate-y-1/2 -rotate-90">
              <span class="text-xs text-[#332C21] opacity-80 whitespace-nowrap">Amount in thousands and TZS</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Budget Statistics Cards -->
      <div class="mx-4 md:mx-8 lg:mx-16 xl:mx-32 mb-8">
        <div class="bg-white rounded-lg shadow-sm">
          <!-- Date Filter -->
          <div class="flex justify-start p-6 pb-4">
            <div class="bg-white border border-[rgba(51,44,33,0.3)] rounded-lg px-3 py-2">
              <div class="flex items-center justify-between gap-2 min-w-[140px]">
                <span class="text-xs font-normal text-[#332C21]">September 2023</span>
                <svg class="w-4 h-4 text-[#332C21]" viewBox="0 0 20 20" fill="none" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 8l4 4 4-4"/>
                </svg>
              </div>
            </div>
          </div>

          <!-- Statistics Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-8 px-6 pb-6 relative">
            <!-- Expected Income -->
            <div class="flex flex-col gap-1">
              <p class="text-lg font-medium text-[#332C21] opacity-90">Expected Income</p>
              <p class="text-2xl font-semibold text-[#332C21]">TZS 1,474,700</p>
              <button class="text-sm font-medium text-[#309F50] opacity-90 text-left hover:opacity-100 mt-1">Edit</button>
            </div>

            <!-- Budgeted Expense -->
            <div class="flex flex-col gap-1">
              <p class="text-lg font-medium text-[#332C21] opacity-90">Budgeted Expense</p>
              <p class="text-2xl font-semibold text-[#332C21]">TZS 1,140,000</p>
              <button class="text-sm font-medium text-[#309F50] opacity-90 text-left hover:opacity-100 mt-1">Edit</button>
            </div>

            <!-- Actual Expense -->
            <div class="flex flex-col gap-1">
              <p class="text-lg font-medium text-[#332C21] opacity-90">Actual Expense</p>
              <p class="text-2xl font-semibold text-[#332C21]">TZS 900,000</p>
            </div>

            <!-- Budgeted Reserves -->
            <div class="flex flex-col gap-1">
              <p class="text-lg font-medium text-[#332C21] opacity-90">Budgeted Reserves</p>
              <p class="text-2xl font-semibold text-[#332C21]">TZS 334,700</p>
            </div>

            <!-- Divider Lines -->
            <div class="absolute left-1/4 top-0 w-px h-20 bg-[rgba(51,44,33,0.2)] hidden xl:block"></div>
            <div class="absolute left-1/2 top-0 w-px h-20 bg-[rgba(51,44,33,0.2)] hidden md:block"></div>
            <div class="absolute right-1/4 top-0 w-px h-20 bg-[rgba(51,44,33,0.2)] hidden xl:block"></div>
          </div>
        </div>
      </div>

      <!-- Content Grid -->
      <div class="px-4 md:px-8 lg:px-16 xl:px-32 mb-8">
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
        <!-- Your Spending Widget - Fixed dimensions from Figma -->
        <div class="bg-white rounded-lg shadow-sm w-full h-[411px] overflow-hidden">
          <!-- Header -->
          <div class="flex justify-between items-center px-5 pt-5 pb-4">
            <h3 class="text-xl font-semibold text-[#332C21]">Your spending</h3>
            <div class="bg-white border border-[rgba(51,44,33,0.3)] rounded-lg px-3 py-2">
              <div class="flex items-center justify-between gap-2 min-w-[140px]">
                <span class="text-xs font-normal text-[#332C21]">September 2023</span>
                <svg class="w-4 h-4 text-[#332C21]" viewBox="0 0 20 20" fill="none" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 8l4 4 4-4"/>
                </svg>
              </div>
            </div>
          </div>

          <!-- Legend and Chart Container -->
          <div class="flex px-5">
            <!-- Legend - Fixed positioning -->
            <div class="w-[216px] pt-6">
              <div class="grid grid-cols-2 gap-5">
                <!-- Left Column -->
                <div class="space-y-2.5">
                  <div class="flex items-center gap-2">
                    <div class="w-2.5 h-2.5 bg-[#5D9EEB] rounded-full"></div>
                    <span class="text-sm text-[#332C21]">Water bill</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="w-2.5 h-2.5 bg-[#D67DCD] rounded-full"></div>
                    <span class="text-sm text-[#332C21]">Food</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="w-2.5 h-2.5 bg-[#607799] rounded-full"></div>
                    <span class="text-sm text-[#332C21]">Gym</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="w-2.5 h-2.5 bg-[#F89B67] rounded-full"></div>
                    <span class="text-sm text-[#332C21]">Home</span>
                  </div>
                </div>

                <!-- Right Column -->
                <div class="space-y-2.5">
                  <div class="flex items-center gap-2">
                    <div class="w-2.5 h-2.5 bg-[#63CDD3] rounded-full"></div>
                    <span class="text-sm text-[#332C21]">Phone bill</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="w-2.5 h-2.5 bg-[#ECB359] rounded-full"></div>
                    <span class="text-sm text-[#332C21]">House Help</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="w-2.5 h-2.5 bg-[#7BC282] rounded-full"></div>
                    <span class="text-sm text-[#332C21]">Shopping</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Pie Chart - Exact dimensions from Figma -->
            <div class="flex-1 flex justify-center items-center">
              <div class="relative w-[270px] h-[270px]">
                <svg class="w-full h-full" viewBox="0 0 454 457">
                  <!-- Pie slices based on exact Figma coordinates -->
                  <path d="M 227 227 L 227 77 A 150 150 0 0 1 315.09 119.98 Z" fill="#5D9EEB" />
                  <path d="M 227 227 L 315.09 119.98 A 150 150 0 0 1 338.02 138.91 Z" fill="#63CDD3" stroke="#F35252" stroke-width="2" />
                  <path d="M 227 227 L 338.02 138.91 A 150 150 0 0 1 377 227 Z" fill="#D67DCD" />
                  <path d="M 227 227 L 377 227 A 150 150 0 0 1 338.02 315.09 Z" fill="#ECB359" />
                  <path d="M 227 227 L 338.02 315.09 A 150 150 0 0 1 227 377 Z" fill="#607799" />
                  <path d="M 227 227 L 227 377 A 150 150 0 0 1 115.98 338.02 Z" fill="#7BC282" stroke="#F35252" stroke-width="2" />
                  <path d="M 227 227 L 115.98 338.02 A 150 150 0 0 1 77 227 Z" fill="#F89B67" />
                </svg>
                
                <!-- Center Total -->
                <div class="absolute inset-0 flex items-center justify-center">
                  <div class="text-center">
                    <div class="text-3xl font-semibold leading-none text-[#332C21]">Total</div>
                    <div class="text-3xl font-semibold leading-none text-[#332C21]">TZS</div>
                    <div class="text-3xl font-semibold leading-none text-[#332C21]">900,000</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Bottom Text -->
          <div class="px-5 pt-4 text-right">
            <p class="text-sm font-medium text-[#332C21]">3.Gym 11.11%</p>
          </div>
        </div>

        <!-- Standard Global Budget Widget - Fixed dimensions from Figma -->
        <div class="bg-white rounded-lg shadow-sm w-full h-[411px] overflow-hidden">
          <!-- Header -->
          <div class="px-5 pt-5 pb-4">
            <h3 class="text-xl font-semibold text-[#332C21]">Standard global budget</h3>
          </div>
            
          <!-- Chart Container -->
          <div class="relative px-5 h-[280px]">
            <!-- Y-axis Labels -->
            <div class="absolute left-8 top-0 h-64 flex flex-col justify-between text-xs text-[#332C21] opacity-80 py-2">
              <span>1000</span>
              <span>800</span>
              <span>600</span>
              <span>400</span>
              <span>200</span>
              <span>0</span>
            </div>
            
            <!-- Chart Area -->
            <div class="ml-16 relative h-64">
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
              
              <!-- Bar Chart - Exact positioning from Figma -->
              <div class="relative h-full flex items-end justify-center gap-20">
                <!-- Needs Bars -->
                <div class="flex flex-col items-center">
                  <div class="w-4 h-[188px] bg-[#309F50] rounded-t-[10px] relative"></div>
                  <div class="w-4 h-[84px] bg-[#5B5B38] rounded-t-[10px] absolute bottom-20"></div>
                  <div class="w-4 h-[39px] bg-[#CCE758] rounded-t-[10px] absolute bottom-0"></div>
                  <span class="text-xs text-[#332C21] opacity-80 mt-2 absolute -bottom-4">Needs</span>
                </div>
                
                <!-- Wants Bars -->
                <div class="flex flex-col items-center">
                  <div class="w-4 h-[118px] bg-[#309F50] rounded-t-[10px] relative"></div>
                  <div class="w-4 h-[64px] bg-[#5B5B38] rounded-t-[10px] absolute bottom-36"></div>
                  <div class="w-4 h-[166px] bg-[#CCE758] rounded-t-[10px] absolute bottom-0"></div>
                  <span class="text-xs text-[#332C21] opacity-80 mt-2 absolute -bottom-4">Wants</span>
                </div>
                
                <!-- Savings Bars -->
                <div class="flex flex-col items-center">
                  <div class="w-4 h-[74px] bg-[#309F50] rounded-t-[10px] relative"></div>
                  <div class="w-4 h-[139px] bg-[#5B5B38] rounded-t-[10px] absolute bottom-6"></div>
                  <div class="w-4 h-[26px] bg-[#CCE758] rounded-t-[10px] absolute bottom-0"></div>
                  <span class="text-xs text-[#332C21] opacity-80 mt-2 absolute -bottom-4">Savings</span>
                </div>
              </div>
            </div>
            
            <!-- Chart Label -->
            <div class="absolute left-5 top-1/2 transform -translate-y-1/2 -rotate-90">
              <span class="text-xs text-[#332C21] opacity-80 whitespace-nowrap">Amount in thousands and TZS</span>
            </div>
          </div>

          <!-- Legend -->
          <div class="flex justify-center gap-5 px-5 pt-6">
            <div class="flex items-center gap-2">
              <div class="w-2.5 h-2.5 bg-[#309F50] rounded-full"></div>
              <span class="text-sm text-[#332C21]">Ideal value</span>
            </div>
            <div class="flex items-center gap-2">
              <div class="w-2.5 h-2.5 bg-[#5B5B38] rounded-full"></div>
              <span class="text-sm text-[#332C21]">Budgeted Value</span>
            </div>
            <div class="flex items-center gap-2">
              <div class="w-2.5 h-2.5 bg-[#CCE758] rounded-full"></div>
              <span class="text-sm text-[#332C21]">Actual value</span>
            </div>
          </div>
        </div>
        </div>
      </div>

      <!-- Budget Illustration -->
      <div class="flex justify-center pb-16 px-4">
        <img src="/icons/budget-illustration.svg" alt="Budget Management Illustration" class="w-72 h-auto" />
      </div>
    </div>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
// Budget Center page logic
</script>

<style scoped>
/* Custom styles for budget center */
.font-archia {
  font-family: 'Archia', sans-serif;
}
</style>
