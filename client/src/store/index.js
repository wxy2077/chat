import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import {UserInfo} from '@/api/user'
export default new Vuex.Store({
    state: {
        // 存储个人信息
        authInfo: {},
        // 存储底部菜单栏信息
        menuTab: {
            active: "home",   // 激活栏
            isShow: true,      // 是否展示菜单栏
        }
    },
    mutations: {
        menuTabShow(state, params) {
            state.menuTab.isShow = params;
        },
        // 添加账户信息
        setAuthINfo(state, payload){
            state.authInfo = payload;
        }
    },
    actions: {
        // 获取用户信息
        getUserInfo(context, payload){
            UserInfo().then(res=>{
                let authInfo = res.authInfo;
                authInfo.token = payload;
                // 保存一份到localStorage
                localStorage.setItem('authInfo', JSON.stringify(authInfo));
                context.commit('setAuthINfo', authInfo)
            });
        }
    },
    getters: {
        // 当前菜单激活栏
        currentMenuTab(state) {
            return state.menuTab.active
        },
        // 是展示菜单激活栏
        showMenuTab(state) {
            return state.menuTab.isShow
        },
        // 获取登录自身用户信息
        fetchAuthInfo(state) {
            // 判断state.authInfo是否是空对象
            if (Object.keys(state.authInfo)>0){
                return state.authInfo
            }else{
                let auth_info = JSON.parse(localStorage.getItem("authInfo"));
                // Vue.set(state.authInfo, auth_info)
                return auth_info
            }
        }
    },
    modules: {}
})
