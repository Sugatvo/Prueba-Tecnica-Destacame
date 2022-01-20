<template>
  <v-card
    elevation="0"
    max-width="500"
    class="ma-lg-0 ma-md-0 ma-sm-auto ma-auto"
  >
    <router-link to="/" name="Destacame Bus" title="Destacame Bus">
      <v-img
        src="@/assets/destacame_bus_logo.svg"
        alt="Destacame Bus Logo"
        contain
        max-height="10vh"
        class="mb-4"
      >
      </v-img>
    </router-link>
    <v-card-title><h1 class="pb-4">Iniciar sesión</h1></v-card-title>
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
        <p v-if="error" class="error--text">{{ this.error }}</p>
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
    async WhoAmI(){
      try {
        let response = await UserDataService.whoami();
        this.$store.state.isAuthenticated = true;
        this.$store.state.username = response.data.username;
        this.$store.state.id = response.data.id;
        this.username = "";
        this.password = "";
        this.error = "";
        this.$router.push("/");
      } catch (error) {
        console.log(error);
      }
    },
    async Login() {
      try {
        await UserDataService.login(
          this.username,
          this.password,
          this.$store.state.csrf
        );
        this.WhoAmI();
      } catch (error) {
        console.log(error);
        this.error = "Contraseña o nombre de usuario incorrecto";
      }
    },
  },
};
</script>