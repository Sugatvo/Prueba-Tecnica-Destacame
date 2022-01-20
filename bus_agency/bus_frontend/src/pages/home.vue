<template>
  <v-row>
    <v-col class="hidden-sm-and-down align-self-center" md="6">
      <v-card elevation="0" max-width="500" class="ml-auto">
        <h1 class="font-weigh-bold text-center">
          Sea cual sea tu destino,<br />
          puedes encontrarlo en <br />
          Destacame Bus
        </h1>
        <v-row class="mt-4" justify="center">
          <v-icon color="amber">mdi-star</v-icon>
          <v-icon color="amber">mdi-star</v-icon>
          <v-icon color="amber">mdi-star</v-icon>
          <v-icon color="amber">mdi-star</v-icon>
          <v-icon color="amber">mdi-star-half</v-icon>
        </v-row>
      </v-card>
    </v-col>
    <v-col class="pt-16 pb-16" cols="12" xs="12" sm="12" md="6" lg="6">
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
};
</script>
