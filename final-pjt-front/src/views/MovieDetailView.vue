<template>
  <div class="container" style="margin-top: 100px;">
    <div class="movie-detail d-flex row">
      <div class="movie-detail-poster col-12 col-md-5">
        <img :src="poster" alt="" class="movie-detail-img">
      </div>
      <div class="col-12 col-md-7">
        <h2>{{ movie.title }}</h2>
        <div class="movie-detail-overview">{{ movie.overview }}</div>
        <div class="movie-detail-credits">출연 배우: {{ movie.credits }}</div>
        <div class="movie-detail-button">
          <b-button :class="{ 'active': isLike }" @click="likeMovie(moviePk)" pill variant="outline-primary">좋아요</b-button>
          <b-button :class="{ 'active': isDislike }" @click="dislikeMovie(moviePk)" pill variant="outline-danger">싫어요</b-button>
        </div>
      </div>
    </div>
    <article-list class="movie-article-list"></article-list>
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
    ...mapGetters(['movie', 'currentUser']),
    poster() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_url
    },
    isLike() {
      let liked = false
      for(const user of this.movie.like_users) {
        if(user.pk === this.currentUser.pk) {
          liked = true
          break
        }
      }
      return liked
    },
    isDislike() {
      let hate = false
      for(const user of this.movie.dislike_users) {
        if(user.pk === this.currentUser.pk) {
          hate = true
          break
        }
      }
      return hate
    }
  },
  methods: {
    ...mapActions([
      'fetchMovie', 'movieArticles', 'likeMovie', 'dislikeMovie'
    ])
  },
  created() {
    this.fetchMovie(this.moviePk)
    this.movieArticles(this.moviePk)
  },
}
</script>

<style>
.movie-detail {
  padding: 2rem;
  border-style: solid;
  border-radius: 3rem;
}
.movie-article-list {
  margin-top: 1rem;
  padding: 1rem;
  border-style: solid;
  border-radius: 3rem;
}
.movie-detail-poster {
  max-height: 600px;
}
.movie-detail-img {
  height: 100%;
  width: 100%;
}
.movie-detail-button > button {
  margin: 6px;;
}
.movie-detail-overview {
  background-color: rgba(125, 125, 125, 0.2);
  margin: 2rem;
  padding: 1rem;
  border-radius: 2rem;
  text-align: left;
}
.movie-detail-overview:first-letter {
  font-size: 40px;
}
.movie-detail-credits {
  background-color: rgba(125, 125, 125, 0.2);
  margin: 2rem;
  padding: 1rem;
  border-radius: 2rem;
  text-align: left;
  font-weight: bold;
}
</style>