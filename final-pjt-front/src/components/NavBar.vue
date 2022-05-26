<template>
  <div class="nav-bar fixed-top">
    <b-navbar type="white"
      class="d-flex justify-content-between my-1"
    > 
  
      <b-navbar-nav style="font-family: 'Segoe UI';">
        <router-link to="/movies" class="logo">eutCha</router-link> 
        <router-link :to="{name: 'community', params: { page } }" v-if="isLoggedIn" class="navbar-community">community</router-link>
      </b-navbar-nav>
      <b-navbar-nav  class="welcome">
        <a>welcome, eutCha</a>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-dropdown id="dropdown" :text="greetingText" variant="outline-light">
          <b-dropdown-item><router-link :to="{ name: 'profile', params: { username } }">Profile</router-link></b-dropdown-item>
          <b-dropdown-item v-if="!isLoggedIn"><router-link to="/login">Login</router-link></b-dropdown-item>
          <b-dropdown-item v-if="isLoggedIn"><router-link to="/logout">Logout</router-link> </b-dropdown-item>
          <b-dropdown-divider v-if="isStaff"></b-dropdown-divider>
          <b-dropdown-item v-if="isStaff"><router-link to="/admin">Admin Page</router-link> </b-dropdown-item>
        </b-dropdown>
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
    greetingText() {
      return this.username + '님 안녕하세요!'
    },
    isStaff() {
      if (this.currentUser.username === 'admin') return true
      return false
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Roboto:ital,wght@0,300;1,300&display=swap');

.nav-bar {
  background-color: rgba(19, 127, 177);
}

.logo {
  position: fixed;
  font-size: 30px;
  top: 8px;
  text-shadow: 2px 2px 0px #1565C0, 3px 3px 0px #42A5F5, 2px 2px 0px #E3F2FD;
}

.welcome {
  position: fixed;
  font-size: 20px;
  left: 50%;
  transform: translate(-50%);
  text-shadow: 2px 2px 0px #1565C0, 3px 3px 0px #42A5F5, 2px 2px 0px #E3F2FD;
}

.navbar-community {
  margin-left: 120px;
}

.dropdown-menu {
  position: absolute;
  top: 45px;
  background-color: rgba(19, 127, 177) !important;
}
#dropdown{
  /* font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; */
  font-family: 'Do Hyeon', sans-serif;
}
</style>