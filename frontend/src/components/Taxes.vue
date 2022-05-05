<template>
  <div>
    <b-table
      striped
      hover
      :fields="fields"
      :items="taxes"
      label-sort-asc="Clique para ordenar"
      label-sort-desc="Clique para ordenar"
      label-sort-clear="Clique para ordenar"
    >
      <template #cell(remover)="tax">
        <b-button size="sm" @click="removeTax(tax)" class="mr-1">
          <b-icon icon="trash"></b-icon>
        </b-button>
      </template>
    </b-table>
    <b-input-group>
      <b-form-input
        class="m-md-2"
        v-model="tax.state"
        placeholder="Estado"
      ></b-form-input>
      <b-form-input
        class="m-md-2"
        type="number"
        min="0"
        v-model="tax.value"
        placeholder="Valor do ICMS"
      ></b-form-input>
      <b-button class="m-md-2" variant="success" v-on:click="saveTax()"
        >Salvar</b-button
      >
    </b-input-group>
  </div>
</template>

<script>
import { getTaxes, createTax, deleteTax } from "../services/taxes.js";

export default {
  name: "TaxList",
  data() {
    return {
      tax: {},
      taxes: [],
      fields: [
        {
          key: "state",
          label: "Estado",
          sortable: true,
        },
        {
          key: "value",
          label: "Valor do ICMS",
          sortable: true,
        },
        {
          key: "Remover",
        },
      ],
    };
  },
  mounted() {
    this.fetchTaxes();
  },
  methods: {
    fetchTaxes() {
      getTaxes().then((taxes) => {
        this.taxes = taxes["data"];
        return;
      });
    },
    saveTax() {
      if (!(this.tax.state && this.tax.value)) {
        return;
      }
      this.taxes.push(this.tax);
      createTax(this.tax);
      this.tax = {};
      return;
    },
    removeTax(tax) {
      deleteTax(tax.item.id).then(() => {
        this.fetchTaxes();
        return;
      });
    },
  },
};
</script>

<style scoped>
</style>
