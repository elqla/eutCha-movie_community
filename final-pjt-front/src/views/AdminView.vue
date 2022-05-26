<template>
  <div style="margin-top: 100px;">
    <h1>adminView</h1>
    <router-link to="/admin/new">
      <b-button class="mb-3" pill variant="success">영화 추가하기</b-button>
    </router-link>
    <ul v-for="movie in movies" :key="movie.id">
      <router-link :to="{ name: 'adminEditView', params: { movieId: movie.id } }">
        <li class="">{{ movie.title }}</li>
      </router-link>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'AdminView',
  computed: {
    ...mapGetters(['movies'])
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

</style>