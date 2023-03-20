<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">

      <!-- logo -->
      <router-link to="/driverHomepage" class="navbar-brand mx-2 routing">
        <img src="../assets/logo.png" alt="Logo" width="50" height="50" class="d-inline-block align-text-top"> 
      </router-link>
      
      <!-- nav items -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item">
            <router-link to="/driverHomepage" class="nav-link routing">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/driverOffer" class="nav-link routing">Offer A Ride</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/driverRequests" class="nav-link routing">Ride Request</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/driverRides" class="nav-link routing">Ride History</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/driverChats" class="nav-link routing">Chats</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/driverProfile" class="nav-link routing">Profile</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/" class="nav-link routing">Log In</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/signUp" class="nav-link routing">Sign Up</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
  

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .nav-item{
    margin-inline-end: 30px;
    text-align:center;
    margin-bottom:15px;
  }
  .routing{
    color:black;
    text-decoration: none;
  }
</style>