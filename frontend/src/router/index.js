// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Login',
        component: () => import(/* webpackChunkName: "home" */ '@/views/LoginPage.vue'),
      },
      {
        path: '/profile',
        name: 'Profile',
        component: () => import(/* webpackChunkName: "home" */ '@/views/ProfilePage.vue'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
