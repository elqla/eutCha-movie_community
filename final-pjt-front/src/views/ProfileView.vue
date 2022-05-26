<template>
<div class="profile rounded">
    <div>
      <img :src="profile.picture" alt="img" class="proflieImg">
      <p class="profileName">{{ profile.nickname || profile.username }}</p>
      <p class="Genre">
        <span v-if="ifNotGenre">LIKE GENRE:
          <router-link to="/movies" class="notlikemovie" >아직 좋아하는 영화가 없어요 ! 🖱️</router-link>
        </span>
        <span v-if="!ifNotGenre">LIKE GENRE:
          {{ifGenres}}
        </span>
      </p>
    </div>


    <div class="articleList">
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
    },
    ifGenres(){
      const arr = []
      this.likeGenres.forEach((value)=>{
        value.genres.forEach((value)=>{
          arr.push(value.genre)
        })
      })
      return [...new Set(arr)].join(" ")
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

.profile{
  display: flex;
  flex-flow: column nowrap;
  margin: auto;
  margin-top: 100px;
  max-width: 1000px;
  font-family: 'Do Hyeon', sans-serif;
  background-color: rgba(138, 138, 138, 0.288);
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
  margin-right:40%;
  margin-top: -80px;
}
.Genre{
  margin-left:-110px;
}
.notlikemovie{
  text-decoration: none;
  color: #bb0083;

}
.articleList{
  margin-top:50px;
  max-width: 900px;
  margin-left: 30px;
  margin-right: 30px;
}

</style>