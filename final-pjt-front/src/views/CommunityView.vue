<template>
  <div class="community">
    <h1>community입니다.</h1>
      <div>
        <b-table stripe hover :items="coArticles">
        </b-table>
      </div>
  </div>
        <!-- <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
        ></b-pagination> -->
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
    ...mapGetters(['coArticles',])
  },
  data(){
    return {
      page: 1,//this.$route.params.page,
      perPage: 40,
      // currentPage: this.page,
      articles: this.coArticles,
    }
  },
  created(){
    // console.log(this.coArticles)
    this.communityArticles(this.page)
    // this.communityArticles(this.page)
    // const payload = { page: 1 } //this.$route.params.page
    // this.communityArticles(payload)
  }


}
</script>

<style>
.community{
  max-width: 1000px;
}
.article-nav{
  display: flex;
  justify-content: space-between;
}
.article-item{
  margin: 0px 20px;
}
</style>