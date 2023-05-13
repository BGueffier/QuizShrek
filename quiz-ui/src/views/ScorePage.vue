<script>
  import participationStorageService from "@/services/ParticipationStorageService";

  export default {

      name: "ScorePage",

      data() {
          let score = 0;
          let playerName = "";
          return {
              score, playerName,
          };
      },

      async created() {
          this.score = participationStorageService.getScore();
          participationStorageService.clearScore();

          this.playerName = participationStorageService.getPlayerName();
      },

      methods:{

      }
  }
</script>

<template>
    <div>
        <img src="@/assets/congrats.jpg" class="picture">
    </div>

    <div>
        <h2 class="congrats">Bravo {{this.playerName}} vous avez terminé, votre score est de {{this.score}}</h2>
    </div>

</template>

<style>
  .picture {
      min-width: 500px;
      max-width: 550px;
      border-radius: 1rem;
  }
  .congrats {
      padding: 1em 0 0 0;
      font-family: "Helvetica";
      color: #B0C400;
  }

</style>