<template>
    <v-row justify="center" class="mb-auto">
        <v-col cols="12" xs="6" sm="5" md="8" lg="6">
            <ProfileForm/>
            <NewPasswordForm/>
        </v-col>
    </v-row>
</template>

<script>
import ProfileForm from '../components/forms/ProfileForm.vue';
import NewPasswordForm from '../components/forms/NewPasswordForm.vue';


export default {
  name: 'Profile',

  components: {
    ProfileForm, 
    NewPasswordForm,
  },
  mounted() {
    if(!this.$store.state.isAuthenticated){
      this.$router.push("/");
    }
  },
};
</script>