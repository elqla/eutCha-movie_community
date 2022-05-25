<template>
<div class="profile">

    <div class="d-flex">
    <img :src="profile.picture" alt="img" class="proflieImg">
    <span class="profileName">{{ profile.nickname || profile.username }}</span>
    </div>

    <p>LIKE MOVIE:
    <span v-if="ifNotGenre">
      영화를 좋아요하러 가보세요 !
    </span>
    <span v-for="(value, idx) in likeGenres"
    :key="idx"><span v-for="(value, idx) in value.genres" :key="idx">{{value.genre}}</span></span></p>

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

<style scope>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Roboto:ital,wght@0,300;1,300&display=swap');
/* @import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Roboto:ital,wght@0,300;1,300&family=Sunflower&display=swap');
  font-family: 'Sunflower', sans-serif; */

.profile{
  display: flex;
  flex-flow: column nowrap;
  margin: auto;
  margin-top: 100px;
  max-width: 1000px;
  font-family: 'Do Hyeon', sans-serif;
  background-color: rgb(138, 138, 138);
}
.proflieImg{
  width: 150px;
  height: 150px; 
  border-radius: 50%;
  margin-right: 70%;
  margin-top: 20px;
}
.profileName{
  font-size: 2rem;
  display: ;

}

</style>