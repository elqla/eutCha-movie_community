import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    articles: [],
    article: {},
  },
  getters: {
    articles: state => state.articles,
    article: state => state.article,
  },
  mutations: {
    ARTICLES: (state, articles) => state.articles = articles,
    ARTICLE: (state, article) => state.article = article,
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
    newArticle ({ commit, getters }, credentials, moviePk){ 
      axios({
        url: drf.articles.newArticles(moviePk),
        method: 'post',
        headers: getters.authHeader,
        data: credentials,
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
  },
}