<template>
  <div class="articleList">
    <h1>내가 작성한 게시글</h1>
    <div class="container">
      <div v-if="isProfile" class="articleItems row">
        <article-item
          v-for="article in articles"
          :key="article.pk"
          :article="article"
          class="articleItem"
        ></article-item>
      </div>
      <div v-if="!isArticle">
        <b-card bg-variant="light" class="text-center mt-4">
          <b-card-text class="profile-article-content">후기가 없습니다.</b-card-text>
        </b-card>
      </div>
  </div>
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem.vue'
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name:'ProfileArticleList',
  components:{
    ArticleItem
  },
  computed:{
    ...mapGetters(['profile', 'isProfile']),
    articles() {
      return [...this.profile.articles].reverse()
    },
    isArticle() {
      return !_.isEmpty(this.profile.articles)
    }
  },
}
</script>

<style>
.articleList{
  /* margin: auto; */
  max-width: 1000px;
  padding: 20px;
}
.articleItems{
  display: flex;
}
.articleItem{
  padding: 10px;
}
.profile-article-content {
  color: black;
  font-size: 20px;
}
</style>