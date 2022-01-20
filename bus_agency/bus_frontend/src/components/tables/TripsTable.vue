<template>
  <v-card class="mt-auto mb-auto">
    <v-simple-table dense>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">ID</th>
            <th class="text-left">Trayecto</th>
            <th class="text-left">Bus</th>
            <th class="text-left">Horario de salida</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in trips" :key="item.id">
            <td>{{item.id}}</td>
            <td>{{item.route}}</td>
            <td>{{item.bus}}</td>
            <td>{{item.departure_time}}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-card>
</template>

<script>
import TripDataService from "../../services/trip.js";

export default {
  data() {
    return {
      trips: [],
    };
  },
  methods: {
    async getTrips() {
      try {
        let response = await TripDataService.get();
        console.log(response);
        this.trips = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getTrips();
  },
};
</script>