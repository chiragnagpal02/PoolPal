import { createRouter, createWebHistory } from 'vue-router'
import identity from '@/views/IdentityChoice.vue'
import driverLogin from '@/views/driver/DriverLogin.vue'
const routes = [
  {
    path: '/1',
    name: 'identity',
    component: identity
  },
  {
    path: '/',
    name: 'driverLogin',
    component: driverLogin
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
