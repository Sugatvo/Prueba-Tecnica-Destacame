<template>
  <v-card class="mt-auto mb-auto">
    <v-alert v-model="showAlert" dense text type="success" dismissible
      >¡El chofer se ha creado exitosamente!</v-alert
    >
    <v-card-title>
      Lista de choferes
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" persistent max-width="600">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="success" outlined dark v-bind="attrs" v-on="on">
            Agregar
          </v-btn>
        </template>
        <DriverForm @close-modal="closeModal" @on-success="onSuccess" />
      </v-dialog>
    </v-card-title>
    <v-simple-table dense>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Nombre de usuario</th>
            <th class="text-left">Nombre</th>
            <th class="text-left">Apellido</th>
            <th class="text-left">Correo</th>
            <th class="text-left">Accciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in drivers" :key="item.id">
            <td>{{ item.username }}</td>
            <td>{{ item.first_name }}</td>
            <td>{{ item.last_name }}</td>
            <td>{{ item.email }}</td>
            <td>
              <v-btn icon>
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-btn icon @click="deleteDriver(item.id)">
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
import DriverDataService from "../../services/driver.js";
import DriverForm from "../forms/DriverForm.vue";

export default {
  components: {
    DriverForm,
  },
  data() {
    return {
      drivers: [],
      show: false,
      dialog: false,
      showAlert: false,
    };
  },
  methods: {
    closeModal() {
      this.dialog = false;
      this.getDrivers();
    },
    onSuccess() {
      this.showAlert = true;
    },
    async getDrivers() {
      try {
        let response = await DriverDataService.get();
        console.log(response);
        this.drivers = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async deleteDriver(id) {
      try {
        let response = await DriverDataService.delete(id);
        console.log(response);
        this.getDrivers();
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getDrivers();
  },
};
</script>