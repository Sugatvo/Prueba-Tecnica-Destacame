<template>
    <v-row align="center" justify="center">
      <SearchTripForm></SearchTripForm>
    </v-row>
</template>

<script>
import SearchTripForm from '../components/forms/SearchTripForm.vue';

export default {
  name: 'Home',

  components: {
    SearchTripForm
  },
  props: ['state']
};
</script>
