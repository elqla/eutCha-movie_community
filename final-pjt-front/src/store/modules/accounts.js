
import drf from "@/api/drf"
import axios from "axios"
// import router from '@/router'


export default {
  // plugins:[
  //   createPersistedState()
  // ],
  state: {
    token: '',
    currentUser: {},
    profile: {},
    authError: null,
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({Authorization: `Token ${state.token}`})
  },
  mutations: {    
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile, 
    SET_AUTH_USER: (state, error) => state.authError = error
  },
  actions: {
    // saveToken({commit}, token){
    //   commit('SET_TOKEN', token)
    //   localStorage.setItem('token', token)
    // },
    // removeToken({commit}){
    //   commit('SET_TOKEN', '')
    //   localStorage.setItem('token', '')
    // },
    signup( credentials){  //{commit, dispatch}
      axios({
        url:drf.accounts.signup(),
        method: 'post',
        data:credentials,
      })
      .then(res=>{
        console.log(res)
        console.log('sdfsf')
      })
      .catch(()=>{
        console.log('haha')
      })
    }


  

  },
}
