# Project12: implement sm2 2P sign with real network communication
## 谢东辰 202000460131（一人完成）
## 代码说明/实验步骤
### 1.利用python设计基于UDP协议的客户端和服务端，保证顺利连接
#### 服务端：
![TQ%@CI836 UG83%Q3XEL} J](https://user-images.githubusercontent.com/109883893/181794150-31f07849-6ea8-4d61-96a8-5c116d705fcc.png)
#### 客户端：
![8{M{KMTK5QV$8CXYGEK6{NW](https://user-images.githubusercontent.com/109883893/181794306-2147e40b-6466-4317-8e45-f29973d39d26.png)
### 2.引入已完成的SM2算法所需内容（详见代码）
### 3.在客户端按步骤计算P1，Q1,e（x,y轴坐标）发送给服务端
### 4.服务端接收信息后计算出r，s2,s3并发送给客户端
### 5.客户端计算s后判断条件，输出σ（r，s）
## 运行指导
### 直接运行
## 得到的σ（r，s）如下
![2{D~EIOJ57X5VL2 4LD7(SC](https://user-images.githubusercontent.com/109883893/181793632-d0dd3230-bcf0-4f0d-bce9-09e81eb7e711.png)
