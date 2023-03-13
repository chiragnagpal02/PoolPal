import { createRouter, createWebHistory } from 'vue-router'
import identity from '@/views/IdentityChoice.vue'
const routes = [
  {
    path: '/',
    name: 'identity',
    component: identity
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
