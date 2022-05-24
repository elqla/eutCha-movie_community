<template>
  <div>
    <h1>profile</h1>
    <p>{{ profile.nickname }}</p>
    <!-- <img :src="profileImg" alt="img"> -->
    <img :src="profile.picture" alt="img">
    <p>좋아하는 장르:
    <span v-for="(value, idx) in likeGenres"
    :key="idx">{{value.genre}}</span></p>

    <p>좋아하는 장르:
    <span v-for="(value, idx) in likeGenres"
    :key="idx">{{value.genres}}</span></p>

  </div>

</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name:'ProfileView',
  computed:{
    ...mapGetters(['profile',]),       
    likeGenres(){
      return this.profile.like_movies
  },
  },
  methods: {
    ...mapActions(['fetchProfile',]),
  },
  created(){
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  }
}
</script>

<style>

</style>