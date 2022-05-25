<template>
  <div class="container">
    <h1>algorithm</h1>
    <div class="row">
      <movie-item
        v-for="movie in eutMovies"
        :key="movie.id"
        :movie="movie"
        category="eut"
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
    ...mapGetters(['eutMovies',]),
  }
}
</script>

<style>

</style>