<template>
  <ContainerLayout>
    <h2 class="mb-4">
      Precio Dolar
      <b>{{ formatNumber({ amount:priceUsdSell, symbolUsd: true }) }}</b>
    </h2>
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
        :priceProduct="formatNumber({amount: getPrice(getLastPrice(product?.price_set)?.price_sell), symbolBs: true})"
      >
        <template v-slot:accordionBody>
          <div class="row align-items-center">
            <div
              class="input-group col-sm-4"
              style="width:unset;"
            >
              <span class="input-group-text">Cantidad</span>
              <input
                type="number"
                aria-label="First name"
                class="form-control col-sm-2"
                style="width: 80px;"
                v-model="quantity[index] "
              >
              <span class="input-group-text">Total: {{ getTotalQuantityUsd(index) }}</span>
              <span class="input-group-text">Total Bs: {{ getTotalQuantityBS(index) }}</span>
            </div>
          </div>
        </template>
      </AccordionItem>
    </div>
  </ContainerLayout>
</template>

<script>
import Numeral from 'numeral'
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
      valueInput: '',
      priceUsdSell: 1083000.0,
      quantity: []
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
      return this._getProducts()
    },
    valueInput: async function () {
      return this._getProducts()
    }
  },
  methods: {
    _getProducts: async function () {
      const { data } = await getProducts(`category=${this.filterValue}&product=${this.valueInput.toUpperCase()}`)
      this.products = data?.results
    },
    getLastPrice: function (prices) {
      prices = prices.sort(
        (a, b) => new Date(b.created_at.replace(' ', 'T')) - new Date(a.created_at.replace(' ', 'T'))
      )
      return prices[0]
    },
    getPrice: function (price) {
      return Numeral(this.priceUsdSell || 0)
        .multiply(price || 0)
        .value()
    },
    formatNumber: function ({ amount, symbolUsd = false, symbolBs = false }) {
      if (symbolBs) {
        return `${Numeral(amount || 0).format('0,0.00')} Bs`
      }
      if (symbolUsd) {
        return Numeral(amount || 0).format('$ 0,0.00')
      }
      return Numeral(amount || 0).format('0,0.00')
    }
  },
  created: async function () {
    const [categories, products] = await Promise.allSettled([getCategories(), getProducts()])
    this.categories = categories?.value?.data?.results
    this.products = products?.value?.data?.results
  },
  computed: {
    getTotalQuantityUsd: function () {
      return function (index) {
        const price = this.getLastPrice(this.products[index]?.price_set)?.price_sell || 0
        return this.formatNumber({
          amount: Numeral(this.quantity[index] || 0)
            .multiply(price)
            .value(),
          symbolUsd: true
        })
      }
    },
    getTotalQuantityBS: function () {
      return function (index) {
        const price = this.getLastPrice(this.products[index]?.price_set)?.price_sell || 0
        return this.formatNumber({
          amount: Numeral(this.quantity[index] || 0)
            .multiply(price)
            .multiply(this.priceUsdSell)
            .value(),
          symbolBs: true
        })
      }
    }
  }
}
</script>
