<template>
  <div class="col-3 mb-4" :class="{ 'col-12': isNull }">
    <div v-if="isNull===1">
      <router-link to="/articles/new" class="text-decoration-none text-black">
        <b-card bg-variant="light" class="text-center">
          <b-card-text class="article-content">첫 후기를 써주세요!</b-card-text>
        </b-card>
      </router-link>
    </div>
    <div v-if="isNull===2"></div>
    <div v-if="isNull===0">
      <router-link :to="{ name: 'article', params: { articlePk } }" class="text-decoration-none text-black movie-card">
        <b-card bg-variant="light" :header="article.title" class="text-center">
          <b-card-text class="article-content">{{ article.content }}</b-card-text>
        </b-card>
      </router-link>
    </div>
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
    },
    isNull() {
      if (this.article.title === null) return this.articlePk
      return 0
    }
  }
}
</script>

<style>
.movie-card .card-header {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
}

.article-content {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
}
</style>