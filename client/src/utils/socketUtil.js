/*
*
* 连接 WebSocket 工具类
*
* 参考链接
* https://stackoverflow.com/questions/46677360/emitting-global-events-from-wset-listener
* https://www.ruanyifeng.com/blog/2017/05/websocket.html
* https://developer.mozilla.org/zh-CN/docs/Web/API/WebSocket
* */

import {appConfig} from '@/config'

// 使用ES6 定义
class WebSocketClass{
    constructor(){
        // 构造方法
        // this.instance = null;
        this.ws = null;
        this.connect()
    }

    // 连接
    connect() {
        let auth_info = localStorage.getItem("authInfo");
        if (auth_info) {
            let auth_info_obj = JSON.parse(auth_info);
            this.ws = new WebSocket(`${appConfig[process.env.NODE_ENV].WebSocketUrl}/${auth_info_obj.token}`);
            // this.ws.onopen = e => {
            //     window.console.log(`连接成功`, e);
            // };

        } else {
            window.console.log("没取到user_info");
        }
    }

    reConnect(){
        /*
        CONNECTING：值为0，表示正在连接。
        OPEN：值为1，表示连接成功，可以通信了。
        CLOSING：值为2，表示连接正在关闭。
        CLOSED：值为3，表示连接已经关闭，或者打开连接失败。
        * */
        if(!this.ws){
            // 如果没有ws实例 则重写连接
            this.connect()
        }
        if(this.ws.readyState !== 1){
            // 如果状态不是open 则重新连接
            this.connect()
        }
    }

    // getMessage() {
    //     this.reConnect();
    //     return this.ws.onmessage
        // this.ws.onmessage = e => {
        //     window.console.log(e.data, '工具类接收到的数据');
        //     return e.data;
        // };
    // }

    // 获取实例
    // static getInstance() {
    //     if (!this.instance) {
    //         this.instance = new WebSocketClass();
    //     }
    //     return this.instance;
    // }

    // heartCheck() {
    //     // 心跳机制的时间可以自己与后端约定
    //     this.pingPong = 'ping'; // ws的心跳机制状态值
    //
    //     this.pingInterval = setInterval(() => {
    //         if (this.ws.readyState === 1) {
    //             // 检查ws为链接状态 才可发送
    //             this.ws.send('ping'); // 客户端发送ping
    //         }
    //     }, 10000);
    //
    //     this.pongInterval = setInterval(() => {
    //         if (this.pingPong === 'ping') {
    //             this.closeHandle('pingPong没有改变为pong'); // 没有返回pong 重启webSocket
    //         }
    //         // 重置为ping 若下一次 ping 发送失败 或者pong返回失败(pingPong不会改成pong)，将重启
    //         window.console.log('返回pong');
    //         this.pingPong = 'ping';
    //     }, 20000);
    // }
    //
    // closeHandle(e = 'err') {
    //     // 因为webSocket并不稳定，规定只能手动关闭(调closeMyself方法)，否则就重连
    //     if (this.status !== 'close') {
    //         window.console.log(`断开，重连websocket`, e);
    //         if (this.pingInterval !== undefined && this.pongInterval !== undefined) {
    //             // 清除定时器
    //             clearInterval(this.pingInterval);
    //             clearInterval(this.pongInterval);
    //         }
    //         this.connect(); // 重连
    //     } else {
    //         window.console.log(`websocket手动关闭,或者正在连接`);
    //     }
    // }

    //
    // close() {
    //     clearInterval(this.pingInterval);
    //     clearInterval(this.pongInterval);
    //     this.status = 'close';
    //     this.ws.send(JSON.stringify({code: 3000, status: 'close'}));
    //     this.ws.close();
    //     window.console.log('close');
    // }
}

export default new WebSocketClass();
