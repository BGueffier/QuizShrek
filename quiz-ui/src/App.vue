<script>
import LoginService from "@/services/LoginService"

export default{
  data() {
    let isTokenGood;
    return {
        isTokenGood,
    };
  },
  async created() {
    await LoginService.isAdminAuthenticated().then(result => {
        this.isTokenGood = result;
    });
    console.log(this.isTokenGood);
  },
  methods: {
    signOut(){
      LoginService.removeToken();
      window.location.reload();
    }
  }
}

</script>

<template>
  <header>
    <div class="navbar">
      <router-link to="/"><img src="@/assets/images/shrek-navbar.ico" class="picture"></router-link>
      <router-link class="btn login-btn" to="/login" v-if="this.isTokenGood === false">Page de connexion</router-link>
      <router-link class="btn login-btn" to="/admin" v-if="this.isTokenGood === true">Espace admin</router-link>
      <button class="btn signout-btn" to="/admin" @click="signOut()" v-if="this.isTokenGood === true">Déconnexion</button>

    </div>
  </header>
  <RouterView /> 
  
   
</template>

<style scoped>

.login-btn {
  margin-left: auto;
}

.signout-btn{
  margin-left: 2%;
}

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
  width: 100%;
  position: fixed;
  left: 0;
  top: 0;
}

.navbar{
  display: flex;
  width: 100%;
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
  min-width: 7rem;
  max-width: 7rem;
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
