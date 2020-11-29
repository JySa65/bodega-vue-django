<template>
  <div class="accordion-item">
    <h2
      class="accordion-header"
      v-bind:id="'productHeading' + convertToSlug(nameProduct)"
    >
      <div
        role="button"
        class="accordion-button collapsed"
        data-toggle="collapse"
        v-bind:data-target="'#productCollapse' + convertToSlug(nameProduct)"
        aria-expanded="false"
        v-bind:aria-controls="'productCollapse' + convertToSlug(nameProduct)"
      >
        <div class="d-flex flex-row justify-content-between w-100">
          <span>{{ nameProduct}}</span>
          <span class="mr-5">{{ priceProduct }}</span>
        </div>
      </div>
    </h2>
    <div
      v-bind:id="'productCollapse' + convertToSlug(nameProduct)"
      class="accordion-collapse collapse"
      v-bind:aria-labelledby="'productHeading' + convertToSlug(nameProduct)"
      data-parent="#accordionFlushExample"
    >
      <div class="accordion-body">
        <slot name="accordionBody">
        </slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AccordionItem',
  props: {
    nameProduct: String,
    priceProduct: {
      default: 0
    }
  },
  methods: {
    convertToSlug: function (text) {
      return text
        .toLowerCase()
        .replace(/ /g, '-')
        .replace(/[^\w-]+/g, '')
    }
  }
}
</script>
