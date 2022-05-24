<template>
  <div>
    <h1>profile</h1>
    <p>{{ profile.nickname }}</p>
    <!-- <img :src="profileImg" alt="img"> -->
    <img :src="profile.picture" alt="img">
    <p>즐겨보는 장르: {{profile}}</p>
  </div>

</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name:'ProfileView',
  data(){
    return{
    }
  },
  computed:{
    ...mapGetters(['profile']),   
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