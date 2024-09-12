<script setup lang="ts">
import { ref } from 'vue'
import { RouterView, useRoute } from 'vue-router'
import router from './router';

const active_tab = ref(0)

const route = useRoute()
</script>

<template>
  <header class="pb-5">
        <h1 class="text-9xl mb-4 pt-4 text-center">Uchazeči UJEP</h1>
        <h2 class="text-7xl mb-4 pb-3 text-center text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400">PŘF

        </h2>

        <div role="tablist" class="tabs tabs-lifted tabs-lg mt-auto pb-0 w-full">
          <router-link
            role="tab"
            to="/books"
            class="tab"
            :class="{ 'tab-active': route.path === '/books' }"
          >Books</router-link>
          <router-link
            role="tab"
            to="/graph"
            class="tab"
            :class="{ 'tab-active': route.path === '/graph' }"
          >Graph</router-link>
          <router-link
            role="tab"
            to="/idk"
            class="tab"
            :class="{ 'tab-active': route.path === '/idk' }"
          >IDK</router-link>
        </div>
  </header>
  <main class="container mx-auto">
    <RouterView />
  </main>
</template>
