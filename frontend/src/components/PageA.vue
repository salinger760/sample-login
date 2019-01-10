<template>
  <div class="pagea">
    This is page A.
    <div>
      Valid until {{ until.toString() }}
    </div>
  </div>
</template>

<script>
import jwt from 'jsonwebtoken'
import router from '../router/index.js'

export default {
  name: 'PageA',
  beforeMount: function(){
    let sJWT = ''
    const ck = document.cookie.split(';')
    ck.forEach(function(value){
      const content = value.split('=')
      if(content[0] === 'token'){
        sJWT = content[1]
      }
      console.log("sJWT")
      console.log(sJWT)
    })

    // JWT用のシークレットトークンをセット(【注意】実際にはコードの中に書いてはいけない！)
    const secretToken = 'oreore'

    //const isValid = jwt.verify(sJWT, secretToken,  { algorithm: 'HS256'});
    //console.log(isValid)

    var self = this

    jwt.verify(sJWT, secretToken, function(err, decoded) {
      if (err) {
        return router.push({ name: 'Login', query: { next: self.$route.name } })
      }
      console.log(decoded)
      if(!decoded){
        console.log('invalid authentication. route to login...')
        document.cookie = 'token=; max-age=0'
        router.push({ name: 'Login', query: { next: self.$route.name } })
      }else{
        console.log('JWT is expired. route to login...1')
        const payload = decoded
        const until = new Date(payload.until)
        const now = new Date()
        if (now > until) {
          console.log('JWT is expired. route to login...2')
          document.cookie = 'token=; max-age=0'
          router.push({ name: 'Login', query: { next: self.$route.name } })
        }
      }
    });
  },
  computed: {
    until: function () {
      const secretToken = 'oreore'
      let sJWT = ''
      const ck = document.cookie.split(';')
      ck.forEach(function (value) {
        // cookie名と値に分ける
        var content = value.split('=')
        if (content[0] === 'token') {
          sJWT = content[1]
        }
      })
      console.log(sJWT)
      if (sJWT.length > 0) {
        let decoded = jwt.verify(sJWT, secretToken, { algorithm: 'HS256'})
        const payload = decoded
        return new Date(payload.until)
      }
    }
  }
}
</script>