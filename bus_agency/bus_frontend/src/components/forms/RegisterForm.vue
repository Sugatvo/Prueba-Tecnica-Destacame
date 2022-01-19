<template>
  <v-card elevation="0" max-width="600" class="ml-auto mr-auto">
    <v-card-title>Registrate</v-card-title>
    <v-card-subtitle>Es rápido y fácil</v-card-subtitle>
    <v-card-text>
      <v-form v-model="valid">
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="firstname"
              label="Nombre"
              outlined
              :rules="[rules.required, rules.firstname]"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="lastname"
              outlined
              label="Apellido"
              :rules="[rules.required, rules.lastname]"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-text-field
          v-model="username"
          :rules="[rules.required, rules.usernameLength, rules.usernamePattern]"
          outlined
          label="Nombre de usuario"
        ></v-text-field>
        <v-text-field
          v-model="email"
          :rules="[rules.required, rules.email]"
          outlined
          label="Correo electrónico"
        ></v-text-field>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="password_1"
              v-if="showPassword"
              label="Contreseña"
              outlined
              :rules="[rules.required, rules.password]"
            ></v-text-field>

            <v-text-field
              v-model="password_1"
              v-else
              label="Contreseña"
              outlined
              type="password"
              :rules="[rules.required, rules.password]"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="password_2"
              v-if="showPassword"
              outlined
              label="Confirmación"
              :rules="[rules.required, rules.confirmPassword]"
            ></v-text-field>
            <v-text-field
              v-model="password_2"
              v-else
              outlined
              label="Confirmación"
              type="password"
              :rules="[rules.required, rules.confirmPassword]"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-checkbox
          v-model="showPassword"
          v-on:change="!showPassword"
          value="false"
          label="Mostrar contraseña"
          type="checkbox"
        ></v-checkbox>
      </v-form>
    </v-card-text>
    <v-card-actions class="justify-center">
      <v-btn
        block
        tile
        color="blue-grey darken-4"
        class="white--text py-6"
        :disabled="!valid"
        @click="Register"
      >
        Registrar
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import UserDataService from "../../services/user.js";

export default {
  data() {
    return {
      valid: false,
      showPassword: false,
      firstname: "",
      lastname: "",
      username: "",
      email: "",
      password_1: "",
      password_2: "",
      rules: {
        firstname: (v) => {
          const pattern = /^[a-zA-Z]+$/;
          return pattern.test(v) || "El nombre debe contener unicamente letras";
        },
        lastname: (v) => {
          const pattern = /^[a-zA-Z]+$/;
          return (
            pattern.test(v) || "El apellido debe contener unicamente letras"
          );
        },
        usernameLength: (v) =>
          v.length <= 150 ||
          "El nombre de usuario debe contener 150 caracteres o menos",
        usernamePattern: (v) => {
          const pattern = /^[a-zA-Z0-9@.-_]+$/;
          return (
            pattern.test(v) ||
            "El nombre de usuario solo puede contener letras, digitos y @/./-/_"
          );
        },
        password: (v) =>
          v.length >= 8 ||
          `Contraseña demasiada corta, te faltan ${8 - v.length} caracteres`,
        confirmPassword: (v) =>
          v === this.password_1 || "Las contraseñas no coinciden.",
        required: (v) => !!v || "Este campo es requerido",
        email: (v) => {
          const pattern =
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(v) || "Correo no válido";
        },
      },
    };
  },
  methods: {
    async Login() {
      try {
        console.log(this.state.csrf);
        let response = await UserDataService.login(
          this.username,
          this.password_1,
          this.state.csrf
        );
        console.log(response);
        this.state.isAuthenticated = true;
        this.firstname = "";
        this.lastname="";
        this.username="";
        this.email="";
        this.password_1="";
        this.password_2="";
        this.$router.push("/");
      } catch (error) {
        console.log(error);
      }
    },
    async Register() {
      try {
        let response = await UserDataService.register(
          this.firstname,
          this.lastname,
          this.username,
          this.email,
          this.password_1
        );
        console.log(response);
        if (response.status == "201") {
            this.Login()
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
  props: ["state"],
};
</script>