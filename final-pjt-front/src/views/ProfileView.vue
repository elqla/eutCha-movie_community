<template>
<div>
  <div>
    <h1>profile</h1>
    <p>{{ profile.nickname }}</p>
    <img :src="profile.picture" alt="img">
    <p>좋아하는 장르:
    <span v-for="(value, idx) in likeGenres"
    :key="idx"><span v-for="(value, idx) in value.genres" :key="idx">{{value.genre}}</span></span></p>
  </div>
  <!-- v-if 최근 본 영화가 있을때, -->
  <div>
    <profile-article-list></profile-article-list>
  </div>
</div>
</template>

<script>
import ProfileArticleList from '@/components/ProfileArticleList.vue'

import { mapGetters, mapActions } from 'vuex'
//새로고침하면 404 뜸
//profile뜨는것도 data가 created보다 먼저 로드되서?



export default {
  name:'ProfileView',
  components:{ ProfileArticleList },
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