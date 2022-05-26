<template>
  <div class="container">
    <h1 class="category-title">{{ currentUser.username }}님을 위한 추천 영화</h1>
    <div class="row">
      <movie-item
        v-for="movie in eutMovies"
        :key="movie.id"
        :movie="movie"
        category="eut"
        class="movieItem"
      ></movie-item>
    </div>
  </div>
</template>

<script>
import MovieItem from './MovieItem.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieEutgorithm',
  components: { 
    MovieItem,
  },
  computed: {
    ...mapGetters(['eutMovies', 'currentUser']),
  }
}
</script>

<style>
.movieItem{
}
</style>