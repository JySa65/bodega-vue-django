<template>
  <div class="row g-3 align-items-center mb-3">
    <div class="col-md-2 col-xs-12 col-sm-12">
      <label
        for="idSeacrhProduct"
        class="col-form-label"
      >Buscar Producto:
      </label>
    </div>
    <div class="col-md-10 col-xs-12 col-sm-12">
      <input
        type="search"
        class="form-control"
        placeholder="Ejemplo: Harina"
        aria-label="Recipient's username"
        aria-describedby="button-addon2"
        name="q"
        autocomplete="off"
        v-model="dataInput"
        @input="getDataInput"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchProduct',
  data: function () {
    return {
      dataInput: ''
    }
  },
  methods: {
    getDataInput: function () {
      this.$emit('datainput', this.dataInput)
    }
  }
}
</script>
