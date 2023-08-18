**<h1 style="text-align: center;">Wechat_Mqtt_Doc</h1>**

<br>

<div style="display: flex; justify-content: center;">

  <span style="margin: 0 8px;">
    <a href="https://github.com/GeekFong/Wechat_Mqtt">
      <img src="https://badgen.net/badge/Wechat_Mqtt/v0.1/green" alt="Wechat_Mqtt">
    </a>
  </span>

  <span style="margin: 0 1px;">
    <a href="https://github.com/RichardLitt/standard-readme">
      <img src="https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square" alt="standard-readme">
    </a>
  </span>

  <span style="margin: 0 8px;">
    <a href="https://www.python.org/">
      <img src="https://badgen.net/badge/python/3.8/blue" alt="python">
    </a>
  </span>

  <span style="margin: 0 8px;">
    <a href="https://github.com/mrsanshui/WeChatPYAPI">
      <img src="https://badgen.net/badge/WeChatPYAPI/免费版/blue" alt="python">
    </a>
  </span>

</div>

<br>


[设备mqtt发送数据给微信](##微信发送数据到mqtt)
[微信发送数据到mqtt](##微信发送数据到mqtt)
[测试数据包](##测试数据包)


## 设备mqtt发送数据给微信
消息流程如下：
设备mqtt发送数据 -> mqtt接受端接收到json数据包 -> 服务端微信（就是使用该软件的微信A）根据wx_account或者nick_name发送到对应的微信号

```json
{
    "mqtt_id": "自定义", // 微信返回数据是根据这个字符串
    "wx_account": "", //微信账号
    "nick_name": "", // 微信昵称，自己微信改的名字
    "remark": "", // 发送微信备注的名字，可用此名字作为群发条件
    "timestamp": 16565655, // 时间戳    "talk": {
        "type": 1, // 发送数据的类型：1, 2, 3
        "msg": "test", // 发送的内容
        "card_title": "Hello_Wechat", // 卡片式内容的简短名字
        "card_desc": "Hello", // 卡片式内容的简单描述
        "card_image_url": "www.baidu.com", // 卡片式内容的图片地址（确保是正确的URL）
        "card_link_url": "www.baidu.com", // 卡片式内容的跳转地址（确保是正确的URL）
        "type4Picname":""
    }
}
```



| 字段名          | 值                           | 说明                                                   |   是否需要填    |
|----------------|----------------------------|-------------------------------------------------------|-------------------|
| mqtt_id        | mac地址                    | mqtt发送方设备的MAC地址                                    |    必填        |
| wx_account       |          | 微信账号 |      必填  （wx_account和nick_name）二选一      |
| nick_name      | 自己微信上的名字               | 微信昵称，自己微信改的名字                              |必填  （wx_account和nick_name）二选一        |
| remark         | 做转发的微信备注               | 发送微信备注的名字，可用此名字作为群发条件              |  选填
| timestamp      | 16565655                   | 时间戳                                                 |  必填
| talk.type      | 1                          | 发送数据的类型：1, 2, 3                                 |  必填
| talk.msg       | test                       | 发送的内容                                             |  根据参数选填
| talk.card_title | Hello_Wechat              | 卡片式内容的简短名字                                    |  根据参数选填
| talk.card_desc  | Hello                      | 卡片式内容的简单描述                                    | 根据参数选填
| talk.card_image_url | www.baidu.com         | 卡片式内容的图片地址（确保是正确的URL）                |    根据参数选填
| talk.card_link_url  | www.baidu.com         | 卡片式内容的跳转地址（确保是正确的URL）                |   根据参数选填
| type4Picname  | 图片名字        | 卡片式内容的跳转地址（确保是正确的URL）                |               根据参数选填


- 服务器默认订阅地址为：/WeChatMqtt/Allmsg





## 微信发送数据到其他地方

消息流程如下：

微信端->发送消息->服务器微信A根据上次保存的mqtt_id发送给->mqtt客户端


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
        "card_link_url": "www.baidu.com", // 卡片式内容的跳转地址（确保是正确的URL）
        "type4Picname":""
    }
}
```



## 测试数据包


- **mqtt客户端发送数据包到微信的测试代码，测试代码中填写自己的 mqtt_id , wx_account就可以使用测试了**

1. type：1, 发送文字内容 ，msg为文字消息
  
```json
// wx_account nick_name 这两个其中一个必填
{
    "mqtt_id": "",
    "wx_account": "", 
    "nick_name": "",
    "remark": "",
    "timestamp": 16565655,
    "talk": {
        "type": 1,
        "msg": "test",
        "card_title": "",
        "card_desc": "",
        "card_image_url": "",
        "card_link_url": "",
        "type4Picname":""
    }
}
```

2. type：2, 发送图片内容 ，msg：http上传的路径。（此部分展示没编写。因为需要有自己服务器存放图片，还要开一个http服务，后续回写上）[这里提供图床工具选择](https://zhuanlan.zhihu.com/p/81713842)
```json
{
    "mqtt_id": "",
    "wx_account": "", 
    "nick_name": "",
    "remark": "",
    "timestamp": 16565655,
    "talk": {
        "type": 2,
        "msg": "test",
        "card_title": "",
        "card_desc": "",
        "card_image_url": "",
        "card_link_url": "",
        "type4Picname":""
    }
}
```

1. type：3, 发送卡片 (就是附带http链接的内容) "card_title": "","card_desc": "","card_image_url": "","card_link_url": "",
```json
{
    "mqtt_id": "",
    "wx_account": "", 
    "nick_name": "",
    "remark": "",
    "timestamp": 16565655,
    "talk": {
        "type": 3,
        "msg": "test",
        "card_title": "百度链接",
        "card_desc": "用于测试的百度连接",
        "card_image_url": "https://i.ibb.co/0Vd9d8N/512.jpg",
        "card_link_url": "www.baidu.com",
        "type4Picname":""
    }
}
```

1. type：4, 发送图片，通过图片base64字符串，发送。（发送的速度和服务器的速度有关）
```json
{
    "mqtt_id": "",
    "wx_account": "", 
    "nick_name": "",
    "remark": "",
    "timestamp": 16565655,
    "talk": {
        "type": 4,
        "msg": "test",
        "card_title": "百度链接",
        "card_desc": "用于测试的百度连接",
        "card_image_url": "https://t7.baidu.com/it/u=4198287529,2774471735&fm=193&f=GIF",
        "card_link_url": "www.baidu.com",
        "type4Picname":""
    }
}
```
``` python
# 以下是python mqtt通过base64字符串发送图片的测试代码





```


- 微信发送数据到mqtt客户端，测试代码中填写自己的 mqtt_id , wx_account就可以使用测试了
```



```