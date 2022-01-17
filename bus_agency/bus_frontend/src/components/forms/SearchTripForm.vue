<template>
  <v-card class="mx-auto" max-width="600" outlined>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-radio-group v-model="row" row>
            <v-radio label="Ida" value="radio-1"></v-radio>
            <v-radio label="Ida y vuelta" value="radio-2"></v-radio>
          </v-radio-group>
        </v-row>
        <v-row>
          <v-select :items="items" label="Ciudad de Origen"></v-select>
        </v-row>
        <v-row>
          <v-select :items="items" label="Ciudad de Destino"></v-select>
        </v-row>
        <v-row>
          <v-col cols="6">
            <v-menu
              ref="departure"
              v-model="departure"
              :close-on-content-click="false"
              :return-value.sync="date"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="dateDeparture"
                  label="Fecha de ida"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="dateDeparture"
                no-title
                scrollable
                :min="dateToday"
              >
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="departure = false">
                  Cancel
                </v-btn>
                <v-btn text color="primary" @click="$refs.departure.save(date)">
                  OK
                </v-btn>
              </v-date-picker>
            </v-menu>
          </v-col>
          <v-col cols="6">
            <v-menu
              ref="arrival"
              v-model="arrival"
              :close-on-content-click="false"
              :return-value.sync="date"
              transition="scale-transition"
              offset-y
              min-width="auto"
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
                no-title
                scrollable
                :min="dateDeparture"
              >
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="arrival = false">
                  Cancel
                </v-btn>
                <v-btn text color="primary" @click="$refs.arrival.save(date)">
                  OK
                </v-btn>
              </v-date-picker>
            </v-menu>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
    <v-card-actions class="pa-0">
      <v-btn block color="blue-grey darken-4" class="white--text py-6"> Buscar viaje </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import TripDataService from "../../services/api.js";

export default {
  data: () => ({
    items: ["Santiago", "Coquimbo", "Algarrobo"],
    valid: false,
    firstname: "",
    lastname: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => v.length <= 10 || "Name must be less than 10 characters",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+/.test(v) || "E-mail must be valid",
    ],
    dateDeparture: new Date(Date.now()).toISOString().substr(0, 10),
    dateArrival: new Date(Date.now()).toISOString().substr(0, 10),
    dateToday: new Date(Date.now()).toISOString().substr(0, 10),
    departure: false,
    arrival: false,
  }),

  methods: {
      async searchTrips(){
          await TripDataService.get()
      }
  },
  mounted(){
      this.searchTrips()
  }
};
</script>