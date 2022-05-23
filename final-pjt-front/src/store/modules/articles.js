// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    articles: [],
  },
  getters: {
    articles: state => state.articles,
  },
  mutations: {
    ARTICLES: (state, articles) => state.articles = articles,
  },
  actions: {
    fetchArticles ({ commit, getters }) {
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
    }
  },
}