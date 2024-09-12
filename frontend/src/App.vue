<script setup lang="ts">
import Tabs from 'primevue/tabs'
import TabList from 'primevue/tablist'
import Tab from 'primevue/tab'
import TabPanels from 'primevue/tabpanels'
import TabPanel from 'primevue/tabpanel'
import { RouterView } from 'vue-router'
</script>

<template>
  <header class="pb-5">
    <h1 class="text-9xl mb-4 pt-4 text-center">Uchazeči UJEP</h1>
    <h2
      class="text-7xl mb-4 pb-3 text-center text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400"
    >
      PŘF
    </h2>
    <Tabs value="0" class="mb-4">
      <TabList>
        <Tab value="0">
          <router-link to="/books"> Books </router-link>
        </Tab>
        <Tab value="1">
          <router-link to="/graph">Graph</router-link>
        </Tab>
        <Tab value="2">
          <router-link to="/idk">IDK</router-link>
        </Tab>
      </TabList>
      <TabPanels>
        <TabPanel value="0"> </TabPanel>
        <TabPanel value="1"> </TabPanel>
        <TabPanel value="2"> </TabPanel>
      </TabPanels>
    </Tabs>
  </header>
  <main class="container mx-auto">
    <RouterView />
  </main>
</template>
