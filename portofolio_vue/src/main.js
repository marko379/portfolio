import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueCookies from 'vue-cookies';
import axios from 'axios'


import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// import 'font-awesome-animation/css/font-awesome-animation.min.css'
library.add(fas,far,fab)

// axios.defaults.baseURL = 'http://127.0.0.1:8000/'
axios.defaults.baseURL = 'https://web-production-6895.up.railway.app/'
createApp(App).use(store).use(router,axios).use(VueCookies).component('font-awesome-icon', FontAwesomeIcon).mount('#app')





// createApp(App).use(store).use(router).mount('#app')
// createApp(App).use(store).use(router,axios).use(VueCookies,VueCropper).component('font-awesome-icon', FontAwesomeIcon).mount('#app')