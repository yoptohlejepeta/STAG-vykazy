<template>
    <DataTable :value="pivotData" tableStyle="min-width: 50rem">
      <Column v-for="col in pivotColumns" :key="col.field" :field="col.field" :header="col.header" />
    </DataTable>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import DataTable from 'primevue/datatable'
  import Column from 'primevue/column'
  
  interface Product {
    OKRUH1: string
    OKRUH2: string
    count: number
  }
  
  interface PivotColumn {
    field: string
    header: string
  }
  
  const products = ref<Product[]>([])
  const pivotData = ref<any[]>([])
  const pivotColumns = ref<PivotColumn[]>([])
  
  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:8000/data/okruhy')
      const data = await response.json()
      products.value = data
      transformToPivotTable(data)
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }
  
  const transformToPivotTable = (data: Product[]) => {
    const uniqueOKRUH1 = [...new Set(data.map(item => item.OKRUH1))]
    const uniqueOKRUH2 = [...new Set(data.map(item => item.OKRUH2))]
  
    pivotColumns.value = [{ field: 'OKRUH1', header: 'OKRUH1' }]
    uniqueOKRUH2.forEach(okruh2 => {
      pivotColumns.value.push({ field: okruh2, header: okruh2 })
    })
  
    const pivotRows = uniqueOKRUH1.map(okruh1 => {
      const row: any = { OKRUH1: okruh1 }
      uniqueOKRUH2.forEach(okruh2 => {
        const product = data.find(item => item.OKRUH1 === okruh1 && item.OKRUH2 === okruh2)
        row[okruh2] = product ? product.count : 0
      })
      return row
    })
  
    pivotData.value = pivotRows
  }
  
  onMounted(() => {
    fetchData()
  })
  </script>