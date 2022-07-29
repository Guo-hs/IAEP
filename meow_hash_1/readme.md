# Project18: Find a key with hash value “sdu_cst_20220610” under a message composed of your name followed by your student ID. For example, “San Zhan 202000460001”.

## 代码说明
对于该算法来说，对于任何固定的32字节消息块，meow混合是一种排列，具有易于计算的逆，并且最终轮次也是可逆的。我们此project便利用其可逆性

打开meow_hash_x64_aesni.h文件观察MeowHash函数，即为hash过程，我们对此函数进行逆序，既能完成得到Key的目的

## 运行结果：
![8](https://user-images.githubusercontent.com/109883154/181770203-5583d3cf-6955-4678-a44c-393daca76d0b.png)
![9](https://user-images.githubusercontent.com/109883154/181770210-d3435d17-43a2-4b2f-a5bd-d0bb429e1ea1.png)




## 参考资料
[1]https://github.com/cmuratori/meow_hash

[2]https://peter.website/meow-hash-cryptanalysis

[3]https://mollyrocket.com/meowhash
