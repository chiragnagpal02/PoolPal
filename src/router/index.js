import { createRouter, createWebHistory } from 'vue-router'

// shared
import login from '@/views/LogIn.vue'
import signUp from '@/views/SignUp.vue'

// driver
import driverHomepage from '@/views/driver/DriverHomePage.vue'
import driverProfile from '@/views/driver/DriverProfile.vue'
import driverRides from '@/views/driver/DriverRides.vue'
import driverChats from '@/views/driver/DriverChats.vue'
import driverOffer from '@/views/driver/DriverOffer.vue'
import driverRequests from '@/views/driver/DriverRequests.vue'

//passenger
import passengerHomepage from '@/views/passenger/PassengerHomePage.vue'
import passengerProfile from '@/views/passenger/PassengerProfile.vue'
import passengerRequest from '@/views/passenger/PassengerRequest.vue'
import passengerRides from '@/views/passenger/PassengerRides.vue'
import passengerChats from '@/views/passenger/PassengerChats.vue'
import passengerOffers from '@/views/passenger/PassengerOffers.vue'

//admin
import adminHomepage from '@/views/admin/AdminHomePage.vue'
import adminCurrent from '@/views/admin/CurrentDisputes.vue'
import adminResolved from '@/views/admin/ResolvedDisputes.vue'

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
    path: '/driverOffer',
    name: 'driverOffer',
    component: driverOffer
  },
  {
    path: '/driverRequests',
    name: 'driverRequests',
    component: driverRequests
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
  {
    path: '/passengerOffers',
    name: 'passengerOffers',
    component: passengerOffers
  },

  // admin
  {
    path: '/adminHomepage',
    name: 'adminHomepage',
    component: adminHomepage
  },
  {
    path: '/adminCurrent',
    name: 'adminCurrent',
    component: adminCurrent
  },
  {
    path: '/adminResolved',
    name: 'adminResolved',
    component: adminResolved
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
