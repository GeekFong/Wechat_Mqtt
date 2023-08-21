<!--
 * @Author: 极客小方 GeekFong@hotmail.com
 * @Date: 2023-08-17 09:04:27
 * @LastEditors: 极客小方 GeekFong@hotmail.com
 * @LastEditTime: 2023-08-21 10:27:20
 * @FilePath: \Wechat_Mqtt\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
**<h1 style="text-align: center;">Wechat_Mqtt</h1>**

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

## **内容列表**
- [**内容列表**](#内容列表)
- [**简介**](#简介)
- [**使用前准备**](#使用前准备)
- [**使用教程**](#使用教程)
- [**对接协议**](#对接协议)
- [**联系方式**](#联系方式)
- [**声明**](#声明)

## **简介**
把微信和mqtt协议融合。目前github上大多是基于http的。对接其他设备有一定的局限性,用起来没有mqtt方便。Wechat_Mqtt可作为消息通知系统和微信控制系统，这样就会有很多的玩法:

1. 重要事情通知，比如物联网设备机房温度, 监控设备有陌生人进入危险区域，等
2. 微信对家里的物联网设备进行控制
3. 标注系统(服务器每10秒向你发送一张图片),你进行回答，记录答案等。

目前支持双向发送文字和图片(mqtt端和微信端相互发送)支持单项的链接卡片(mqtt端客户端到微信)。图片的发送速度比较慢，和图片的大小还有服务器的能力有关。

本项目是基于
- [WeChatPYAPI](https://github.com/mrsanshui/WeChatPYAPI)免费版本进行开发
- mqtt服务器部署，可以自行谷歌
- 本项目目前暂时不开源,提供程序的打包程序给大家使用，和对接接口


## **使用前准备**
- [mqtt服务器（可以使用免费的mqtt服务器，但是发送图片会偏慢，自己有服务器的尽量自己搭建。）](https://www.lddgo.net/network/mqttlist)
- 在window电脑 [微信版本：3.6.0.18下载传送门](https://geekfong.cn/?p=46)


## **使用教程**
1. 安装好微信版本：3.6.0.18
2. 安装Releases中提供的安装包，打开安装后的程序按照提示登录微信就能够使用了
3. [免费mqtt服务器](https://www.lddgo.net/network/mqttlist),已经配置在config.json当中
4. [mqtt客户端在线测试](http://www.emqx.io/online-mqtt-client/#/recent_connections/0?oper=create)，可用于测试指令
5. test中提供测试的python代码

## **对接协议**
以下是mqtt指令对接微信文档

[对接协议](./doc.md)


## **联系方式**
- qq: 502969366
- tg: https://t.me/f0x15
- 关注 **微信公众号** 获取安装密码, 发送 jkxf01 获取安装密码
![微信公众号](./test/1.jpg)



## **声明**
 **本项目仅供技术研究，请勿用于非法用途，如有任何人凭此做何非法事情，均于作者无关，特此声明**



