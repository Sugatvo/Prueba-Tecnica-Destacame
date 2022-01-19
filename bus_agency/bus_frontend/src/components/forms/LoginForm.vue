<template>
  <v-card elevation="0" max-width="500" class="pa-0 pa-sm-3 pb-3 col-sm-8 col-12">
    <router-link to="/" name="Destacame Bus" title="Destacame Bus">
      <v-img
        src="@/assets/destacame_bus_logo.svg"
        alt="Destacame Bus Logo"
        contain
        max-height="20vh"
        class="mb-xs-4 mb-md-8 lg-mb-8 mb-xl-8"
      >
      </v-img>
    </router-link>
    <v-card-title><h1  class="pb-4">Iniciar sesión</h1></v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field
          v-model="username"
          label="Enter you username"
          name="Username"
          prepend-inner-icon="mdi-mail"
          type="text"
          class="rounded-0"
          outlined
          tile
        ></v-text-field>
        <v-text-field
          v-model="password"
          label="Enter your password"
          name="password"
          prepend-inner-icon="mdi-lock"
          type="password"
          outlined
          tile
        >
        </v-text-field>
        <v-row v-if="error">
          <small class="text--danger">{{this.error}} </small>
        </v-row>
        <v-card-actions class="text--secondary">
          <v-spacer></v-spacer>
          ¿No tienes una cuenta?
          <router-link to="/register" class="pl-2" color="black"
            >Registrate acá</router-link
          >
        </v-card-actions>
        <v-btn class="rounded-0" color="black" x-large block dark @click="Login"
          >Ingresar</v-btn
        >
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
import UserDataService from "../../services/user.js";

export default {
  data: () => ({
    username: "",
    password: "",
    error: "",
  }),
  methods: {
    async Login() {
      try {
        console.log(this.state.csrf);
        let response = await UserDataService.login(
          this.username,
          this.password,
          this.state.csrf
        );
        console.log(response);
        this.state.isAuthenticated = true;
        this.username = "";
        this.password = "";
        this.error = "";
        this.$router.push("/");
      } catch (error) {
        console.log(error);
        this.error = "Wrong username or password.";
      }
    },
  },
  props: ["state"],
};
</script>