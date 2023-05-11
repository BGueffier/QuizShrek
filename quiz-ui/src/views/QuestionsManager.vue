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
            possibleAnswers: ["L'âne","Damso","Frédéric"],
        };
        let currentQuestionPosition = 0;
        let totalNumberOfQuestion = 1;

        return {
            currentQuestion, currentQuestionPosition, totalNumberOfQuestion
        };

    },
    methods:{
        answerClickedHandler(){
        },
    }
}


</script>

<template>
    <h1 style="font-family:'ShrekFont';">Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<style>
</style>