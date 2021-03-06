import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import CommunityView from '@/views/CommunityView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import MovieCategoryView from '@/views/MovieCategoryView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleEditView from '@/views/ArticleEditView.vue'
import ArticleNewView from '@/views/ArticleNewView.vue'
import AdminNewView from '@/views/AdminNewView.vue'
import AdminEditView from '@/views/AdminEditView.vue'
import AdminView from '@/views/AdminView.vue'
import store from '@/store'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/movies',
    name: 'movies',
    component: MovieCategoryView
  },
  {
  path: '/admin',
  name: 'admin',
  component: AdminView
  },
  {
  path: '/admin/new',
  name: 'adminNewView',
  component: AdminNewView
  },
  {
  path: '/admin/:movieId',
  name: 'adminEditView',
  component: AdminEditView
  },
  {
    path: '/community/:page',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/movies/:movieId',
    name: 'movieDetail',
    component: MovieDetailView
  },
  {
    path: '/articles/new',
    name: 'newArticle',
    component: ArticleNewView
  },
  {
    path: '/articles/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/articles/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


router.beforeEach((to, from, next) => {
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup', 'home']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('Require Login. Redirecting..')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'movies' })
  }
})


export default router
