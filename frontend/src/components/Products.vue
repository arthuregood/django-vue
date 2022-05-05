<template>
  <div>
    <b-table
      striped
      hover
      :fields="fields"
      :items="products"
      label-sort-asc="Clique para ordenar"
      label-sort-desc="Clique para ordenar"
      label-sort-clear="Clique para ordenar"
    >
      <template #cell(remover)="product">
        <b-button size="sm" @click="removeProduct(product)" class="mr-1">
          <b-icon icon="trash"></b-icon>
        </b-button>
      </template>
    </b-table>
    <b-input-group>
      <b-form-input
        class="m-md-2"
        v-model="product.name"
        placeholder="Nome do Produto"
      ></b-form-input>
      <b-form-input
        class="m-md-2"
        type="number"
        min="0"
        v-model="product.value"
        placeholder="Valor do Produto"
      ></b-form-input>
      <b-button class="m-md-2" variant="success" v-on:click="saveProduct()"
        >Salvar</b-button
      >
    </b-input-group>
  </div>
</template>

<script>
import {
  getProducts,
  createProduct,
  deleteProduct,
} from "../services/products.js";

export default {
  name: "ProductList",
  data() {
    return {
      product: {},
      products: [],
      fields: [
        {
          key: "name",
          label: "Nome do Produto",
          sortable: true,
        },
        {
          key: "value",
          label: "Valor do Produto",
          sortable: true,
        },
        {
          key: "Remover",
        },
      ],
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    fetchProducts() {
      getProducts().then((products) => {
        this.products = products["data"];
        return;
      });
    },
    saveProduct() {
      if (!(this.product.name && this.product.value)) {
        return;
      }
      this.products.push(this.product);
      createProduct(this.product).then(() => {
        this.product = {};
        this.fetchProducts();
        return;
      });
    },
    removeProduct(product) {
      deleteProduct(product.item.id).then(() => {
        this.fetchProducts();
        return;
      });
    },
  },
};
</script>

<style scoped>
</style>
