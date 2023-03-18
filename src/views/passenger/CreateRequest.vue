<template>
    <!-- nav bar -->
    <PassengerNavbar/>
  
    <div class="background container-fluid d-flex align-items-center justify-content-center">
        <div class="whitebox bg-white rounded-4 w-100 p-4 mt-4 d-flex align-items-center justify-content-center">
            <div class="w-100">
                <div>
                    <h3 class="text-center">Book a Ride</h3>
                </div>
                <div class="d-flex justify-content-center">
                    <div class="w-75">
                        <form>
                            <div class="my-2">
                                <label for="startLocation" class="form-label">From</label>
                                <input type="text" class="form-control" id="startLocation">
                            </div>
                            <div class="my-2">
                                <label for="endLocation" class="form-label">To</label>
                                <input type="text" class="form-control" id="endLocation">
                            </div>
                            <div class="my-2">
                                <label for="date" class="form-label">Date</label>
                                <input type="date" class="form-control" id="date">
                            </div>
                            <div class="my-2">
                                <label for="time" class="form-label">Time</label>
                                <input type="time" class="form-control" id="time">
                            </div>
                            
                            <button type="submit" class="btn btn-outline-dark my-5 w-100">Book</button>
                        </form>
                    </div>
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
    import PassengerNavbar from '@/components/PassengerNavbar.vue';
  </script>
  
  <style scoped>
  .background {
    padding: 5% 20% ;
    width:100%;
    height:100%;
    background-repeat: no-repeat;
    background-image: url('../../assets/forms.jpg');
    height: 100%; 
    background-position: center;
    background-size: cover;
  }
  </style>