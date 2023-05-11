<script>
import QuestionDisplay from "@/components/QuestionDisplay.vue";

export default {

    name: "QuestionsManager",
    components: {
        QuestionDisplay
    },

    data() {
        let currentQuestion = {
            questionTitle: "Comment s'appelle l'âne dans Shrek ?",
            questionText: "Nom de l'âne, de Shrek : ",
            possibleAnswers: [{text:"L'âne", id:0},{text:"Greg", id:1},{text:"Reforme des retraites", id:2},{text:"Suzie", id:3}],
        };
        let currentQuestionPosition = 0;
        let totalNumberOfQuestion = 1;

        return {
            currentQuestion, currentQuestionPosition, totalNumberOfQuestion
        };

    },
    methods:{
        async answerClickedHandler(index){
            alert(index);
        },
    }
}


</script>

<template>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
</template>

<style>
</style>