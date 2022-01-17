<template>
  <v-app>
    <NavBar></NavBar> 
    <v-main>
      <router-view></router-view>
    </v-main>
    <Footer></Footer>
  </v-app>
</template>

<script>
import Footer from './components/layout/Footer';
import NavBar from "./components/layout/NavBar";
export default {
  name: 'App',

  components: {
    Footer,
    NavBar
  }
};
</script>
