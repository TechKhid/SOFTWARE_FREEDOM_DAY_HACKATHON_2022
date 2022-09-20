<template>
  <div class="section container">
    <img :src="previewImage" class="uploading-image" />
    <form>

      <input type="file" accept="image/jpeg" @change=uploadImage>
    </form>
    <button :onclick="submit">Detect</button>
    

  <div>
    {{c}}
    </div>
  </div>

</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
export default {
  name: 'HomeView',
  data() {
    return {
      previewImage: "a4a72105d37447734c2b1f36c1049d07.png",
      image :"null",
      c :"",
    }
  },
  components: {
    // /  HelloWorld
  },
  methods: {
    
    uploadImage(e) {
      this.image = e.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(this.image);
      reader.onload = e => {
        this.previewImage = e.target.result;
        console.log(this.previewImage);
      };
    },


    submit() {
      
     
      const formData = new FormData();
      formData.append("files",   this.image);
      // formData.append("file", "this.previewImage");
      axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
      // console.log(formData);
      // let Data={"file":this.previewImage};
      axios.post("http://127.0.0.1:8000/uploadfile/", formData, {
       'Access-Control-Allow-Origin': '*',
       'Content-type': 'application/json',
    })
        .then(function (result) {
          const i =result.data.data;
          if (i)
          {
          
            alert(i);
          }
        console.log();
        }, function (error) {
          console.log(error);
        });
       
    }

  },
  computed: {

  }
}


</script>

<style scoped>
.section {
  padding: 20px;
}



img {

  height: 500px;
  margin: auto;
}
</style>
