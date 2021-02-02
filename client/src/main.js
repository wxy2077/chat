import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import {
    NavBar,
    Tabbar,
    TabbarItem,
    Form,
    Field,
    Button,
    Toast,
    Image as VanImage,
    SwipeCell
} from 'vant';


Vue.use(NavBar);
Vue.use(Tabbar);
Vue.use(TabbarItem);
Vue.use(Form);
Vue.use(Field);
Vue.use(Button);
Vue.use(Toast);
Vue.use(VanImage);
Vue.use(SwipeCell);

Vue.config.productionTip = false


import wsInstance from './utils/socketUtil'

Vue.prototype.$ws = wsInstance;


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
