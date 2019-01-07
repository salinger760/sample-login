<template>
  <div class="login">
    <h1>Login</h1>
    <h2>Username(Correct Login Name: myLoginName)</h2>
    <div>
      <p>{{ loginaccountname }}</p>
      <input id="loginaccount" v-model="loginaccountname"/>
    </div>
    <h2>Password</h2>
    <div>
      <p>{{ loginpassword }}</p>
      <input type="password" id="loginpassword" v-model="loginpassword"/>
    </div>
    <div class="loginsubmit">
      <button v-on:click="checklogin">LOGIN</button>
    </div>
    <div id="loginResult"></div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data: function(){
    return{
      loginaccountname: '',
      loginpassword: ''
    }
  },
  methods: {
    checklogin: function(event){
      let nextPage = this.$route.query.nextPage
      if(nextPage === undefined){
        nextPage = 'PageA'
      }
      
      console.log(nextPage)

      const correntLoginName = 'myLoginName'
      const correntPassword = 'mySecretPassword1234'

      let myLoginName = document.getElementById('loginaccount').value
      let myLoginPass = document.getElementById('loginpassword').value

      if( (myLoginName === correntLoginName) && (myLoginPass === correntPassword) ){
        this.$router.push({name: nextPage, query: {auth: 'authenticated' }})
      }else{
        document.getElementById('loginResult').innerHTML = 'Login Failed !'
      }
    }
  }
}
</script>