<template>
    <v-row align="center" justify="center" dense>
        <v-col cols="12" xs="6" sm="5" md="8" lg="6">
            <RegisterForm :state="state"/>
        </v-col>
    </v-row>
</template>

<script>
import RegisterForm from '../components/forms/RegisterForm.vue';

export default {
  name: 'Register',

  components: {
    RegisterForm
  },
  props: ["state"]
};
</script>