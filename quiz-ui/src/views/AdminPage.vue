<script>
    import QuizApiServices from "@/services/QuizApiServices";
    import LoginService from "@/services/LoginService"

    
    export default {
        name: "Login",
        
        data() {
            let totalNumberOfQuestion = 0;
            let questions = [];
            let position = 1;

            return {
                totalNumberOfQuestion, questions, position
            };

        },
        async created() {
            await LoginService.isAdminAuthenticated().then(result => {
                if(!result){
                    this.$router.push('/');
                }
            });
            await QuizApiServices.getQuizInfo().then(data => {
                this.totalNumberOfQuestion = data.data.size;
            });
            for(this.position = 1; this.position <= this.totalNumberOfQuestion; this.position++){
                await QuizApiServices.getQuestion(this.position).then(data => {
                    this.questions.push(data.data);
                });
            }
        } ,

        methods: {
            deleteSelectedQuestion(id){
                QuizApiServices.deleteQuestion(id).then(() => {
                    window.location.reload();
                })
                .catch((error) => {
                    alert(error);
                });
            },
            editQuestion(position){
                this.$router.push("/question/?position=" + position);
            }
        }
    }

    
</script>

<template>
    <div class="question-card" v-for="question in this.questions" :key="question.position">
        <h2 class="title">Question {{ question.position }}</h2>
        <div class="card text-white bg-dark mb-3" style="width: 40rem;">
            <img class="card-img-top" :src="`${question.image}`" alt="Card image cap" v-if="question.image">
            <div class="card-body">
                <h5 class="card-title">{{ question.text }}</h5>
                <div class="answers-area">
                    <div class="answer" v-for="(answer, index) in question.possibleAnswers" v-bind:key="answer.id">
                        <p v-if="answer.isCorrect === false " class="btn wrong-answer">{{answer.text}}</p>
                        <p v-else class="btn">{{answer.text}}</p>
                    </div>
                </div>
                <div>
                    <button class="btn wrong-answer action-button" @click="deleteSelectedQuestion(question.id)">Supprimer</button>
                    <button class="btn action-button" @click="editQuestion(question.position)">Modifier</button>
                </div>
            </div>
        </div>
    </div>
    <router-link to="/question" class="btn add-answer-btn action-button add-btn">Ajouter une question</router-link>
    
    
    
</template>

<style>

    .wrong-answer:hover{
        color: #8f3f3f;
    }
    .wrong-answer{
        background-color: #791b1b;
        border-color: #791b1b;
    }
    .question-card{
        margin: 5% 0 5% 0;
    }
    .action-button{
        margin: 0 5% 0 5%;
    }

    .add-btn{
        margin-bottom: 5%;
    }

</style>