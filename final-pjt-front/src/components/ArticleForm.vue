<template>
  <div>
    <h1>FORM</h1>
    <b-form @submit.prevent="newArticle(credentials)" align="left">
      <b-form-group label-for="title" label="Title">
        <b-form-input v-model="credentials.title" id="title" placeholder="제목" type="text" required>
        </b-form-input>
      </b-form-group>
      <br>
      <!-- movie object를 어떻게 넘겨주지? -->
      <b-form-group label-for="movie" label="Movie">  
        <b-form-input  v-model="credentials.movie" id="movie" placeholder="영화제목" type="text" required>
        </b-form-input>
      </b-form-group>
      <br>
      <!--  -->
      <b-form-group label-for="content" label="Content">
        <b-form-input v-model="credentials.content" id="content" placeholder="내용" type="text" required>
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
        title : this.payload.title,
        movie : this.payload.movie,
        content : this.payload.content,
      }
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