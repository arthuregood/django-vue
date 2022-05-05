<template>
  <b-row class="vh-100 vw-100 row-login">
    <div class="col-8">
      <h2 class="text-center mb-5 title-login">Faça o login</h2>
      <b-form>
        <b-form-group label-for="email">
          <label class="d-flex justify-content-between"> E-mail </label>
          <b-form-input
            id="email"
            type="email"
            placeholder="turivius@email.com"
            autocomplete="off"
            v-model="form.username"
          ></b-form-input>
        </b-form-group>

        <b-form-group label-for="password">
          <label class="d-flex justify-content-between"> Senha </label>
          <b-form-input
            id="password"
            type="password"
            placeholder="Digite sua senha"
            v-model="form.password"
          ></b-form-input>
        </b-form-group>

        <b-button
          style="margin-top: 2%"
          type="button"
          variant="primary"
          block
          @click="loginButton"
        >
          <i class="fas fa-sign-in-alt"></i> Entrar
        </b-button>

        <hr />

        <b-button
          type="button"
          variant="outline-secondary"
          block
          @click="register"
        >
          <i class="fas fa-user-plus"></i> Não tenho conta
        </b-button>
      </b-form>
    </div>
  </b-row>
</template>

<script>
import axios from "axios";
import { login } from "../services/auth.js";
export default {
  name: "LoginPage",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    loginButton() {
      login(this.form)
        .then((response) => {
          const token = response["data"].auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          this.$router.replace("/");
        })
        .catch(() => {
          axios.defaults.headers.common["Authorization"] = "";
          this.$store.commit("removeToken");
        });
    },

    register() {
      this.$router.push({ name: "register" });
    },
  },
};
</script>

