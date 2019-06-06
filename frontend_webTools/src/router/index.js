import Vue from 'vue'
import Router from 'vue-router'
/**
 * [lazy loading]
 */
const Home = () => import('@/pages/home')
const FinanceReport = () => import('@/pages/financeReport')

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/financeReport',
      name: 'financeReport',
      component: FinanceReport
    }
  ]
})
