<template>
    <div class="index">
        <van-nav-bar
                fixed
                placeholder
                title="聊天客户端"
                right-text="+"
                left-arrow
        />
        <div class="user-list">
            <template v-for="(item,index) in friendList">
                <van-swipe-cell :key="index">
                    <div class="user-item" @click="toChart(item)">
                        <van-image round class="user-item-img" :src="item.avatar"/>
                        <div class="user-item-container">
                            <div class="user-info">
                                <span class="name">{{ item.nickname }}</span>
                                <span class="message">{{ item.userId | lastMessage }}</span>
                            </div>
                            <div class="other-info">
                                <span class="time">{{ item.time }}</span>
                            </div>
                        </div>
                    </div>
                    <template #right>
                        <van-button style="height: 100%" square type="danger" text="删除"/>
                    </template>
                </van-swipe-cell>
            </template>
        </div>
    </div>
</template>

<script>
    import { FriendsList } from '@/api/user'
    export default {
        name: "index",
        data() {
            return {
                // 好友列表
                friendList: [],
                friendMessage: [
                    // {userId: xx, message: xx, time: xx}
                ]
            }
        },
        created() {
            this.initFriends()
            this.receiveMessage()
        },
        mounted() {

        },
        destroyed() {
            this.saveFriends()
        },
        methods: {
            // 初始化朋友圈列表
            initFriends(){
                // 首先获取朋友圈
                let friendsList = localStorage.getItem('friendsList');
                friendsList = JSON.parse(friendsList)
                if(friendsList) {
                    this.friendList = friendsList
                } else{
                    FriendsList().then(res=>{
                        if(res) {
                            this.friendList = res.friendsInfoList
                        }
                    })
                }
            },
            receiveMessage(){
                // 如果没有连接 则重新连接
                if(!this.$ws.ws){
                    this.$ws.connect()
                }
            },
            // 保存对话框好友到localStorage
            saveFriends(){
                localStorage.setItem('friendsList', JSON.stringify(this.friendList));
            },
            // 跳转到聊天详情
            toChart(item) {
                this.$router.push({name: 'chat', params: {userInfo: item}})
            }
        },
        filters: {
            // 取最后一条对话
            lastMessage(friendId) {
                let tempMessageList = JSON.parse(localStorage.getItem(`dialog${friendId}`));
                if(tempMessageList){
                    return tempMessageList[tempMessageList.length-1].message
                }else{
                    return ''
                }
            }
        }
    }
</script>

<style scoped>
    .user-item {
        height: 70px;
        display: flex;
        align-items: center;
        border-bottom: 1px solid #ebedf0;
        position: relative;
    }

    .user-item-img {
        width: 60px;
        height: 60px;
        margin: 10px;
        border-radius: 10px;
    }

    .user-item-container {
        flex: 1;
        display: flex;
    }

    .user-item-container > .user-info {
        display: flex;
        flex-direction: column;
    }
    .user-info > .name{
        position: relative;
        top: -5px;
    }
    .user-info > .message {
        font-size: 14px;
        color: #909497;
    }

    .user-item-container > .other-info {
        margin-left: auto;
        /*background-color: aqua;*/
    }

    .other-info > .time {
        font-size: 14px;
        margin-right: 5px;
    }

</style>
