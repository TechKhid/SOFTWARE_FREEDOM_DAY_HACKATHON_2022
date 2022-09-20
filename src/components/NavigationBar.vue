
<template>
  <div class="nav">
    <h1 style="color:whitesmoke;width:max-content center">Weather Detection-AI  <span>(HACKTHON 2022)</span></h1>
   
  </div>
  <div class="container" style="background-color:black">
 <ul>
  <li>
  <router-link  active-class="active" to="/" t>Upload Image</router-link> </li>
  <li>
  <router-link  active-class="active" to="/about">Live Stream</router-link>
</li>
 </ul>
  </div>
    
</template>

<script>
export default {

}
</script>

<style scoped>

  .nav{
    width: 100% !important;;
   
  background-color: black;
  padding-top: 20px;
  padding-bottom: 20px;
  }
  ul li
  {
    list-style: none;
  }
  ul li a
  {
    margin: 0;
   
    float:left;
    padding: 30px 60px;
    background-color: orange;
    color: #000;
    
  }
  a{
    color: #000;
    text-decoration: none;
  }
ul li a:hover{
  color: white!important;
  background-color: #000;
}
.active{
  color: white!important;
  background-color: #000;
}
 
</style>