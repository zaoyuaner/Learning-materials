import Vue from 'vue'
import App from './App.vue'


// 1. 安装和导入vue-router
// 需要先在当前项目中安装vue-router：
// 		npm install vue-router: 
import VueRouter from 'vue-router'

Vue.config.productionTip = false
Vue.use(VueRouter)  // 使用vue-router

// 导入axios
import Axios from 'axios'
Vue.prototype.$ajax = Axios  // 目的：让vue实例可以使用$.ajax来调用Axios
//prototype:原型

// 2. 导入组件
import BaseUseView from './components/BaseUseView.vue'
import OptionView from './components/OptionView.vue'
import ArgsView from './components/ArgsView.vue'
import AxiosView from './components/AxiosView.vue'
import DemoView from './components/DemoView.vue'

// 3. 定义路由
var routes = [
		{
			path: '/',
			redirect: '/baseuseview'  // 重定向
		},
		{
			path: '/baseuseview',
			component: BaseUseView
		}, 
		{
			path: '/optionview',
			component: OptionView
		},
		{
			path: '/argsview',
			component: ArgsView
		},
		{
			path: '/axiosview',
			component: AxiosView
		},
		{
			path: '/demoview',
			component: DemoView
		}
]

// 4. 创建router对象
var router = new VueRouter({
	routes,
	// 选中后的类名 (默认值是router-link-active)
  linkActiveClass: 'active'
})


// 5. 挂载根实例
new Vue({
  render: h => h(App),
	router  //挂载根实例 
}).$mount('#app')
