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
.category-title {
  margin: 2rem;
  font-family: 'Segoe UI';
  text-shadow: 1px 1px 0px #1565C0, 2px 2px 0px #42A5F5, 1px 3px 0px #E3F2FD;
}
</style>