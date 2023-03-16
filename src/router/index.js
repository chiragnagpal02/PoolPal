import { createRouter, createWebHistory } from 'vue-router'
import identity from '@/views/IdentityChoice.vue'
import login from '@/views/LogIn.vue'
import signUp from '@/views/SignUp.vue'
import homepage from '@/views/HomePage.vue'
import createcarpool from '@/views/CreateCarpool.vue'

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
  },
  {
    path: '/signUp',
    name: 'signUp',
    component: signUp
  },
  {
    path: '/homepage',
    name: 'homepage',
    component: homepage
  },
  {
    path: '/createcarpool',
    name: 'createcarpool',
    component: createcarpool
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
