import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Basket from '../views/Basket.vue'
import Create from '../views/Create.vue'
import Delete from '../views/Delete.vue'
import Update from '../views/Update.vue'
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
  {
    path: "/admin-e8312685-4209-4773-969b-8f3587a6dac5",
    name: "Admin",
    component: Admin
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
