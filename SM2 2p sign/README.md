# Project12: implement sm2 2P sign with real network communication
## 谢东辰 202000460131（一人完成）
## 代码说明/实验步骤
### 1.利用python设计基于UDP协议的客户端和服务端，保证顺利连接
#### 服务端：
![TQ%@CI836 UG83%Q3XEL} J](https://user-images.githubusercontent.com/109883893/181794150-31f07849-6ea8-4d61-96a8-5c116d705fcc.png)
#### 客户端：
![8{M{KMTK5QV$8CXYGEK6{NW](https://user-images.githubusercontent.com/109883893/181794306-2147e40b-6466-4317-8e45-f29973d39d26.png)
### 2.将初始值赋给h1，h2
### 3.每次循环对h1，h2分别进行一次和两次SM3加密后加上i（对应映射x^2+1)
### 4.记录当h1和h2产生nbit碰撞时的输出值
## 运行指导
### 直接运行
## 8bit和16bit碰撞测试的结果如下
![LIB3IUQDP1`KTNZ8A@G)MB5](https://user-images.githubusercontent.com/109883893/181028820-99b2f5a1-09ae-41c8-b8b8-a5bb75383322.png)

![2{D~EIOJ57X5VL2 4LD7(SC](https://user-images.githubusercontent.com/109883893/181793632-d0dd3230-bcf0-4f0d-bce9-09e81eb7e711.png)
