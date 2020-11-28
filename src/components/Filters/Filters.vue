<template>
  <div class="dropdown">
    <button
      class="btn btn-outline-primary dropdown-toggle"
      type="button"
      :id="'dropdownMenu2' + name"
      data-toggle="dropdown"
      aria-expanded="false"
    >
      {{ name }}
    </button>
    <ul
      class="dropdown-menu"
      :aria-labelledby="'dropdownMenu2' + name"
    >
      <li
        v-for="(item, index) in children"
        :key="index"
      >
        <button
          class="dropdown-item"
          type="button"
        >{{ item }}
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
    children: Array
  }
}
</script>
