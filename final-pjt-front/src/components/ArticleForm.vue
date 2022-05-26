<template>
  <div class="article-form container">
    <h1>{{ buttonText }}</h1>
    <b-form @submit.prevent="makeArticle(credentials)" align="left">
      <b-form-group label-for="title" label="Title" style="margin: 0 2rem 0 2rem">
        <b-form-input v-model="credentials.article.title" id="title" placeholder="제목" type="text" required>
        </b-form-input>
      </b-form-group>
      <br>
      <!--  -->
      <b-form-group label-for="content" label="Content" style="margin: 0 2rem 0 2rem">
        <b-form-textarea v-model="credentials.article.content" id="content" placeholder="내용" rows="5" required>
        </b-form-textarea>
      </b-form-group>
      <br>
      <b-button type="submit" variant="primary" style="margin: 0 2rem 0 2rem">{{ buttonText }}</b-button>
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
.article-form {
  padding: 2rem;
  background-color: rgba(19, 127, 177, 0);
  border-style: solid;
  border-radius: 2rem;
}

.article-form label {
  color: white;
  font-size: 20px;
}
</style>