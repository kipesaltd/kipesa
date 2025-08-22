<template>
  <footer class="bg-[#5B5B38] text-white px-6 md:px-12 lg:px-20 py-8 md:py-10">
    <div class="max-w-7xl mx-auto relative">
      <!-- Scroll to top button -->
      <button
        class="hidden sm:inline-flex items-center justify-center w-12 h-12 rounded-full bg-white/20 hover:bg-white/30 transition-colors absolute right-0 md:right-2 -top-4 md:top-1/2 md:-translate-y-1/2"
        aria-label="Scroll to top"
        @click="scrollToTop"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="w-6 h-6 text-white">
          <circle cx="12" cy="12" r="10" stroke-width="2" class="opacity-80" />
          <path d="M8 12l4-4 4 4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </button>

      <!-- Links grid -->
      <div class="grid gap-10 md:gap-20 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
        <!-- About (left group 1) -->
        <div class="space-y-5">
          <h3 class="text-[20px] font-semibold">About</h3>
          <ul class="space-y-3 text-[16px]">
            <li>
              <NuxtLink to="/" class="hover:underline">Home</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/careers" class="hover:underline">Careers</NuxtLink>
            </li>
          </ul>
        </div>

        <!-- About (left group 2) -->
        <div class="space-y-5">
          <h3 class="text-[20px] font-semibold">About</h3>
          <ul class="space-y-3 text-[16px]">
            <li>
              <NuxtLink to="/articles" class="hover:underline">Articles</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/news" class="hover:underline">Latest News</NuxtLink>
            </li>
          </ul>
        </div>

        <!-- Help (right group 1) -->
        <div class="space-y-5">
          <h3 class="text-[20px] font-semibold">Help</h3>
          <ul class="space-y-3 text-[16px]">
            <li>
              <NuxtLink to="/community" class="hover:underline">Community</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/contact" class="hover:underline">Contact Us</NuxtLink>
            </li>
          </ul>
        </div>

        <!-- Help (right group 2) + Social Media stacked on mobile -->
        <div class="space-y-5">
          <h3 class="text-[20px] font-semibold">Help</h3>
          <ul class="space-y-3 text-[16px]">
            <li>
              <NuxtLink to="/privacy" class="hover:underline">Privacy Policy</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/settings" class="hover:underline">Settings</NuxtLink>
            </li>
          </ul>

          <!-- Social Media -->
          <div class="pt-4">
            <h4 class="text-[20px] font-semibold mb-4">Social Media</h4>
            <div class="flex items-center gap-4">
              <!-- Generic social icons (placeholders matching white fills) -->
              <a href="#" aria-label="Follow on Twitter" class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5 text-white">
                  <path d="M19.633 7.997c.013.176.013.353.013.53 0 5.4-4.112 11.63-11.63 11.63-2.312 0-4.46-.676-6.267-1.843.323.038.633.05.968.05 1.917 0 3.68-.65 5.087-1.742-1.792-.037-3.3-1.215-3.817-2.837.251.037.502.063.766.063.366 0 .732-.05 1.073-.139-1.868-.377-3.273-2.017-3.273-3.993v-.05c.54.3 1.168.49 1.83.515-1.085-.724-1.792-1.955-1.792-3.35 0-.74.2-1.418.553-2.01 2.007 2.462 5.012 4.075 8.39 4.248-.063-.3-.101-.612-.101-.926 0-2.256 1.83-4.087 4.087-4.087 1.176 0 2.238.49 2.984 1.28.926-.176 1.818-.515 2.611-.968-.303.943-.943 1.742-1.78 2.244.826-.087 1.617-.314 2.35-.64-.54.814-1.217 1.53-2 2.1z"/>
                </svg>
              </a>
              <a href="#" aria-label="Follow on Facebook" class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5 text-white">
                  <path d="M22 12a10 10 0 10-11.5 9.95v-7.04H7.9V12h2.6V9.8c0-2.57 1.53-3.99 3.87-3.99 1.12 0 2.3.2 2.3.2v2.54h-1.3c-1.28 0-1.68.79-1.68 1.6V12h2.86l-.46 2.91h-2.4v7.04A10 10 0 0022 12z"/>
                </svg>
              </a>
              <a href="#" aria-label="Subscribe on YouTube" class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5 text-white">
                  <path d="M23.5 6.2a3 3 0 00-2.1-2.1C19.4 3.5 12 3.5 12 3.5s-7.4 0-9.4.6A3 3 0 00.5 6.2 31.7 31.7 0 000 12a31.7 31.7 0 00.5 5.8 3 3 0 002.1 2.1c2 .6 9.4.6 9.4.6s7.4 0 9.4-.6a3 3 0 002.1-2.1 31.7 31.7 0 00.5-5.8 31.7 31.7 0 00-.5-5.8zM9.75 15.02V8.98L15.5 12l-5.75 3.02z"/>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Disclaimer -->
      <div class="mt-10 md:mt-12 space-y-3 max-w-5xl">
        <h5 class="text-[14px] font-medium">Disclaimer:</h5>
        <p class="text-[14px] leading-relaxed/loose text-white/80">
          Kipesa strive's to help you make smarter financial decisions. While we adhere to strict editorial integrity, this site may contain references to products from our partners. The content on this page is accurate as of the posting date; however, some of the offers mentioned may have expired. Terms apply to the offers listed on this page. Any opinions, analyses, reviews or recommendations expressed in this article are those of the author’s alone, and have not been reviewed, approved or otherwise endorsed by any individual.
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const scrollToTop = () => {
  if (typeof window !== 'undefined') {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}
</script>
