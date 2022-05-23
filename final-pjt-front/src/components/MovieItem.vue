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
      Some quick example text to build on the card title and make up the bulk of the card's content.
    </b-card-text>

    <b-button href="#" variant="primary">Go somewhere</b-button>
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
    }
  }
}
</script>

<style>

</style>