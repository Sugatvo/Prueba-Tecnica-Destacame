<template>
  <div>
    <v-app-bar class="white" elevation="1">
      <span class="hidden-sm-and-up">
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      </span>
      <v-toolbar-title class="ml-16">
        <router-link to="/" tag="span" style="cursor: pointer">
          <v-img
            max-height="32"
            max-width="250"
            src="@/assets/destacame_bus_logo.svg"
            alt="Destacame Bus Logo"
            contain
          ></v-img>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-if="!$store.state.isAuthenticated"
        outlined
        to="/login"
        color="primary"
        rounded
        small
        class="unactive hidden-xs-only ml-16"
      >
        <v-icon left>mdi-account-circle-outline</v-icon>
        Iniciar sesión
      </v-btn>
      <v-btn
        v-if="!$store.state.isAuthenticated"
        to="/register"
        color="primary"
        rounded
        small
        depressed
        class="unactive hidden-xs-only mr-8 ml-4"
      >
        <v-icon left>mdi-account-plus</v-icon>
        Regístrate
      </v-btn>

      <v-menu top :close-on-click="true" v-if="$store.state.isAuthenticated">
        <template v-slot:activator="{ on, attrs }">
          <v-btn elevation="0" color="primary" dark v-bind="attrs" v-on="on" rounded text>
            <v-icon left>mdi-account-circle</v-icon>
            {{$store.state.username}}
          </v-btn>
        </template>

        <v-list>
          <v-list-item link to="/profile">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Perfil</v-list-item-title>
          </v-list-item>
          <v-list-item link @click="Logout"> 
            <v-list-item-icon>
              <v-icon>mdi-logout</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Cerrar sesión</v-list-item-title>
          </v-list-item>
      </v-list>
      </v-menu>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Account</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import UserDataService from "../../services/user.js";

export default {
  data: () => ({
    drawer: false,
    group: null,
  }),
  methods: {
    async Logout() {
      try {
        console.log("Logout");
        let response = await UserDataService.logout();
        console.log(response);
        console.log(response.data);
        this.$store.state.isAuthenticated = false;
        this.$emit("get-csrf");
        this.$router.push("/");
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    console.log("nav bar mounted");
    console.log(this.$store.state.isAuthenticated);
  },
};
</script>

<style>
.unactive.v-btn--active::before {
  background-color: transparent;
}
</style>