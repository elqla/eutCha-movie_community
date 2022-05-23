<template>
  <div class="nav-bar fixed-top">
    <b-navbar type="white"
      class="d-flex justify-content-between"
    >
      <b-navbar-brand href="#">eutCha</b-navbar-brand>
      <b-navbar-nav>
        <a>welcome, eutCha</a>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <router-link to="/">Home</router-link> | 
        <router-link to="/login">Login</router-link> | 
        <a>my Profile</a>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
}
</script>

<style>
  .nav-bar {
    background-color: rgba(255, 255, 255, 0.8);
  }
</style>