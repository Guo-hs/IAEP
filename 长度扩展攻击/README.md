# Project3:implement length extension attack for SM3, SHA256, etc
## 谢东辰 202000460131（一人完成）
## 代码说明/实验步骤
### 1.修改gmssl库中sm3的hash函数，以便进行长度扩展攻击
#### 具体内容如下：
![image](https://user-images.githubusercontent.com/109883893/181297685-65f99be1-bc66-4e41-902b-dc3b72fc84d2.png)  
如图所示对hash函数添加一个参数iv用于传递向量，同时将图中的i改为i+1以实现长度扩展，最后更改append的参数为iv
### 2.
### 3.
### 4.
## 运行指导
### 直接运行
## 8bit和16bit碰撞测试的结果如下

