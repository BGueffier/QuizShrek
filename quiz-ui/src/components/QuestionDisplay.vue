<script>
    export default {

        name: "QuestionDisplay",
        data() {
        },
    }
</script>

<template>
    <div>
        <img src="@/assets/lane.png" class="picture">
    </div>
    
    <div>
        <h2 class="question-title">Comment s'appelle L'Âne dans Shrek ?</h2>
    </div>
    <div class="answers-area d-grid">
        <div>
            <button type="button" class="btn answer" @click="launchNewQuiz">L'ane</button>
            <button type="button" class="btn answer" @click="launchNewQuiz">Bouriquet</button>
        </div>
        <div>
            <button type="button" class="btn answer" @click="launchNewQuiz">Fils de pute</button>
            <button type="button" class="btn answer" @click="launchNewQuiz">Réponse d</button>
        </div>
        
    </div>
    
</template>

<style>

    .answer {
        width: 40%;
        margin: 3% 5% 3% 5%;
    }
    .picture {
        min-width: 500px;
        max-width: 550px;
        border-radius: 1rem;
    }
    .question-title {
        padding: 1em 0 0 0;
        font-family: "Helvetica";
        color: #B0C400;
    }

    .answers-area {
        padding: 1em 0 0 0;
        display: flex;
    }

</style>