<template>   
    <div class="container-fluid d-flex align-items-center justify-content-center" id="identity">
        <div class="whitebox bg-white rounded-4 w-75 d-flex align-items-center justify-content-center">
            <div class="w-100">
                <div>
                    <h3 class="text-center">Log In as ROLE</h3>
                </div>
                <div class="d-flex justify-content-center">
                    <div class="w-75">
                        <form>
                            <div class="my-2">
                                <label for="exampleInputEmail1" class="form-label">Email Address</label>
                                <input type="email" class="form-control" id="exampleInputEmail1">
                            </div>
                            <div class="my-2">
                                <label for="exampleInputPassword1" class="form-label">Password</label>
                                <input type="password" class="form-control" id="exampleInputPassword1">
                            </div>
                            
                            <button type="submit" class="btn btn-outline-dark mt-3 mb-5 w-100">Submit</button>
                                
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
    .whitebox{
        height:500px;
    }
</style>