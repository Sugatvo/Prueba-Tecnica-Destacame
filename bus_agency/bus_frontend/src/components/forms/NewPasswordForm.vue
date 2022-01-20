<template>
  <v-card elevation="0">
    <v-card-title>Cambiar contraseña</v-card-title>
    <v-divider></v-divider>
    <v-card-text>
      <v-form v-model="valid">
        <v-text-field
          v-model="old_password"
          v-if="showPassword"
          label="Contraseña actual"
          outlined
          :rules="[rules.required]"
        ></v-text-field>

        <v-text-field
          v-model="old_password"
          v-else
          label="Contraseña actual"
          outlined
          type="password"
          :rules="[rules.required]"
        ></v-text-field>
        <p class="mb-6 error--text">{{error_message}}</p>
        <v-text-field
          v-model="password_1"
          v-if="showPassword"
          label="Nueva contraseña"
          outlined
          :rules="[rules.required, rules.password]"
        ></v-text-field>

        <v-text-field
          v-model="password_1"
          v-else
          label="Nueva contraseña"
          outlined
          type="password"
          :rules="[rules.required, rules.password]"
        ></v-text-field>

        <v-text-field
          v-model="password_2"
          v-if="showPassword"
          outlined
          label="Repetir nueva contraseña"
          :rules="[rules.required, rules.confirmPassword]"
        ></v-text-field>
        <v-text-field
          v-model="password_2"
          v-else
          outlined
          label="Repetir nueva contraseña"
          type="password"
          :rules="[rules.required, rules.confirmPassword]"
        ></v-text-field>
        <p class="mb-6 success--text">{{message}}</p>
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
        color="info"
        class="white--text py-6"
        :disabled="!valid"
        @click="changePassword"
      >
        Guardar cambios
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
      old_password: "",
      password_1: "",
      password_2: "",
      message: "",
      error_message: "",
      rules: {
        password: (v) =>
          v.length >= 8 ||
          `Contraseña demasiada corta, te faltan ${8 - v.length} caracteres`,
        confirmPassword: (v) =>
          v == this.password_1 || "Las contraseñas no coinciden.",
        required: (v) => !!v || "Este campo es requerido",
      },
    };
  },
  methods: {
    async changePassword() {
      this.error_message = "";
      this.message = "";
      let data = {
        'old_password': this.old_password,
        'new_password': this.password_1,
      };
      try {
        await UserDataService.change_password(
        this.$store.state.id,
        data
      );
      this.message = "Contraseña cambiada exitosamente";
      } catch (error) {
        if(error.response.status == 400){
          this.error_message = "La contraseña actual es incorrecta, por favor intentelo de nuevo";
        }
      }
    },
  },
};
</script>
