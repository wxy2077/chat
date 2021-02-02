
/**
 *
 * 自定义的一些配置信息
 * 调用的时候通过 process.env.NODE_ENV 区分
 * */

export let appConfig = {
    development: {
        baseUrl: 'http://127.0.0.1:8010',                      // 本地开发地址
        WebSocketUrl: 'ws://127.0.0.1:8010/api/chat/v1/ws',   // 开发环境ws接口
    },
    production: {
        baseUrl: 'https://xxx',                                // 线上生产地址
        WebSocketUrl: 'wss://xxx/api/chat/v1/ws',             // 线上ws接口
    },
};
