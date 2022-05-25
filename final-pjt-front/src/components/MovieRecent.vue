<template>
  <div class="container">
    <h1>recent</h1>
    <div class="row">
      <movie-item
        v-for="movie in recentMovies"
        :key="movie.id"
        :movie="movie"
        category="rec"
      ></movie-item>
    </div>
  </div>
</template>

<script>
import MovieItem from './MovieItem.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieRecent',
  components: { 
    MovieItem,
  },
  computed: {
    ...mapGetters(['recentMovies',]),
  }
}
</script>

<style>

</style>