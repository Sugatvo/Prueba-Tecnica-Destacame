<template>
  <v-card elevation="2" class="ml-auto mr-auto">
    <v-card-title>Agregar a chofer</v-card-title>
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
        tile
        color="error"
        class="white--text py-6"
        @click="closeModal"
      >
        Cancel
      </v-btn>
      <v-btn
        tile
        color="success"
        class="white--text py-6"
        :disabled="!valid"
        @click="Register"
      >
        Crear cuenta
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import DriverDataService from "../../services/driver.js";

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
    closeModal(){
        this.$emit('close-modal');
    },
    async Register() {
      try {
        let response = await DriverDataService.post(
          this.firstname,
          this.lastname,
          this.username,
          this.email,
          this.password_1
        );
        console.log(response);
        this.$emit('on-success');
        this.$emit('close-modal');
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>