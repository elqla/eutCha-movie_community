<template>
  <div class="flip-container">
    <b-card
    overlay
    :img-src="poster"
    img-alt="Image"
    style="max-width: 20rem;"
    class="mb-2 front"
  ></b-card>

  <b-card
    overlay
    :img-src="poster"
    img-alt="Image"
    style="max-width: 20rem; opacity:90%;"
    class="mb-2 back"

    text-variant="black"
    :title="movie.title"
    :sub-title="movie.overview"
  >
      <!-- <b-card-text>
        {{ movie.overview }}
      </b-card-text> -->
      <b-card-text>
        출연: {{ movie.credits }}
      </b-card-text>

      장르:
      <span v-for="(value, idx) in movie.genres" :key="idx">
        {{ value.genre }}, </span>

      <b-card-text>
        ID : {{ movie.id }}
      </b-card-text>
      <router-link :to="{ name: 'movieDetail', params: { movieId } }">
        <b-button variant="primary">Go somewhere</b-button>
      </router-link>
  </b-card>


    <!-- <b-card
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
        출연: {{ movie.credits }}
      </b-card-text>

      장르:
      <span v-for="(value, idx) in movie.genres" :key="idx">
        {{ value.genre }}, </span>

      <b-card-text>
        ID : {{ movie.id }}
      </b-card-text>
      <router-link :to="{ name: 'movieDetail', params: { movieId } }">
        <b-button variant="primary">Go somewhere</b-button>
      </router-link>
    </b-card> -->
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
// /* entire container, keeps perspective */

// /* fliper가 뭔지 모르겠음 */


// .flip-container {
// 	perspective: 1000px;
// }
// 	/* flip the pane when hovered */
// 	.flip-container:hover .flipper, .flip-container.hover .flipper {
// 		transform: rotateY(180deg);
// 	}

// .flip-container, .front, .back {
// 	width: 320px;
// 	height: 480px;
// }

// /* flip speed goes here */
// .flipper {
// 	transition: 0.6s;
// 	transform-style: preserve-3d;

// 	position: relative;
// }

// /* hide back of pane during swap */
// .front, .back {
// 	backface-visibility: hidden;

// 	position: absolute;
// 	top: 0;
// 	left: 0;
// }

// /* front pane, placed above back */
// .front {
// 	z-index: 2;
// 	/* for firefox 31 */
// 	transform: rotateY(0deg);
// }

// /* back, initially hidden pane */
// .back {
// 	transform: rotateY(180deg);
// }
</script>

<style>

</style>