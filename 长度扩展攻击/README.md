# Project3:implement length extension attack for SM3, SHA256, etc
## 谢东辰 202000460131（一人完成）
## 代码说明/实验步骤
### 1.修改gmssl库中sm3的hash函数，以便进行长度扩展攻击
#### 具体内容如下：
![image](https://user-images.githubusercontent.com/109883893/181297685-65f99be1-bc66-4e41-902b-dc3b72fc84d2.png)  
如图所示对hash函数添加一个参数iv用于传递向量，同时将图中的i改为i+1以实现长度扩展，最后更改append的参数为iv
### 2.随机生成一个消息m，对其进行sm3加密得到hash
### 3.利用hash计算加密结束后的iv值作为初始向量加密附加消息m_append（任意值），填充后得到猜测hash值
### 4.对消息进行加密、扩展（添加附加消息）、填充得到对应的hash值
### 5.将3，4两步得到的hash值对比，判断长度扩展攻击猜测的hash值是否正确
## 运行指导
### 直接运行
## 攻击结果如下
![O7A}%C(1I5L9V~KW$BC)VTU](https://user-images.githubusercontent.com/109883893/181300280-e26a8175-5800-45d8-87fa-c12778316c3d.png)

