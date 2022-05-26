<template>
  <div class="article-list">
    <h1>Articles</h1>
    <router-link to="/articles/new" v-if="!articleNull">
      <b-button class="active mb-3" pill variant="outline-success">새 후기 쓰기</b-button>
    </router-link>
    <div class="container">
      <div class="row">
        <article-item
          v-for="article in reverse_articles"
          :key="article.id"
          :article="article"
        ></article-item>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleItem from './ArticleItem.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'ArticleList',
  components: { ArticleItem },
  computed: {
    ...mapGetters(['articles']),
    articleNull() {
      if (this.articles === null) return true
      return false
    },
    reverse_articles() {
      if (this.articleNull) return [{id:1, title: null}, {id:2, title: null}]
      return [...this.articles].reverse()
    }
  }
}
</script>

<style>
.article-list {
  font-family: 'Gowun Dodum', sans-serif;
}
</style>