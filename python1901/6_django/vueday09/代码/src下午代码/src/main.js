// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

const ajax = axios.create({
  baseURL: 'http://127.0.0.1:8000'
})
Vue.config.productionTip = false
Vue.prototype.axios = ajax

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
