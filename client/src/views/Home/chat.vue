<template>
    <div class="chat">
        <van-nav-bar
                fixed
                placeholder
                :title="friend.nickname"
                right-text="+"
                left-arrow
                @click-left="goBack"
        ></van-nav-bar>
        <div class="chat-content">
            <!--<div class="show-time"><span>{{ time }}</span></div>-->

            <template v-for="(item, index) in messageList">
                <chat-item
                        :key="index"
                        :position="item.type"
                        :username="item.type==='left'?friend.nickname:authInfo.nickname"
                        :avatar="item.type==='left'?friend.avatar:authInfo.avatar"
                        :message="item.message"
                />
            </template>

        </div>
        <div class="chat-user-panel">
            <van-field
                    autofocus
                    rows="1"
                    autosize
                    v-model="message"
                    center
                    type="textarea"
                    style="padding: 0 10px; margin: 0 10px; background-color: #F2F3F4"
            >
                <template #button>
                    <van-button
                            @click="sendMessage"
                            size="small"
                            type="primary"
                            style="width: 50px;"
                    >发送</van-button>
                </template>
            </van-field>
        </div>
    </div>
</template>

<script>
    import chatItem from  './childComps/chatItem'
    export default {
        name: "chat",
        components: {
            chatItem
        },
        data() {
            return {
                // 好友信息
                friend: {},
                // 所有消息
                messageList: [],
                message: '',
                authInfo:{}
            }
        },
        created(){
            this.$store.commit("menuTabShow", false);
            // 接收数据
            this.receiveMessage();
            this.fetchUser();
        },
        mounted() {
            this.fetchDialog()
        },
        beforeDestroy () {
            this.saveDialog()
        },
        destroyed() {
            this.$store.commit("menuTabShow", true)
        },
        methods: {
            // 获取传递的用户信息
            fetchUser(){
                // 由于是params传递，刷新当前页面数据会消失，引发报错
                this.friend = this.$route.params.userInfo;
                this.authInfo = this.$store.getters.fetchAuthInfo
            },
            fetchDialog(){
                let tempMessageList = JSON.parse(localStorage.getItem(`dialog${this.$route.params.userInfo.userId}`))
                if(tempMessageList){
                    this.messageList = tempMessageList
                }
            },
            receiveMessage(){
                // 如果没有连接 则重新连接
                // this.$ws.reConnect()
                // 监听回调事件
                this.$ws.ws.onmessage = event =>{
                    let receiveJson = JSON.parse(event.data);
                    window.console.log(this.friend.username, 'this.friend.username')
                    if(receiveJson.username === this.friend.username){
                        this.messageList.push({message: receiveJson.message, type: 'left'})
                    }
                }
                // this.$ws.getMessage = event => {
                //     window.console.log(event, 'liaotjieshou1d')
                // }

            },
            // 发送Json数据
            sendMessage (){
                let token = this.$store.getters.fetchAuthInfo.token
                let message = {
                    message: this.message,
                    token: token,
                    messageType: 1000,
                    toTargetId: this.friend.userId,
                    timestamp: Date.parse(new Date())
                };
                this.$ws.ws.send(JSON.stringify(message));
                this.messageList.push({message: this.message, type: 'right'});
                // 移动高度
                this.message = ''
            },
            // save存储对话
            saveDialog(){
                if(this.messageList.length>0){
                    localStorage.setItem(`dialog${this.friend.userId}`, JSON.stringify(this.messageList));
                }
            },
            // 返回
            goBack() {
                this.$router.go(-1)
            }
        }
    }
</script>

<style scoped>
    .show-time{
        font-size: 13px;
        text-align: center;
        margin: 10px auto;
    }
    .show-time>span{
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 5px;
        background-color: #F8F9F9;
    }
    .chat-content{
        margin-bottom: 55px;
    }
    .chat-user-panel{
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        min-height: 45px;
    }

</style>
