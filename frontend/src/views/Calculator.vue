<template>
  <div>
    <div>
      <h2>Calculadora de ICMS</h2>
      <div class="row">
        <div class="column">
          <div>
            Selecionar -
            <b-form-select
              class="m-md-2"
              text="ICMS"
              :options="taxes"
              v-model="select"
            />
          </div>
          <b-table
            style="margin-top: 2%"
            striped
            hover
            :fields="fields"
            :items="products"
          >
            <template v-if="products.length == 0" #table-caption
              >Insira um produto na aba de Produtos e Impostos.</template
            >
            <template #cell(Selecionar)="product">
              <input
                type="checkbox"
                :id="product.item.id"
                :value="product.item"
                v-model="selectedProducts"
              />
            </template>
          </b-table>
        </div>
        <div class="column">
          <h3>Resultado</h3>
          <b-list-group style="margin-top: 4%">
            <b-list-group-item
              >Valor bruto - R${{ raw_value }}</b-list-group-item
            >
            <b-list-group-item
              >Valor com impostos - R${{ total_value }}</b-list-group-item
            >
            <b-list-group-item>
              Produtos - {{ responseProducts.toString() }}
            </b-list-group-item>
            <b-list-group-item> Valor ICMS - {{ select }}% </b-list-group-item>
          </b-list-group>
          <div style="margin-top: 5%">
            <b-button size="lg" @click="saveCalculator()" class="mr-1"
              >Calcular</b-button
            >
          </div>
        </div>
      </div>
    </div>
    <div style="margin-top: 5%">
      <h2>Histórico</h2>
      <b-table
        style="margin-top: 2%"
        striped
        hover
        :fields="historicFields"
        :items="historic"
        label-sort-asc="Clique para ordenar"
        label-sort-desc="Clique para ordenar"
        label-sort-clear="Clique para ordenar"
      ></b-table>
    </div>
  </div>
</template>

<script>
import { getTaxes } from "../services/taxes.js";
import { getProducts } from "../services/products.js";
import { getCalculator, createCalculator } from "../services/calculator.js";

export default {
  name: "CalculatorPage",
  data() {
    return {
      historic: [],
      raw_value: 0,
      total_value: 0,
      select: 0,
      selectedProducts: [],
      responseProducts: [],
      taxes: [{ value: 0, text: "Estado para Envio" }],
      products: [],
      fields: [
        {
          key: "name",
          label: "Nome do Produto",
        },
        {
          key: "value",
          label: "Valor do Produto",
        },
        {
          key: "Selecionar",
        },
      ],
      historicFields: [
        {
          key: "date",
          label: "Data",
          sortable: true,
        },
        {
          key: "products",
          label: "Produtos",
          sortable: true,
        },
        {
          key: "tax_value",
          label: "Valor ICMS",
          sortable: true,
        },
        {
          key: "raw_value",
          label: "Valor Bruto",
          sortable: true,
        },
        {
          key: "total_value",
          label: "Valor Total",
          sortable: true,
        },
      ],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      getTaxes().then((taxes) => {
        var filtered_taxes = taxes["data"];
        for (var tax in filtered_taxes) {
          this.taxes.push({
            value: filtered_taxes[tax].value,
            text: filtered_taxes[tax].state,
          });
        }
      });
      getProducts().then((products) => {
        var filtered_products = products["data"];
        for (var prod in filtered_products) {
          this.products.push({
            value: filtered_products[prod].value,
            name: filtered_products[prod].name,
          });
        }
      });
      this.fetchCalculator();
    },
    fetchCalculator() {
      getCalculator().then((historic_raw) => {
        this.historic = historic_raw["data"];
        for (var i in this.historic) {
          this.historic[i]["date"] = this.convertDate(this.historic[i]["date"]);
          this.historic[i]["products"] =
            this.historic[i]["products"].toString();
          this.historic[i]["tax_value"] += "%";
          this.historic[i]["raw_value"] = "R$" + this.historic[i]["raw_value"];
          this.historic[i]["total_value"] =
            "R$" + this.historic[i]["total_value"];
        }
      });
    },
    saveCalculator() {
      if (this.selectedProducts.length > 0) {
        var calculator = {
          tax_value: this.select,
          products: this.selectedProducts,
        };
        createCalculator(calculator).then((response) => {
          this.selectedProducts = [];
          this.responseProducts = response["data"].products;
          this.raw_value = response["data"].raw_value;
          this.total_value = response["data"].total_value;

          this.fetchCalculator();
          return;
        });
      }
    },
    convertDate(dateString) {
      var p = dateString.split(/\D/g);
      return [p[2], p[1], p[0]].join("/");
    },
  },
};
</script>

<style scoped>
.column {
  float: left;
  width: 50%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>
