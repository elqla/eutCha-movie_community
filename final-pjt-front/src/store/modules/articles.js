import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

import Vue from 'vue'
import vueMoment from 'vue-moment'
Vue.use(vueMoment)

export default {
  state: {
    articles: [],
    article: {},
    coArticles:[],
  },
  getters: {
    articles: state => state.articles,
    article: state => state.article,
    coArticles: state => state.coArticles,
  },
  mutations: {
    ARTICLES: (state, articles) => state.articles = articles,
    ARTICLE: (state, article) => state.article = article,
    COMMUNITY_ARTICLES:(state, articles) => state.coArticles = articles,
  },
  actions: {
    fetchArticle ({ commit, getters }, articlePk) {
      axios({
        url: drf.articles.article(articlePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('ARTICLE', res.data)
        })
        .catch(err => {
          console.error(err)
        })
    },
    allArticles ({ commit, getters }) {
      axios({
        url: drf.articles.articles(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('ARTICLES', res.data)
        })
        .catch(err => {
          console.error(err)
        })
    },
    movieArticles ({ commit, getters }, moviePk) {
      axios({
        url: drf.articles.movieArticles(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('ARTICLES', res.data)
        })
        .catch(() => {
          commit('ARTICLES', null)
        })
    },
    newArticle ({ commit, getters }, { article, moviePk }){ 
      axios({
        url: drf.articles.newArticles(moviePk),
        method: 'post',
        headers: getters.authHeader,
        data: article,
      })
        .then(res => {
          commit('ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    communityArticles({getters, commit}, page ){
      const tmp = []
      axios({
        url: drf.articles.community(page),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res=>{
        res.data.forEach((article)=>{
          tmp.push({
            '글 번호': article.pk,
            '영화 제목':article.movie.title,
            '게시글 제목':article.title,
            '댓글':article.comment_count,
            '작성일': Vue.moment(article.created_at).calendar(),
            '작성자': article.user.nickname||article.user.username
          })
        })
        commit('COMMUNITY_ARTICLES', tmp)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
    editArticle ({ commit, getters }, { article, articlePk }){ 
      axios({
        url: drf.articles.article(articlePk),
        method: 'put',
        headers: getters.authHeader,
        data: article,
      })
        .then(res => {
          commit('ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    deleteArticle ({ getters }, articlePk) {
      axios({
        url: drf.articles.article(articlePk),
        method: 'delete',
        headers: getters.authHeader,
      })
        .then(() => {
          alert('글이 정상적으로 삭제되었습니다.')
          router.go(-1)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    newComment ({ getters, dispatch }, { content, articlePk }) {
      const comment = { content: content }
      axios({
        url: drf.articles.comments(articlePk),
        method: 'post',
        headers: getters.authHeader,
        data: comment
      })
        .then(() => {
          dispatch('fetchArticle', articlePk)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
  },
}