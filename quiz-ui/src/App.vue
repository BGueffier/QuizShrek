<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="navbar">
      <img src="@/assets/images/shrek-navbar.ico" class="picture">

      <div class="">
        <!-- <router-link class="btn" to="/start-new-quiz-page">Démarrer le challenge !</router-link> -->
      </div>
    </div>
  </header>
  <RouterView /> 
  
   
</template>

<style scoped>

@font-face {
  font-family: "ShrekFont";
  src: local("ShrekFont"),
   url(@/assets/fonts/Shrek.ttf) format("truetype");
}

@font-face {
  font-family: "Helvetica";
  src: local("Helvetica"),
   url(@/assets/fonts/Helvetica.ttf) format("truetype");
}

header {
  line-height: 1.5;
  max-height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
}

.navbar{
  display: flex;
}
.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

.picture {
  min-width: 20%;
  max-width: 25%;
}
nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
