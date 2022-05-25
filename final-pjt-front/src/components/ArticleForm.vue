<template>
  <div>
    <h1>FORM</h1>
    <b-form @submit.prevent="makeArticle(credentials)" align="left">
      <b-form-group label-for="title" label="Title">
        <b-form-input v-model="credentials.article.title" id="title" placeholder="제목" type="text" required>
        </b-form-input>
      </b-form-group>
      <br>
      <!--  -->
      <b-form-group label-for="content" label="Content">
        <b-form-input v-model="credentials.article.content" id="content" placeholder="내용" type="text" required>
        </b-form-input>
      </b-form-group>
      <br>
      <b-button type="submit" variant="dark">{{ buttonText }}</b-button>
    </b-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ArticleForm',
  data(){
    return {
      credentials:{
        article: {
          title : this.payload.title,
          content : this.payload.content,
        },
        moviePk: this.payload.movie.id,
        articlePk: this.articlePk
      },
    }
  },
  props: {
    payload: Object,
    method: String,
    articlePk: Number,
  },
  computed: {
    buttonText () {
      if (this.method === 'post') return '글쓰기'
      else return '수정하기'
    }
  },
  methods: {
    ...mapActions(['newArticle', 'editArticle']),
    makeArticle (credentials) {
      if (this.method === 'post') this.newArticle(credentials)
      else this.editArticle(credentials)
    }
  }
}
</script>

<style>

</style>