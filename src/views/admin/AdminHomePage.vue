<template>
    <!-- nav bar -->
    <AdminNavbar/>
    
    
</template>

<script>
  export default {
  name: 'app',
  components: {
      AdminNavbar
  }
  }
  import AdminNavbar from '@/components/AdminNavbar.vue';
</script>

<style scoped>
    #homepageImage{
        padding:20%;
        width:100%;
        height:100%;
        background-repeat: no-repeat;
        background-image: url('../../assets/homepage.jpg');
        height: 100%; 
        background-position: center;
        background-size: cover;
    }
</style>