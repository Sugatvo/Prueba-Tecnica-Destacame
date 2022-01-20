<template>
  <v-card class="mt-auto mb-auto">
    <v-alert v-model="showAlert" dense text type="success" dismissible
      >¡El bus se ha creado exitosamente!</v-alert
    >
    <v-card-title>
      Lista de buses
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" persistent max-width="600">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="success" outlined dark v-bind="attrs" v-on="on">
            Agregar
          </v-btn>
        </template>
        <BusForm @close-modal="closeModal" @on-success="onSuccess" />
      </v-dialog>
    </v-card-title>
    <v-simple-table dense>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">ID</th>
            <th class="text-left">Chofer</th>
            <th class="text-center">Wifi</th>
            <th class="text-center">Usb</th>
            <th class="text-center">Espacio extra</th>
            <th class="text-center">Entretenimiento</th>
            <th class="text-left">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in buses" :key="item.id">
            <td>
              {{ item.id }}
            </td>
            <td>
              <span v-if="item.driver">{{ item.driver }}</span>
              <span v-else>Sin chofer</span>
            </td>

            <td class="text-center">
              <v-icon v-if="item.wifi" color="success">mdi-check</v-icon>
              <v-icon v-else color="error">mdi-close</v-icon>
            </td>
            <td class="text-center">
              <v-icon v-if="item.q" color="success">mdi-check</v-icon>
              <v-icon v-else color="error">mdi-close</v-icon>
            </td>
            <td class="text-center">
              <v-icon v-if="item.extra_leg_room" color="success"
                >mdi-check</v-icon
              >
              <v-icon v-else color="error">mdi-close</v-icon>
            </td>
            <td class="text-center">
              <v-icon v-if="item.entertainment" color="success"
                >mdi-check</v-icon
              >
              <v-icon v-else color="error">mdi-close</v-icon>
            </td>
            <td>
              <v-btn icon>
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-btn icon @click="deleteBus(item.id)">
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-card>
</template>

<script>
import BusDataService from "../../services/bus.js";
import BusForm from "../forms/BusForm.vue";

export default {
  components: {
    BusForm,
  },
  data() {
    return {
      buses: [],
      dialog: false,
      showAlert: false,
    };
  },
  methods: {
    closeModal() {
      this.dialog = false;
      this.getBuses();
    },
    onSuccess() {
      this.showAlert = true;
    },
    async getBuses() {
      try {
        let response = await BusDataService.get();
        console.log(response);
        this.buses = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getBuses();
  },
};
</script>