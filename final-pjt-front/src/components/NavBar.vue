<template>
  <div class="nav-bar fixed-top">
    <b-navbar type="white"
      class="d-flex justify-content-between my-1"
    > 
  
      <b-navbar-nav style="font-family: 'Segoe UI';">
        <router-link to="/movies">eutCha</router-link> 
        <router-link :to="{name: 'community', params: { page } }" v-if="isLoggedIn">community</router-link>
      </b-navbar-nav>
      <b-navbar-nav  class="welcome">
        <a>welcome, eutCha</a>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <router-link to="/movies">Home</router-link> 
        <router-link to="/login" v-if="!isLoggedIn">Login</router-link> 
        <router-link to="/logout" v-if="isLoggedIn">Logout  </router-link> 
        <router-link to="/articles/new" v-if="isLoggedIn">NEW</router-link> 
        <router-link :to="{ name: 'profile', params: { username } }">profile</router-link>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'NavBar',
  data(){
    return {
      page: 1,
    }
  },
  computed:{
    ...mapGetters(['isLoggedIn', 'currentUser',]),
    username(){
      return this.currentUser.username
    },

  }
}
</script>

<style>
  .nav-bar {
    background-color: rgba(255, 255, 255, 0.8);
    background-color: purple;
    background-color: rgb(93, 26, 161);
    background-color: rgba(19, 127, 177);
  }

  .welcome {
    position: fixed;
    font-size: 20px;
    left: 50%;
    transform: translate(-50%);
    text-shadow: 2px 2px 0px #1565C0, 3px 3px 0px #42A5F5, 2px 2px 0px #E3F2FD;

    }
</style>