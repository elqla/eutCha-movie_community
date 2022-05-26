<template>
  <div class="container" style="margin-top: 100px;" v-if="ifArticle">
    <div class="d-flex flex-column align-items-start">
      <router-link :to="{ name: 'movieDetail', params: { movieId } }" class="text-decoration-none text-white">
        <h2 style="font-family: 'Gowun Dodum', sans-serif;">{{ article.movie.title }}</h2>
      </router-link>
      <div class="article-detail d-flex row">
        <div class="container-item1 article-detail-user-info d-flex flex-column col-12 col-lg-3">
          <div class="d-flex">
            <div class="article-detail-user-info-img">
              <img :src="picture" alt="profile image">
            </div>
            <div class="article-detail-user-info-username">{{ article.user.nickname || article.user.username }}</div>
          </div>
            <span class="article-detail-user-info-created">create: {{$moment(article.created_at).calendar()}}</span>
            <span class="article-detail-user-info-updated">update: {{$moment(article.updated_at).calendar()}}</span>
          <div v-if="isCurrentUser" class="article-detail-user-info-button d-flex justify-content-end">
            <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
              <b-button pill variant="primary">수정</b-button>
            </router-link>
            <b-button @click="deleteArticle(articlePk)" pill variant="danger">삭제</b-button>
          </div>
        </div>
        
        <div class="container-item2 d-flex flex-column col-12 col-lg-9">
          <h1 style="font-family: 'Gowun Dodum', sans-serif;">{{ article.title }}</h1>
          <div class="article-detail-context d-flex flex-column align-items-start">
            <p>{{ article.content }}</p>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <div class="container">
      <b-form @submit.prevent="createComment(credential)" align="left" class="comment-form d-flex mb-3">
        <b-form-input v-model="comment" id="content" placeholder="댓글을 작성해주세요." type="text" required>
        </b-form-input>
        <b-button type="submit" variant="dark">작성</b-button>
      </b-form>
      <div v-if="ifNotComment">
        <comment-list
          v-for="comment in comments"
          :key="comment.id"
          :comment="comment"
        ></comment-list>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import vueMoment from 'vue-moment'
Vue.use(vueMoment)
import _ from 'lodash'

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
    },
    ifNotComment(){
      if(!_.isEmpty(this.comments)){
        return true
      }
      else{
        return false
      }
    },
    ifArticle(){
      if(!_.isEmpty(this.article)){
        return true
      }
      else{
        return false
      }
    }
  },
  methods: {
    ...mapActions(['fetchArticle', 'deleteArticle', 'newComment']),
    createComment (credential) {
      this.newComment(credential)
      this.comment = ''
    }
  },
  created() {
    this.fetchArticle(this.$route.params.articlePk)
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Noto+Sans+KR&display=swap');

.article-detail {
  width: 100%;
  font-family: 'Gowun Dodum', sans-serif;
}

.article-detail-user-info {
  box-sizing: border-box;
  max-height: 250px;
  padding: 1rem;
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
  margin-top: 10px;
  text-align: end;
}
.article-detail-user-info-updated {
  margin-bottom: 5px;
  text-align: end;
}

.article-detail-context {
  padding: 0 1rem 1rem 1rem;
  font-size: 20px;
  text-align: start;
  background-color: rgba(0, 0, 0, 0.1);

}

.comment-form > button {
  margin-left: 20px;
  width: 80px;
}

.container-item2{
  padding: 1rem;
  /* border-style: solid; */
  /* border-color: rgba(66, 66, 66, 0.185); */
  background-color: rgba(121, 121, 121, 0.144);
  color: rgb(255, 255, 255);
  border-radius: 1rem;
  line-height: 35px;
}

</style>