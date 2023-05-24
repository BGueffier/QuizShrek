<template>
  <h2 class="title">Shrek's Dreamland Challenge</h2>
  <div v-if="registeredScores.length !== 0">
    <h4 class="subtitle">Best Shrek Lovers</h4>
  <table class="table table-dark table-striped">
    <thead>
      <tr>
        
      </tr>
      <tr>
        <th scope="col">Nom du joueur</th>
        <th scope="col">Score</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
        <td>{{ scoreEntry.playerName }}</td>
        <td>{{ scoreEntry.score }}</td>
      </tr>

    </tbody>
  </table>
  </div>
  
<router-link class="btn start-quiz" to="/start-new-quiz-page">Démarrer le challenge !</router-link>
  
</template>

<script>
import QuizApiServices from "@/services/QuizApiServices";

export default {

  name: "HomePage",

  data() {
    let registeredScores = [];
    return {
      registeredScores,
    };
  },
  async created() {
      QuizApiServices.getQuizInfo().then(data => {
          this.registeredScores = data.data.scores;
      });
      console.log(this.registeredScores);
  }
};
</script>

<style>

.title {
  font-family: "ShrekFont";
  color: #B0C400
}

.subtitle {
  font-family: "ShrekFont";
  color: #C5EE7D;
  padding-top: 1rem;
  padding-bottom: 1rem;
}
.start-quiz {
  font-size: 1.2rem;
  color: #fff;
  background-color: #778212;
  border-color: #778212;
  
}
</style>