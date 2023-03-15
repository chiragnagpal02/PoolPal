<template>   
    <div class="container-fluid d-flex align-items-center justify-content-center" id="identity">
        <div class="whitebox bg-white rounded-4 w-75 d-flex align-items-center justify-content-center">
            <div>
                <div>
                    <h3 class="text-center">Choose your identity:</h3>
                </div>
                <div class="d-flex justify-content-center">
                    <div>
                        <button type="button" class="btn btn-outline-dark w-100 my-3"><router-link to="/login" class="routerlink">Driver</router-link></button>
                        <button type="button" class="btn btn-outline-dark w-100 my-3"><router-link to="/login" class="routerlink">Passenger</router-link></button>
                        <button type="button" class="btn btn-outline-dark w-100 my-3"><router-link to="/login" class="routerlink">Admin</router-link></button>
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
    .routerlink{
        color:black;
        text-decoration: none;
    }
    .whitebox{
        height:500px;
    }
</style>