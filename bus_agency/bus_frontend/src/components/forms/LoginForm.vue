<template>
  <v-card elevation="0" max-width="500" class="ml-auto mr-auto">
    <router-link to="/" name="Destacame Bus" title="Destacame Bus">
      <v-img src="@/assets/logo.svg" alt="Destacame Bus Logo" contain max-height="20vh" class="mb-xs-4 mb-md-8 lg-mb-8 mb-xl-8">
      </v-img>
    </router-link>
    <v-card-text>
      <v-form>
        <v-text-field
          label="Enter you email"
          name="Email"
          prepend-inner-icon="mdi-mail"
          type="email"
          class="rounded-0"
          outlined
          tile
        ></v-text-field>
        <v-text-field
          label="Enter your password"
          name="password"
          prepend-inner-icon="mdi-lock"
          type="password"
          outlined
          tile
        >
        </v-text-field>
        <v-card-actions class="text--secondary">
          <v-spacer></v-spacer>
          ¿No tienes una cuenta? <router-link to="/" class="pl-2" color="black">Registrate acá</router-link>
        </v-card-actions>
        <v-btn class="rounded-0" color="black" x-large block dark>Login</v-btn>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
export default {};
</script>