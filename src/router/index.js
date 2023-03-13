import { createRouter, createWebHistory } from 'vue-router'
import identity from '@/views/IdentityChoice.vue'
import login from '@/views/LogIn.vue'
const routes = [
  {
    path: '/',
    name: 'identity',
    component: identity
  },
  {
    path: '/login',
    name: 'login',
    component: login
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
