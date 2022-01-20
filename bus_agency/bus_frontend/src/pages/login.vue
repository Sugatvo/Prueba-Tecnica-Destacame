<template>
  <v-row>
    <v-col cols="12" class="hidden-sm-and-down pt-16 pb-16" md="6">
      <v-img
          src="@/assets/chile.svg"
          alt="Mapa de chile"
          max-height="500"
          max-width="300"
          class="ml-auto mr-16"
          contain
        ></v-img>
    </v-col>
    <v-col
      cols="12"
      xs="12"
      sm="12"
      md="6"
      lg="6"
      class="pt-16 pb-16"
    >
      <LoginForm :state="state" />
    </v-col>
  </v-row>
</template>

<script>
import LoginForm from "../components/forms/LoginForm.vue";

export default {
  name: "Login",

  components: {
    LoginForm,
  },
  props: ["state"],
};
</script>