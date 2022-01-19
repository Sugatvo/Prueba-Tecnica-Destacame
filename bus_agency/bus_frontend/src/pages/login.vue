<template>
  <v-row>
    <v-col cols="12" class="hidden-xs" md="6"></v-col>

    <v-col
      cols="12"
      xs="6"
      sm="5"
      md="6"
      lg="6"
      class="align-self-center d-md-flex"
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