<template>
  <v-card
    elevation="2"
    class="rounded-lg ma-lg-0 ma-md-0 ma-sm-auto ma-auto"
    max-width="450"
    outlined
  >
    <v-card-title><h3>Reservar tu pasaje</h3></v-card-title>
    <v-card-subtitle>Nunca fue más rápido y fácil</v-card-subtitle>
    <v-card-text>
      <v-form v-model="valid">
        <v-radio-group
          v-model="isRoundTrip"
          v-on:change="onChangeType"
          mandatory
          class="mt-0"
          row
        >
          <v-radio
            label="Ida"
            v-bind:value="false"
            color="blue-grey darken-4"
          ></v-radio>
          <v-radio
            label="Ida y vuelta"
            v-bind:value="true"
            color="blue-grey darken-4"
          ></v-radio>
        </v-radio-group>
        <v-select
          v-model="selectedDepartureCity"
          :items="departure_cities"
          item-value="from_station"
          item-text="city"
          label="Ciudad de Origen"
          prepend-icon="mdi-map-marker"
          required
          @change="(selection) => selectionChanged(selection)"
        >
          ></v-select
        >
        <v-select
          v-model="selectedArrivalCity"
          :items="arrival_cities"
          item-value="to_station"
          item-text="city"
          label="Ciudad de Destino"
          prepend-icon="mdi-map-marker"
          required
        ></v-select>

        <v-row>
          <v-col cols="12" md="6">
            <v-menu
              v-model="showDeparture"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="dateDeparture"
                  label="Fecha de Ida"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="dateDeparture"
                @input="showDeparture = false"
              ></v-date-picker>
            </v-menu>
          </v-col>
          <v-col cols="12" md="6">
            <v-menu
              v-if="isRoundTrip"
              v-model="showArrival"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="dateArrival"
                  label="Fecha de Regreso"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="dateArrival"
                @input="showArrival = false"
              ></v-date-picker>
            </v-menu>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
    <v-card-actions class="pa-0">
      <v-btn
        block
        color="blue-grey darken-4"
        class="white--text py-6 rounded-b-lg rounded-0"
        @click="getTrips"
      >
        Buscar pasaje
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import TripDataService from "../../services/trip.js";

export default {
  data: () => ({
    selectedDepartureCity: "",
    selectedArrivalCity: "",
    departure_cities: [],
    arrival_cities: [],
    trips: [],
    isRoundTrip: true,
    showDeparture: false,
    showArrival: false,
    valid: false,
    dateDeparture: new Date(Date.now()).toISOString().substr(0, 10),
    dateArrival: new Date(Date.now()).toISOString().substr(0, 10),
    dateToday: new Date(Date.now()).toISOString().substr(0, 10),
  }),

  methods: {
    async getDepartureCities() {
      let response = await TripDataService.get_departure_cities();
      this.departure_cities = response.data;
    },
    async getArrivalCities(id) {
      let response = await TripDataService.get_arrival_cities(id);
      this.arrival_cities = response.data;
    },
    async getTrips() {
      let response = await TripDataService.get_trips(
        this.dateDeparture,
        this.selectedDepartureCity,
        this.selectedArrivalCity
      );
      this.trips = response.data;
    },
    selectionChanged(selection) {
      this.selectedArrivalCity = "";
      this.getArrivalCities(selection);
    },
    onChangeType(selection) {
      console.log(selection);
      console.log(this.isRoundTrip);
    },
  },
  mounted() {
    this.getDepartureCities();
  },
};
</script>