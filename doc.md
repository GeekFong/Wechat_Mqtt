[设备mqtt发送数据给微信](##微信发送数据到mqtt)
[微信发送数据到mqtt](##微信发送数据到mqtt)

## 设备mqtt发送数据给微信
```json
{
    "mqtt_id": "mac地址", // 设备的MAC地址
    "wx_account": "", //微信账号
    "nick_name": "", // 微信昵称，自己微信改的名字
    "remark": "", // 发送微信备注的名字，可用此名字作为群发条件
    "timestamp": 16565655, // 时间戳    "talk": {
        "type": 1, // 发送数据的类型：1, 2, 3
        "msg": "test", // 发送的内容
        "card_title": "Hello_Wechat", // 卡片式内容的简短名字
        "card_desc": "Hello", // 卡片式内容的简单描述
        "card_image_url": "www.baidu.com", // 卡片式内容的图片地址（确保是正确的URL）
        "card_link_url": "www.baidu.com" // 卡片式内容的跳转地址（确保是正确的URL）
    }
}
```



| 字段名          | 值                           | 说明                                                   |
|----------------|----------------------------|-------------------------------------------------------|
| mqtt_id        | mac地址                    | mqtt发送方设备的MAC地址                                |                            |
| wx_account       |          | 微信账号 |
| nick_name      | 自己微信上的名字               | 微信昵称，自己微信改的名字                              |
| remark         | 做转发的微信备注               | 发送微信备注的名字，可用此名字作为群发条件              |
| timestamp      | 16565655                   | 时间戳                                                 |
| talk.type      | 1                          | 发送数据的类型：1, 2, 3                                 |
| talk.msg       | test                       | 发送的内容                                             |
| talk.card_title | Hello_Wechat              | 卡片式内容的简短名字                                    |
| talk.card_desc  | Hello                      | 卡片式内容的简单描述                                    |
| talk.card_image_url | www.baidu.com         | 卡片式内容的图片地址（确保是正确的URL）                |
| talk.card_link_url  | www.baidu.com         | 卡片式内容的跳转地址（确保是正确的URL）                |


- 服务器默认订阅地址为：/WeChatMqtt/Allmsg





## 微信发送数据到其他地方
用户聊天界面输入内容：
有两种数据格式：
1. 第一种快速回复
```
    直接输入字符串，默认字符串，会发送到这个人对应的mqtt订阅的mac地址中（客户端必须以自身mac地址作为topic）
```

2. 第二种是多功能模式，不仅能回复，还能回复其他数据
微信只能发送2中数据，一种是文件，一种是图片。但是可以发给不同的人
```json
{
    "my_vxid" : "", //发送方的微信id
    "nick_name": "a卖房", //通过这个名字找到对应的mac地址（可以发送给其他人）
    "nick_name_mac": "a卖房", //对应的mac地址
    "talk": {
        "type": 1, // 发送数据的类型：1, 2
        "msg": "test", // 发送的内容
        "card_title": "Hello_Wechat", // 卡片式内容的简短名字
        "card_desc": "Hello", // 卡片式内容的简单描述
        "card_image_url": "www.baidu.com", // 卡片式内容的图片地址（确保是正确的URL）
        "card_link_url": "www.baidu.com" // 卡片式内容的跳转地址（确保是正确的URL）
    }
}
```