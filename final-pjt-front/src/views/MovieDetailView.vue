<template>
  <div style="margin-top: 100px;">
    <div class="movie-detail d-flex">
      <img :src="poster" alt="">
      <div>
        <p>{{ movie.title }}</p>
        <p>{{ movie.overview }}</p>
        <div>
          <button>찜</button>
          <button>like</button>
          <button>dislike</button>
        </div>
      </div>
    </div>
    <div class="article-list">
      <h1>Articles</h1>
      <article-list></article-list>
    </div>
    <div class="related-movies">
      <h1>related movies</h1>
      <p>관련 영화를 구분할 기준이 없음...</p>
    </div>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  components: { ArticleList },
  name: 'MovieDetailView',
  data() {
    return {
      moviePk: this.$route.params.movieId,
    }
  },
  computed: {
    ...mapGetters(['movie']),
    poster() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_url
    },
  },
  methods: {
    ...mapActions([
      'fetchMovie', 'movieArticles'
    ])
  },
  created() {
    this.fetchMovie(this.moviePk)
    this.movieArticles(this.moviePk)
  },
}
</script>

<style>

</style>