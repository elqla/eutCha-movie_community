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
  </div>
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem.vue'
import { mapGetters } from 'vuex'
export default {
  name:'ProfileArticleList',
  components:{
    ArticleItem
  },
  computed:{
    ...mapGetters(['profile', 'isProfile']),
    articles() {
      return [...this.profile.articles].reverse()
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
</style>