<script>
    export default {

        name: "QuestionDisplay",
        emits: ["answer-selected"],
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
        <img :src="`${question.image}`" class="picture" v-if="question.image">
    </div>
    
    <div>
        <h2 class="question-title">{{question.questionText}}</h2>
    </div>
    <div class="answers-area">
        <div class="answer" v-for="(answer, index) in question.possibleAnswers" v-bind:key="answer.id">
            <button type="button" class="btn" @click="$emit('answer-selected', answer, index+1)">{{answer.text}}</button>
        </div>
    </div>
    
</template>

<style>
    .picture {
        min-width: 250px;
        max-width: 250px;
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