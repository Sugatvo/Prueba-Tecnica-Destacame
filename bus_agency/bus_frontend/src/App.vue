<template>
  <v-app>
    <NavBar @get-csrf="getCSRF"/>
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
import AuthenticationService from "./services/auth.js";

export default {
  name: "App",
  components: {
    Footer,
    NavBar,
  },
  methods: {
    async getCSRF() {
      try {
        let response = await AuthenticationService.getCSRF();
        console.log(response);
        let csrfToken = response.headers["x-csrftoken"];
        console.log(csrfToken);
        this.$store.state.csrf = csrfToken;
      } catch (error) {
        console.log(error);
      }
    },
    async getSession() {
      try {
        let response = await AuthenticationService.getSession();
        let data = response.data;
        console.log(response);
        if (data.isAuthenticated) {
          this.$store.state.isAuthenticated = true;
        } else {
          this.$store.state.isAuthenticated = false;
          this.getCSRF();
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    console.log("app mounted");
    this.getSession();
  },
};
</script>

<style>
.custom-margin{
  margin-right: 128px;
  margin-left: 128px;
}

</style>