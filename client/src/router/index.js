import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home/index.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "about" */ '../views/Login/index.vue')
    },
    {
        path: '/chat',
        name: 'chat',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/Home/chat.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
});

// 判断是否登录
router.beforeEach((to, from, next) => {
    let UserInfo = localStorage.getItem('authInfo');

    // 直接访问的登录页面
    if (to.path === "/login") {
        if (UserInfo) {
            next("/");
        } else {
            next();
        }
    } else {
        if (UserInfo) {
            next();
        } else {
            next("/login");
        }
    }
});

export default router
