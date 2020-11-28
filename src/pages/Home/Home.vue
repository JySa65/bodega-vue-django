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
        <Filters name="Categorias" />
      </div>
    </div>
    <SearchProduct />
    <div
      class="accordion accordion-flush"
      id="accordionFlushExample"
    >
      <AccordionItem
        nameProduct="harina"
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
export default {
  name: 'Home',
  components: {
    ContainerLayout,
    AccordionItem,
    SearchProduct,
    Filters
  }
}
</script>
