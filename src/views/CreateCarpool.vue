<template>   
    <div class="container-fluid d-flex align-items-center justify-content-center" id="identity">
        <div class="whitebox bg-white rounded-4 w-75 d-flex align-items-center justify-content-center">
            <div class="w-100">
                <div>
                    <h3 class="text-center">Create carpool</h3>
                </div>
                <div class="d-flex justify-content-center">
                    <div class="w-75">
                        <form>
                            <div class="my-2">
                                <label for="exampleInputEmail1" class="form-label">Date & Time of Request</label>
                                <input id="startDate" class="form-control" type="date" />
                            </div>
                            <div class="my-2">
                                <label for="exampleInputPassword1" class="form-label">Available seats</label>
                                <!-- <input type="password" class="form-control" id="exampleInputPassword1"> -->

                                <select class="form-select" aria-label="Default select example">
                                    <option value="1" selected> 1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                </select>
                            </div>

                            <div class="my-2">
                                <label for="exampleInputPassword1" class="form-label">Start location</label>
                                <!-- <input type="password" class="form-control" id="exampleInputPassword1"> -->
                                <div class="input-group mb-3">
                                    <input type="text" class="form-control" placeholder="Type here" aria-label="Recipient's username" aria-describedby="button-addon2">
                                    <button class="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
                                </div>
                            </div>
                            <div class="my-2">
                                <label for="exampleInputPassword1" class="form-label">Destination Address</label>
                                <!-- <input type="password" class="form-control" id="exampleInputPassword1"> -->
                                <div class="input-group mb-3">
                                    <input type="text" class="form-control" placeholder="Type here" aria-label="Recipient's username" aria-describedby="button-addon2">
                                    <button class="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
                                </div>
                            </div>

                            <div class="my-2">
                                <label for="exampleInputPassword1" class="form-label">Price</label>
                                <input type="password" class="form-control" id="exampleInputPassword1">
                            </div>
                            
                            <button type="submit" class="btn btn-outline-dark mt-3 mb-5 w-100">Submit</button>
                            
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<style scoped>
    #identity{
        position: absolute;
        top: 0;
        left: 0; 
        right: 0;
        bottom: 0;
        background-image: url("../assets/background.jpg");
        background-repeat: no-repeat;
        padding:10%;
        height: 100%; 
        background-position: center;
        background-size: cover;
    }
    .whitebox{
        height:600px;
    }
</style>