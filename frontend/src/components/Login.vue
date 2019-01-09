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
import Axios from 'axios'
import {jwt} from 'jsonwebtoken'
import router from '../router/index.js'

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
      const axios = Axiot.create({
        baseURL: 'http://localhost:4000',
        header: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        responseType: 'json'
      })

      // nextページの取得
      try{
        let nextPage = this.$route.query.next
      }catch(e){
        nextPage = 'PageA'
      }
      console.log(nextPage)

      // axiosのthenメソッドの中ではthisがvueコンポーネントを指さなくなるので別の変数に割り当てておく
      const self = this

      axios.get('/auth', {
        // クエリパラメータをセット
        params: {
          username: document.getElementById('loginaccount').value,
          password: document.getElementById('loginpassword').value
        }
      }).then(function(response) {
        // 応答が戻ってきたら結果を処理。
        // "success" だったら次のページにジャンプし、失敗だったらその旨表示
        if(response.data.result === 'success'){
          let token = self.generateToken(document.getElementById('loginaccount').value)
          // cookieとしてトークンを付与
          document.cookie = 'token=' + token
          // 次のページにジャンプ
          // router.push({name: nextPage, params: { auth: 'authenticated' }})
          router.push({name: nextPage})
        } else {
          document.getElementById('loginResult').innerHTML = 'Login Failed !'
        }
      })
    },
    generateToken: function(username){
      /* JWTトークンの生成 */
      // JWT用のシークレットトークンをセット(【注意】実際にはコードの中に書いてはいけない！)
      const secretToken = 'oreore'

      // JWTのヘッダー
      //const oHeader = {alg: 'HS256', typ: 'JWT'}

      // JWTペイロード
      let offset = Math.floor(Math.random() * Math.floor(25))
      const DO = new Date()
      DO.setSeconds(DO.getSeconds() + offset)
      let dY = DO.getFullYear()
      let dm = DO.getMonth() + 1
      let dd = DO.getDate()
      let dH = ('0' + DO.getHours()).slice(-2)
      var dM = ('0' + DO.getMinutes()).slice(-2)
      var dS = ('0' + DO.getSeconds()).slice(-2)
      var dStr = dY + '/' + dm + '/' + dd + ' ' + dH + ':' + dM + ':' + dS + ' +0900'
      var oPayload = {username: username, until: dStr}
      console.log(oHeader, oPayload)
      // JWTを生成
      var sJWT = jwt.sign(oPayload, secretToken, { algorithm: 'HS256'});
      // var sJWT = KJUR.jws.JWS.sign('HS256', JSON.stringify(oHeader), JSON.stringify(oPayload), secretToken)
      console.log(sJWT)
      return sJWT
    }
  }
}
</script>