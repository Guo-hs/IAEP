# 服务端
import socket
from random import randint
from gmpy2 import invert


# -------------------------------------以下是SM2算法的内容---------------------------------------------------

def add(x1,y1,x2,y2):
    if x1==x2 and y1==p-y2:
        return False
    if x1!=x2:
        lamda=((y2-y1)*invert(x2-x1, p))%p
    else:
        lamda=(((3*x1*x1+a)%p)*invert(2*y1, p))%p
    x3=(lamda*lamda-x1-x2)%p
    y3=(lamda*(x1-x3)-y1)%p
    return x3,y3

def mul(G,k):
    k=bin(k)[2:]
    qx,qy = G
    qx1, qy1 = G
    for i in range(1,len(k)):
        qx1,qy1=add(qx1, qy1, qx1, qy1)
        if k[i]=='1':
            qx1,qy1=add(qx1, qy1, qx, qy)
    return qx1,qy1


p=0x8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3
a=0x787968B4FA32C3FD2417842E73BBFEFF2F3C848B6831D7E0EC65228B3937E498
b=0x63E4C6D3B23B0C849CF84241484BFE48F61D59A5B16BA06E6E12D1DA27C5249A
n=0x8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7
Gx=0x421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D
Gy=0x0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2
G=(Gx,Gy)

# --------------------------------------------------以上为SM2算法的内容-------------------------------------------------

host = ''
port = 5200
address = (host, port)
s_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_client.bind(address)

# ------------连接完毕-------------

# 接收客户端发来的P1(x,y)
x,address = s_client.recvfrom(1024)
x=int(x.decode(),16)
y,address= s_client.recvfrom(1024)
y=int(y.decode(),16)
p1=(x,y)

d2=randint(1,n)  # 任取一个d2

P = mul(p1,invert(d2,p))  # 计算P
P = add(P[0],P[1],Gx,-Gy)

# 接收客户端发来的Q1(x,y),e
x,address = s_client.recvfrom(1024)
x=int(x.decode(),16)
y ,address= s_client.recvfrom(1024)
y=int(y.decode(),16)
Q1=(x,y)
e,address=s_client.recvfrom(1024)
e=int(e.decode(),16)

# 任取k2,k3
k2=randint(1,n)
k3=randint(1,n)

Q2=mul(G,k2)  # 计算Q2

# 计算r,s2,s3
x1,y1=mul(Q1,k3)
x1,y1=add(x1,y1,Q2[0],Q2[1])
r=(x1+e)%n
s2=(d2*k3)%n
s3=(d2*(r+k2))%n

# 发送计算r,s2,s3
s_client.sendto(hex(r).encode(),address)
s_client.sendto(hex(s2).encode(),address)
s_client.sendto(hex(s3).encode(),address)

# ---------------------------------------------------------------结束--------------------------------------------------------

