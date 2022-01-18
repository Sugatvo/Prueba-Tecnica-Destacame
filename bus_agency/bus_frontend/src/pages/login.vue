<template>
    <v-row align="center" justify="center" dense>
        <v-col cols="12" xs="6" sm="5" md="8" lg="6">
            <LoginForm :state="state"/>
        </v-col>
    </v-row>
</template>

<script>
import LoginForm from '../components/forms/LoginForm.vue';

export default {
  name: 'Login',

  components: {
    LoginForm
  },
  props: ['state']
};
</script>