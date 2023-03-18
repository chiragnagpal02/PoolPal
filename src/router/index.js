import { createRouter, createWebHistory } from 'vue-router'

// shared
import login from '@/views/LogIn.vue'
import signUp from '@/views/SignUp.vue'

// driver
import driverHomepage from '@/views/driver/DriverHomePage.vue'
import driverProfile from '@/views/driver/DriverProfile.vue'

//passenger
import passengerHomepage from '@/views/passenger/PassengerHomePage.vue'
import passengerProfile from '@/views/passenger/PassengerProfile.vue'
//admin
import adminHomepage from '@/views/admin/AdminHomePage.vue'


// import createcarpool from '@/views/CreateCarpool.vue'

const routes = [
  // shared
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

  // driver
  {
    path: '/driverHomepage',
    name: 'driverHomepage',
    component: driverHomepage
  },
  {
    path: '/driverProfile',
    name: 'driverProfile',
    component: driverProfile
  },

  // passenger
  {
    path: '/passengerHomepage',
    name: 'passengerHomepage',
    component: passengerHomepage
  },

  {
    path: '/passengerProfile',
    name: 'passengerProfile',
    component: passengerProfile
  },

  // admin
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
