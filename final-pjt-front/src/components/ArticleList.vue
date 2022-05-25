<template>
  <div class="container">
    <div class="row">
      <article-item
        v-for="article in reverse_articles"
        :key="article.pk"
        :article="article"
      ></article-item>
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
    reverse_articles() {
      return [...this.articles].reverse()
    }
  }
}
</script>

<style>

</style>