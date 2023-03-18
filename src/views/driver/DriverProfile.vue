<template>
  <!-- nav bar -->
  <DriverNavbar/>

  <div class="background container-fluid d-flex align-items-center justify-content-center">
    <div class="profile py-4 w-100">
      <div class="card shadow-sm">
        <div class="card-header bg-transparent text-center">
          <img class="profile_img" src="../../assets/profile.jpg">
          <h3>Name</h3>
        </div>
        <div class="card-body d-flex align-items-center justify-content-center">
          <table class="table">
            <tr>
              <th width="49%">Age</th>
              <td width="2%">:</td>
              <td>age</td>
            </tr>
            <tr>
              <th width="49%">Gender</th>
              <td width="2%">:</td>
              <td>m/f</td>
            </tr>
            <tr>
              <th width="49%">Email</th>
              <td width="2%">:</td>
              <td>xx@gmail.com</td>
            </tr>
            <tr>
              <th width="49%">Address</th>
              <td width="2%">:</td>
              <td>xxx</td>
            </tr>
            <tr>
              <th width="49%">Vehicle Number</th>
              <td width="2%">:</td>
              <td>xxx</td>
            </tr>
            <tr>
              <th width="49%">License Number</th>
              <td width="2%">:</td>
              <td>xxx</td>
            </tr>
            <tr>
              <th width="49%">Phone Number</th>
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
    DriverNavbar
  }
  }
  import DriverNavbar from '@/components/DriverNavbar.vue';
</script>

<style scoped>
.background {
  padding: 5% 20% ;
  width:100%;
  height:100%;
  background-repeat: no-repeat;
  background-image: url('../../assets/forms.jpg');
  background-position: center;
  background-size: cover;
}
.profile .card {
    border-radius: 10px;
}
.profile .profile_img {
    width: 200px;
    object-fit: cover;
    margin: 10px auto;
    border: 5px solid #ccc;
    border-radius: 50%;
    aspect-ratio: 1/1;
}
.profile .card h3 {
    font-size: 20px;
    font-weight: 700;
}
.profile .table th,
.profile .table td {
    padding: 5px 10px;
}
</style>