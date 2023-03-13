import { createRouter, createWebHistory } from 'vue-router'
import identity from '@/views/IdentityChoice.vue'
const routes = [
  {
    path: '/',
    name: 'identity',
    component: identity
  },
  {
    path: '/home',
    name: 'home',
  },
  {
    path: '/profile',
    name: 'profile',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/ProfileView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
