<template>
  <div>
    <b-list-group-item class="article-box d-flex">
      <div>
      <span class="article-pk">{{article.pk}}</span>
      <span class="article-movie">{{article.movie.title}}</span>
      <span class="article-title">{{article.title}}</span>
      <span>댓글: {{article.comment_count}}</span>
      </div>
      <div>
      <span class="article-date">{{$moment(article.created_at).calendar()}}</span>
      <span class="article-nickname">{{article.user.nickname || article.user.username}}</span>
      </div>
    </b-list-group-item>
      <!-- <router-link :to="{ name: 'articleEdit', params: { articlePk } }"> -->


  </div>
</template>

<script>
import Vue from 'vue'
import vueMoment from 'vue-moment'
Vue.use(vueMoment)

export default {
  name: 'CommunityItem',
  props:{
    article:Object,
  }
}
</script>

<style>
.article-box{
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
}
.article-pk .article-movie{
  padding-left: 15px;
}
.article-title{
  padding: 14px 10px;
}
.article-nickname{
  padding-left: 20px;
}
.article-date{
  margin-right:20px;

}
/* .article-item{
  margin: 0px 10px;
} */
</style>