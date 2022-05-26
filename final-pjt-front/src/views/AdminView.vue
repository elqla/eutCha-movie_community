<template>
  <div style="margin-top: 100px;">
    <h1>adminView</h1>
    <router-link to="/admin/new">
      <b-button class="mb-3" pill variant="success">영화 추가하기</b-button>
    </router-link>

    <div class="container">
      <div class="row">
        <div v-for="movie in movies" :key="movie.id" class="col-3">
          <b-card class="adminMovie" :img-src="'https://image.tmdb.org/t/p/w500'+movie.poster_url" alt="img" img-top>
            <router-link :to="{ name: 'adminEditView', params: { movieId: movie.id } }">
              <b-card-text>
                <p>{{ movie.title }}</p>
              </b-card-text>
            </router-link>
              <b-button @click="deleteMovie(movie.id)" pill variant="outline-danger">삭제</b-button>
          </b-card>
        </div>
      </div>
    </div>


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
    ...mapActions(['fetchAdmin', 'deleteMovie'])
  },
  created() {
    this.fetchAdmin()
  }
}
</script>

<style>
.adminMovie{
  width: 250px;
  margin: 20px;
}
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