
import requests from '@/utils/requests'

// 获取首页信息
export function AuthLogin(data) {
    return requests(
        '/auth/login',
        'post',
        data
    )
}

// 获取用户信息
export function UserInfo() {
    return requests(
        '/user/info',
        'get',
    )
}

// 获取好友列表
export function FriendsList() {
    return requests(
        '/friends/list',
        'get',
    )
}
