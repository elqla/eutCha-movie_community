<template>
  <div class="container">
    <h1>popular</h1>
    <div class="row">
      <movie-item
        v-for="movie in popularMovies"
        :key="movie.id"
        :movie="movie"
        category="pop"
      ></movie-item>
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'MoviePopular',
  components: { 
    MovieItem,
  },
  computed: {
    ...mapGetters(['popularMovies',]),
  }
}
</script>

<style>

</style>