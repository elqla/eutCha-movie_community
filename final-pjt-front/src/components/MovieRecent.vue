<template>
  <div>
    <h1>recent</h1>
    <movie-item
      v-for="movie in recentMovies"
      :key="movie.id"
      :movie="movie"
    ></movie-item>
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