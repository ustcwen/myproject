import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Hello from '@/components/Hello'
import trymodel from '@/components/trymodel'
import trytable from '@/components/trytable'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/hello',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/trymodel',
      name: 'trymodel',
      component: trymodel
    },{
      path: '/trytable',
      name: 'trytable',
      component: trytable
    },
  ]
})
