<script>
// import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
    export default {

        name: "QuestionsManager",

        data() {
            let currentQuestion = { 
                questionTitle: "Comment s'appelle l'âne dans Shrek ?", 
                questionText: "Nom de l'âne, de Shrek : ",
                possibleAnswers: ["L'âne","Damso","Frédéric","Michel"],
            }

            return {
                currentQuestion
            };
            
        }
    }
</script>

<style>

</style>