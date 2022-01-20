<template>
  <v-card class="mt-auto mb-auto">
    <v-simple-table dense>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">ID</th>
            <th class="text-left">Nombre</th>
            <th class="text-left">Dirección</th>
            <th class="text-left">Ciudad</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in stations" :key="item.id">
            <td>{{item.id}}</td>
            <td>{{item.name}}</td>
            <td>{{item.street_address}}</td>
            <td>{{item.city}}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-card>
</template>


<script>
import StationDataService from "../../services/station.js";

export default {
  data() {
    return {
      stations: [],
    };
  },
  methods: {
    async getStations() {
      try {
        let response = await StationDataService.get();
        console.log(response);
        this.stations = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getStations();
  },
};
</script>