<template>
  <v-app>
    <NavBar />
    <v-main>
      <v-container class="fill-height" fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Footer from "./components/layout/Footer";
import NavBar from "./components/layout/NavBar";

export default {
  name: "App",

  components: {
    Footer,
    NavBar,
  },
};
</script>
