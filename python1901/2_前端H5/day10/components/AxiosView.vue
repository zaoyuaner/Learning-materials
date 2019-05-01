<template>
	<div>
		<h2>网络请求Axios</h2>
		
		<ul>
			<li v-for="news in newss">
				<a :href="news.link">{{ news.title }}</a>
			</li>
		</ul>
		
	</div>
</template>

<script>
	export default {
		data(){
			return {
				newss: null
			}
		},
		// 钩子函数: 周期性函数
		// created: 会被自动调用
		created() {
			this.$ajax.get('https://www.apiopen.top/journalismApi')
				.then( r => this.newss = r.data.data.money )  // 请求成功
				.catch( err => console.log("err:" + err) )   // 请求失败
		}
		
	}
</script>

<style>
</style>
