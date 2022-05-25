import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    eutMovies: [],
    popularMovies: [],
    recentMovies: [],
    movies: [],
    movie: {},
  },
  getters: {
    eutMovies: state => state.eutMovies,
    popularMovies: state => state.popularMovies,
    recentMovies: state => state.recentMovies,
    movies: state => state.movies,
    movie: state => state.movie,
  },
  mutations: {
    EUT_MOVIES: (state, movies) => state.eutMovies = movies,
    POPULAR_MOVIES: (state, movies) => state.popularMovies = movies,
    RECENT_MOVIES: (state, movies) => state.recentMovies = movies,
    MOVIES: (state, movies) => state.movies = movies,
    MOVIE: (state, movie) => state.movie = movie,
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
    likeMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movieLike(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) router.push({ name: 'NotFound404' })
        })
    },
    dislikeMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movieDislike(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) router.push({ name: 'NotFound404' })
        })
    },
    newMovie({ commit, getters }, credentials) {
      axios({
        url: drf.movies.newMovie(),
        method: 'post',
        headers: getters.authHeader,
        data: credentials
      })
        .then(res => {
          commit('MOVIE', res.data)
          router.push({
            name: 'movieDetail',
            params: { movieId: getters.movie.id }
          })
        })
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) router.push({ name: 'NotFound404' })
        })
    },
    fetchAdmin({ commit, getters }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('MOVIES', res.data)
        })
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) router.push({ name: 'NotFound404' })
        })
    },
  },
}