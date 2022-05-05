import Vue from 'vue'
import VueRouter from 'vue-router'

import AddonsPage from '../views/Addons.vue'
import CalculatorPage from '../views/Calculator.vue'
import LoginPage from '../views/Login.vue'
import RegisterPage from '../views/Register.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'calculator',
        component: CalculatorPage,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/produtos-impostos',
        name: 'addons',
        component: AddonsPage,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    },
    {
        path: '/register',
        name: 'register',
        component: RegisterPage
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})
//couldn't make this code work in my notebook
//but in my computed it worked xD
// anyway, I intended to check every redirect for authenticity 
/* 
import store from '../store/index.js'

router.beforeEach((to, from, next) => {
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (localStorage.getItem("token") == null) {
            next({
                path: "/login",
                params: { nextUrl: to.fullPath },
            });
        } else {
            if (!store.state.isAuthenticated) {
                next({
                    path: "/login",
                    params: { nextUrl: to.fullPath },
                });
            } else {
                next();
            }
        }
    } else {
        next();
    }
}); */

export default router
