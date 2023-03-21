<template>
    <PassengerNavbar/>
     <div class="container-fluid background">
        <div class="row">
            <h3 class="my-3 text-center">Ride Offers</h3>
        </div>
        <div class="row my-4">
            <div class="card">
                <p class="card-text p-4" style="text-align:left;" >
                    Starting Location: <br>
                    Destination: <br>
                    Date: <br>
                    Time: <br>
                    Driver Name: <br>
                    Price: <br>
                </p>
                <div class="d-flex justify-content-center">
                    <button type="submit" class="btn btn-outline-dark m-4 mt-0 w-100">Accept</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
    name: 'app',
    components: {
        PassengerNavbar
    }
    }
    import PassengerNavbar from '@/components/passengerNavbar.vue';
</script>



<style scoped>
.background {
  padding: 5% 20% ;
  width:100%;
  height:100%;
  background-color:honeydew;
}
</style>