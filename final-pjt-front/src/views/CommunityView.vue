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
      perPage: 5,
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
.community{
  max-width: 1000px;
  margin-top: 100px;
  color: rgb(19, 127, 177);
  color:rgb(197, 197, 197); 
  font-weight: bold;
  display: flex;
  flex-direction:column;
  margin: 100px auto;
}
.commu-nav{
  text-align: left;
  margin-left: 20px;
  margin-bottom: 10px;
  font-weight: bolder;
  font-family: 'Segoe UI';
  text-shadow: 1px 1px 0px #1565C0, 2px 2px 0px #42A5F5, 1px 3px 0px #E3F2FD;
}
.ta{
  background-color: white;
}
.ta-nav{
  margin: 10px;
}
</style>