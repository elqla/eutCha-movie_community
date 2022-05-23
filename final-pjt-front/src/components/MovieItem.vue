<template>
  <div>
    <b-card
    :title="movie.title"
    :img-src="poster"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
      <b-card-text>
        {{ movie.overview }}
      </b-card-text>
      <b-card-text>
        ID : {{ movie.id }}
      </b-card-text>
      <router-link :to="{ name: 'movieDetail', params: { movieId } }">
        <b-button variant="primary">Go somewhere</b-button>
      </router-link>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie: Object,
  },
  computed: {
    poster() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_url
    },
    movieId() {
      return this.movie.id
    }
  }
}
</script>

<style>

</style>