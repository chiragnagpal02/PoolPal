<template>
    <DriverNavbar/>

    <div class="container-fluid background">
        <!-- back button -->
        <div class="container" >
            <img src="../../assets/backbutton.png" width="30" height="30" style="aspect-ratio:1/1;opacity:65%">
        </div>

        <!-- chat -->
        <div class="container bg-white border border-3 mt-3">
            <!-- receiver -->
            <div class="row text-center">
                <h3 class="py-4">Receiver Name</h3>
                <hr>
            </div>
            <!-- messages -->
            <div class="container message">
                <img src="../../assets/profile.jpg" alt="Avatar">
                <p>Hello. How are you today?</p>
                <span class="time-right">11:00</span>
            </div>

            <div class="container message darker">
                <img src="../../assets/profile.jpg" alt="Avatar" class="right">
                <p>Hey! I'm fine. Thanks for asking!</p>
                <span class="time-left">11:01</span>
            </div>

            <div class="container message">
                <img src="../../assets/profile.jpg" alt="Avatar">
                <p>Sweet! So, what do you wanna do today?</p>
                <span class="time-right">11:02</span>
            </div>

            <div class="container message darker">
                <img src="../../assets/profile.jpg" alt="Avatar" class="right">
                <p>Nah, I dunno. Play soccer.. or learn more coding perhaps?</p>
                <span class="time-left">11:05</span>
            </div>

            <!-- send message -->

            <div class="row my-4">
                <div class="col-10 d-flex justify-content-center align-items-center">
                    <div class="container sendMessage d-flex">
                        <h8 class="my-1">send message....</h8>
                    </div>
                </div>
                <div class="col container d-flex justify-content-center align-items-center">
                    <img src="../../assets/send.png" width="30" height="30" style="opacity:65%;">
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

<style>
    .background {
    padding: 5% 20% ;
    width:100%;
    height:100%;
    background-color:honeydew;
    }
    /* Chat containers */
    .message {
    border: 2px solid #dedede;
    background-color: #f1f1f1;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
    }

    /* Darker chat container */
    .darker {
    border-color: #ccc;
    background-color: #ddd;
    }

    /* Clear floats */
    .message::after {
    content: "";
    clear: both;
    display: table;
    }

    /* Style images */
    .message img {
    float: left;
    max-width: 60px;
    width: 100%;
    margin-right: 20px;
    border-radius: 50%;
    }

    /* Style the right image */
    .message img.right {
    float: right;
    margin-left: 20px;
    margin-right:0;
    }

    /* Style time text */
    .time-right {
    float: right;
    color: #aaa;
    }

    /* Style time text */
    .time-left {
    float: left;
    color: #999;
    }

    .sendMessage{
        border: 2px solid #dedede;
        background-color: #f1f1f1;
        border-radius: 15px;
    }
</style>