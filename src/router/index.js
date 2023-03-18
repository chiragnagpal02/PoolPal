import { createRouter, createWebHistory } from 'vue-router'

// shared
import login from '@/views/LogIn.vue'
import signUp from '@/views/SignUp.vue'

// driver
import driverHomepage from '@/views/driver/DriverHomePage.vue'
import driverProfile from '@/views/driver/DriverProfile.vue'
import driverRides from '@/views/driver/DriverRides.vue'
import driverChats from '@/views/driver/DriverChats.vue'

//passenger
import passengerHomepage from '@/views/passenger/PassengerHomePage.vue'
import passengerProfile from '@/views/passenger/PassengerProfile.vue'
import createRequest from '@/views/passenger/CreateRequest.vue'
import passengerRides from '@/views/passenger/PassengerRides.vue'

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
    path: '/createRequest',
    name: 'createRequest',
    component: createRequest
  },
  {
    path: '/passengerRides',
    name: 'passengerRides',
    component: passengerRides
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
