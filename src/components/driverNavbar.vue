<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">

      <!-- logo -->
      <a class="navbar-brand mx-2" href="#">
        <img src="../assets/logo.png" alt="Logo" width="50" height="50" class="d-inline-block align-text-top"> 
      </a>

      <!-- nav items -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Book A Ride</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Ride History</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">Chats</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">Profile</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">Log In</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">Sign Up</a>
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
  }
</style>
