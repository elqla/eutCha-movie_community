<template>
  <div>
    <h2>{{ article.title }}</h2>
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