<script>
// import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
    export default {

        name: "NewQuiz",

        data() {
            let username = "";
            return {
                username,
            };
        },
        methods:{
            launchNewQuiz(){
                participationStorageService.savePlayerName(this.username);
                this.$router.push('/questions');
            },

        }
    }
</script>

<template>
    <h2 class="title">Saisissez votre nom</h2>

    <form>
        <div class="form-group">
            <input type="text" class="form-control" id="name1" placeholder="Saisissez votre nom d'utilisateur" v-model="username">
        </div>
        <div>
            <button type="button" class="btn" @click="launchNewQuiz" :disabled="this.username.length <= 0">GO!</button>
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