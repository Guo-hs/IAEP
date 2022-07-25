# Project8: impl sm2 with RFC6979

## SM2椭圆曲线公钥密码算法：
我国自主知识产权的商用密码算法，是ECC（Elliptic Curve Cryptosystem）算法的一种，基于椭圆曲线离散对数问题，计算复杂度是指数级，求解难度较大，同等安全程度要求下，椭圆曲线密码较其他公钥秒速昂发所需密钥长度小很多。

## ECC算法描述：
1.用户A选定一条适合加密的椭圆曲线Ep(a,b)(如:y2=x3+ax+b)，并取椭圆曲线上一点，作为基点G。  
2、用户A选择一个私有密钥k，并生成公开密钥（公钥PB）K=kG。  
3、用户A将Ep(a,b)和点（公钥）K，G传给用户B。 　  
4、用户B接到信息后 ，将待传输的明文（M）编码到Ep(a,b)上一点M，并产生一个随机整数r（r<n）。加密开始  
5、用户B计算点C1=M+rK；C2=rG。  
6、用户B将C1、C2传给用户A。 　　  
7、用户A接到信息后，计算C1-kC2，结果就是点M。因为C1-kC2=M+rK-k(rG)=M+rK-r(kG)=M 　　再对点M进行解码就可以得到明文。  

## 运行结果：

![%FD SK7HGUT~WH{C%VD D_4](https://user-images.githubusercontent.com/109883154/180712867-d3cca612-2122-438b-866a-22ffdc3193d5.png)
