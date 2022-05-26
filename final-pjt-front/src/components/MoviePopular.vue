<template>
  <div class="container">
    <h1 class="category-title">인기 영화</h1>
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