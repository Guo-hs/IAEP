import random
import time
from gmssl import sm3, func

def Rho_attack(n):
        i = random.randint(2**31, 2 ** 32 - 1)#随机取一个32bit数作为初始值
        H1 = H2 = i.to_bytes(32,"big")#将初始值转化为byte类型后赋值给H1,H2
        while True:
            h1 = sm3.sm3_hash(func.bytes_to_list(H1))#对H1进行一次加密
            H1=int(h1, 16).to_bytes(32, "big")#类型转换
            h2 = sm3.sm3_hash(func.bytes_to_list(int(sm3.sm3_hash(func.bytes_to_list(H2)),16).to_bytes(32 ,"big")))#对H2进行两次加密
            H2 =(int(h2, 16)+i).to_bytes(32, "big")#类型转换
            if h1[: int(n / 4)]==h2[: int(n / 4)]:#取前nbit做碰撞对比
                return (h1,h2)


start=time.time()
print(Rho_attack(8))
end = time.time()
print('前8比特碰撞耗时：',end-start)
start=time.time()
print(Rho_attack(16))
end = time.time()
print('前16比特碰撞耗时：',end-start)

