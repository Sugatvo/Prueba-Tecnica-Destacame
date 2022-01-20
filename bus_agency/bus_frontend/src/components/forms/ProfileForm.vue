<template>
  <v-card elevation="0">
    <v-card-title>Perfil de usuario</v-card-title>
    <v-divider></v-divider>
    <v-card-text>
      <v-list>
        <v-list-item style="display: block">
          <v-form v-model="validName">
            <v-container>
              <v-row v-if="!editName">
                <v-col cols="12" md="4">
                  <v-text-field
                    v-model="firstname"
                    label="Nombre"
                    readonly
                    filled
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4">
                  <v-text-field
                    v-model="lastname"
                    label="Apellido"
                    readonly
                    filled
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4">
                  <v-btn
                    color="info"
                    rounded
                    min-height="48"
                    @click="editName = !editName"
                    >Editar</v-btn
                  >
                </v-col>
              </v-row>
              <v-row v-else>
                <v-col cols="12" md="4">
                  <v-text-field
                    v-model="firstname"
                    label="Nombre"
                    :rules="[rules.required, rules.firstname]"
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4">
                  <v-text-field
                    v-model="lastname"
                    :rules="[rules.required, rules.lastname]"
                    label="Apellido"
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4">
                  <v-btn
                    class="mx-2"
                    fab
                    small
                    color="success"
                    :disabled="!validName"
                    @click="changeName"
                  >
                    <v-icon dark> mdi-check-bold </v-icon>
                  </v-btn>

                  <v-btn
                    class="mx-2"
                    fab
                    small
                    color="error"
                    @click="cancelEditName"
                  >
                    <v-icon dark> mdi-close </v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-list-item>
        <v-list-item style="display: block">
          <v-form v-model="validUsername">
            <v-container>
              <v-row v-if="!editUsername">
                <v-col cols="12" md="8">
                  <v-text-field
                    v-model="username"
                    label="Nombre de usuario"
                    readonly
                    filled
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-btn
                    color="info"
                    rounded
                    min-height="48"
                    @click="editUsername = !editUsername"
                    >Editar</v-btn
                  >
                </v-col>
              </v-row>
              <v-row v-else>
                <v-col cols="12" md="8">
                  <v-text-field
                    v-model="username"
                    label="Nombre de usuario"
                    :rules="[
                      rules.required,
                      rules.usernameLength,
                      rules.usernamePattern,
                    ]"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-btn
                    class="mx-2"
                    fab
                    small
                    color="success"
                    :disabled="!validUsername"
                    @click="changeUsername"
                  >
                    <v-icon dark> mdi-check-bold </v-icon>
                  </v-btn>
                  <v-btn
                    class="mx-2"
                    fab
                    small
                    color="error"
                    @click="cancelEditUsername"
                  >
                    <v-icon dark> mdi-close </v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-list-item>
        <v-list-item style="display: block">
          <v-form v-model="validEmail">
            <v-container>
              <v-row v-if="!editEmail">
                <v-col cols="12" md="8">
                  <v-text-field
                    v-model="email"
                    label="Correo"
                    filled
                    readonly
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-btn
                    color="info"
                    rounded
                    min-height="48"
                    @click="editEmail = !editEmail"
                  >
                    <span class="pt-3 pb-3"> Editar </span>
                  </v-btn>
                </v-col>
              </v-row>
              <v-row v-else>
                <v-col cols="12" md="8">
                  <v-text-field
                    v-model="email"
                    :rules="[rules.required, rules.email]"
                    label="Correo"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-btn
                    class="mx-2"
                    fab
                    small
                    color="success"
                    :disabled="!validEmail"
                    @click="changeEmail"
                  >
                    <v-icon dark> mdi-check-bold </v-icon>
                  </v-btn>

                  <v-btn
                    class="mx-2"
                    fab
                    small
                    color="error"
                    @click="cancelEditEmail"
                  >
                    <v-icon dark> mdi-close </v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
    </v-card-text>
    <v-card-actions>
      <v-dialog v-model="dialog" persistent max-width="600">
        <template v-slot:activator="{ on, attrs }">
          <v-btn class="ml-auto mr-auto" color="error" outlined rounded v-bind="attrs" v-on="on">
            Borrar cuenta
          </v-btn>
        </template>
        <v-card>
          <v-card-title class="text-h5 justify-center">
            ¿Estas seguro que deseas borrar tu cuenta?
          </v-card-title>
          <v-card-actions class="justify-center">
            <v-btn color="error" outlined @click="dialog = false">
              no
            </v-btn>
            <v-btn color="success" outlined @click="deleteAccount">
              Si
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card-actions>
  </v-card>
</template>



<script>
import PassengerDataService from "../../services/passenger.js";

export default {
  data: () => ({
    dialog: false,
    editName: false,
    editUsername: false,
    editEmail: false,
    validName: false,
    validUsername: false,
    validEmail: false,
    firstname: "",
    firstname_aux: "",
    lastname: "",
    lastname_aux: "",
    username: "",
    username_aux: "",
    email: "",
    email_aux: "",
    rules: {
      firstname: (v) => {
        const pattern = /^[a-zA-Z]+$/;
        return pattern.test(v) || "El nombre debe contener unicamente letras";
      },
      lastname: (v) => {
        const pattern = /^[a-zA-Z]+$/;
        return pattern.test(v) || "El apellido debe contener unicamente letras";
      },
      usernameLength: (v) =>
        v.length <= 150 ||
        "El nombre de usuario debe contener 150 caracteres o menos",
      usernamePattern: (v) => {
        const pattern = /^[a-zA-Z0-9@.-_]+$/;
        return (
          pattern.test(v) ||
          "El nombre de usuario solo puede contener letras, digitos y @/./-/_"
        );
      },
      required: (v) => !!v || "Este campo es requerido",
      email: (v) => {
        const pattern =
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return pattern.test(v) || "Correo no válido";
      },
    },
  }),
  methods: {
    cancelEditName() {
      this.editName = false;
      this.firstname = this.firstname_aux;
      this.lastname = this.lastname_aux;
    },
    cancelEditUsername() {
      this.editUsername = false;
      this.username = this.username_aux;
    },
    cancelEditEmail() {
      this.editEmail = false;
      this.email = this.email_aux;
    },
    async getPassenger() {
      let response = await PassengerDataService.get(this.$store.state.id);
      this.firstname = response.data.first_name;
      this.firstname_aux = response.data.first_name;
      this.lastname = response.data.last_name;
      this.lastname_aux = response.data.last_name;
      this.username = response.data.username;
      this.username_aux = response.data.username;
      this.email = response.data.email;
      this.email_aux = response.data.email;
    },

    async changeName() {
      this.editName = false;
      let data = {
        first_name: this.firstname,
        last_name: this.lastname,
      };
      await PassengerDataService.patch(this.$store.state.id, data);
      this.getPassenger();
    },
    async changeUsername() {
      this.editUsername = false;
      let data = {
        username: this.username,
      };
      await PassengerDataService.patch(this.$store.state.id, data);
      this.$store.state.username = this.username;
      this.getPassenger();
    },
    async changeEmail() {
      this.editEmail = false;
      let data = {
        email: this.email,
      };
      await PassengerDataService.patch(this.$store.state.id, data);
      this.getPassenger();
    },
    async deleteAccount(){
        await PassengerDataService.delete(this.$store.state.id);
        this.$store.state.isAuthenticated = false;
        this.$store.state.username = "";
        this.$store.state.id = "";
        this.$router.push("/login");
    }
  },
  mounted() {
    this.getPassenger();
  },
};
</script>
