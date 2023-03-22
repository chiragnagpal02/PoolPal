<template>
    <DriverNavbar/>
     <div class="container-fluid background">
        <!-- earnings -->
        <div class="row">
            <h3 class="my-3 text-center">Earnings Summary</h3>
        </div>
        <div class="row my-4">
            <div class="col p-0">
                <div class="container p-4 bg-white rounded-3 border">
                    <p class="fw-bold">Total Earnings</p>
                    <h4>$ xxx</h4>
                </div>
            </div>
            <div style="width:30px"></div>
            <div class="col p-0">
                <div class="container p-4 bg-white rounded-3 border">
                    <p class="fw-bold">Number of Rides Completed</p>
                    <h4>500</h4>
                </div>
            </div>
        </div>

        <div class="row my-4">
            <div class="col p-0">
                <div class="container p-4 bg-white rounded-3 border text-center">
                    <p class="fw-bold">Average Earnings Per Ride</p>
                    <h2>$ xxx</h2>
                </div>
            </div>
        </div>

        <!-- upcoming -->
        <div class="row">
            <h3 class="my-3 text-center">Upcoming Rides</h3>
        </div>
        <div class="row my-4">
            <div class="card">
                <p class="card-text px-2 py-4" style="text-align:left;" >
                    Carpool ID: <br>
                    Starting Location: <br>
                    Destination: <br>
                    Date: <br>
                    Time: <br>
                    Passenger Name: <br>
                    Price: <br>                    
                </p>
            </div>
        </div>

        <!-- past -->
        <div class="row">
            <h3 class="my-3 text-center">Past Rides</h3>
        </div>
        <div class="row my-4">
            <div class="card">
                <p class="card-text px-2 py-4" style="text-align:left;" >
                    Carpool ID: <br>
                    Starting Location: <br>
                    Destination: <br>
                    Date: <br>
                    Time: <br>
                    Passenger Name: <br>
                    Price: <br>  
                </p>
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
.background {
  padding: 5% 20% ;
  width:100%;
  height:100%;
  background-color:honeydew;
}
</style>