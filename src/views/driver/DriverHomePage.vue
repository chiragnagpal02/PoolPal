<template>
    <!-- nav bar -->
    <DriverNavbar/>
    <!-- the image -->
    <div class="container-fluid d-flex align-items-center justify-content-center" id="homepageImage">
        <div class="text-center">
            <h1 class="text-white" style="font-size:50px">YOUR CARPOOLING MATTERS.</h1>
            <h3 class="text-white">Share the Ride, Save the Planet</h3>
            <button class="btn bg-white mt-5 px-5 py-2 opacity-75"><h5>OFFER A RIDE NOW</h5></button>
        </div>
    </div>

    <!-- the 3 points -->
    <div class="container-fluid">
        <div class="row text-center mt-5 mb-3">
            <h3>How It Works</h3>
        </div>
        <div class="row text-center">
            <div class="col-4 p-3">
                <div>
                    <img src="../../assets/homepageIcons/location.png" width="50" height="50">
                </div>
                <div class="p-3">
                    <p>Choose your start and end locations</p>
                </div>
            </div>
            <div class="col-4 p-3">
                <div>
                    <img src="../../assets/homepageIcons/path.png" width="50" height="50">
                </div>
                <div class="p-3">
                    <p>Offer a ride to another</p>
                </div>
            </div>
            <div class="col-4 p-3">
                <div>
                    <img src="../../assets/homepageIcons/pay.png" width="50" height="50">
                </div>
                <div class="p-3">
                    <p>Earn extra income with ease</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
  name: 'app',
  components: {
    DriverNavbar
  }
  }
  import DriverNavbar from '@/components/DriverNavbar.vue';
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