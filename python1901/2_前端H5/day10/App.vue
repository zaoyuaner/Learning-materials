<template>
	<div id="app">
		<ul class="nav">
			<li>
				<router-link to='/baseuseview'>VUE基本使用</router-link>
			</li>
			<li>
				<router-link to='/optionview'>VUE组件重要选项</router-link>
			</li>
			<li>
				<router-link to='/argsview'>VUE组件间传参</router-link>
			</li>
			<li>
				<router-link to='/axiosview'>VUE网络请求Axios</router-link>
			</li>
			<li>
				<router-link to='/demoview'>VUE小项目</router-link>
			</li>
		</ul>
		
		<!-- 组件渲染的地方 -->
		<router-view></router-view>
		
	</div>
</template>

<script>
	export default {
		name: 'app',
		components: {
			
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
	
	ul {
		list-style: none;
		overflow: hidden;
	}
	.nav li {
		width: 19%;
		height: 30px;
		border: 1px solid gray;
		float: left;
		text-align: center;
		line-height: 30px;
	}
  .nav li a {
		text-decoration: none;
	}
	
	
</style>
