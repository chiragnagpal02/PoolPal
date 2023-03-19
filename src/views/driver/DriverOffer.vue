<template>
    <!-- nav bar -->
    <DriverNavbar/>
  
    <div class="background container-fluid d-flex align-items-center justify-content-center">
        <div class="whitebox bg-white rounded-4 w-100 p-4 mt-4 d-flex align-items-center justify-content-center">
            <div class="w-100">
                <div>
                    <h3 class="text-center">Offer a Ride</h3>
                </div>
                <div class="d-flex justify-content-center">
                    <div class="w-75">
                        <form>
                            <!-- start location -->
                            <div class="my-2">
                                <label for="startLocation" class="form-label">Start Location</label>
                                <div class="input-group mb-3">
                                    <input type="text" class="form-control">
                                    <button class="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
                                </div>
                            </div>
                            <!-- end location -->
                            <div class="my-2">
                                <label for="endLocation" class="form-label">End Location</label>
                                <div class="input-group mb-3">
                                    <input type="text" class="form-control" id="endLocation">
                                    <button class="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
                                </div>
                            </div>
                            <!-- date -->
                            <div class="my-2">
                                <label for="date" class="form-label">Date</label>
                                <input id="date" class="form-control" type="date" />
                            </div>
                            <!-- time -->
                            <div class="my-2">
                                <label for="time" class="form-label">Time</label>
                                <input type="time" class="form-control" id="time">
                            </div>
                            <!-- available seats -->
                            <div class="my-2">
                                <label for="availableSeats" class="form-label">Available seats</label>
                                <select id="availableSeats" class="form-select" aria-label="Default select example">
                                    <option value="1" selected> 1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                </select>
                            </div>
                            <!-- price -->
                            <div class="my-2">
                                <label for="price" class="form-label">Price</label>
                                <input type="number" class="form-control" id="price">
                            </div>
                            
                            <button type="submit" class="btn btn-outline-dark my-4 w-100">Book</button>
                            
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
    background-repeat: no-repeat;
    background-image: url('../../assets/forms.jpg');
    height: 100%; 
    background-position: center;
    background-size: cover;
  }
  </style>