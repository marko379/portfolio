<template>

<div v-show="showMsg" class="msg">
  <h1 class="has-text-weight-bold is-family-sans-serif title is-2 has-text-black">Email sent</h1>
</div>

<div v-if="errors.length" class="msg-error">
  <h1 class="has-text-weight-bold title is-4">FAILED</h1>
  <h1 class="has-text-weight-bold title is-5" v-for="error in errors" v-bind:key="error">{{ error }}</h1>
</div>

<div class="container">

  <!-- to show project videos -->
  <div v-for="item in Article">
    <div class="modal" :ref="`${item.slug}`">
      <div class="modal-background"></div>
      <div class="modal-card modal-card-project">
        <header class="modal-card-head">
          <p class="modal-card-title">{{ item.name }}</p>
          <button class="delete is-large" aria-label="close" @click="projectOff(item.slug)"></button>
        </header>
        <section class="modal-card-body">
          <video controls class="video">
            <source :src="item.video_path" type="video/mp4">
            <source :src="item.video_path" type="video/ogg">
          </video> 
        </section>
        <footer class="modal-card-foot">
          <p>this is description</p>
        </footer>
      </div>
    </div>
  </div>

  <!-- to show video about me -->
  <div class="modal" ref="aboutMeModal">
    <div class="modal-background"></div>
    <div class="modal-card modal-card-about-me">
      <header class="modal-card-head">
        <p class="modal-card-title">1 min read</p>
        <button class="delete" aria-label="close" @click="closeModalAboutMe"></button>
      </header>
      <section class="modal-card-body">
        <div class="photo-about-me">
          <img :src="require('../assets/img/profile.jpg')"/>
        </div>
        <div class="resume-about-me">
            <p style="color:black;" class="about-me-paragraf-hello">Hello everyone</p>
            <p style="color:black;" class="about-me-paragraf">I am Marko. I have l ived and worekd in UK since 2019.
            The purpose of this portfolio is to show my knowledge of programming and the projects I have made</p>
            <p style="color:black;" class="about-me-paragraf">All my projects are available online and can be used right now.
            To access the projects(web-pages) click the link below the project image.</p>
            <p style="color:black;" class="about-me-paragraf">Also you can find here video clips of my projects so that you can see exactly what each project is about and that you can see all the features of the project. To start the video clip just click on the image of the project.</p>
            <p style="color:black;" class="about-me-paragraf">If you would like to see a source code of the projects then click a link on menu bar(links).
            My resume is also available.</p>
            <p style="color:black;" class="about-me-paragraf">I have experience with Python Java Script Vue js Django Css Sql Git Html and some other technologies. </p>
            <p style="color:black;" class="about-me-paragraf">I am open to learning new technologies, I am hardworking, honest and a team player.</p>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button" @click="closeModalAboutMe">Cancel</button>
      </footer>
    </div>
  </div>



  <div class="main-div">

      <font-awesome-icon icon="fa-solid fa-bars" @click="showHelpNavBar" v-show="bar" ref="bar" class="bars" size="4x" fade/>
      <font-awesome-icon icon="fa-solid fa-square-xmark" @click="showXmark" v-show="varXmark" ref="xmark" class="x-mark" size="4x"/>
    <div class="section-1" ref="art1">

      <div class="proffesion">
        <h1 class="has-text-weight-bold is-family-sans-serif title is-2 has-text-white">Portofolio</h1>
      </div>

      <div class="details">

        <div class="name-place">

          <div class="name">
            <h2 class="has-text-weight-bold is-family-sans-serif title is-3 has-text-white">Marko Gojkovic</h2>
          </div>


          <div class="place">
            <h2 class="has-text-weight-bold is-family-sans-serif title is-3 has-text-white has-text-centered">About me</h2>
            <p> Bellow you will find projects I’ve delivered that showcase my skills and general 
                background in develpoing software.         
            </p>
            <p>If you wanna know more about me:</p>
            <p style="text-decoration: underline; cursor: pointer;" @click="aboutMe">Click me</p>
          </div>

        </div>

        <div class="skils-portofolio">
          <div class="portofolio">
            <h2 class="has-text-weight-bold is-family-sans-serif title is-3 has-text-white">Software Developer</h2>
          </div>


          <div class="skills">
            <h2 class="has-text-weight-bold is-family-sans-serif title is-3 has-text-white">Skills</h2>
            <p class="mt-2">Python</p>
            <p class="mt-2">Java Script</p>
            <p class="mt-2">Vue js</p>
            <p class="mt-2">Django</p>
            <p class="mt-2">Css</p>
            <p class="mt-2">Sql</p>
            <p class="mt-2">Git</p>
            <p class="mt-2">Html</p>
          </div>
        </div>

      </div>
    </div>


    <div class="section-2" ref="art2">
      <div class="proffesion">
        <h1 class="has-text-weight-bold is-family-sans-serif title is-2 has-text-white">Projects</h1>
      </div>


      <div class="section-2-details">
        <p>Click on the project to discover more</p>
      </div>

      <div class="projects-div">
        <div class="image" v-for="item in Article" @click="showProject(item.slug)">
          <img :src="item.image_path" alt="">
        </div>
      </div>
    </div>

    <div class="section-3" ref="art3">
      <div class="proffesion">
        <h1 class="has-text-weight-bold is-family-sans-serif title is-2 has-text-white">Links</h1>
      </div>

      <div class="github">

        <div class="cv">
          <a href="https://github.com/marko379/e_commerce"><h2 class="has-text-weight-bold <!-- is-family-sans-serif title is-4">
          <font-awesome-icon icon="fa-regular fa-file-pdf" /> My resume</h2></a>
        </div>

        <div class="github-link">
          <a href="https://github.com/marko379/e_commerce"><h2 class="has-text-weight-bold <!-- is-family-sans-serif title is-4">
          <font-awesome-icon icon="fa-brands fa-github" /> Link to my github</h2></a>
        </div>

        <div class="github-source-code">
          <div class="github-title">
            <h2 class="has-text-weight-bold is-family-sans-serif title is-4 has-text-white"><font-awesome-icon icon="fa-solid fa-gear" /> My projects source code</h2>
          </div>

          <a href="https://github.com/marko379/e_commerce" class="a-link"><h2 class="has-text-weight-bold <!-- is-family-sans-serif title is-4">
          <font-awesome-icon icon="fa-brands fa-github" /> Online Book Store</h2></a>

          <a href="https://github.com/marko379/e_commerce" class="a-link"><h2 class="has-text-weight-bold <!-- is-family-sans-serif title is-4">
          <font-awesome-icon icon="fa-brands fa-github" /> Snake Game</h2></a>

          <a href="https://github.com/marko379/e_commerce" class="a-link"><h2 class="has-text-weight-bold <!-- is-family-sans-serif title is-4">
          <font-awesome-icon icon="fa-brands fa-github" /> To-Do App</h2></a>

          <a href="https://github.com/marko379/e_commerce" class="a-link"><h2 class="has-text-weight-bold <!-- is-family-sans-serif title is-4">
          <font-awesome-icon icon="fa-brands fa-github" /> Weather app</h2></a>
        </div>
      </div>
    </div>

    <div class="section-4" ref="art4">
      <div class="proffesion">
        <h1 class="has-text-weight-bold is-family-sans-serif title is-2 has-text-white">Contact</h1>
      </div>

      <div class="maps-and-contact">

        <div class="container-contact">
           <h2 class="has-text-weight-bold is-family-sans-serif title is-4 h2-blue"><font-awesome-icon icon="fa-regular fa-envelope"/> contact by email</h2>
          <form @submit.prevent="sendEmail" ref="form">
            <input 
              type="text" 
              v-model="name"
              name="name"
              placeholder="Your name"
            >
            <input 
              type="email" 
              v-model="email"
              name="email"
              placeholder="email"
              >
            <textarea
              name="message"
              v-model="message"
              cols="30" rows="5"
              placeholder="Message">
            </textarea>
            <button class="button is-link is-medium" type="submit">Send</button>
          </form>
        </div>

        <div class="google-maps">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1244.639580686609!2d-3.277301010934914!3d51.39792511639933!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x486e05f0e15ac057%3A0x97e31840b06da955!2sBarry%20CF62%205BR%2C%20UK!5e0!3m2!1sen!2shr!4v1690296969950!5m2!1sen!2shr" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>

      </div>

        <div class="contact-num">
         <h2 class="has-text-weight-bold is-family-sans-serif title is-5 has-text-white"><font-awesome-icon icon="fa-solid fa-phone"/> 079 368 78 370</h2>
          <h2 class="has-text-weight-bold is-family-sans-serif title is-5 has-text-white"><font-awesome-icon icon="fa-regular fa-envelope"/> markogojkovic045@gmail.com</h2>
          <h2 class="has-text-weight-bold is-family-sans-serif title is-5 has-text-white"><font-awesome-icon icon="fa-solid fa-location-dot" /> Barry / Wales UK</h2>
        </div>

    </div>

  </div>

    <nav class="navbar" ref="navbar">
      <div class="navbar-item-container">
       <div class="arrow-icon" @click="goto('art1')">
          <div class="abc"><font-awesome-icon icon="fa-solid fa-arrow-right" class="ab" size="2x" fade/></div>
          <div class="nav-item">
             <a class="nav-link" href="#section-1"><span><font-awesome-icon icon="fa-solid fa-user-large" size="2x" 
              class="icon"/></span>About Me</a>
          </div>
        </div>

        <div class="arrow-icon" @click="goto('art2')">
          <font-awesome-icon icon="fa-solid fa-arrow-right" class="ab" size="2x" fade/>
          <div class="nav-item">
            <a class="nav-link" href="#section-2"><span ><font-awesome-icon icon="fa-solid fa-circle-nodes" size="2x" class="icon"/></span>My Projects</a>
          </div>
        </div>

        <div class="arrow-icon" @click="goto('art3')">
          <font-awesome-icon icon="fa-solid fa-arrow-right" class="ab" size="2x" fade/>
          <div class="nav-item">
            <a class="nav-link" href="#section-3"><span ><font-awesome-icon icon="fa-solid fa-file" size="2x" 
              class="icon"/></span>Links</a>
          </div>
        </div>

        <div class="arrow-icon" @click="goto('art4')">
          <font-awesome-icon icon="fa-solid fa-arrow-right" class="ab" size="2x" fade/>
          <div class="nav-item">
            <a class="nav-link" href="#section-4"><span ><font-awesome-icon icon="fa-solid fa-message" size="2x" 
              class="icon"/></span> Contact</a>
          </div>
        </div>
      </div>
    </nav>



</div>
</template>



<style lang="scss">

.container{
  display: flex;
  // border: solid;
  max-width: 1500px;
  width: 100%;
  margin: auto ;
}

.msg{
  // position: sticky;
  background-color: #ccffcc;
  width: 100%;
  margin: auto;
  top:50px;
  text-align: center;
  padding: 55px;
  position: fixed;
  z-index: 77;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  animation-name: homepics;
}

.msg-error{
  // position: sticky;
  background-color: #ff4d4d;
  width: 100%;
  margin: auto;
  top:50px;
  text-align: center;
  padding: 25px;
  position: fixed;
  z-index: 77;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  animation-name: homepics;
}

.main-div{
  // border: solid;
  width: 100%;
  // box-shadow: 0px 9px 30px rgba(255, 149, 5, 0.3);
  -moz-box-shadow: rgba(0, 0, 0, 0.56) 0px 12px 9px 4px;
  -webkit-box-shadow: rgba(0, 0, 0, 0.56) 0px 12px 9px 4px;
  box-shadow: rgba(0, 0, 0, 0.56) 0px 12px 9px 4px;
}









// modal css
.modal-card-about-me{
  max-width: 800px;
  width: 100%;
}

.resume-about-me{
  width: 90%;
  margin: auto;
  text-align: justify;
}

.about-me-paragraf{
  // letter-spacing: 0px;
  font-weight: bold;
  font-size: 18px;
  line-height: 1.30;
  margin-top: 15px;
  background-color: #e6e6e6;
  // padding-top: 5px;
  // padding-bottom: 5px;
  padding: 5PX;
  // box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
}

.about-me-paragraf-hello{
  font-weight: bold;
  font-size: 18px;
  line-height: 1.30;
  margin-top: 15px;
  background-color: #e6e6e6;
  padding: 5PX;
  text-align: center;
}

.modal-card-project{
  max-width: 1400px;
  width: 100%;
}

.delete{
  background-color: red;
}

.bars{
  display: none;
}

.x-mark{
  display: none;
}









.section-1{
  height: 100vh;
  // border:solid red;
  margin: auto;
  background-image: url('~@/assets/img/z20.jpg');
  background-size: cover;
  background-position: center;

}

.details{
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: 100%;

}
.proffesion{
  z-index: 1;
  background-color: rgb(51, 51, 51,0.7);
  // border:solid;
  padding: 17px;
  


}

.skills{
  background-color: rgb(0, 102, 204,0.7);
  margin-top: 80px;
  padding: 30px;
  max-height: 500px;
  // border:solid red;
  width:180px;
  align-self: center;
  



}

.name{
  background-color: rgb(0, 102, 204,0.7);
  // border:solid;
  margin-top: 90px;
  padding: 22px;
  margin-left: 30px;
  max-width: 350px;


}

.portofolio{
  background-color: rgb(0, 102, 204,0.7);
  margin-top: 135px;
  padding: 22px;
  max-width: 350px;
  margin-right: 7px;
  // border:solid;
}

.place{
  background-color: rgb(0, 102, 204,0.7);
  // border:solid;
  text-align: left;
  padding: 10px;
  margin-top: 200px;
  margin-left: 5px;
  min-width: 300px;
  max-width: 500px;
  align-self: end;


}


p{
  color:white;
  font-weight: bold;
  // color: #fff;
  font-size: 20px;
  line-height: 1.50;
}


.skils-portofolio{
  display: flex;
  flex-direction: column; 
  width: 41%;
}



.name-place{
  display: flex;
  flex-direction: column;
  justify-content: left;
  width: 59%;
  // border: solid white;
}












.section-2{

  background-image: url('~@/assets/img/z21.jpg');
  background-size: cover;
  max-height: 100vh;
  min-height: 100vh;
  width: 100%;
}

.projects-div{
  display: flex;
  justify-content: space-evenly;
  // border: solid;

}


.image{
  margin: 150px 3px 3px 3px;
  // border: solid red;
  opacity: 0.95;
  cursor: pointer;
}

.video{
  max-width: 1350px;
  min-height: 320px;
  width: 100%;
}

img{
  border:2px double black;
  max-width: 250px;
  
}

.section-2-details{
  background-color: rgb(51, 51, 51,0.7);
  min-width: 300px;
  width: 450px;
  margin: 50px auto auto auto;
  padding: 20px;
}













.section-3{
  background-image: url('~@/assets/img/z26.jpg');
  background-size: cover;
  background-position: bottom right;
  height: 100vh;
  // border:solid red;
  margin: auto;
}

.github{
  display: flex;
  flex-direction: column;
  width: 100%;
  // border:solid;
}

.github-title{
  margin: auto;
  padding: 20px;
  background-color: rgb(0, 102, 204,0.7);
  width: 100%;
}

.cv{
  padding-top: 20px;
  padding-bottom: 20px;
  // margin-top: 20px;
  // margin-bottom: 20px; 
  background-color: white;
  width: 94%;
  margin: 15px auto 10px auto;
  // border: solid;
  box-shadow: 0 7px 15px 0 rgba(0, 0, 0, .13), 0 1px 4px 0 rgba(0, 0, 0, .11);
}

.github-link{
  padding-top: 20px;
  padding-bottom: 20px;
  // margin-top: 20px;
  // margin-bottom: 20px; 
  background-color: white;
  width: 94%;
  margin: 30px auto auto auto;
  // border: solid red;
  box-shadow: 0 7px 15px 0 rgba(0, 0, 0, .13), 0 1px 4px 0 rgba(0, 0, 0, .11);
}

.a-link{
  // border:solid;
  padding-top: 13px;
  padding-bottom: 13px;
}

.github-source-code{
  display: flex;
  flex-direction: column;
  width: 94%;
  // border: solid;
  margin: 60px auto auto auto;
  background-color: rgb(255, 255, 255);
  box-shadow: 0px -25px 20px -20px rgba(0, 0, 0, 0.45), 0px 25px 20px -20px rgba(0, 0, 0, 0.45);
}

.a-link:hover{
  background-color: rgb(217, 217, 217);
}

.cv:hover{
  background-color: rgb(217, 217, 217);
}

.github-link:hover{
  background-color: rgb(217, 217, 217);
}













.section-4{
  background-image: url('~@/assets/img/z25.jpg');
  background-size: cover;
  background-position: center;
  height: 100vh;

  // background-color:rgb(153, 221, 255);

}


.contact-num{
  background-color: rgb(0, 102, 204,0.7);
  margin: 50px auto auto auto;
  padding: 30px;
  max-width: 500px;

}

.h2-blue{
  color: rgb(0, 136, 204);
}

.maps-and-contact{
  display: flex;
  justify-content: space-between;
  // border: solid blue;
  // color: black;
}

.google-maps{
  padding: 10px;
  width: 100%;

  // border: solid red;

}

iframe{
  background-color: white;
  margin: auto;
  border-radius: 5px;
  // box-shadow: 0 60px 80px rgba(0,0,0,0.60), 0 45px 26px rgba(0,0,0,0.14);
  // width: 300px;
  // height: 300px;
  width: 100%;
  height: 100%;
  box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px;
  // -moz-box-shadow: rgba(0, 0, 0, 0.56) 10px 10px 10px 10px;
  // -webkit-box-shadow: rgba(0, 0, 0, 0.56) 10px 10px 10px 10px;
  // box-shadow: rgba(0, 0, 0, 0.56)10px 10px 10px 10px; 
}



* {box-sizing: border-box;}

.container-contact {
  display: block;
  padding: 10px;
  text-align: center;
  // border-radius: 5px;
  max-width: 450px;
  background-color: white;
  margin-top: 10px;
  margin-left: 10px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;
  // border: solid;

}

label {
  float: left;
}

input[type=text], [type=email], textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 12px;
  resize: vertical;
  font-size:16px;
  font-weight: 900;
  // color: rgb(0, 136, 204);
  letter-spacing: 1px;
  // opacity: 0.1;
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}











// nav bar css
.nav-item{
  font-weight: 900;
  font-size: 18px;
  margin-left: 10px;
  // border:solid;
}

.arrow-icon{
  display: flex;
  color:#e6f0ff;
  // border:solid;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 25px;
  width: 100%;
  cursor: pointer;
}

.arrow-icon:hover{
  background-color: white;
}

.arrow-icon:hover  .ab{
  color: rgb(0, 102, 204,0.7);
}

.arrow-icon:hover a{
  color: rgb(0, 102, 204,0.7);
}

.arrow-icon:hover .icon{
  color: rgb(0, 102, 204,0.7);
}



.icon{
  color:#e6f0ff;
  // margin-top: 20px;
  margin-right: 8px;
  // border:solid red;
}

.navbar{
  background-color: rgb(0, 102, 204,0.7);
  display: flex;
  justify-content: center;
  min-width: 300px;
  margin-left: 30px;
  // border: solid red;
  -moz-box-shadow: rgba(0, 0, 0, 0.56) 0px 12px 9px 4px;
  -webkit-box-shadow: rgba(0, 0, 0, 0.56) 0px 12px 9px 4px;
  box-shadow: rgba(0, 0, 0, 0.56) 0px 12px 9px 4px;
}

.nav-link{
  color:#e6f0ff;
  float: left;

}



.navbar-item-container{
  position: sticky;
  top:0;
  padding-top: 70px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  max-height: 400px;
  width: 100%;
  // border:solid orange;

}









// only for navbar
@media screen and (max-width: 1100px) {

  .navbar {
    display: none;
    background-color: rgb(51, 51, 51,0.9);
    position: fixed;
    right: 0;
    margin-top: 78px;
    height: 100vh;
  }


  .bars{
    display: inline;
    position: fixed;
    z-index: 7;
    color:white;
    right: 4px;
    top:0;
  }

  .x-mark{
    display: inline;
    position: fixed;
    z-index: 7;
    color:white;
    right: 4px;
    top:0;
}

  .proffesion{
    z-index: 1;
    background-color: rgb(51, 51, 51,0.7);
    // border:solid;
    padding: 17px;
    position: sticky;
    top:0;
  }

}












//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// screen smaller then 900px and bigger then 700px

@media screen and (max-width: 900px) {


  // nav bar css
  .nav-item{
    font-weight: 900;
    font-size: 18px;
    margin-left: 10px;
    // border:solid;
  }

  .arrow-icon{
    display: flex;
    color:#e6f0ff;
    // border:solid;
    padding-top: 20px;
    padding-bottom: 20px;
    padding-left: 25px;
    width: 100%;
    cursor: pointer;
  }

  .arrow-icon:hover{
    background-color: white;
  }

  .arrow-icon:hover  .ab{
    color: rgb(0, 102, 204,0.7);
  }

  .arrow-icon:hover a{
    color: rgb(0, 102, 204,0.7);
  }

  .arrow-icon:hover .icon{
    color: rgb(0, 102, 204,0.7);
  }



  .icon{
    color:#e6f0ff;
    // margin-top: 20px;
    margin-right: 8px;
    // border:solid red;
  }

  .navbar {
    display: none;
    background-color: rgb(51, 51, 51,0.9);
    position: fixed;
    right: 0;
    margin-top: 78px;
    height: 100vh;
    }

  .nav-link{
    color:#e6f0ff;
    float: left;

  }



  .navbar-item-container{
    position: sticky;
    top:0;
    padding-top: 70px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    max-height: 400px;
    width: 100%;
    // border:solid orange;

  }

}








//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// screen smaller then 700px and bigger then 

@media screen and (max-width: 700px) {


  .section-4{
    background-image: url('~@/assets/img/z25.jpg');
    background-size: cover;
    background-position: center;
    // height: 100vh;

  }


  .contact-num{
    background-color: rgb(0, 102, 204,0.7);
    margin: 30px auto auto auto;
    padding: 10px;
    max-width: 500px;

  }

  .h2-blue{
    color: rgb(0, 136, 204);
  }

  .maps-and-contact{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
  }

  .google-maps{
   
  }

  iframe{
    
  }

  
  * {box-sizing: border-box;}

  .container-contact {
    display: block;
    padding: 10px;
    text-align: center;
    // border-radius: 5px;
    max-width: 670px;
    width: 100%;
    background-color: white;
    margin: 10px auto auto auto;
    // margin-left: 0px;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;
    // border: solid;
  }

  label {
    float: left;
  }

  input[type=text], [type=email], textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 12px;
    resize: vertical;
    font-size:16px;
    font-weight: 900;
    // color: rgb(0, 136, 204);
    letter-spacing: 1px;
    // opacity: 0.1;
  }

  input[type=submit] {
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  input[type=submit]:hover {
    background-color: #45a049;
  }




  .section-2{

    background-image: url('~@/assets/img/z21.jpg');
    background-size: cover;
    // max-height: 100vh;
    max-height: 100%;
    width: 100%;
  }

  .projects-div{
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    // border: solid;

  }


  .image{
    margin: 20px 3px 3px 3px;
    // border: solid red;
    opacity: 0.95;
    cursor: pointer;
  }

  .video{
    max-width: 1350px;
    min-height: 320px;
    width: 100%;
  }

  img{
    border:2px double black;
    max-width: 250px;
    
  }

  .section-2-details{
    background-color: rgb(0, 102, 204,0.7);
    min-width: 300px;
    width: 100%;
    margin: 10px auto 10px auto;
    padding: 20px;
  }





  .section-1{
    height: 100vh;
    // border:solid red;
    margin: auto;
    background-image: url('~@/assets/img/z20.jpg');
    background-size: cover;
    background-position: center;

  }

  .details{
    display: flex;
    flex-direction: column;
    // justify-content: space-between;
    width: 100%;
    height: 100%;
    // border: solid red;

  }
    


  
  .skills{
    background-color: rgb(0, 102, 204,0.7);
    margin-top: 0px;
    padding: 0px;
    // max-height: 200px;
    // border:solid red;
    max-width: 690px;
    width:100%;
    // align-self: center;

    // background-color: rgb(0, 102, 204,0.7);
    // margin-top: 80px;
    // padding: 30px;
    // max-height: 500px;
    // // border:solid red;
    // width:180px;
    // align-self: center;
    



  }

  .name{
    background-color: rgb(0, 102, 204,0.7);
    // border:solid;
    margin-top: 0px;
    padding: 22px;
    margin-left: 6px;
    max-width: 680px;


  }

  .portofolio{
    display: none;
    // background-color: rgb(0, 102, 204,0.7);
    // margin-top: 5px;
    // padding: 22px;
    // max-width: 500px;
    // width: 100%;
    // margin-right: 0px;
    // border:solid orange;
  }

  .place{
    background-color: rgb(0, 102, 204,0.7);
    // border:solid yellow;
    text-align: left;
    padding: 10px;
    margin-top: 0px;
    margin-left: 5px;
    // min-width: 300px;
    max-width: 680px;
    // align-self: end;


  }


  p{
    color:white;
    font-weight: bold;
    // color: #fff;
    font-size: 20px;
    line-height: 1.50;
  }


  .skils-portofolio{
    display: flex;
    flex-direction: column; 
    // border: solid purple;
    justify-content: start;
    height: 50%;
    width: 100%;
  }



  .name-place{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    height: 50%;
    width: 100%;
    // border: solid white;
  }


  

}

</style>




<script>
// import emailjs from 'Emailjs-com'
import emailjs from '@emailjs/browser';
import axios from 'axios'
export default {
  name: 'HomeView',
  components: {

  },
  data() {
    return {
      varXmark:false,
      bar:true,
      screenWidth: window.innerWidth,
      Article: [],
      name: '',
      email: '',
      message: '',
      from_name:'',
      showMsg: false,
      errors: []

    }
  },

  mounted() {
    this.showArticle(),

    window.addEventListener('resize', () => {
      this.screenWidth = window.innerWidth
      if(this.screenWidth > 1101){
        let navbar = this.$refs['navbar']
        this.bar = true
        navbar.style.display = 'flex'
      }
      if(this.screenWidth < 1101){
        let navbar = this.$refs['navbar']
        this.varXmark = false  
        navbar.style.display = 'none'
      }
    })

  },



  methods: {
      goto(refName) {
          var element = this.$refs[refName];
          var top = element.offsetTop;
          window.scrollTo({
            top: top,
            behavior: "smooth",
          });
      },
      showHelpNavBar(){
        // ref.style.backgroundColor = '#66bb6a';
        let navbar = this.$refs['navbar']
        this.bar = false
        this.varXmark = true  
        navbar.style.display = 'inline'

        
      },
      showXmark(){
        this.varXmark = false
        this.bar = true
        let navbar = this.$refs['navbar']
        navbar.style.display = 'none'
      },

      showArticle(){
        axios.get("projects/").then(response => {console.log(response),this.Article = response.data}).catch(error => {console.log(error)})
      },
      showProject(slug){
        this.$refs[slug][0].classList.add('is-active')
      },
      projectOff(slug){
        this.$refs[slug][0].classList.remove('is-active')
      },

      aboutMe(){
        this.$refs.aboutMeModal.classList.add('is-active')
      },
      closeModalAboutMe(slug){
        this.$refs.aboutMeModal.classList.remove('is-active')
      },
      deleteEmail(){
        this.name = ''
        this.email = ''
        this.message = ''

      },



    sendEmail() {

      if (this.name === '' ){
          this.errors.push('The username is missing')
      }
      if (this.email === '' ){
          this.errors.push('The email is missing')
      }

      if (this.message.length < 20 ){
          this.errors.push('The message is too short, at least 20 charachters')
      }

      if (!this.errors.length){

        emailjs
          .sendForm('service_dc7vrjx', 'template_tje9htf', this.$refs.form, {
            publicKey: 'l25sWdp6lbhiH0kLT',
          })

          .then(

              function(value) { console.log(value) },
              this.deleteEmail(),
              this.showMsg = true,
              setTimeout(() => this.showMsg = false,3000)
            );

      }

      else{
        setTimeout(() => this.errors = [], 3200)
        this.deleteEmail()
      }

    },

  }
}
</script>
