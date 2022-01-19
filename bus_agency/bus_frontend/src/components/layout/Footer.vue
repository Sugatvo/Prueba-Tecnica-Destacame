<template>
  <v-footer color="secondary pt-4 mt-auto" paddles>
    <v-container class="pb-4">
      <v-row>
        <v-col cols="12" lg="4">
          <router-link to="/" tag="span" style="cursor: pointer">
            <v-img
              class="ml-auto mr-auto"
              max-height="64"
              max-width="250"
              src="@/assets/destacame_bus_logo_blank.svg"
              alt="Destacame Bus Logo"
              contain
            ></v-img>
          </router-link>
        </v-col>
        <v-col cols="12" lg="4">
          <ul class="text-footer">
            <li>
              <p><strong>DESTÁCAME BUS</strong></p>
            </li>
            <li><router-link to="/" tag="a" class="router-link">
              Reservar pasajes
            </router-link></li>
            <li><router-link to="/login" tag="a" class="router-link">
              Iniciar sesión
            </router-link> </li>
            <li><router-link to="/register" tag="a" class="router-link">
              Regístrate
            </router-link></li>
          </ul>
        </v-col>
        <v-col cols="12" lg="4">
          <ul class="text-footer">
            <li>
              <p><strong>SÍGUENOS EN:</strong></p>
            </li>
            <v-btn
            v-for="icon in icons"
            :key="icon"
            class="footer-icon mx-4 white--text"
            icon
          >
            <v-icon size="24px">
              {{ icon }}
            </v-icon>
          </v-btn>
          </ul> 
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    icons: ["mdi-facebook", "mdi-twitter", "mdi-linkedin", "mdi-instagram"],
  }),
};
</script>

<style scoped>
ul {
  list-style: none;
  margin-top: 0;
  margin-bottom: 1rem;
  width: fit-content;
  margin: auto;
}

a {
  text-decoration: none;
  background-color: transparent;
}

div > ul > li > p {
  font-size: 16px;
  color: #fff;
}

ul.text-footer li a {
  color: #fff;
  opacity: 0.7;
  line-height: 2.3;
  font-size: 14px !important;
  cursor: pointer;
}

ul.text-footer li a:hover {
    opacity: .9;
    text-decoration: underline;
}

.footer-icon {
  min-height: 40px;
  min-width: 40px;
  display: inline-block;
  background-color: #464f6b;
  border-radius: 4px;
  color: #fff;
  text-align: center !important;
}
</style>