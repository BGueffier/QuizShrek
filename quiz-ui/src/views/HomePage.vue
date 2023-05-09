<template>
  <h2 class="title">Shrek's Dreamland Challenge</h2>

  <h4 class="subtitle">Best Shrek Lovers</h4>
  <table class="table table-dark table-striped">
  <thead>
    <tr>
      
    </tr>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Nom du joueur</th>
      <th scope="col">Score</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.index">
      <th scope="row">{{ scoreEntry.index }}</th>
      <td>{{ scoreEntry.playerName }}</td>
      <td>{{ scoreEntry.score }}</td>
    </tr>

  </tbody>
</table>
  <router-link class="btn start-quiz" to="/start-new-quiz-page">Démarrer le challenge !</router-link>
  
</template>

<script>
// import quizApiService from "@/services/QuizApiService";

export default {

  name: "HomePage",

  data() {
    let registeredScores = [];
    return {
      registeredScores,
    };
  },
  async created() {
    this.registeredScores.push({playerName: "Micel", score: 500, index: 1});
    this.registeredScores.push({playerName: "Ben", score: 150, index: 2});
		this.registeredScores.push({playerName: "Vinc", score: 128, index: 3});
    this.registeredScores.push({playerName: "Yoyo", score: 1, index: 4});



    console.log(JSON.stringify(this.registeredScores));
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