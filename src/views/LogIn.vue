<template>   
    <div class="container-fluid d-flex align-items-center justify-content-center" id="identity">
        <div class="bg-white rounded-4 w-75 h-75 d-flex align-items-center justify-content-center">
            <div>
                <div>
                    <h3 class="text-center">Log In as ROLE</h3>
                </div>
                <div class="d-flex justify-content-center">
                    <div>
                        <form>
                            <div class="my-2">
                                <label for="exampleInputEmail1" class="form-label">Email Address</label>
                                <input type="email" class="form-control" id="exampleInputEmail1">
                            </div>
                            <div class="my-2">
                                <label for="exampleInputPassword1" class="form-label">Password</label>
                                <input type="password" class="form-control" id="exampleInputPassword1">
                            </div>
                            <button type="submit" class="btn btn-outline-dark w-100 my-2">Submit</button>
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
        padding:10%
    }
</style>