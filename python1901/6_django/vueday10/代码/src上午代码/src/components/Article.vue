<template>
<div>
  <p v-for="item in articles">{{ item.title }}  {{ item.desc }}</p>
  <p>搜索</p>
  <p>标题: <input type="text" v-model="search_title" /> <input type="button" value="搜索" @click="search()"/></p>
  <p>创建</p>
  <p>创建文章为: {{ article.title }}  {{ article.desc }}</p>
  <p>标题: <input type="text" v-model="sub_title"></p>
  <p>描述: <input type="text" v-model="sub_desc"></p>
  <p><input type="submit" value="提交" @click="submit_article()"></p>
</div>
</template>

<script>
export default {
  name: 'article',
  data () {
    return {
      articles: '',
      article: '',
      search_title: '',
      sub_title: '',
      sub_desc: ''
    }
  },
  mounted () {
    // $(document).ready()
    // 当页面渲染时，向后端发送获取文章列表的请求，并渲染页面
    const url = '/app/article/'
    this.axios.get(url).then(res => {
      // res.data取的是后端返回的json格式数据
      // res.data===>>{code:200,msg:'请求成功', data: {count:10, next='', results={}}
      const resp = res.data
      // ===  ==
      if (resp.code === 200) {
        console.log(resp.data.results)
        this.articles = resp.data.results
      }
    }).catch(err => {
      console.log(err)
    })
  },
  methods: {
    search: function () {
      const title = this.search_title
      const params = {
        'title': title
      }
      const url = '/app/article/'
      // 传参数，注意1： 传递的参数定义为params，this.axios.get(url，{params})
      // 注意2：传递的参数定义为searchData, this.axios.get(url, {params: searchData})
      this.axios.get(url, {params}).then(
        res => {
          // res.data==>{code:200,msg:'请求成功', data: {count:10, next='', results={}}
          console.log(res.data)
          this.articles = res.data.data.results
        }
      ).catch(
        err => {
          console.log(err)
        }
      )
    },
    submit_article: function () {
      const title = this.sub_title
      const desc = this.sub_desc
      const params = {
        'title': title,
        'desc': desc
      }
      const url = '/app/article/'
      this.axios.post(url, params).then(
        res => {
          console.log(res.data)
          this.article = res.data.data
        }
      ).catch(
        err => {
          console.log(err)
        }
      )
    }
  }
}
</script>

<style scoped>

</style>
