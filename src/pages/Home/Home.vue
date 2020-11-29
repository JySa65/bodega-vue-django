<template>
  <ContainerLayout>
    <div class="row">
      <div class="col-sm-6">
        <h2>Fecha: <time>{{ getDate }}</time></h2>
      </div>
      <div class="col-sm-6">
        <h2>Hora: {{ getTime }}</h2>
      </div>
      <div class="col-sm-6">
        <h3 class="mb-4">
          Precio de Pagina
          <b>{{ formatNumber({ amount: priceUsd?.price_page, symbolBs: true }) }}</b>
        </h3>
      </div>
      <div class="col-sm-6">
        <h3 class="mb-4">
          Precio de Venta
          <b>{{ formatNumber({ amount: priceUsd?.price_sell, symbolBs: true }) }}</b>
        </h3>
      </div>
    </div>
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
        :priceProduct="formatNumber({amount: getPriceSell(getLastPrice(product?.price_set)?.price_sell), symbolBs: true})"
      >
        <template v-slot:accordionBody>
          <div class="row align-items-center">

            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Precio de Compra en Dolares</th>
                  <th scope="col">Precio de Venta en Dolares</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    {{ formatNumber({amount: getLastPrice(product?.price_set)?.price_buy, symbolUsd: true}) }}
                    ({{ formatNumber({amount: getPricePage(getLastPrice(product?.price_set)?.price_buy), symbolBs: true}) }})
                  </td>
                  <td>
                    {{ formatNumber({amount: getLastPrice(product?.price_set)?.price_sell, symbolUsd: true}) }}
                    ({{ formatNumber({amount: getPriceSell(getLastPrice(product?.price_set)?.price_sell), symbolBs: true}) }})
                  </td>
                </tr>
                <tr>
                  <td colspan="2">
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
                      <span class="input-group-text">x {{ formatNumber({amount: priceUsd?.price_page}) }}</span>
                      <span class="input-group-text">Total: {{ getTotalQuantityUsd(index) }}</span>
                      <span class="input-group-text">Total Bs: {{ getTotalQuantityBS(index) }}</span>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </template>
      </AccordionItem>
    </div>
  </ContainerLayout>
</template>

<script>
import Numeral from 'numeral'
import dayjs from 'dayjs'
import ContainerLayout from '../../components/layouts/Container'
import AccordionItem from '../../components/AccordionItem'
import SearchProduct from '../../components/SearchProduct'
import Filters from '../../components/Filters'

import { getCategories, getProducts, getPriceUSD } from '../../data/APIInterface'
export default {
  name: 'Home',
  data: () => {
    return {
      products: [],
      categories: [],
      filterValue: '',
      valueInput: '',
      quantity: [],
      priceUsd: {},
      countUp: new Date(),
      interval: ''
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
    getPricePage: function (price) {
      return Numeral(this.priceUsd?.price_page || 0)
        .multiply(price || 0)
        .value()
    },
    getPriceSell: function (price) {
      return Numeral(this.priceUsd?.price_sell || 0)
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
    const [categories, products, priceUsd] = await Promise.allSettled([getCategories(), getProducts(), getPriceUSD()])
    this.categories = categories?.value?.data?.results
    this.products = products?.value?.data?.results
    this.priceUsd = priceUsd?.value?.data?.results[0]
  },
  mounted: function () {
    this.interval = setInterval(() => {
      this.countUp = new Date()
    })
  },
  computed: {
    getTotalQuantityUsd: function () {
      return function (index) {
        const price = this.getLastPrice(this.products[index]?.price_set)?.price_buy || 0
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
        const price = this.getLastPrice(this.products[index]?.price_set)?.price_buy || 0
        return this.formatNumber({
          amount: Numeral(this.quantity[index] || 0)
            .multiply(price)
            .multiply(this.priceUsd?.price_page)
            .value()
        })
      }
    },
    getDate: function () {
      return dayjs(this.countUp).format('DD-MM-YYYY')
    },
    getTime: function () {
      return dayjs(this.countUp).format('hh:mm:ss a')
    }
  },
  beforeUnmount: function () {
    clearInterval(this.interval)
  }
}
</script>
