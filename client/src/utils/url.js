/**
 *
 * 封装url路由前缀
 * 后面扩展版本区分 可以更改这里
 * */

import { appConfig } from '@/config'

export default function concatUrl(e) {
    // 区分生产 开发
    let url = `${appConfig[process.env.NODE_ENV].baseUrl}/api/chat/v1${e}`;
    return url;
}
