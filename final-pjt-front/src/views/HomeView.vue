<template>
  <div class="home">
    <router-link to="/login" class="gate">
      <img src="../assets/title.png" alt="Home title">
      <p>안녕하세요</p>
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
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&family=Noto+Sans+KR&display=swap');

  .gate {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: black;
    min-height: 100vh;
  }

  p {
    font-family: 'Nanum Myeongjo', serif;
  }
</style>