<template>
  <div class="accordion-item">
    <h2
      class="accordion-header"
      v-bind:id="'productHeading' + nameProduct"
    >
      <div
        role="button"
        class="accordion-button collapsed"
        data-toggle="collapse"
        v-bind:data-target="'#productCollapse' + nameProduct"
        aria-expanded="false"
        v-bind:aria-controls="'productCollapse' + nameProduct"
      >
        <div class="d-flex flex-row justify-content-between w-100">
          <span>{{ nameProduct}}</span>
          <span class="mr-5">{{ priceProduct }}</span>
        </div>
      </div>
    </h2>
    <div
      v-bind:id="'productCollapse' + nameProduct"
      class="accordion-collapse collapse"
      v-bind:aria-labelledby="'productHeading' + nameProduct"
      data-parent="#accordionFlushExample"
    >
      <div class="accordion-body">
        Todavia no se que va aqui.
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AccordionItem',
  props: {
    nameProduct: String,
    priceProduct: String
  }
}
</script>
