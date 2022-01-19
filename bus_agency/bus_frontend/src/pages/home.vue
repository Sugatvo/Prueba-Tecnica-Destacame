<template>
  <v-row>
    <v-col class="hidden-xs align-self-center" md="6" >
      <h1 class="font-weigh-bold text-center">Sea cual sea tu destino,<br> puedes encontrarlo en <br> Destacame Bus</h1>
      <v-row class="mt-4" justify="center" dense>
        <v-icon color="amber">mdi-star</v-icon>
        <v-icon color="amber">mdi-star</v-icon>
        <v-icon color="amber">mdi-star</v-icon>
        <v-icon color="amber">mdi-star</v-icon>
        <v-icon color="amber">mdi-star-half</v-icon>
      </v-row>
    </v-col>
    <v-col
      cols="12"
      xs="6"
      sm="5"
      md="6"
      lg="6"
      class="align-self-center"
    >
      <SearchTripForm />
    </v-col>
  </v-row>
</template>

<script>
import SearchTripForm from "../components/forms/SearchTripForm.vue";

export default {
  name: "Home",

  components: {
    SearchTripForm,
  },
  props: ["state"],
};
</script>
