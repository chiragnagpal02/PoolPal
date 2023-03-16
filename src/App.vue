<template>
  <div id="app">
    <div>
      <PassengerNavbar/>
    </div>
    <div>
      <router-view/>
    </div>
  </div>
</template>

<script>
import PassengerNavbar from '@/components/passengerNavbar.vue'
// import DriverNavbar from '@/components/DriverNavbar.vue'
// import AdminNavbar from '@/components/AdminNavbar.vue'

export default {
  name: 'app',
  components: {
    PassengerNavbar
    // DriverNavbar
    // AdminNavbar
  }
}
</script>

<style>

</style>
