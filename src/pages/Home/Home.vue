<template>
  <ContainerLayout>
    <h2 class="mb-4">Precio Dolar $: <b>450,000.00</b></h2>
    <div class="row align-items-center mt-4 mb-4">
      <div class="col-md-1 col-xs-12 col-sm-12">
        <label class="col-form-label">
          Filtros:
        </label>
      </div>
      <div class="col-md-11 col-xs-12 col-sm-12">
        <Filters
          name="Categorias"
          :children="categories"
          @filtervalue="filterValue=$event"
        />
      </div>
    </div>
    <SearchProduct @datainput="valueInput=$event" />
    <div
      class="accordion accordion-flush"
      id="accordionFlushExample"
    >
      <AccordionItem
        v-for="(product, index) in products"
        :key="index"
        :nameProduct="product.name"
        priceProduct="400"
      ></AccordionItem>
    </div>
  </ContainerLayout>
</template>

<script>
import ContainerLayout from '../../components/layouts/Container'
import AccordionItem from '../../components/AccordionItem'
import SearchProduct from '../../components/SearchProduct'
import Filters from '../../components/Filters'

import { getCategories, getProducts } from '../../data/APIInterface'
export default {
  name: 'Home',
  data: () => {
    return {
      products: [],
      categories: [],
      filterValue: '',
      valueInput: ''
    }
  },
  components: {
    ContainerLayout,
    AccordionItem,
    SearchProduct,
    Filters
  },
  watch: {
    filterValue: async function () {
      const { data } = await getProducts(`category=${this.filterValue}&product=${this.valueInput}`)
      this.products = data
    },
    valueInput: async function () {
      const { data } = await getProducts(`category=${this.filterValue}&product=${this.valueInput}`)
      this.products = data
    }
  },
  created: async function () {
    const [categories, products] = await Promise.allSettled([getCategories(), getProducts()])
    this.categories = categories?.value?.data
    this.products = products?.value?.data
  }
}
</script>
