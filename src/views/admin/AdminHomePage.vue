<template>
    <!-- nav bar -->
    <AdminNavbar/>

    <div class="container-fluid" id="image">
        <div class="row my-5">
            <div class="col p-3">
                <div class="container p-4 bg-white rounded-3 border">
                    <p class="fw-bold">Number of Current Disputes</p>
                    <h4>xx</h4>
                </div>
            </div>
            <div style="width:30px"></div>
            <div class="col p-3">
                <div class="container p-4 bg-white rounded-3 border">
                    <p class="fw-bold">Number of Ongoing Carpools</p>
                    <h4>xx</h4>
                </div>
            </div>
        </div>

        <div class="row my-5">
            <div class="col p-3">
                <div class="container p-4 bg-white rounded-3 border text-center">
                    <p class="fw-bold">Number of Upcoming Carpools</p>
                    <h2>xx</h2>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
  name: 'app',
  components: {
      AdminNavbar
  }
  }
  import AdminNavbar from '@/components/adminNavbar.vue';
</script>

<style scoped>
    #image{
        padding: 5% 20% ;
        width:100%;
        height:100%;
        background-image: url("../../assets/homepage.jpg");
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
    }
</style>