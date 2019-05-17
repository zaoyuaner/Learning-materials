<template>
<div>
  <p>{{ msg }}</p>
  <!-- v-if v-else -->
  <p>
    <h6 v-if="isLogin">{{ username }}</h6>
    <h6 v-else>登录 | 注册</h6>
  </p>
  <!-- v-show -->
  <p v-show="isShow">今天好happy</p>
  <!-- v-for -->
  <p v-for="a in scores">{{ a }}</p>
  <p v-for="item in res">{{ item.name }}  {{ item.age }}</p>
  <!-- v-bind -->
  <p class="redcolor" style="font-weight: bold;">今天天气不错</p>
  <p v-bind:class="color" v-bind:style="styleObj">今天天气不错</p>
  <!--点击事件-->
  <!--<p v-bind:onclick="happy()">点我让你happy</p>-->
  <p v-on:click="happy()">点我让你happy</p>
  <p @click="happy()" :style="styleObj" :class="color">再点我一下</p>
  <!-- v-text  v-html-->
  {{ content }}
  <p v-text="content"></p>
  <p  v-html="content"></p>
  <!-- v-model -->
  <input type="text" v-model="title" />
  <input type="button" @click="submit_title()"/>
  <!--修改值-->
  <p @click="add()">+</p>
  <p> {{ num }} </p>
  <p> {{ new_num.score }}</p>
  <p @click="sub()">-</p>
</div>
</template>

<script>
import Vue from 'vue'
export default {
  name: 'VueBase',
  data () {
    return {
      msg: 'vue基础，好简单',
      username: 'COCO',
      isLogin: false,
      isShow: true,
      scores: [80, 90, 78, 100],
      res: [{
        name: '小明',
        age: '20'
      }, {
        name: '小花',
        age: '18'
      }
      ],
      color: 'redcolor',
      styleObj: {
        fontWeight: 'bold'
      },
      content: '<h3>我是h3标签</h3>',
      title: 'vue基础内容介绍',
      num: 50,
      new_num: {
        score: 90,
        username: '小明'
      }
    }
  },
  methods: {
    happy: function () {
      alert('happy day')
    },
    submit_title: function () {
      alert(this.title)
    },
    add: function () {
      // 将num加一
      console.log(this)
      this.num++
      this.scores[0]++
      Vue.set(this.scores, 0, 10)
      this.new_num.score++
    },
    sub: function () {
      // 将num减一
      this.num--
    }
  }
}
</script>

<style scoped>
.redcolor {color:red;}
</style>
