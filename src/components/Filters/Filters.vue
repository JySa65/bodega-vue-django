<template>
  <div
    class="dropdown"
    id="filterDropdown"
  >
    <button
      class="btn btn-outline-primary dropdown-toggle"
      type="button"
      :id="'dropdownMenu2' + name"
      data-toggle="dropdown"
      aria-expanded="false"
    >
      {{ valueSelect || name  }}
    </button>
    <ul
      class="dropdown-menu"
      :aria-labelledby="'dropdownMenu2' + name"
    >
      <template v-if="addSearch && children.length > 0">
        <li>
          <input
            type="search"
            class="form-control dropdown-item"
            placeholder="Buscar en Categoria"
            v-model="inputSearch"
            style="box-shadow: unset;"
          >
        </li>
        <li>
          <hr class="dropdown-divider">
        </li>
      </template>
      <li v-if="inputSearch === ''">
        <button
          class="dropdown-item"
          type="button"
          @click="setValueSelect('')"
        >
          Seleccionar
        </button>
      </li>
      <li
        v-for="(item, index) in searchCategory"
        :key="index"
      >
        <button
          :class="valueSelect === searchCategory[index]?.name ? 'dropdown-item active' : 'dropdown-item'"
          type="button"
          @click="setValueSelect(searchCategory[index]?.name)"
        >
          {{ item.name  }}
        </button>
      </li>
      <li v-if="children.length <= 0">
        <button
          class="dropdown-item"
          type="button"
        >
          No hay categorias
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Filters',
  props: {
    name: String,
    children: Array,
    addSearch: {
      type: Boolean,
      default: true
    }
  },
  data: function () {
    return {
      inputSearch: '',
      valueSelect: ''
    }
  },
  methods: {
    setValueSelect: function (value) {
      this.$emit('filtervalue', value)
      this.valueSelect = value
      this.inputSearch = ''
    }
  },
  computed: {
    searchCategory: function () {
      return this.children.filter((item) => item.name.toLowerCase().includes(this.inputSearch.toLowerCase()))
    }
  }
}
</script>
