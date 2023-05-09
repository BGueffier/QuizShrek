<template>
  <h1 class="title">Shrek's Dreamland Challenge</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <router-link class="start-quiz" to="/start-new-quiz-page">Démarrer le challenge !</router-link>
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
		this.registeredScores.push({playerName: "Vinc", score: 128});
    this.registeredScores.push({playerName: "Yoyo", score: 1});
    this.registeredScores.push({playerName: "Ben", score: 150});
    this.registeredScores.push({playerName: "Micel", score: 500});
    console.log(JSON.stringify(this.registeredScores));
  }
};
</script>

<style>

.title {
  font-family: "ShrekFont";
  color: #C5EE7D
}
.start-quiz {
  font-size: 2rem;
  font-style: bold;
}
</style>