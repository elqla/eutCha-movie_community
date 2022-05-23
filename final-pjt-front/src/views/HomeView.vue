<template>
  <div class="home">
    <router-link to="/login" class="gate">
      <img src="../assets/title.png" alt="Home title">
    </router-link>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'HomeView',
}
</script>

<style>
  /* body {
    background: #000;
  } */

  .gate {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }
</style>