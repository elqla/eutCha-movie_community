<template>
<div style="margin-top: 100px;">
  <div>
    <p>{{ profile.nickname || profile.username }}</p>
    <img :src="profile.picture" alt="img">
    <p>LIKE Movie:
    <span v-if="ifNotGenre">
      영화를 좋아요하러 가보세요 !
    </span>
    <span v-for="(value, idx) in likeGenres"
    :key="idx"><span v-for="(value, idx) in value.genres" :key="idx">{{value.genre}}</span></span></p>
  </div>
  <div>
    <profile-article-list></profile-article-list>
  </div>
</div>
</template>

<script>
import ProfileArticleList from '@/components/ProfileArticleList.vue'
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'

export default {
  name:'ProfileView',
  components:{ ProfileArticleList },
  computed:{
    ...mapGetters(['profile',]),       
    likeGenres(){
      return this.profile.like_movies
    },
    ifNotGenre(){
      if(_.isEmpty(this.likeGenres)){
        return true
      }
      else{
        return false
      }
    }
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