<template>
    <div>
        <div>
          <h2>Cadastro de Produtos</h2>
          <product-list/>
        </div>
        <div style="margin-top:5%">
          <h2>Cadastro de Impostos</h2>
          <tax-list/>
        </div>
    </div>
</template>

<script>
import ProductList from "../components/Products.vue"
import TaxList from "../components/Taxes.vue"

export default {
  name: 'AddonsPage',
  components: {
    ProductList,
    TaxList
  },
  mounted(){
  }
}
</script>

<style scoped>

</style>
