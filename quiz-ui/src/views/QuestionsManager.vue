<script>
import QuestionDisplay from "@/components/QuestionDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
    name: "QuestionsManager",
    components: {
        QuestionDisplay
    },

    data() {
        let currentQuestion = {};
        let currentQuestionPosition = 0;
        let totalNumberOfQuestion = 0;
        let score = 0;

        return {
            currentQuestion, currentQuestionPosition, totalNumberOfQuestion, score
        };

    },

    async created() {
        this.currentQuestion = {
            questionTitle: "Comment s'appelle l'âne dans Shrek ?",
            questionText: "Nom de l'âne, de Shrek : ",
            possibleAnswers: [{text:"L'âne", id:0},{text:"Greg", id:1},{text:"Reforme des retraites", id:2},{text:"Suzie", id:3}],
        };
        this.currentQuestionPosition = 1;
        this.totalNumberOfQuestion = 1;
    },

    methods:{
        async answerClickedHandler(index){
            if (index === 0) //TODO:fait en dur changer
                this.score++;

            this.currentQuestionPosition++;
            if (this.currentQuestionPosition > this.totalNumberOfQuestion) {
                await this.endQuiz();
            }
        },

        async endQuiz(){
            participationStorageService.saveScore(this.score)
            this.$router.push('/votre-score');
        }
    }
}


</script>

<template>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
</template>

<style>
</style>