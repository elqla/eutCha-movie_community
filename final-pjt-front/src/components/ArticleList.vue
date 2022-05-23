<template>
  <div>
    <article-item
      v-for="article in articles"
      :key="article.pk"
      :article="article"
    ></article-item>
  </div>
</template>

<script>
import ArticleItem from './ArticleItem.vue'
export default {
  name: 'ArticleList',
  components: { ArticleItem },
    computed: {
    ...mapGetters(['articles',]),
  }
}
</script>

<style>

</style>