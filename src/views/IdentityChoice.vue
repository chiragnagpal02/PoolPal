<template>   
    <div class="container-fluid d-flex align-items-center justify-content-center" id="identity">
        <div class="whiteBox">
            <div class="row">
                <h1>Who are you?</h1>
            </div>
            <div class="row">
                <button type="button" class="btn btn-outline-dark">Driver</button>
            </div>
            <div class="row">
                <button type="button" class="btn btn-outline-dark">Passenger</button>
            </div>
            <div class="row">
                <button type="button" class="btn btn-outline-dark">Admin</button>
            </div>
        </div>
    </div>
</template>
  
<script>
// @ is an alias to /src
// import NavBar from '@/components/NavBar.vue'

// export default {
//   name: 'HomeView',
//   components: {
//     NavBar
//   }
// }
</script>
  
<style scoped>
    #identity{
        position: absolute;
        top: 0;
        left: 0; 
        right: 0;
        bottom: 0;
        background-image: url("../assets/background.jpg");
        background-repeat: no-repeat;
        padding:10%
    }
    .whiteBox{
        background-color:white;
        opacity:0.8;
        padding: 10%;
        width:80%;
        height:80%;
        border-radius: 25px;
    }
    .row{
        padding:5%;
    }
    .btn{
        background-color: white;
    }
</style>