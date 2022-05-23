<template>
  <div class="movie-detail">
    {{ $route.params.movieId }}
  </div>
</template>

<script>
export default {
  name: 'MovieDetailView',
}
</script>

<style>
.movie-detail {
  margin-top: 100px;
}
</style>