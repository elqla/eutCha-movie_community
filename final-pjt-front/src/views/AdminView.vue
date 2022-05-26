<template>
  <div style="margin-top: 100px;">
    <h1>adminView</h1>
    <router-link to="/admin/new">
      <b-button class="mb-3" pill variant="success">영화 추가하기</b-button>
    </router-link>
    <ul v-for="movie in movies" :key="movie.id" class="d-flex align-items-center list-group">
      <router-link :to="{ name: 'adminEditView', params: { movieId: movie.id } }">
        <li class="list-group-item text-center">
          <div class="img">
            <img :src="'https://image.tmdb.org/t/p/w500'+movie.poster_url" alt="">
          </div>
          <div>{{ movie.title }}</div>
        </li>
      </router-link>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'AdminView',
  computed: {
    ...mapGetters(['movies']),
  },
  methods: {
    ...mapActions(['fetchAdmin'])
  },
  created() {
    this.fetchAdmin()
  }
}
</script>

<style>
.list-group-item {
  margin: 10px;
  max-width: 300px;
  background-color: white;
  border-radius: 1rem !important;
}

.list-group-item > .img {
  max-width: 300px;
}

.list-group-item > .img > img {
  width: 100%;
}
</style>