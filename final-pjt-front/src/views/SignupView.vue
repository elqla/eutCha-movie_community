<template>
  <div>
    <b-card style="max-width: 20rem; margin-top:100px;" 
        class="container justify-content-center"
        border-variant="grey"
        bg-variant="light"
        >
    <h1>signup</h1>
    <account-error-list v-if="authError"></account-error-list>

        <!-- <form @submit.prevent="signup(credentials)">
          <div>
            <label for="username">Username: </label>
            <input  v-model="credentials.username" type="text" id="username" required/>
          </div>
          <div>
            <label for="password1">Password: </label>
            <input v-model="credentials.password1" type="password" id="password1" required />
          </div>
          <div>
            <label for="password2">Password Confirmation:</label>
            <input v-model="credentials.password2" type="password" id="password2" required />
          </div>
          <div>
            <button>Signup</button>
          </div>
        </form> -->
      <b-form @submit.prevent="signup(credentials)" align="left">
        <b-form-group label-for="username" label="ID">
          <b-form-input v-model="credentials.username" id="username" placeholder="ID를 입력하세요" type="text" required>
          </b-form-input>
        </b-form-group>
        <br>
        <b-form-group label-for="username" label="Password">
          <b-form-input  v-model="credentials.password1" id="username" placeholder="비밀번호를 입력하세요" required>
          </b-form-input>
        </b-form-group>
        <br>
        <b-form-group label-for="username" label="Password Confirmation">
          <b-form-input v-model="credentials.password2" id="username" placeholder="비밀번호 확인" required>
          </b-form-input>
        </b-form-group>
        <br>
        <b-button type="submit" variant="dark">signup</b-button>
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
          // nickname: '',
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