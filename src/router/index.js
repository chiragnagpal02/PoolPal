import { createRouter, createWebHistory } from 'vue-router'
import login from '@/views/LogIn.vue'
import signUp from '@/views/SignUp.vue'
import homepage from '@/views/HomePage.vue'
import createcarpool from '@/views/CreateCarpool.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: login
  },
  {
    path: '/signUp',
    name: 'signUp',
    component: signUp
  },
  {
    path: '/driverHomepage',
    name: 'driverHomepage',
    component: driverHomepage
  },
  {
    path: '/passengerHomepage',
    name: 'passengerHomepage',
    component: passengerHomepage
  },
  {
    path: '/adminHomepage',
    name: 'adminHomepage',
    component: adminHomepage
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
