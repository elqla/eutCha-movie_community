<template>
  <div style="margin-top: 100px;">
    <article-form
      :payload="{ title: article.title, movie: movie, content: article.content }"
      :method="method"
      :articlePk="articlePk"
    ></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'ArticleEditView',
  components: { ArticleForm },
  computed: {
    ...mapGetters(['movie', 'article']),
    method: () => 'put',
    articlePk () {
      return this.$route.params.articlePk
    }
  }
}
</script>

<style>

</style>