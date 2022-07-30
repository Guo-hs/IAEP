# Project12: implement sm2 2P sign with real network communication
## 谢东辰 202000460131（一人完成）
## 代码说明/实验步骤
### 1.利用python设计基于UDP协议的客户端和服务端，保证顺利连接
#### 服务端：
![TQ%@CI836 UG83%Q3XEL} J](https://user-images.githubusercontent.com/109883893/181794150-31f07849-6ea8-4d61-96a8-5c116d705fcc.png)
#### 客户端：
![8{M{KMTK5QV$8CXYGEK6{NW](https://user-images.githubusercontent.com/109883893/181794306-2147e40b-6466-4317-8e45-f29973d39d26.png)
### 2.引入已完成的SM2算法所需内容（详见代码）
### 3.在客户端利用sm2加密得到C，计算T1（x,y轴坐标）发送给服务端
### 4.服务端接收信息后计算出T2并发送给客户端
### 5.客户端计算出u后与c3比较相等则输出M2
## 运行指导
### 直接运行
## 输出的M2如下
![9TWCSY5ME{(VD}CAZ~F7WEK](https://user-images.githubusercontent.com/109883893/181925671-5d00166b-fcf8-498f-b657-3531486f9d26.png)
