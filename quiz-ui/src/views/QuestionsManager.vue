<script>
import QuestionDisplay from "@/components/QuestionDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";
import QuizApiServices from "@/services/QuizApiServices";
import ParticipationStorageService from "@/services/ParticipationStorageService";

export default {
    name: "QuestionsManager",
    components: {
        QuestionDisplay
    },

    data() {
        let currentQuestion = {};
        let currentQuestionPosition = 0;
        let totalNumberOfQuestion = 0;
        let answers = [];
        let score = 0;

        return {
            currentQuestion, currentQuestionPosition, totalNumberOfQuestion, score, answers
        };

    },

    async created() {
        this.currentQuestionPosition = 1;
        await QuizApiServices.getQuestion(this.currentQuestionPosition).then(data => {
            this.currentQuestion = {
                image: data.data.image,
                questionTitle: data.data.title,
                questionText: data.data.text,
                possibleAnswers: data.data.possibleAnswers,
            };
        });
        await QuizApiServices.getQuizInfo().then(data => {
           this.totalNumberOfQuestion = data.data.size;
        });
    },

    methods:{
        async answerClickedHandler(answer, index){
            this.answers.push(index);
            this.currentQuestionPosition++;
            if (this.currentQuestionPosition > this.totalNumberOfQuestion) {
                await this.endQuiz();
                return;
            }
            QuizApiServices.getQuestion(this.currentQuestionPosition).then(data => {
                this.currentQuestion = {
                    image: data.data.image,
                    questionTitle: data.data.title,
                    questionText: data.data.text,
                    possibleAnswers: data.data.possibleAnswers,
                };
            });
        },

        async endQuiz(){
            await QuizApiServices.pushScore(ParticipationStorageService.getPlayerName(), this.answers).then(data =>{
                this.score = data.data.score;
            });
            participationStorageService.saveScore(this.score);
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