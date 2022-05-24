<template>
  <div>
    <b-card style="max-width: 20rem; margin-top:100px;" 
        class="container justify-content-center"
        border-variant="grey"
        bg-variant="light"
        >
    <h1>signup</h1>
    <account-error-list v-if="authError"></account-error-list>
      <b-form @submit.prevent="signup(credentials)" align="left">
        <b-form-group label-for="username" label="ID">
          <b-form-input v-model="credentials.username" id="username" placeholder="ID를 입력하세요" type="text" required>
          </b-form-input>
        </b-form-group>
        <br>
        <b-form-group label-for="password1" label="Password">
          <b-form-input  v-model="credentials.password1" id="password1" placeholder="비밀번호를 입력하세요" type="password" required>
          </b-form-input>
        </b-form-group>
        <br>
        <b-form-group label-for="password2" label="Password Confirmation">
          <b-form-input v-model="credentials.password2" id="password2" placeholder="비밀번호 확인" type="password" required>
          </b-form-input>
        </b-form-group>
        <br>
        <b-button type="submit" pill variant="outline-danger">signup</b-button>
      </b-form>
    </b-card>
    
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data(){
      return {
        credentials:{
          username : '',
          password1 : '',
          password2 : '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style>

</style>