<template>
  <div class="nav-bar fixed-top">
    <b-navbar type="white"
      class="d-flex justify-content-between"
    >
      <router-link to="/movies">
      <b-navbar-brand>eutCha</b-navbar-brand>
      </router-link>
      <b-navbar-nav class="welcome">
        <a>welcome, eutCha</a>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <router-link to="/movies">Home</router-link> | 
        <router-link to="/login" v-if="!isLoggedIn">Login</router-link> | 
        <router-link to="/logout" v-if="isLoggedIn">Logout</router-link> | 
        <router-link to="/articles/new" v-if="isLoggedIn">NEW</router-link> | 
        <router-link :to="{ name: 'profile', params: { username } }">profile</router-link>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'NavBar',
  computed:{
    ...mapGetters(['isLoggedIn', 'currentUser']),
    username(){
      return this.currentUser.username
    }
  }
}
</script>

<style>
  .nav-bar {
    background-color: rgba(255, 255, 255, 0.8);
  }

  .welcome {
    position: fixed;
    left: 50%;
    transform: translate(-50%)
  }
</style>