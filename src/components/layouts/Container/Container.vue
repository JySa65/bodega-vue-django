<template>
  <NavBar />
  <div class="container mt-3">
    <slot></slot>
  </div>
</template>

<script>
import NavBar from '../../NavBar'
export default {
  name: 'ContainerLayout',
  components: {
    NavBar
  }
}
</script>
