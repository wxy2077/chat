<template>
    <div class="login">
        <van-nav-bar
                title="登录"
                left-arrow
        />
        <div class="content">
            <van-form @submit="onSubmit">
                <van-field
                        v-model="username"
                        name="user"
                        label="用户名"
                        placeholder="用户名"
                        :rules="[{ required: true, message: '请填写用户名' }]"
                />
                <van-field
                        v-model="password"
                        type="password"
                        name="password"
                        label="密码"
                        placeholder="密码"
                        :rules="[{ required: true, message: '请填写密码' }]"
                />
                <div style="margin: 16px;">
                    <van-button round block type="info" native-type="submit">
                        提交
                    </van-button>
                </div>
            </van-form>
        </div>
    </div>
</template>

<script>
    import {AuthLogin} from '@/api/user'
    export default {
        name: "index",
        data() {
            return {
                username: '',
                password: '',
            }
        },
        created() {
            this.showMenuTab(false)
        },
        destroyed() {
            this.showMenuTab(true)
        },
        methods: {
            // 是否展示底部菜单
            showMenuTab(status) {
                // false 隐藏  true 展示
                this.$store.commit("menuTabShow", status)
            },
            onSubmit() {
                // cookie 和 localStorage 的区别
                // https://stackoverflow.com/questions/3220660/local-storage-vs-cookies
                // 把登录信息存储到 localStorage 中
                AuthLogin({username: this.username, password: this.password}).then(res => {
                    if(res){
                        // 保存
                        localStorage.setItem('authInfo', JSON.stringify({token: res.token}));
                        // 获取用户信息
                        this.$store.dispatch("getUserInfo", res.token);
                        this.$router.push({name: "home"});
                    }
                })
            },
        }
    }
</script>

<style scoped>
    .content {
        margin-top: 100px;
    }

</style>
