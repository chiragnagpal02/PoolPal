import { createRouter, createWebHistory } from 'vue-router'
import login from '@/views/LogIn.vue'
import signUp from '@/views/SignUp.vue'
import passengerHomepage from '@/views/passenger/PassengerHomePage.vue'
import driverHomepage from '@/views/driver/DriverHomePage.vue'
import adminHomepage from '@/views/admin/AdminHomePage.vue'



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
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
