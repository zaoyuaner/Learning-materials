<template>
	<div>
		<h2>用户增删改查小项目</h2>
		
		<input type="button" value="新增用户"> 
		<hr>
		
		<table border="1" width="100%" cellspacing="0">
			<tr>
				<th>id</th>
				<th>用户名</th>
				<th>邮箱</th>
				<th>性别</th>
				<th>省份</th>
				<th>操作</th>
			</tr>
			<tr v-for="user in user_list">
				<th>{{ user.id }}</th>
				<th>{{ user.name }}</th>
				<th>{{ user.email }}</th>
				<th>{{ user.sex }}</th>
				<th>{{ user.province }}</th>
				<th>
					<a href="#">修改</a> /
					<a href="#">删除</a>
				</th>		
			</tr>
		</table>
		
		<PopView> </PopView>

	</div>
</template>

<script>
	
	// 导入组件
	import PopView from './PopView.vue'
	
	export default {
		components: {  //注册组件
			PopView
		},
		data() {
			return {
				user_list: [
					{
						id: 1,
						name: "张三",
						email: "邮箱",
						sex: '男',
						province: '广东省',
					},
					{
						id: 2,
						name: "李四",
						email: "邮箱",
						sex: '男',
						province: '广东省',
					}
				],
			}
		}
		
	}
</script>

<style>
</style>
