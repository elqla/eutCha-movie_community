<template>
  <div>
    <h1>ProfileItem</h1>
    <!-- {{movie_id}}
    {{watchMovie}} -->

    <div class="movie-detail d-flex">
      <img :src="poster" alt="img" style="width:100px">
      <div>
        <p>{{ watchMovie.title }}</p>
        <p>{{ watchMovie.id}}</p>
        <div>
          <button>찜</button>
          <button>like</button>
          <button>dislike</button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>


import { mapGetters } from 'vuex'
// MOVIE ID 가 하나씩 넘어옴
export default {
  name:'ProfileItem',
  props:{
    movie_id: Number,
  },
  computed:{
    ...mapGetters(['watchMovie']),
    poster() {
      return 'https://image.tmdb.org/t/p/w500' + this.watchMovie.poster_url
    },
  },
  created(){
    this.$store.dispatch('profileMovie', this.movie_id)
  }
}
</script>

<style>

</style>