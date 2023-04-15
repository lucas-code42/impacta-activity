import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Basket from '../views/Basket.vue'
import Product from '../views/Product.vue'
import Admin from '../views/Admin.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/basket',
    name: 'Basket',
    component: Basket
  },
  {
    path: '/product',
    name: 'Product',
    component: Product
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
