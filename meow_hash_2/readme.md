# Project19: Find a 64-byte message under some k fulfilling that their hash value is symmetrical.

## 内容

Meow_hash中使用的所有操作都具有对称属性，我们在此project中利用对称性。

如果 128 位值的高阶和低阶 64 位半部分相等，则将其称为对称值。Meow_hash完全由三个操作构建：

在 128 位通道上应用一轮 AES 解密。

将 128 位值 Xor 转换为 128 位通道。

通过按元素添加低和高 64 位字，将 128 位值添加到 128 位通道中。

这三个操作都具有这样的属性：如果输入是对称的，那么输出也将是对称的。这种对称性显然适用于异或和加法，但由于指令使用的字节顺序，它最终也适用于AES解密。

对于任何小于256的消息长度（即32的倍数），我们可以构造一个密钥，该密钥在长度被吸收后将达到对称状态，只需向后运行Meow_hash的吸收函数。这样的密钥将使给定长度的任何abc对称消息发送到对称的64位哈希。

头文件仍是可逆性实验中的头文件，源文件进行改变

## 运行结果

![10](https://user-images.githubusercontent.com/109883154/181870348-d5c3384e-b0a9-4207-9e19-0f1fbfe6327d.png)

## 参考资料

[1]https://github.com/cmuratori/meow_hash

[2]https://peter.website/meow-hash-cryptanalysis

[3]https://mollyrocket.com/meowhash
