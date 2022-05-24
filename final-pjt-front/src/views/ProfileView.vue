<template>
  <div>
    <h1>profile</h1>
    <p>{{ profile.username }}</p>
    {{profile.picture}}
    <!-- <img :src="" 
    alt="profileImg"
    > -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name:'ProfileView',
  computed:{
    ...mapGetters(['profile'])
    // profile(){
    //   // return
    // }
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created(){
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  }
}
</script>

<style>

</style>