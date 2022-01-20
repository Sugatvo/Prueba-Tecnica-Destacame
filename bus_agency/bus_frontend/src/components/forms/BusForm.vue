<template>
  <v-card elevation="2" class="ml-auto mr-auto">
    <v-card-title>Agregar bus</v-card-title>
    <v-card-text>
      <v-form v-model="valid">
        <v-row>
          <v-col cols="12" sm="6" md="6" lg="6">
            <v-checkbox
              v-model="wifi"
              label="Wifi"
              color="red"
              hide-details
            ></v-checkbox>
          </v-col>
          <v-col cols="12" sm="6" md="6" lg="6">
            <v-checkbox
              v-model="usb"
              label="Usb"
              color="indigo"
              hide-details
            ></v-checkbox>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" sm="6" md="6" lg="6">
            <v-checkbox
              v-model="extra_leg_room"
              label="Espacio extra"
              color="orange"
              hide-details
            ></v-checkbox>
          </v-col>
          <v-col cols="12" sm="6" md="6">
            <v-checkbox
              v-model="entertainment"
              label="Entretenimiento"
              color="orange"
              hide-details
            ></v-checkbox>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
    <v-card-actions class="justify-center">
      <v-btn tile color="error" class="white--text py-6" @click="closeModal">
        Cancelar
      </v-btn>
      <v-btn
        tile
        color="success"
        class="white--text py-6"
        :disabled="!valid"
        @click="closeModal"
      >
        Crear
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    valid: false,
    wifi: false,
    usb: false,
    extra_leg_room: false,
    entertainment: false,
  }),
  methods: {
    closeModal() {
      this.$emit("close-modal");
    },
  },
};
</script>