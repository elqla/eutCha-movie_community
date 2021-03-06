const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'
const PROFILE = 'profile/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
  },
  articles: {
    articles: () => HOST + ARTICLES,
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
    community: page => HOST + ARTICLES + 'community/' + `${page}/`,
    profileArticles: username => HOST + ARTICLES + PROFILE + `${username}/`,
    movieArticles: moviePk => HOST + ARTICLES + MOVIES + `${moviePk}/`,
    newArticles: moviePk => HOST + ARTICLES + 'new/' + `${moviePk}/`,
  },
  movies: {
    movieAlgorithm: () => HOST + MOVIES + 'eut/',
    movieGenre: () => HOST + MOVIES + 'eut-genre/',
    moviePopular: () => HOST + MOVIES + 'popular/',
    movieRecent: () => HOST + MOVIES + 'recent/',
    movies: () => HOST + MOVIES + 'movies/',
    newMovie: () => HOST + MOVIES + 'new/',
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    movieLike: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',
    movieDislike: moviePk => HOST + MOVIES + `${moviePk}/` + 'dislike/',
  },
}
