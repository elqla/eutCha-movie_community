import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    eutMovies: [],
    popularMovies: [],
    recentMovies: [],
    movie: {},
    // allGenres:{},
  },
  getters: {
    eutMovies: state => state.eutMovies,
    popularMovies: state => state.popularMovies,
    recentMovies: state => state.recentMovies,
    movie: state => state.movie,
    // allGenrs: state => state.allGenres,
  },
  mutations: {
    EUT_MOVIES: (state, movies) => state.eutMovies = movies,
    POPULAR_MOVIES: (state, movies) => state.popularMovies = movies,
    RECENT_MOVIES: (state, movies) => state.recentMovies = movies,
    MOVIE: (state, movie) => state.movie = movie,
    // ALL_GENRES: (state, movie)
  },
  actions: {
    fetchMovies ({ commit, getters }) {
      axios({
        url: drf.movies.movieAlgorithm(),
        method: 'get',
        headers: getters.authHeader,
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
        headers: getters.authHeader,
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
        headers: getters.authHeader,
      })
        .then(res => {
          commit('RECENT_MOVIES', res.data)
        })
        .catch(err => {
          console.error(err)
        })
    },
    fetchMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

  },
}