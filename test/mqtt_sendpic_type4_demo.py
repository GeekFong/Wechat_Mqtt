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
    "wx_account": "a502969366",
    "nick_name": "方镇杰",
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