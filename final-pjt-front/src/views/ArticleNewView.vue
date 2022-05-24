<template>
  <div style="margin-top: 100px;">
    <article-form
      :payload="payload"
    ></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'

export default {
  name: 'ArticleNewView',
  components: { ArticleForm },
  data() {
    return {
      payload: {
        title: '',
        movie: '',
        content: '',
      }
    }
  }
}
</script>

<style>

</style>