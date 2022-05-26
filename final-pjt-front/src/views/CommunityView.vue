<template>
  <div class="community">
    <h1 class="commu-nav">eutcha-community</h1>
      <div class="ta">
        <b-table stripe hover :items="coArticles" :per-page="perPage" :current-page="currentPage" 
        :select-mode="selectMode"
        responsive="sm"
        ref="selectableTable"
        selectable
        @row-selected="onRowSelected">
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
import router from '@/router'

import { mapActions, mapGetters } from 'vuex'
export default {
  name:'CommunityView',
  data(){
    return {
      page: 1,
      perPage: 8,
      currentPage: 1,
      articles: this.coArticles,

      selectMode: 'multi',
      selected: [],
    }
  },
  methods:{
    ...mapActions(['communityArticles',]), 
    onRowSelected(items) {
      this.selected = items[0]['글 번호']
      router.push({name: 'article', params: {articlePk : this.selected}})
    },
  },
  computed:{
    ...mapGetters(['coArticles',]),
      rows() {
        return this.coArticles.length
      }
  },
  created(){
    this.communityArticles(this.page)
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Roboto:ital,wght@0,300;1,300&display=swap');

.community{
  max-width: 1000px;
  margin-top: 100px;
  color: rgb(19, 127, 177);
  color:rgb(197, 197, 197); 
  /* font-weight: bold; */
  display: flex;
  flex-direction:column;
  margin: 100px auto;
  font-family: 'Do Hyeon', sans-serif;

}
.commu-nav{
  text-align: left;
  margin-left: 20px;
  margin-bottom: 10px;
  /* font-weight: bolder; */
  color:rgb(192, 0, 144);
  font-family: 'Do Hyeon', sans-serif;
}
.ta{
  background-color: white;
}
.ta-nav{
  padding-top:30px;
  margin: 10px;
}
</style>