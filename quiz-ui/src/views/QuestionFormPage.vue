<script>
    import QuizApiServices from "@/services/QuizApiServices";
    import LoginService from "@/services/LoginService"

    
    export default {
        name: "QuestionForm",
        props: ['position'],

        data() {
            let totalNumberOfQuestion = 0;
            let answerCount = 2;
            let title = "";
            let text = "";
            let possibleAnswers = [];
            let answerValues = [];
            let goodAnswer = 0;
            let formattedImage = "";
            let position = 0;
            let i = 1;
            let questionId;

            return {
                totalNumberOfQuestion, answerCount, title, text, possibleAnswers, answerValues, i, goodAnswer, formattedImage, position, questionId
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
            if(this.$route.query.position !== undefined){
                QuizApiServices.getQuestion(this.$route.query.position).then(data => {
                    this.title = data.data.title;
                    this.text = data.data.text;
                    this.answerCount = data.data.possibleAnswers.length;
                    this.formattedImage = data.data.image;
                    this.questionId = data.data.id;
                    

                    this.i = 0
                    for(this.i; this.i <= this.answerCount; this.i++){
                        this.answerValues[this.i + 1] = data.data.possibleAnswers[this.i].text;
                        if(data.data.possibleAnswers[this.i].isCorrect === true){
                            this.goodAnswer = this.i+1;
                        }
                    }
                    
                }).catch(() => {
                    if(this.title === ""){
                        this.$router.push("/admin");
                    }
                })
            }
        },

        methods: {
            addAnswer(){
                this.answerCount += 1;
            },

            removeAnswer(){
                this.answerCount -= 1;
            },
            handleImageChange(event){
                const image = event.target.files[0];
                if(image){
                    const fileReader = new FileReader();
                    fileReader.onload = () => {
                        this.formattedImage = fileReader.result;
                    };
                    fileReader.readAsDataURL(image)
                }
            },  
            isFormValid(){
                this.i = 1;
                for(this.i ; this.i <= this.answerCount; this.i++){
                        if(this.answerValues[this.i] === ""){
                            return false;
                        }
                    }
                if(this.title === "" || this.text === "" || this.goodAnswer === 0){
                    return false;
                } else {
                    return true;
                }
            },
            setAnswer(){
                this.i = 1;
                for(this.i ; this.i <= this.answerCount; this.i++){
                    if(this.goodAnswer === this.i){
                        this.possibleAnswers.push({text: this.answerValues[this.i], isCorrect: true});
                    } else {
                        this.possibleAnswers.push({text: this.answerValues[this.i], isCorrect: false});
                    }
                    
                }
            },
            async sendQuestion(){
                this.i = 1;
                this.setAnswer();
                await QuizApiServices.pushQuestion(this.title, this.text, this.totalNumberOfQuestion +1, this.formattedImage, this.possibleAnswers).then((result) => {
                    this.$router.push("/admin");
                }).catch((error) => {
                    console.log(error);
                });

            },
            async updateQuestion(){
                this.setAnswer();
                
                await QuizApiServices.updateQuestion(this.questionId, this.title, this.text, parseInt(this.$route.query.position), this.formattedImage, this.possibleAnswers).then((result) => {
                    this.$router.push("/admin");
                }).catch((error) => {
                    console.log(error);
                });
            }   
        }
        
    }

    
</script>

<template>
    <form style="padding-top:20%">

    
        <div class="question-card">
            <div class="card text-white bg-dark mb-3" style="width: 40rem;">
                <img class="card-img-top" :src="`${this.formattedImage}`" v-if="this.formattedImage !==''" >
                <div class="card-body">
                    <div class="input-div">
                        <h5 class="card-title">Votre question : </h5>
                        <input type="text" class="form-control" id="question-title" placeholder="Question" v-model="text">
                    </div>
                    <div class="input-div">
                        <h5 class="card-title">Le titre de votre question : </h5>
                        <input type="text" class="form-control" id="question-title" placeholder="Titre de la question" v-model="title">
                    </div>
                    <div class="input-div">
                        <h5 class="card-title">Ajoutez / Enlevez vos réponses possibles</h5>
                        <button class="btn add-answer-btn action-button" type="button" @click="addAnswer()" :disabled="answerCount > 3">Ajouter une réponse</button>
                        <button class="btn add-answer-btn action-button" type="button" @click="removeAnswer()" :disabled="answerCount <= 2">Enlever une réponse</button>
                    </div>
                    <div class="answers-area">
                        <div class="answer" v-for="index in answerCount" :key="index">
                            <input type="text" class="form-control" id="question-title" :placeholder="'Réponse ' + index" v-model="answerValues[index]">
                        </div>
                    </div>
                    <div class="input-div">
                        <h5 class="card-title">Choisir la bonne réponse</h5>
                        <select class="form-select" v-model="goodAnswer">
                            <option v-for="index in answerCount" :value=index>Réponse {{ index }}</option>

                        </select>
                    </div>
                    
                    <div class="input-div">
                        <h5 class="card-title">Ajout d'une photo : </h5>
                        <input class="form-control" type="file" @change="handleImageChange($event)" accept="image/png, image/jpeg">
                    </div>
                    <div>
                        <button class="btn action-button" type="button" @click="sendQuestion()" :disabled="!isFormValid()" v-if="this.$route.query.position === undefined" >Créer question</button>
                        <button class="btn action-button" type="button" @click="updateQuestion(this.questionId)" :disabled="!isFormValid()" v-else>Update question</button>
                    </div>
                </div>
            </div>
        </div>
    </form>
    
    
    
</template>

<style>

    .add-answer-btn{
        background-color: #343a40;
        border-color: #343a40;
    }
    
    .add-answer-btn:hover{
        color: #737980;
    }
    
    .input-div{
        margin: 5% 0 5% 0;
    }

</style>