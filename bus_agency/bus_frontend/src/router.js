import Vue from "vue";
import Router from "vue-router";
import Home from "./pages/home";
import Login from "./pages/login";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      alias: "/home",
      name: "home",
      component: Home
    },
    {
      path: "/login",
      alias: "/login",
      name: "login",
      component: Login
    },
  ]
});