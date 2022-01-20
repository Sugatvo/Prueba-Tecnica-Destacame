<template>
  <v-row justify="center" class="mb-auto">
    <v-col cols="12" md="2" lg="2">
      <v-card elevation="0" class="mx-auto" max-width="300" tile>
        <v-list dense>
          <v-subheader>Tablas</v-subheader>
          <v-list-item-group v-model="selectedItem" color="primary">
            <v-list-item v-for="(item, i) in items" :key="i">
              <v-list-item-icon>
                <v-icon v-text="item.icon"></v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title v-text="item.text"> </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card>
    </v-col>
    <v-col cols="12" md="6" lg="6" class="pt-8">
      <DriversTable v-if="selectedItem == 0" />
      <BusesTable v-if="selectedItem == 1" />
      <StationsTable v-if="selectedItem == 2" />
      <RoutesTable v-if="selectedItem == 3" />
      <TripsTable v-if="selectedItem == 4" />
    </v-col>
  </v-row>
</template>

<script>
import DriversTable from "../components/tables/DriversTable.vue";
import BusesTable from "../components/tables/BusesTable.vue";
import StationsTable from "../components/tables/StationsTable.vue";
import RoutesTable from "../components/tables/RoutesTable.vue";
import TripsTable from "../components/tables/TripsTable.vue";


export default {
  name: "AdminPanel",
  components: {
    DriversTable,
    BusesTable,
    StationsTable,
    RoutesTable,
    TripsTable,
  },
  data: () => ({
    selectedItem: 0,
    items: [
      { text: "Choferes", icon: "mdi-card-account-details-outline" },
      { text: "Buses", icon: "mdi-bus" },
      { text: "Terminales", icon: "mdi-bus-marker" },
      { text: "Trayectos", icon: "mdi-routes" },
      { text: "Viajes", icon: "mdi-bus-clock" },
    ],
  }),
  mounted() {
    if (
      !this.$store.state.isAuthenticated ||
      this.$store.state.role != "Manager"
    ) {
      this.$router.push("/");
    }
  },
};
</script>