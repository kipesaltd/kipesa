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

    <!-- Search Bar -->
    <div class="relative z-10 flex justify-center py-8">
      <div class="relative bg-white rounded-full shadow-sm w-full max-w-[609px] h-16 mx-4">
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

    <!-- Main Content -->
    <div class="relative z-10 max-w-7xl mx-auto px-4 md:px-8 lg:px-16 xl:px-32">
      <!-- Page Header -->
      <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4 mb-8">
        <div>
          <h1 class="text-2xl font-semibold text-[#332C21] mb-2">Calendar</h1>
          <p class="text-base font-normal text-[#332C21] opacity-80">Let's add your event or reminders</p>
        </div>
        
        <!-- Add Button -->
        <button class="bg-[#309F50] rounded-full w-[52px] h-[52px] flex items-center justify-center hover:bg-[#309F50]/90 transition-colors flex-shrink-0">
          <svg class="w-[12.83px] h-[12.83px] text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
          </svg>
        </button>
      </div>

      <!-- Calendar Controls -->
      <div class="flex flex-col lg:flex-row lg:justify-between lg:items-center gap-4 mb-6">
        <!-- Navigation Controls -->
        <div class="flex items-center gap-2.5">
          <!-- Back Button -->
          <button class="flex items-center justify-center w-12 h-12 border border-[rgba(51,44,33,0.3)] rounded-lg hover:bg-gray-50 transition-colors">
            <img src="/icons/arrow-back.svg" alt="Previous" class="w-2 h-3.5" />
          </button>
          
          <!-- Forward Button -->
          <button class="flex items-center justify-center w-12 h-12 border border-[rgba(51,44,33,0.3)] rounded-lg hover:bg-gray-50 transition-colors">
            <svg class="w-2 h-3.5 text-[#332C21]" viewBox="0 0 8 14" fill="currentColor">
              <path d="M1 1l6 6-6 6" stroke="currentColor" stroke-width="1" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>

        <!-- Month/Year Display and View Toggle -->
        <div class="flex flex-col sm:flex-row sm:items-center gap-4">
          <h2 class="text-xl font-semibold text-[#332C21]">September 2023</h2>
          
          <!-- View Toggle Tabs -->
          <div class="flex">
            <!-- Month Tab (Active) -->
            <div class="bg-[#309F50] rounded-l-lg px-4 py-3 min-w-[90px] flex items-center justify-center">
              <span class="text-white font-medium text-lg">Month</span>
            </div>
            <!-- Week Tab -->
            <div class="bg-white border border-[#309F50] px-4 py-3 min-w-[90px] flex items-center justify-center shadow-sm">
              <span class="text-[#332C21] font-normal text-lg">Week</span>
            </div>
            <!-- Day Tab -->
            <div class="bg-white border border-[#309F50] border-l-0 rounded-r-lg px-4 py-3 min-w-[90px] flex items-center justify-center shadow-sm">
              <span class="text-[#332C21] font-normal text-lg">Day</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Calendar -->
      <div class="bg-white rounded-lg shadow-sm overflow-hidden mb-8">
        <!-- Day Headers -->
        <div class="grid grid-cols-7 bg-[rgba(48,159,80,0.1)]">
          <div class="h-14 flex items-center justify-center border-r border-[rgba(51,44,33,0.1)] rounded-tl-lg">
            <span class="text-lg font-medium text-[#332C21]">Sun</span>
          </div>
          <div class="h-14 flex items-center justify-center border-r border-[rgba(51,44,33,0.1)]">
            <span class="text-lg font-medium text-[#332C21]">Mon</span>
          </div>
          <div class="h-14 flex items-center justify-center border-r border-[rgba(51,44,33,0.1)]">
            <span class="text-lg font-medium text-[#332C21]">Tue</span>
          </div>
          <div class="h-14 flex items-center justify-center border-r border-[rgba(51,44,33,0.1)]">
            <span class="text-lg font-medium text-[#332C21]">Wed</span>
          </div>
          <div class="h-14 flex items-center justify-center border-r border-[rgba(51,44,33,0.1)]">
            <span class="text-lg font-medium text-[#332C21]">Thu</span>
          </div>
          <div class="h-14 flex items-center justify-center border-r border-[rgba(51,44,33,0.1)]">
            <span class="text-lg font-medium text-[#332C21]">Fri</span>
          </div>
          <div class="h-14 flex items-center justify-center rounded-tr-lg">
            <span class="text-lg font-medium text-[#332C21]">Sat</span>
          </div>
        </div>

        <!-- Calendar Grid -->
        <div class="grid grid-cols-7">
          <!-- Week 1 -->
          <!-- Previous month dates -->
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[rgba(51,44,33,0.5)] self-end">27</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[rgba(51,44,33,0.5)] self-end">28</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[rgba(51,44,33,0.5)] self-end">29</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[rgba(51,44,33,0.5)] self-end">30</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[rgba(51,44,33,0.5)] self-end">31</span>
          </div>
          <!-- Current month starts -->
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">01</span>
            <div class="space-y-1">
              <div class="bg-[#1B7EDA] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">DSTV payment</span>
              </div>
              <div class="bg-[#F35252] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">Investment</span>
              </div>
            </div>
          </div>
          <div class="h-32 p-2 border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">02</span>
          </div>

          <!-- Week 2 -->
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">03</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">04</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">05</span>
            <div class="space-y-1">
              <div class="bg-[#F35252] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">DSTV payment</span>
              </div>
              <div class="bg-[#F35252] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">Taifa Gas</span>
              </div>
              <div class="bg-[#F35252] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">Vacation</span>
              </div>
            </div>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">06</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">07</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">08</span>
          </div>
          <div class="h-32 p-2 border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">09</span>
          </div>

          <!-- Week 3 -->
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">10</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">11</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">12</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">13</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">14</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">15</span>
          </div>
          <div class="h-32 p-2 border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">16</span>
          </div>

          <!-- Week 4 -->
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">17</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between bg-[rgba(48,159,80,0.1)]">
            <span class="text-lg font-medium text-[#332C21] self-end">18</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">19</span>
            <div class="space-y-1">
              <div class="bg-[#4BD1B9] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">Reminder 1</span>
              </div>
            </div>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">20</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">21</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">22</span>
            <div class="space-y-1">
              <div class="bg-[#F35252] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">DSTV payment</span>
              </div>
              <div class="bg-[#EC923F] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">Healthcare</span>
              </div>
              <div class="bg-[#EC923F] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">Netflix</span>
              </div>
            </div>
          </div>
          <div class="h-32 p-2 border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">23</span>
          </div>

          <!-- Week 5 -->
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">24</span>
            <div class="space-y-1">
              <div class="bg-[#4BD1B9] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">Reminder 2</span>
              </div>
            </div>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">25</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">26</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">27</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">28</span>
          </div>
          <div class="h-32 p-2 border-r border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">29</span>
          </div>
          <div class="h-32 p-2 border-b border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">30</span>
            <div class="space-y-1">
              <div class="bg-[#1B7EDA] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">DSTV payment</span>
              </div>
              <div class="bg-[#1B7EDA] rounded px-2 py-0 text-center">
                <span class="text-white font-medium text-sm">Insurance</span>
              </div>
            </div>
          </div>

          <!-- Week 6 (Next month start) -->
          <div class="h-32 p-2 border-r border-[rgba(51,44,33,0.1)] flex flex-col justify-between rounded-bl-lg">
            <span class="text-lg font-medium text-[#332C21] self-end">01</span>
          </div>
          <div class="h-32 p-2 border-r border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">02</span>
          </div>
          <div class="h-32 p-2 border-r border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">03</span>
          </div>
          <div class="h-32 p-2 border-r border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">04</span>
          </div>
          <div class="h-32 p-2 border-r border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">05</span>
          </div>
          <div class="h-32 p-2 border-r border-[rgba(51,44,33,0.1)] flex flex-col justify-between">
            <span class="text-lg font-medium text-[#332C21] self-end">06</span>
          </div>
          <div class="h-32 p-2 flex flex-col justify-between rounded-br-lg">
            <span class="text-lg font-medium text-[#332C21] self-end">07</span>
          </div>
        </div>
      </div>

      <!-- Legend -->
      <div class="flex flex-wrap items-center justify-center gap-5 mb-16">
        <div class="flex items-center gap-2">
          <div class="w-2.5 h-2.5 bg-[#F35252] rounded-full"></div>
          <span class="text-sm font-normal text-[#332C21]">Overdue</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-2.5 h-2.5 bg-[#EC923F] rounded-full"></div>
          <span class="text-sm font-normal text-[#332C21]">Due</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-2.5 h-2.5 bg-[#1B7EDA] rounded-full"></div>
          <span class="text-sm font-normal text-[#332C21]">Upcoming</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-2.5 h-2.5 bg-[#4BD1B9] rounded-full"></div>
          <span class="text-sm font-normal text-[#332C21]">Reminders</span>
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
  title: 'Calendar - Kipesa'
})
</script>

