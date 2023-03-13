<template>   
    <div class="container-fluid d-flex align-items-center justify-content-center" id="identity">
        <div class="bg-white opacity-75 rounded-4 w-75 h-75 d-flex align-items-center justify-content-center">
            <div>
                <div>
                    <h2 class="text-center">Who are you?</h2>
                </div>
                <div class="d-flex justify-content-center">
                    <div>
                        <button type="button" class="btn btn-outline-dark w-100 my-3">Driver</button>
                        <button type="button" class="btn btn-outline-dark w-100 my-3">Passenger</button>
                        <button type="button" class="btn btn-outline-dark w-100 my-3">Admin</button>
                    </div>
                </div>
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
</style>