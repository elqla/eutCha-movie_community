<template>
  <div>
    <h1>popular</h1>
    <movie-item
      v-for="movie in popularMovies"
      :key="movie.id"
      :movie="movie"
    ></movie-item>
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