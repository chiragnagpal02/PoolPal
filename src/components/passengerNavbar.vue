<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">

      <!-- logo -->
      <router-link to="/passengerHomepage" class="navbar-brand mx-2 routing">
        <img src="../assets/logo.png" alt="Logo" width="50" height="50" class="d-inline-block align-text-top"> 
      </router-link>

      <!-- nav items -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item">
            <router-link to="/passengerHomepage" class="nav-link routing">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/passengerOffer" class="nav-link routing">Request A Ride</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/passengerRequests" class="nav-link routing">Ride Offers</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/passengerRides" class="nav-link routing">Ride History</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/passengerChats" class="nav-link routing">Chats</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/passengerProfile" class="nav-link routing">Profile</router-link>
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
