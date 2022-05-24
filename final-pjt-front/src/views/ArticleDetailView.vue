<template>
  <div class="container" style="margin-top: 100px;">
    <h1>ArticleDetailView</h1>
    <div>
      <h2>영화 제목: {{ article.movie.title }}</h2>
      <div class="user-info d-flex">
        <img class="article-profile-img" :src="picture" alt="profile image">
        <p>{{ article.user.username }}</p>
        <button>수정</button>
        <button>삭제</button>
      </div>
      <div>
        <h2>게시글 제목: {{ article.title }}</h2>
        <p>게시글 내용: {{ article.content }}</p>
      </div>
    </div>
    <hr>
    <h1>Comment List</h1>
    <comment-list
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    ></comment-list>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name:'ArticleDetailView',
  components: { CommentList },
  computed: {
    ...mapGetters(['article']),
    picture () {
      return 'http://localhost:8000' + this.article.user.picture
    },
    comments () {
      return this.article.comments
    }
  },
  methods: {
    ...mapActions(['fetchArticle'])
  },
  created() {
    this.fetchArticle(this.$route.params.articlePk)
  }
}
</script>

<style>
.article-profile-img {
  border-radius: 5rem;
}
</style>