<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">

      <!-- logo -->
      <a class="navbar-brand" href="#">
        <img src="../assets/logo.png" alt="Logo" width="50" height="50" class="d-inline-block align-text-top"> 
      </a>

      <!-- nav items -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Request A Ride</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Offer A Ride</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">Chats</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">Profile</a>
          </li>
        </ul>
      
      </div>
    </div>
  </nav>
</template>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar-right {
  float: right;
}
</style>

