// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    eutMovies: [],
    popularMovies: [],
    recentMovies: [],
  },
  getters: {
    eutMovies: state => state.eutMovies,
    popularMovies: state => state.popularMovies,
    recentMovies: state => state.recentMovies,
  },
  mutations: {
    EUT_MOVIES: (state, movies) => state.eutMovies = movies,
    POPULAR_MOVIES: (state, movies) => state.popularMovies = movies,
    RECENT_MOVIES: (state, movies) => state.recentMovies = movies,
  },
  actions: {
    fetchMovies ({ commit }) {
      axios({
        url: drf.movies.movieAlgorithm(),
        method: 'get',
        // headers: getters.authHeader,
        headers: {Authorization: 'Token 69a8a34bec720138c380b80b914f982804ab6e63'}
      })
        .then(res => {
          commit('EUT_MOVIES', res.data)
        })
        .catch(err => {
          console.error(err)
        })
      axios({
        url: drf.movies.moviePopular(),
        method: 'get',
        // headers: getters.authHeader,
        headers: {Authorization: 'Token 69a8a34bec720138c380b80b914f982804ab6e63'}
      })
        .then(res => {
          commit('POPULAR_MOVIES', res.data)
        })
        .catch(err => {
          console.error(err)
        })
      axios({
        url: drf.movies.movieRecent(),
        method: 'get',
        // headers: getters.authHeader,
        headers: {Authorization: 'Token 69a8a34bec720138c380b80b914f982804ab6e63'}
      })
        .then(res => {
          commit('RECENT_MOVIES', res.data)
        })
        .catch(err => {
          console.error(err)
        })
    },
  },
}