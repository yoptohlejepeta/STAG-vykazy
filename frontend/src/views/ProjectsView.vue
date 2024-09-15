<template>
  <div v-if="projects.length">
    <h2>Projects:</h2>
    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>DEV</th>
          <th>TEST</th>
          <th>PROD</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(project, index) in projects" :key="index">
          <td>
            {{ project.name }}
          </td>
          <td>
            {{ project.dev_url }}
          </td>
          <td>
            {{ project.test_url }}
          </td>
          <td>
            {{ project.prod_url }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <p v-else>No books yet.</p>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const projects = ref<{ name: string; dev_url: string; test_url: string; prod_url: string }[]>([])

const fetchProjects = async () => {
  try {
    const response = await fetch('http://localhost:8000/projects')
    if (response.ok) {
      projects.value = await response.json()
    } else {
      console.error('Failed to fetch projects:', response.status)
    }
  } catch (error) {
    console.error('Error fetching projects:', error)
  }
}

onMounted(() => {
  fetchProjects()
})
</script>
