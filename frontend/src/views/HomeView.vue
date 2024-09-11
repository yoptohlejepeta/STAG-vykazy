<template>
    <main class="container">
      <h1>Hello</h1>
        <button @click="fetchBooks">
            Get books
        </button>
        <button @click="clear">
            Clear
        </button>
  
      <div v-if="books.length">
        <h2>Fetched Books:</h2>
        <table>
            <thead>
                <tr>
                <th>Name</th>
                <th>Author</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(book, index) in books" :key="index">
                <td>{{ book.name }}</td>
                <td>{{ book.author }}</td>
                </tr>
            </tbody>
        </table>
      </div>
      <p v-else>No books yet.</p>
    </main>
  </template>
  
  <script setup lang="ts">
    import { ref } from 'vue'

    const numbers = ref<number[]>([])
    const books = ref<{ name: string; author: string }[]>([])

    const fetchBooks = async () => {
        try {
        const response = await fetch('http://localhost:8000/books')
        if (response.ok) {
            books.value = await response.json()
        } else {
            console.error('Failed to fetch books:', response.status)
        }
        } catch (error) {
        console.error('Error fetching books:', error)
        }
    }

    const clear = () => {
        numbers.value = []
        books.value = []
    }
  </script>
  