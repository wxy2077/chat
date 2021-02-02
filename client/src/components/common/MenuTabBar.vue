<template>
    <div class="MenuTabBar" v-show="this.$store.getters.showMenuTab">
        <van-tabbar
                placeholder
                v-model="active"
                @change="changeMenu"
        >
            <van-tabbar-item name="home" icon="home-o">主页</van-tabbar-item>
            <van-tabbar-item name="friends" icon="friends-o">好友</van-tabbar-item>
            <van-tabbar-item name="search" icon="search">发现</van-tabbar-item>
            <van-tabbar-item name="setting" icon="setting-o">设置</van-tabbar-item>
        </van-tabbar>
    </div>
</template>

<script>
    export default {
        name: "MenuTabBar",
        data() {
            return {
                active: this.$store.getters.currentMenuTab,
            }
        },
        methods: {
            changeMenu(active){
                window.console.log('当前激活', active)
            }
        }
    }
</script>

<style scoped>

</style>
