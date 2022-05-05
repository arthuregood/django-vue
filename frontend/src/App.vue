<template>
  <div id="app">
    <header-page />
    <router-view id="body" />
  </div>
</template>

<script>
import HeaderPage from "./components/HeaderPage.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    HeaderPage,
  },
  beforeCreate() {
    this.$store.commit("initializeStore");

    const token = this.$store.state.token;

    axios.defaults.headers.common["Authorization"] = "";
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#body {
  margin-top: 5%;
  margin-left: 15%;
  margin-right: 15%;
}
</style>
