import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionManager from '../views/QuestionsManager.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/start-new-quiz-page',
      name: 'New Quiz',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'Questions',
      component: QuestionManager
    }
  ]
})

export default router
