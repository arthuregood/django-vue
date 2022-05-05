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
          <label class="d-flex justify-content-between">
            A senha deve conter mais de 8 caracteres e 2 caracteres especiais!
          </label>
        </b-form-group>

        <b-button
          style="margin-top: 2%"
          type="button"
          variant="primary"
          block
          @click="registerButton"
        >
          <i class="fas fa-sign-in-alt"></i> Criar
        </b-button>
      </b-form>
    </div>
  </b-row>
</template>

<script>
import { register } from "../services/auth.js";
export default {
  name: "RegisterPage",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    registerButton() {
      register(this.form).then(() => this.$router.replace("/login"));
    },
  },
};
</script>

