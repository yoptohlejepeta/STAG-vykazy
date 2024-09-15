<script setup lang="ts">
import TabMenu from 'primevue/tabmenu'
import { RouterView } from 'vue-router'
</script>

<template>
  <header class="pb-5">
    <!-- <TabMenu :model="items">
    <template #item="{ item, props }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                <span v-bind="props.icon" />
                <span v-bind="props.label">{{ item.label }}</span>
            </a>
        </router-link>
        <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
            <span v-bind="props.icon" />
            <span v-bind="props.label">{{ item.label }}</span>
        </a>
    </template>
</TabMenu> -->
  </header>
  <main class="container mx-auto">
    <RouterView />
  </main>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100..900&display=swap');

/* Styling for the fancy and modern heading */
h1 {
  font-family: 'Roboto Slab', sans-serif; /* Modern and clean font */
}
</style>
