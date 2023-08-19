import random
import time
from paho.mqtt import client as mqtt_client
import base64
from PIL import Image
from io import BytesIO
import time
import json

# MQTT Broker 地址和端口
broker = 'broker-cn.emqx.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}'
image_save_path = "received_image.jpg"
topic = "123123"  #之前对应的发送的topic

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set("lisiniot", "lisiniot@0801#1657")
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, message):
        print(f"Received `{message.payload.decode()}` from `{message.topic}` topic")
        
        
        #以下是测是测四图片时打开
        # 解码 Base64 编码的图片数据
        '''
        base64_image = message.payload.decode("utf-8")
        image_data = base64.b64decode(base64_image)

        image = Image.open(BytesIO(image_data))
        image.save(image_save_path)

        print(f"Image saved to {image_save_path}")
        '''


    client.subscribe(topic)
    client.on_message = on_message


def run():

    # 设置用户名和密码

    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    while True:
        time.sleep(10)


if __name__ == '__main__':

    run()