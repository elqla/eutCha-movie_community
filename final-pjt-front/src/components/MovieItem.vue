<template>
  <div class="d-flex justify-content-center col-sm-12 col-md-6 col-xl-4 col-xxl-3"
    :class="container"
    @mouseover="flipFront"
    @mouseout="flipBack"
  >
    <b-card
      overlay
      :img-src="poster"
      img-alt="Image"
      style="height: 500px; max-width: 20rem; position: absolute;"
      class="mb-2 front"
    ></b-card>
    <router-link :to="{ name: 'movieDetail', params: { movieId } }" class="text-decoration-none">
      <b-card
        style="height: 500px; max-width: 20rem;"
        class="mb-2 back"
        text-variant="black"
      >
        <b-card-title>{{ movie.title }}</b-card-title>
        <b-card-text class="movie-text">
          {{ movie.overview }}
        </b-card-text>
        <b-card-text class="movie-text">
          출연: {{ movie.credits }}
        </b-card-text>
  
        <div class="movie-genre">장르: 
        <span v-for="(value, idx) in movie.genres" :key="idx" class="movie-genre">
          <span v-if="idx!=0">, </span>{{ value.genre }}</span></div>
      </b-card>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie: Object,
    category: String,
  },
  computed: {
    poster() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_url
    },
    movieId() {
      return this.movie.id
    },
    container() {
      return 'flip-container' + this.category + this.movieId
    }
  },
  methods: {
    flipFront() {
      const card = document.querySelector(`.flip-container${this.category}${this.movieId}`)
      card.classList.add('cardRotate')
      card.classList.remove('backRotate')
    },
    flipBack() {
      const card = document.querySelector(`.flip-container${this.category}${this.movieId}`)
      card.classList.add('backRotate')
      card.classList.remove('cardRotate')
    }
  }
}
</script>

<style>
.front{
  overflow: hidden;
  width: 20rem;
}
.front img{
  position: absolute;
  left: 0;
  height: 500px;
}
.back{
  background-color: rgb(46, 46, 46) !important;
  transform: rotateY(90deg);
  font-family: 'Gowun Dodum', sans-serif;
}
.cardRotate .front{
  opacity: 1;
  animation: rotateAni 0.5s 1;
  transform: rotateY(90deg);
}
.cardRotate .back{
  opacity: 1;
  animation: rotateAni2 0.5s 0.5s 1 backwards;
  transform:rotateY(0);
}
.backRotate .front{
  animation: backAni 0.5s   1; 
  opacity: 1;
}
.backRotate .back{
  opacity: 0;
}

@keyframes rotateAni{
  0%{transform:rotateY(0);}
  100%{transform:rotateY(90deg);}
}
@keyframes rotateAni2{
  0%{transform:rotateY(-90deg);}
  100%{transform:rotateY(0deg);}
}

@keyframes backAni{
  0%{transform:rotateY(90deg);}
  100%{transform:rotateY(0deg);}
}

.card-title {
  font-size: 30px;
  padding: 1rem;
  color: rgb(255, 245, 225);
  word-break: keep-all;
  }

.movie-text{
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 10;
  overflow: hidden;
  color: rgb(255, 245, 225);
  text-align: start;
}

.movie-genre {
  color: rgb(255, 245, 225);
}
</style>