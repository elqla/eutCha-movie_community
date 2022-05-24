<template>
  <div class="col-3 mb-4">
    <router-link :to="{ name: 'article', params: { articlePk } }" class="text-decoration-none text-black">
      <b-card bg-variant="light" :header="article.title" class="text-center">
        <b-card-text class="article-content">{{ article.content }}</b-card-text>
      </b-card>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  computed: {
    articlePk () {
      return this.article.id
    }
  }
}
</script>

<style>

.article-content {
    display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
}
</style>