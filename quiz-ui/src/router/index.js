import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import ScorePage from '../views/ScorePage.vue'
import LoginPage from '../views/LoginPage.vue'
import AdminPage from '../views/AdminPage.vue'
import QuestionFormPage from '../views/QuestionFormPage.vue'


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
      component: QuestionsManager
    },
    {
      path: '/votre-score',
      name: 'Score',
      component: ScorePage
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginPage
    },
    {
      path: '/admin',
      name: 'Admin',
      component: AdminPage
    },
    {
      path: '/new-question',
      name: 'QuestionForm',
      component: QuestionFormPage,
      props: (route) => ({ position: route.query.position })
    },
  ]
})

export default router