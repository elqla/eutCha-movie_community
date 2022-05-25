<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style>
:root{
  background:black;
}
#app {
  background-color: black;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #F8F9FA;

}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: white;
  margin-right: 5px;
  text-decoration: none;

}

nav a.router-link-exact-active {
  color: white;
  text-decoration: none;
}
</style>
