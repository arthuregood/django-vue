<template>
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item href="/">Calculadora</b-nav-item>
        <b-nav-item href="/produtos-impostos">Produtos e Impostos</b-nav-item>
        <b-button @click="logoutButton">Sair</b-button>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import { logout } from "../services/auth.js";
import axios from "axios";
export default {
  name: "HeaderPage",

  methods: {
    logoutButton() {
      logout().then(() => {
        axios.defaults.headers.common["Authorization"] = "";
        localStorage.removeItem("token");
        this.$store.commit("removeToken");
        this.$router.replace("/login");
      });
    },
  },
};
</script>

<style scoped>
</style>
