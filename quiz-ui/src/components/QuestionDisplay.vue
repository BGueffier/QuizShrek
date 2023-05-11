<script>
    export default {

        name: "QuestionDisplay",
        props: {
            question: {
                type: Object
            }
        },
        data() {
        },
    }
</script>

<template>
    <div>
        <img src="@/assets/lane.png" class="picture">
    </div>
    
    <div>
        <h2 class="question-title">{{question.questionTitle}}</h2>
    </div>
    <div class="answers-area">
        <div class="answer" v-for="answer in question.possibleAnswers" v-bind:key="answer">
            <button type="button" class="btn" @click="launchNewQuiz">{{answer}}</button>
        </div>
    </div>
    
</template>

<style>
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
        flex-wrap: wrap;
        justify-content: center;
    }

    .answer{
        width: 40%;
        margin: 3% 2% 3% 2%;
    }

    .answer>.btn{
        width: 100%;
    }

</style>