import socket
import sys
import math
from random import randint
from gmpy2 import invert


# -------------------------------------以下是SM2算法的内容---------------------------------------------------

def modinv(a,m):
    x1,x2,x3=1,0,a
    y1,y2,y3=0,1,m
    while y3!=0:
        q=x3//y3
        t1,t2,t3=x1-q*y1,x2-q*y2,x3-q*y3
        x1,x2,x3=y1,y2,y3
        y1,y2,y3=t1,t2,t3
    return x1%m

iv='7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e'
def t(j):
    if j<16:
        return 0x79cc4519
    return 0x7a879d8a
def csl(x,k):#cycle_shift_left
    x='{:032b}'.format(x)
    k=k%32
    x=x[k:]+x[:k]
    return int(x,2)
#bool function
def ff(x,y,z,j):
    if j<16:
        return x^y^z
    return (x&y)|(y&z)|(z&x)
def gg(x,y,z,j):
    if j<16:
        return x^y^z
    return (x&y)|(~x&z)

#displace function
def p0(x):
    return x^csl(x, 9)^csl(x, 17)
def p1(x):
    return x^csl(x, 15)^csl(x, 23)

#plaintext:m(length<2^64bit)
def fill(m):
    l=len(m)*4
    m=m+'8'
    k=112-(len(m)%128)
    m=m+'0'*k+'{:016x}'.format(l)
    return m

def grouping(m):
    n=len(m)//128
    b=[]
    for i in range(n):
        b.append(m[i*128:(i+1)*128])
    return b

def extend(bi):
    w=[]
    global h
    h+=1
    for i in range(16):
        w.append(int(bi[i*8:(i+1)*8],16))
    for j in range(16,68):
        w.append(p1(w[j-16]^w[j-9]^csl(w[j-3], 15))^csl(w[j-13], 7)^w[j-6])
    for j in range(68,132):
        w.append(w[j-68]^w[j-64])
        154996
    if (h==1):
        print(hex(0xEE0C62D1DC3140C2DE4532F668AFA2D97A63228BB59A0094A960A39BAC470B24A4677D10E))
    return w

def cf(vi,bi):
    w=extend(bi)
    a,b,c,d,e,f,g,h=int(vi[0:8],16),int(vi[8:16],16),int(vi[16:24],16),int(vi[24:32],16),int(vi[32:40],16),int(vi[40:48],16),int(vi[48:56],16),int(vi[56:64],16)
    for j in range(64):
        ss1=csl((csl(a,12)+e+csl(t(j),j))%pow(2,32),7)
        ss2=ss1^csl(a,12)
        tt1=(ff(a,b,c,j)+d+ss2+w[j+68])%pow(2,32)
        tt2=(gg(e,f,g,j)+h+ss1+w[j])%pow(2,32)
        d=c
        c=csl(b,9)
        b=a
        a=tt1
        h=g
        g=csl(f,19)
        f=e
        e=p0(tt2)
    abcdefgh=int('{:08x}'.format(a)+'{:08x}'.format(b)+'{:08x}'.format(c)+'{:08x}'.format(d)+'{:08x}'.format(e)+'{:08x}'.format(f)+'{:08x}'.format(g)+'{:08x}'.format(h),16)
    return '{:064x}'.format(abcdefgh^int(vi,16))

def iteration(b):
    n=len(b)
    v=iv
    for i in range(n):
        v=cf(v,b[i])
    return v

def Hash(m):
    m=fill(m)
    b=grouping(m)
    return iteration(b)

def KDF(z,klen):
    ct=1
    k=''
    for i in range(math.ceil(klen/256)):
        t=hex(int(z+'{:032b}'.format(ct),2))[2:]
        k=k+hex(int(Hash(t),16))[2:]
        ct=ct+1
    k='0'*((256-(len(bin(int(k,16))[2:])%256))%256)+bin(int(k,16))[2:]
    return k[:klen]


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


def encrypt(m:str,d1):
    plen=len(hex(p)[2:])
    x=mul(G,d1)
    m='0'*((4-(len(bin(int(m.encode().hex(),16))[2:])%4))%4)+bin(int(m.encode().hex(),16))[2:]
    klen=len(m)
    while True:
        k=randint(1, n)
        while k==d1:
            k=randint(1, n)
        x2,y2=mul(x,k)
        x2,y2='{:0256b}'.format(x2),'{:0256b}'.format(y2)
        t=KDF(x2+y2, klen)
        if int(t,2)!=0:
            break
    c1 = mul(G, k)
    print()
    c2=((klen//4)-len(hex(int(m,2)^int(t,2))[2:]))*'0'+hex(int(m,2)^int(t,2))[2:]
    c3=hash(hex(int(x2+m+y2,2))[2:])
    return c1,c2,c3


def decrypt(c1,c2,c3,a,b,p):
    c1=c1[2:]
    x=int(c1[:len(c1)//2],16),int(c1[len(c1)//2:],16)
    if pow(y1,2,p)!=(pow(x1,3,p)+a*x1+b)%p:
        return False
    x2,y2=mul(x, d1)
    x2,y2='{:0256b}'.format(x2),'{:0256b}'.format(y2)
    klen=len(c2)*4
    t=KDF(x2+y2, klen)
    if int(t,2)==0:
        return False
    m='0'*(klen-len(bin(int(c2,16)^int(t,2))[2:]))+bin(int(c2,16)^int(t,2))[2:]
    u=hash(hex(int(x2+m+y2,2))[2:])
    if u!=c3:
        return False
    return hex(int(m,2))[2:]

h=0
p=0x8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3
a=0x787968B4FA32C3FD2417842E73BBFEFF2F3C848B6831D7E0EC65228B3937E498
b=0x63E4C6D3B23B0C849CF84241484BFE48F61D59A5B16BA06E6E12D1DA27C5249A
n=0x8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7
Gx=0x421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D
Gy=0x0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2
G=(Gx,Gy)  # 用元组表示点的坐标


# --------------------------------------------------以上为SM2算法的内容---------------------------------------------------


host = '127.0.0.1'
port=5200  # 任意设计端口号
address=(host,port)
s_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s_client.connect(address)
    print("连接成功！")

except Exception:
    print('连接失败！')
    sys.exit()

# ------------连接完毕-------------
else:
    M="202000460131"  # 任取信息M
    d1=randint(1,n)  # 任取一个d1
    C1,C2,C3=encrypt(M,d1)  # 利用d1得到C
    T1 = mul(C1, invert(d1, p))  # 计算T1

    # 将T1发送给服务端
    x, y = hex(T1[0]), hex(T1[1])
    s_client.sendto(x.encode('utf-8'), address)
    s_client.sendto(y.encode('utf-8'), address)

    # 接收T2
    x1, address = s_client.recvfrom(1024)
    x1 = int(x1.decode(), 16)
    y1, address = s_client.recvfrom(1024)
    y1 = int(y1.decode(), 16)
    T2 = (x1, y1)
    # 计算x2,y2
    x2, y2 = add(T2[0], T2[1], C1[0], -C1[1])
    x2, y2 = '{:0256b}'.format(x2), '{:0256b}'.format(y2)
    # 计算t
    klen=len(C2)*4
    t = KDF(x2 + y2, klen)
    M2 = '0' * (klen - len(bin(int(C2, 16) ^ int(t, 2))[2:])) + bin(int(C2, 16) ^ int(t, 2))[2:]
    u = hash(hex(int(x2 + M2 + y2, 2))[2:])
    if (u == C3):
        print(hex(int(M2)).upper()[2:])
    s_client.close()
