<template>
  <div>
    <v-app-bar elevation="1" flat>
      <span class="hidden-sm-and-up">
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      </span>
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">
          Destacame Bus
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-if="!state.isAuthenticated"
        outlined
        to="/login"
        color="black"
        tile
        large
        class="unactive hidden-xs-only"
      >
        <v-icon left>mdi-account-circle-outline</v-icon>
        Acceder
      </v-btn>
      <v-btn
        v-if="state.isAuthenticated"
        outlined
        color="black"
        tile
        large
        @click="Logout"
        class="unactive hidden-xs-only"
      >
        <v-icon left>mdi-logout</v-icon>
        Cerrar sesión
      </v-btn>
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
        this.state.isAuthenticated = false;
        this.$emit("get-csrf")
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    console.log("nav bar mounted");
    console.log(this.state.isAuthenticated);
  },
  props: ["state"],
};
</script>

<style>
.unactive.v-btn--active::before {
  background-color: transparent;
}
</style>