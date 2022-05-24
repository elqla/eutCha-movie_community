<template>
  <div style="margin-top: 100px;">
    <article-form
      :payload="{ title: '', movie: movie, content: '' }"
    ></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'ArticleNewView',
  components: { ArticleForm },
  computed: {
    ...mapGetters(['movie'])
  }
}
</script>

<style>

</style>