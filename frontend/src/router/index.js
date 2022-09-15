import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue"; // 追記
import HelloWorld from "../components/HelloWorld.vue";
import ElasticSearch from "../components/ElasticSearch.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/hello-world",
    name: "HelloWorld",
    component: HelloWorld,
  },
  {
    path: "/es-demo",
    name: "ElasticSearch",
    component: ElasticSearch,
  },
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
