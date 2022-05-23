<template>
  <div>
    <h1>algorithm</h1>
    <movie-item
      v-for="movie in eutMovies"
      :key="movie.id"
      :movie="movie"
    ></movie-item>
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
    ...mapGetters(['eutMovies',]),
  }
}
</script>

<style>

</style>