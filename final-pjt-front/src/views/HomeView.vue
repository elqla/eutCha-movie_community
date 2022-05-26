<template>
  <div class="home">
    <router-link to="/login" class="gate mast animate" id="mast">
      <header class="mast__header">
        <span class="mast__icon">📽</span>
        <h1 class="mast__title js-letters text-animate" style="font-family: 'Gowun Dodum', sans-serif;"></h1>
      </header>
      <!-- <img src="../assets/title.png" alt="Home title"> -->
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      gateLetters: '나는 네가.. 어제 본 영화를 알고있다!!!!'
    }
  },
  methods: {
    animation () {
      const letters = document.querySelector('.js-letters')
      for (let letter of this.gateLetters) 
        letters.innerHTML += `<span>${letter}</span>`
    }
  },
  mounted () {
    this.animation()
  }
}
</script>

<style>
.gate {
  text-decoration: none;
  
}
.gate:hover {
  color: #fe6513;
}

.mast {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: grey;
}

.mast:hover {
  color: grey;
}
.mast__header {
  padding: 1em;
}
.mast__title {
  margin: 0.15em auto;
  padding: 0 1em;
  font-family: Shrikhand, georgia;
  font-size: calc(100% + 3.85vw);
  color: white;
  text-shadow: 1px 1px 0px rgba(255, 255, 255, 0.5);
}
.mast__text {
  font-size: 1em;
  font-family: "Fredoka One", arial;
  text-shadow: 1px 1px 0px rgba(255, 255, 255, 0.4);
}
@media (min-width: 54em) {
  .mast__text {
    font-size: calc(100% + 0.5vw);
  }
}
.mast__icon {
  display: block;
  font-size: 2.5em;
  filter: hue-rotate(414deg) brightness(1.15) saturate(1.4);
  text-shadow: 1px 1px 0px rgba(255, 255, 255, 0.6);
}
@media (min-width: 54em) {
  .mast__icon {
    font-size: calc(100% + 3.25vw);
  }
}

.animate .mast__title {
  overflow-y: hidden;
}
.animate .mast__title > * {
  display: inline-block;
  min-width: 0.1em;
  -webkit-backface-visibility: hidden;
          backface-visibility: hidden;
  -webkit-animation: slide-up 0.6s cubic-bezier(0.19, 0.9, 0.9, 1) both;
          animation: slide-up 0.6s cubic-bezier(0.19, 0.9, 0.9, 1) both;
}
.animate .mast__title > *:nth-child(1) {
  -webkit-animation-delay: 0.1s;
          animation-delay: 0.1s;
}
.animate .mast__title > *:nth-child(2) {
  -webkit-animation-delay: 0.2s;
          animation-delay: 0.2s;
}
.animate .mast__title > *:nth-child(3) {
  -webkit-animation-delay: 0.3s;
          animation-delay: 0.3s;
}
.animate .mast__title > *:nth-child(4) {
  -webkit-animation-delay: 0.4s;
          animation-delay: 0.4s;
}
.animate .mast__title > *:nth-child(5) {
  -webkit-animation-delay: 0.5s;
          animation-delay: 0.5s;
}
.animate .mast__title > *:nth-child(6) {
  -webkit-animation-delay: 0.6s;
          animation-delay: 0.6s;
}
.animate .mast__title > *:nth-child(7) {
  -webkit-animation-delay: 0.7s;
          animation-delay: 0.7s;
}
.animate .mast__title > *:nth-child(8) {
  -webkit-animation-delay: 0.8s;
          animation-delay: 0.8s;
}
.animate .mast__title > *:nth-child(9) {
  -webkit-animation-delay: 0.9s;
          animation-delay: 0.9s;
}
.animate .mast__title > *:nth-child(10) {
  -webkit-animation-delay: 1s;
          animation-delay: 1s;
}
.animate .mast__title > *:nth-child(11) {
  -webkit-animation-delay: 1.1s;
          animation-delay: 1.1s;
}
.animate .mast__title > *:nth-child(12) {
  -webkit-animation-delay: 1.2s;
          animation-delay: 1.2s;
}
.animate .mast__title > *:nth-child(13) {
  -webkit-animation-delay: 1.3s;
          animation-delay: 1.3s;
}
.animate .mast__title > *:nth-child(14) {
  -webkit-animation-delay: 1.4s;
          animation-delay: 1.4s;
}
.animate .mast__title > *:nth-child(15) {
  -webkit-animation-delay: 1.5s;
          animation-delay: 1.5s;
}
.animate .mast__title > *:nth-child(16) {
  -webkit-animation-delay: 1.6s;
          animation-delay: 1.6s;
}
.animate .mast__title > *:nth-child(17) {
  -webkit-animation-delay: 1.7s;
          animation-delay: 1.7s;
}
.animate .mast__title > *:nth-child(18) {
  -webkit-animation-delay: 1.8s;
          animation-delay: 1.8s;
}
.animate .mast__title > *:nth-child(19) {
  -webkit-animation-delay: 1.9s;
          animation-delay: 1.9s;
}
.animate .mast__title > *:nth-child(20) {
  -webkit-animation-delay: 2s;
          animation-delay: 2s;
}
.animate .mast__title > *:nth-child(21) {
  -webkit-animation-delay: 2.1s;
          animation-delay: 2.1s;
}
.animate .mast__title > *:nth-child(22) {
  -webkit-animation-delay: 2.2s;
          animation-delay: 2.2s;
}
.animate .mast__title > *:nth-child(23) {
  -webkit-animation-delay: 2.3s;
          animation-delay: 2.3s;
}
.animate .mast__title > *:nth-child(24) {
  -webkit-animation-delay: 2.4s;
          animation-delay: 2.4s;
}
.animate .mast__title > *:nth-child(25) {
  -webkit-animation-delay: 2.5s;
          animation-delay: 2.5s;
}
.animate .mast__text > * {
  display: inline-block;
  min-width: 0.25em;
  -webkit-animation: slide-right 0.6s cubic-bezier(0.19, 0.9, 0.9, 1) both;
          animation: slide-right 0.6s cubic-bezier(0.19, 0.9, 0.9, 1) both;
}
.animate .mast__icon {
  -webkit-animation: shake-it 1.5s cubic-bezier(0.19, 0.9, 0.9, 1) both;
          animation: shake-it 1.5s cubic-bezier(0.19, 0.9, 0.9, 1) both;
}

@-webkit-keyframes slide-up {
  0% {
    opacity: 0;
    transform: translate3d(0, 100%, 0);
  }
  80% {
    opacity: 1;
  }
  100% {
    transform: translate3d(0, 0, 0);
  }
}

@keyframes slide-up {
  0% {
    opacity: 0;
    transform: translate3d(0, 100%, 0);
  }
  80% {
    opacity: 1;
  }
  100% {
    transform: translate3d(0, 0, 0);
  }
}
@-webkit-keyframes slide-right {
  0% {
    opacity: 0;
    transform: translate3d(-2em, 0, 0);
  }
  100% {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}
@keyframes slide-right {
  0% {
    opacity: 0;
    transform: translate3d(-2em, 0, 0);
  }
  100% {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}
@-webkit-keyframes shake-it {
  0%, 100% {
    transform: rotate(0deg);
  }
  10%, 20%, 30%, 40%, 50% {
    transform: rotate(-6deg);
  }
  15%, 25%, 35%, 45%, 55% {
    transform: rotate(6deg);
  }
  60%, 70%, 80%, 90% {
    transform: rotate(-3deg);
  }
  65%, 75%, 85%, 95% {
    transform: rotate(3deg);
  }
}
@keyframes shake-it {
  0%, 100% {
    transform: rotate(0deg);
  }
  10%, 20%, 30%, 40%, 50% {
    transform: rotate(-6deg);
  }
  15%, 25%, 35%, 45%, 55% {
    transform: rotate(6deg);
  }
  60%, 70%, 80%, 90% {
    transform: rotate(-3deg);
  }
  65%, 75%, 85%, 95% {
    transform: rotate(3deg);
  }
}
</style>