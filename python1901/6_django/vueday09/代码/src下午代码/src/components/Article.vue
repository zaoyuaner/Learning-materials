<template>
<div>
  <p v-for="item in articles">{{ item.title }}  {{ item.desc }}</p>
</div>
</template>

<script>
export default {
  name: 'article',
  data () {
    return {
      articles: ''
    }
  },
  mounted () {
    // 当页面渲染时，向后端发送获取文章列表的请求，并渲染页面
    const url = '/app/article/'
    this.axios.get(url).then(res => {
      const resp = res.data
      if (resp.code === 200) {
        console.log(resp.data.results)
        this.articles = resp.data.results
      }
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>

<style scoped>

</style>
