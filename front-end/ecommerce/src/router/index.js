import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Basket from '../views/Basket.vue'
import Product from '../views/Product.vue'
import Create from '../views/Create.vue'
import Delete from '../views/Delete.vue'
import Update from '../views/Update.vue'

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
    path: '/create',
    name: 'Create',
    component: Create
  },
  {
    path: "/delete",
    name: "Delete",
    component: Delete
  },
  {
    path: "/update",
    name: "Update",
    component: Update
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
