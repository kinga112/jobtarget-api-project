import { createRouter, createWebHistory } from 'vue-router';
import Details from './components/Details.vue'
import Jobs from './components/Jobs.vue'

const routes = [
  {
    path: '/',
    component: Jobs
  },
  {
    name: 'job',
    path: '/job/:id',
    component: Details
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
