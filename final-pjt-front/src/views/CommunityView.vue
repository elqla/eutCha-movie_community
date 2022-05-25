<template>
  <div class="community">
    <h1 class="commu-nav">eutcha-community</h1>
      <div class="ta">
        <b-table stripe hover :items="coArticles" :per-page="perPage" :current-page="currentPage">
        </b-table>
      </div>
      <div>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
        class="ta-nav"
        align="center"
      ></b-pagination>
      </div>
  </div>
</template>

<script>
import Vue from 'vue'
import vueMoment from 'vue-moment'
Vue.use(vueMoment)

import { mapActions, mapGetters } from 'vuex'
export default {
  name:'CommunityView',
  // 처음 로드될때, 1페이지 뜨도록
  components:{
    // CommunityItem,
  },
  methods:{
    ...mapActions(['communityArticles',]),
  },
  computed:{
    ...mapGetters(['coArticles',]),
      rows() {
        return this.coArticles.length
      }
  },
  data(){
    return {
      page: 1,//this.$route.params.page,
      perPage: 5,
      currentPage: 1,
      articles: this.coArticles,
    }
  },
  created(){
    this.communityArticles(this.page)
  }


}
</script>

<style>
.community{
  max-width: 1000px;
  margin-top: 100px;
  color: rgb(19, 127, 177);
  color:chocolate;
  font-weight: bold;
  display: flex;
  flex-direction:column;
  margin: 100px auto;
}
.commu-nav{
  /* background-color: white; */
  text-align: left;
  margin-left: 20px;
  margin-bottom: 10px;
  font-weight: bolder;
  font-family: serif;
  font-family: sans-serif;
}
.ta{
  background-color: white;
}
.ta-nav{
  margin: 10px;
  /* background-color: rgba(255, 255, 255, 0.871); */
}
</style>