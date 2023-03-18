<template>
  <!-- nav bar -->
  <PassengerNavbar/>

  <div class="background container-fluid d-flex align-items-center justify-content-center">
    <div class="student-profile py-4">
      <div class="card shadow-sm">
        <div class="card-header bg-transparent text-center">
          <img class="profile_img" src="../../assets/profile.jpg">
          <h3>Name</h3>
        </div>
        <div class="card-body d-flex align-items-center justify-content-center">
          <table class="table">
            <tr>
              <th width="40%">Age</th>
              <td width="2%">:</td>
              <td>age</td>
            </tr>
            <tr>
              <th width="40%">Gender</th>
              <td width="2%">:</td>
              <td>m/f</td>
            </tr>
            <tr>
              <th width="40%">Email</th>
              <td width="5%">:</td>
              <td>xx@gmail.com</td>
            </tr>
            <tr>
              <th width="40%">Address</th>
              <td width="2%">:</td>
              <td>xxx</td>
            </tr>
            <tr>
              <th width="40%">Phone Number</th>
              <td width="2%">:</td>
              <td>xxx</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
  name: 'app',
  components: {
    PassengerNavbar
  }
  }
  import PassengerNavbar from '@/components/PassengerNavbar.vue';
</script>

<style scoped>
.background {
  padding: 5% 20% ;
  width:100%;
  height:100%;
  background-repeat: no-repeat;
  background-image: url('../../assets/homepage.jpg');
  height: 100%; 
  background-position: center;
  background-size: cover;
}
.student-profile .card {
    border-radius: 10px;
}
.student-profile .profile_img {
    width: 50%;
    object-fit: cover;
    margin: 10px auto;
    border: 5px solid #ccc;
    border-radius: 50%;
    aspect-ratio: 1/1;
}
.student-profile .card h3 {
    font-size: 20px;
    font-weight: 700;
}
.student-profile .table th,
.student-profile .table td {
    padding: 5px 10px;
}
</style>