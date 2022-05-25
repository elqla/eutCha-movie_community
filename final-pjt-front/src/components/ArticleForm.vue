<template>
  <div>
    <h1>FORM</h1>
    <p>{{credentials.moviePk}}</p>
    <b-form @submit.prevent="newArticle(credentials)" align="left">
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
      <b-button type="submit" variant="dark">글쓰기</b-button>
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
        moviePk: this.payload.movie.id
      },
    }
  },
  props: {
    payload: Object,
  },
  methods: {
    ...mapActions(['newArticle',])
  }
}
</script>

<style>

</style>