<template>
  <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

interface ChartData {
  labels: string[]
  datasets: {
    label: string
    data: number[]
  }[]
}

interface ChartOptions {
  responsive: boolean
}

const chartData = ref<ChartData>({
  labels: [],
  datasets: []
})

const chartOptions = ref<ChartOptions>({
  responsive: true
})

const fetchData = async () => {
  try {
    const response = await fetch('http://localhost:8000/data')

    chartData.value = await response.json()
    console.log(chartData.value)
  } catch (error) {
    console.error('Error fetching data:', error)
  }
}

onMounted(() => {
  fetchData()
})
</script>
