<template>
  <passengerNavbar/>
  <router-view/>
</template>

<script>
import passengerNavbar from '@/components/passengerNavbar.vue'
// import driverNavbar from '@/components/driverNavbar.vue'
// import adminNavbar from '@/components/adminNavbar.vue'

export default {
  name: 'app',
  components: {
    passengerNavbar
  }
}
</script>

<style>

</style>
