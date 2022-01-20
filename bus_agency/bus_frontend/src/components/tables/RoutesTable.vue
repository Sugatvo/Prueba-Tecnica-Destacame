<template>
  <v-card class="mt-auto mb-auto">
    <v-simple-table dense>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">ID</th>
            <th class="text-left">Ciudad de origen</th>
            <th class="text-left">Ciudad de destino</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in routes" :key="item.id">
            <td>{{item.id}}</td>
            <td>{{item.from_city}}</td>
            <td>{{item.to_city}}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-card>
</template>


<script>
import RouteDataService from "../../services/route.js";

export default {
  data() {
    return {
      routes: [],
    };
  },
  methods: {
    async getRoutes() {
      try {
        let response = await RouteDataService.get_by_city();
        console.log(response);
        this.routes = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getRoutes();
  },
};
</script>