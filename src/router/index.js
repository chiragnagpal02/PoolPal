import { createRouter, createWebHistory } from 'vue-router'

// shared
import login from '@/views/LogIn.vue'
import signUp from '@/views/SignUp.vue'

// driver
import driverHomepage from '@/views/driver/DriverHomePage.vue'
import driverProfile from '@/views/driver/DriverProfile.vue'
import driverRides from '@/views/driver/DriverRides.vue'
import driverChats from '@/views/driver/DriverChats.vue'
import driverRequest from '@/views/driver/DriverRequest.vue'

//passenger
import passengerHomepage from '@/views/passenger/PassengerHomePage.vue'
import passengerProfile from '@/views/passenger/PassengerProfile.vue'
import passengerRequest from '@/views/passenger/PassengerRequest.vue'
import passengerRides from '@/views/passenger/PassengerRides.vue'
import passengerChats from '@/views/passenger/PassengerChats.vue'

//admin
import adminHomepage from '@/views/admin/AdminHomePage.vue'


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
  {
    path: '/driverRides',
    name: 'driverRides',
    component: driverRides
  },
  {
    path: '/driverChats',
    name: 'driverChats',
    component: driverChats
  },
  {
    path: '/driverRequest',
    name: 'driverRequest',
    component: driverRequest
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
  {
    path: '/passengerRequest',
    name: 'passengerRequest',
    component: passengerRequest
  },
  {
    path: '/passengerRides',
    name: 'passengerRides',
    component: passengerRides
  },
  {
    path: '/passengerChats',
    name: 'passengerChats',
    component: passengerChats
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
