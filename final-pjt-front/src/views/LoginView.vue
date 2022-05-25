<template>
  <div>
    <b-card style="max-width: 20rem; margin-top:100px;" 
        class="container justify-content-center"
        border-variant="grey"
        bg-variant="light"
        >
    <h1 class="login-title">login</h1>
    <account-error-list v-if="authError"></account-error-list>
      <b-form @submit.prevent="login(credentials)" align="left">
        <b-form-group label-for="username" label="ID">
          <b-form-input v-model="credentials.username" id="username" placeholder="ID를 입력하세요" type="text" required>
          </b-form-input>
        </b-form-group>
        <br>
        <b-form-group label-for="password" label="Password">
          <b-form-input  v-model="credentials.password" id="password" placeholder="비밀번호를 입력하세요" type="password" required>
          </b-form-input>
        </b-form-group>
        <br>
        <b-button type="submit" pill variant="outline-danger">login</b-button>
        <router-link to="/signup" style="text-decoration:none; color: black;">
          <b-button type="link" pill variant="outline-secondary" class="mx-2">signup</b-button>
        </router-link>
      </b-form>
    </b-card>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data(){
      return {
        credentials:{
          username : '',
          password : '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style>
.login-title {
  color: black
}
label {
  color: black
}
</style>