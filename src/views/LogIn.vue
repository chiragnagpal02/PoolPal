<template>   
    <div class="container-fluid d-flex align-items-center justify-content-center" id="image">
        <div class="whitebox bg-white rounded-4 w-75 d-flex align-items-center justify-content-center">
            <div class="w-100">
                <div>
                    <h3 class="text-center">Log In</h3>
                </div>
                <div class="d-flex justify-content-center">
                    <div class="w-75">
                        <form>
                            <div class="my-2">
                                <label for="email" class="form-label">Email Address</label>
                                <input type="email" class="form-control" id="email">
                            </div>
                            <div class="my-2">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" class="form-control" id="password">
                            </div>
                            <div class="my-2">
                                <label for="identity" class="form-label">Identity</label>
                                <select name="identity" class="form-control" id="identity">
                                    <option>Select Identity--</option>
                                    <option value="driver">Driver</option>
                                    <option value="passenger">Passenger</option>
                                    <option value="admin">Admin</option>
                                </select>
                            </div>
                            
                            <button type="submit" class="btn btn-outline-dark mt-3 mb-5 w-100">
                                <router-link to="/driverHomepage" style="color:black; text-decoration:none;">Log In</router-link>
                            </button>
                                
                            <div class="pt-5 text-center">
                                Don't have an account? <router-link to="/signUp">Create new one</router-link>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<style scoped>
    #image{
        position: absolute;
        top: 0;
        left: 0; 
        right: 0;
        bottom: 0;
        background-image: url("../assets/loginSignup.jpg");
        background-repeat: no-repeat;
        padding:10%;
        height: 100%; 
        background-position: center;
        background-size: cover;
    }
    .whitebox{
        height:500px;
    }
</style>