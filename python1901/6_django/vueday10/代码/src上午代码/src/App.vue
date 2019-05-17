<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
    <!-- 3. 使用自定义的helloworld组件 -->
    <helloworld1></helloworld1>
    <a href="/base/">a标签的跳转----VUE基础操作</a>
    <router-link to="/base/">router-link标签的跳转----VUE基础操作</router-link>
    <router-link to="/article/">文章列表</router-link>
  </div>
</template>

<script>
// 1. 引入自定义组件HelloWorld1.vue
import helloworld1 from './components/HelloWorld1.vue'
export default {
  name: 'App',
  components: {
    // 2. 加载自定义的组件
    helloworld1
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
