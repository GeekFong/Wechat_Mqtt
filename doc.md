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


# **目录**

[1. 协议简单介绍](#协议简单介绍)

[2. 设备mqtt发送数据给微信](#设备mqtt发送数据给微信)

[3. 微信发送数据到其他地方](#微信发送数据到其他地方)

[4. 测试数据包](#测试数据包)



# **协议简单介绍**
![Wechat_Mqtt](./image/Wechat_Mqtt.png)

这是整个程序的设计示意图,mqtt发送端B发送消息后，根据协议默认绑定的就是(wx_account)对应的微信好友B，所以微信好友回复消息时。默认发送的数据也是发送到mqtt发送端B。微信好友如果想发送消息给mqtt发送端C，要提前知道c的mqtt_id.然后再根据协议发送数据。mqtt发送端b如果发送数据给微信好友C,那么微信好友C就默认和mqtt发送端b绑定在一起。微信好友B就会变成没有绑定关系。

因此必须先由mqtt发送端先发起。后续才能正常的交互。

<br>

# **设备mqtt发送数据给微信**
消息流程如下：
设备mqtt发送数据 -> mqtt接受端接收到json数据包 -> 服务端微信（就是使用该软件的微信A）根据wx_account或者nick_name发送到对应的微信号

```json
{
    "mqtt_id": "自定义", // 微信返回数据是根据这个字符串
    "wx_account": "", //微信账号
    "nick_name": "", // 微信昵称，自己微信改的名字
    "remark": "", // 发送微信备注的名字，可用此名字作为群发条件
    "timestamp": 16565655, // 时间戳    "talk": 
    {
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

| 字段名             | 值                        | 说明                                                 | 是否需要填 |
|------------------|-------------------------|-------------------------------------------------------|------------|
| mqtt_id          | 自定义                   | 接受数据的topic使用这个地址才能获取返回数据           | 必填       |
| wx_account       | 自己微信上的账号         | 微信账号                                             | 必填       （wx_account和nick_name）二选一 |
| nick_name        | 自己微信上的名字         | 微信昵称，自己微信改的名字                           | 必填       （wx_account和nick_name）二选一 |
| remark           | 做转发的微信备注         | 发送微信备注的名字，可用此名字作为群发条件           | 选填       |
| timestamp        | 16565655                | 时间戳                                               | 必填       |
| talk.type        | 1                       | 发送数据的类型：1, 2, 3                              | 必填       |
| talk.msg         | test                    | 发送的内容                                           | 根据参数选填 |
| talk.card_title  | Hello_Wechat           | 卡片式内容的简短名字                                   | 根据参数选填 |
| talk.card_desc   | Hello                   | 卡片式内容的简单描述                                   | 根据参数选填 |
| talk.card_image_url | www.baidu.com        | 卡片式内容的图片地址（确保是正确的URL）               | 根据参数选填 |
| talk.card_link_url | www.baidu.com         | 卡片式内容的跳转地址（确保是正确的URL）               | 根据参数选填 |
| type4Picname     | 图片名字                | 卡片式内容的跳转地址（确保是正确的URL）               | 根据参数选填 |

- 服务器默认订阅地址为：/WeChatMqtt/Allmsg



<br>

# **微信发送数据到其他地方**

用户聊天界面输入内容：

有两种数据格式：
1. 第一种快速回复
```
    直接输入字符串（图片数据默认也是base64字符串），默认字符串。这个字符串会发送到对应的mqtt_id上。
```

1. 第二种是根据协议，可以发送数据给其他mqtt_id客户端（以下方式暂时没完成）
```json
1. 文字
{
    "mqtt_id": "自定义", // 微信返回数据是根据这个字符串
    "wx_account": "", //微信账号
    "nick_name": "", // 微信昵称，自己微信改的名字
    "remark": "", // 发送微信备注的名字，可用此名字作为群发条件
    "timestamp": 16565655, // 时间戳    "talk": 
    {
        "type": 1, // 发送数据的类型：1, 2, 3
        "msg": "test", // 发送的内容
    }
}

2. 发送图片
先发送文字，"上传图片"
然后会返回图片的图床url
最后发送下面协议即可
{
    "mqtt_id": "自定义", // 微信返回数据是根据这个字符串
    "wx_account": "", //微信账号
    "nick_name": "", // 微信昵称，自己微信改的名字
    "remark": "", // 发送微信备注的名字，可用此名字作为群发条件
    "timestamp": 16565655, // 时间戳    "talk": 
    {
        "type": 2, // 发送数据的类型：1, 2, 3
        "msg": url, // 发送的内容
    }
}

```



# **测试数据包**


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

2. type：2, 发送图片内容 ，msg：http上传的路径。（此部分展示没编写。因为需要有自己服务器存放图片，还要开一个http服务，后续回写上）[这里提供我使用的免费图床](https://imgbb.com/)
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

3. type：3, 发送卡片 (就是附带http链接的内容) "card_title": "","card_desc": "","card_image_url": "","card_link_url": "",
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

4. type：4, 发送图片，通过图片base64字符串，发送。（发送的速度和服务器的速度有关）
```json
{
    "mqtt_id": "",
    "wx_account": "", 
    "nick_name": "",
    "remark": "",
    "timestamp": 16565655,
    "talk": {
        "type": 4,
        "msg": base64_image, //图片数据
        "card_title": "",
        "card_desc": "",
        "card_image_url": "",
        "card_link_url": "",
        "type4Picname":"1.jpg"
    }
}
```
``` python
# 以下是python mqtt通过base64字符串发送图片的测试代码
import paho.mqtt.client as mqtt
import base64
import json

# MQTT Broker 地址和端口
broker = 'broker-cn.emqx.io'
#broker = '172.245.129.232'
port = 1883

topic = "/WeChatMqtt/Allmsg"

# 图片文件路径
image_file_path = "2.png"

# 读取图片并进行 Base64 编码
with open(image_file_path, "rb") as image_file:
    image_data = image_file.read()
    base64_image = base64.b64encode(image_data).decode("utf-8")

# Create the JSON message with image data in the "msg" field
message_data = {
    "mqtt_id": "123123",
    "wx_account": "",
    "nick_name": "",
    "remark": "",
    "timestamp": 16565655,
    "talk": {
        "type": 4,
        "msg": base64_image,  # Include the Base64-encoded image data here
        "card_title": "Hello_Wechat",
        "card_desc": "Hello",
        "card_image_url": "www.baidu.com",
        "card_link_url": "www.baidu.com",
        "type4Picname": image_file_path  # 必须和你的图片名字一样
    } 
}

# Convert the JSON message to a string
json_message = json.dumps(message_data)

def on_publish(client, userdata, mid):
    print("Message Published")

client = mqtt.Client()
client.on_publish = on_publish

# Set username and password
client.username_pw_set("", "") #有账号密码的添加在这里

client.connect(broker, port, 60)

print(json_message)
# Publish the JSON message with image data to the MQTT topic
client.publish(topic, json_message)

client.loop_forever()
```
5. type:5,获取所有用户wx_account
```
暂时未添加，还有好多功能添加在上面协议
```

- **微信发送数据到mqtt客户端，测试代码中填写自己的 mqtt_id , mqtt_id_name， wx_account就可以使用测试了**

1. 快速回复模式
```
微信好友 
```

2. 协议回复模式
```
发送文字和图片
```