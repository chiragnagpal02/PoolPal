<template>
    <PassengerNavbar/>
     <div class="container-fluid background text-center">
        <div class="row">
            <h3 class="my-3">Upcoming Rides</h3>
        </div>
        <div class="row my-4">
            <div class="card">
                <p class="card-text p-4" style="text-align:left;" >
                    Starting Location: <br>
                    Destination: <br>
                    Date: <br>
                    Time: <br>
                    Driver: <br>
                </p>
            </div>
        </div>

        <div class="row my-4">
            <div class="card">
                <p class="card-text p-4" style="text-align:left;" >
                    Starting Location: <br>
                    Destination: <br>
                    Date: <br>
                    Time: <br>
                    Driver: <br>
                </p>
            </div>
        </div>

        <div class="row my-4">
            <div class="card">
                <p class="card-text p-4" style="text-align:left;" >
                    Starting Location: <br>
                    Destination: <br>
                    Date: <br>
                    Time: <br>
                    Driver: <br>
                </p>
            </div>
        </div>

        <div class="row">
            <h3 class="my-3">Past Rides</h3>
        </div>
        <div class="row my-4">
            <div class="card">
                <p class="card-text p-4" style="text-align:left;" >
                    Starting Location: <br>
                    Destination: <br>
                    Date: <br>
                    Time: <br>
                    Driver: <br>
                </p>
            </div>
        </div>

        <div class="row my-4">
            <div class="card">
                <p class="card-text p-4" style="text-align:left;" >
                    Starting Location: <br>
                    Destination: <br>
                    Date: <br>
                    Time: <br>
                    Driver: <br>
                </p>
            </div>
        </div>

        <div class="row my-4">
            <div class="card">
                <p class="card-text p-4" style="text-align:left;" >
                    Starting Location: <br>
                    Destination: <br>
                    Date: <br>
                    Time: <br>
                    Driver: <br>
                </p>
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
    import PassengerNavbar from '@/components/PassengerNavbar.vue';
</script>



<style scoped>
.background {
  padding: 5% 20% ;
  width:100%;
  height:100%;
  background-color:honeydew;
}
</style>