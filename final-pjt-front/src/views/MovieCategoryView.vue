<template>
  <div class="category d-flex flex-column">
    <movie-eutgorithm></movie-eutgorithm>
    <movie-popular></movie-popular>
    <movie-recent></movie-recent>
  </div>
</template>

<script>
import MovieEutgorithm from '@/components/MovieEutgorithm.vue'
import MoviePopular from '../components/MoviePopular.vue'
import MovieRecent from '../components/MovieRecent.vue'

import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieCategoryView',
  components: {
    MovieEutgorithm,
    MoviePopular,
    MovieRecent,
  },
  methods: {
    ...mapActions(['fetchMovies',])
  },
  computed: {
    ...mapGetters(['eutLoaded']),
  },
  created() {
    this.fetchMovies()
  }
}
</script>

<style>
.category {
  margin-top: 100px;
}
</style>