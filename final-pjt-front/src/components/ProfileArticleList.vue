<template>
  <div>
    <h1>profilearticlelist</h1>
    <div class="container">
    <div v-if="isProfile" class="row">
      <article-item
        v-for="article in articles"
        :key="article.pk"
        :article="article"
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

</style>