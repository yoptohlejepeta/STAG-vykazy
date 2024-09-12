import { createRouter, createWebHistory } from 'vue-router'
import BooksView from '@/views/BooksView.vue'
import GraphView from '@/views/GraphView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/books',
      name: 'books',
      component: BooksView
    },
    {
      path: '/graph',
      name: 'graph',
      component: GraphView
    }
  ]
})

export default router
