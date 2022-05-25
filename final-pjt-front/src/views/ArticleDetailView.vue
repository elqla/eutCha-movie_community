<template>
  <div class="container" style="margin-top: 100px;">
    <h1>ArticleDetailView</h1>
    <div class="d-flex flex-column align-items-start">
      <router-link :to="{ name: 'movieDetail', params: { movieId } }" class="text-decoration-none text-black">
        <h2>{{ article.movie.title }}</h2>
      </router-link>
      <div class="article-detail d-flex row">
        <div class="article-detail-user-info d-flex flex-column col-3">
          <div class="d-flex">
            <div class="article-detail-user-info-img">
              <img :src="picture" alt="profile image">
            </div>
            <div class="article-detail-user-info-username">{{ article.user.username }}</div>
          </div>
          <div class="article-detail-user-info-created">{{$moment(article.created_at).calendar()}}</div>
          <div v-if="isCurrentUser" class="article-detail-user-info-button d-flex justify-content-end">
            <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
              <b-button pill variant="primary">수정</b-button>
            </router-link>
            <b-button @click="deleteArticle(articlePk)" pill variant="danger">삭제</b-button>
          </div>
        </div>
        <div class="article-detail-context d-flex flex-column align-items-start col-8">
          <h2 class="align-self-center">{{ article.title }}</h2>
          <p>{{ article.content }}</p>
        </div>
      </div>
    </div>
    <hr>
    <h1>Comment List</h1>
    <b-form @submit.prevent="newComment(credential)" align="left" class="comment-form d-flex">
      <b-form-input v-model="comment" id="content" placeholder="댓글을 작성해주세요." type="text" required>
      </b-form-input>
      <b-button type="submit" variant="dark">작성</b-button>
    </b-form>
    <comment-list
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    ></comment-list>
  </div>
</template>

<script>
import Vue from 'vue'
import vueMoment from 'vue-moment'
Vue.use(vueMoment)

import CommentList from '@/components/CommentList.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name:'ArticleDetailView',
  components: { CommentList },
  data () {
    return {
      comment: ''
    }
  },
  computed: {
    ...mapGetters(['article', 'currentUser']),
    picture () {
      return 'http://localhost:8000' + this.article.user.picture
    },
    comments () {
      return this.article.comments
    },
    articlePk () {
      return this.article.id
    },
    isCurrentUser () {
      if (this.currentUser.pk === this.article.user.pk) return true
      else return false
    },
    movieId() {
      return this.article.movie.id
    },
    credential () {
      return {
        content: this.comment,
        articlePk: this.articlePk
      }
    }
  },
  methods: {
    ...mapActions(['fetchArticle', 'deleteArticle', 'newComment'])
  },
  created() {
    this.fetchArticle(this.$route.params.articlePk)
  }
}
</script>

<style>
.article-detail {
  width: 100%;
}

.article-detail-user-info {
  max-height: 250px;
  padding: 2rem;
  border-style: dashed;
  border-radius: 1rem;
}

.article-detail-user-info-img {
  width: 100px;
}

.article-detail-user-info-img > img {
  width: 100%;
  height: 100%;
  border-radius: 5rem;
}

.article-detail-user-info-username {
  margin-top: 25px;
  margin-left: 25px;
  font-size: 30px;
}

.article-detail-user-info-created {
  margin-top: 20px;
  text-align: end;
}

.article-detail-context {
  margin-left: 1rem;
  padding: 1rem;
  background-color: rgba(0, 0, 0, 0.1);
}

.article-detail-context > h2 {
  font-size: 3rem;
}

.comment-form > button {
  margin-left: 20px;
  width: 80px;
}
</style>