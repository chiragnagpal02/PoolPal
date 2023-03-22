//vue
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// bootstrap
import "bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"

// axios
import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:8080/api",
  headers: {
    "Content-type": "application/json"
  }
});

createApp(App).use(router).mount('#app')
