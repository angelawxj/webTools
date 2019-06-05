import Vue from 'vue'
import Router from 'vue-router'
import home from '@/pages/home'
import financeReport from '@/pages/financeReport'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/financeReport',
      name: 'financeReport',
      component: financeReport,
      meta: {
        title: '财务报表'
      }
    }
  ]
})
