<template>
  <v-card elevation="0" max-width="600" class="ml-auto mr-auto">
    <v-card-title>Perfil de usuario</v-card-title>
    <v-divider></v-divider>
    <v-card-text>
        <v-list>
            <v-list-item>
                Nombre
            </v-list-item>
            <v-list-item>
                Nombre de usuario
            </v-list-item>
            <v-list-item>
                Correo
            </v-list-item>
            <v-list-item>
                Contraseña
            </v-list-item>
        </v-list>
    </v-card-text>
  </v-card>
</template>

<script>
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
      getPassenger(){
          
      }
  },
  props: ["state"],
};
</script>