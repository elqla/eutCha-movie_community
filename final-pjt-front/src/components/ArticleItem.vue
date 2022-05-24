<template>
  <div>
    <b-card bg-variant="light" :header="article.title" class="text-center">
      <b-card-text>{{ article.content }}</b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>