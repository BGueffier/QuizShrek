<script>
import QuizApiServices from "@/services/QuizApiServices";
import LoginService from "@/services/LoginService"
    export default {

        name: "Login",

        data() {
            let password = "";
            let token = "";
            return {
                password, token,
            };
        },
        methods:{
            async tryLogin(){
              await QuizApiServices.login(this.password).then(data => {
                this.token = data.data.token;
                LoginService.saveToken(this.token);
              })
              .catch(error => {
                alert(error);
              });
              
            },

        }
    }
</script>

<template>
    <h2 class="title">Saisissez le mot de passe</h2>

    <form>
        <div class="form-group">
            <input type="password" class="form-control" id="password" placeholder="Saisissez le mot de passe admin" v-model="password">
        </div>
        <div>
            <button type="button" class="btn" @click="tryLogin" :disabled="this.password.length <= 0">Connexion</button>
        </div>
    </form>
</template>

<style>
  form > div {
      padding: 1vh;
  }

  form *:focus {
      box-shadow: 0 0 0 0.1rem #B0C400 !important;
  }

  .btn{
      font-size: 1.2rem;
      color: #fff;
      background-color: #778212;
      border-color: #778212;
  }

  .btn:hover{
      color: #B0C400;
  }

</style>