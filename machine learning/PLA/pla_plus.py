import numpy as np
import matplotlib.pyplot as plt
import copy

def readdata(filename):#读数据，其中第一位人为设置为1，即w的偏执d
    if filename==None:
        return 0
    else:
        file=open(filename)
        i = file.read()
        i = i.split('\n')[:-1]
        data = []
        label = []
        for j in i:
            n = j.split(',')
            data0 = [1.0]
            for p in n[:-1]:
                data0.append(float(p))
            data.append(data0)
            label.append(int(n[-1]))
        return data[:int(len(data)*0.75)],label[:int(len(label)*0.75)],data[int(len(data)*0.75):],label[int(len(label)*0.75):]

def definel(n):#判断直线是否正确划分
    t=float(n)
    if t>0: return 1
    elif t==0:return 0
    else: return -1

def pocket(data,lable):
    count=0
    traindata=np.mat(data)#通过mat函数将列表转化为矩阵
    trainlabel=np.mat(lable).transpose()#获得标签的转置的矩阵
    m,n=np.shape(traindata)#获得traindata的行数与列数
    w=np.ones((n,1))#使用ones函数生成n行1列的数据作为法向量的初始值，即1列n维的单位向量
    while True:
        isfinish=True
        wmin=copy.deepcopy(w)
        nmin=len(data)
        # print(count)
        for i in range(m):
            if(definel(np.dot(traindata[i],w))==trainlabel[i]):#np的dot函数获得两个向量的乘积
                #权重w与点坐标的乘积，判断能否正确划分
                continue
            else:
                isfinish=False
                w1=w+(trainlabel[i]*traindata[i]).transpose()#获得wi+1
                n1=0
                n2=0
                for j in range(m):#判断是否更好
                    if (definel(np.dot(traindata[i], w)) != trainlabel[i]):
                        n1+=1
                    if (definel(np.dot(traindata[i], w1)) != trainlabel[i]):
                        n2+=1
                if n1>n2:
                    if nmin>n2:
                        nmin=copy.deepcopy(n2)
                        wmin=copy.deepcopy(w1)
                else:
                    continue
        w = copy.deepcopy(wmin)  # 对w进行更新
        # print(w)
        # input()
        count += 1
        if isfinish:
            break
        if count>=2000:#阈值
            break
    return w,count

def definey(c,w):#验证w划分结果是否与label一致
    r=definel(np.dot(np.mat(c),w))
    if r>0:
        return 1
    else:
        return -1

def paint(w,data,label):
    dataarr=np.array(data)
    n=np.shape(dataarr)[0]
    x1=[]
    y1=[]
    x2=[]
    y2=[]
    for i in range(n):
        if int(label[i])==1:
            x1.append(dataarr[i,1])
            y1.append(dataarr[i,2])
        else:
            x2.append(dataarr[i,1])
            y2.append(dataarr[i,2])
    fig=plt.figure()
    ax=fig.add_subplot(111)# 这些是编码为单个整数的子图栅格参数。例如，”111″表示“1×1网格，第一子图”，”234″表示“2×3网格，第4子图”。
    ax.scatter(x1, y1, s=30, c='red', marker='s')
    ax.scatter(x2, y2, s=30, c='green')
    x = np.arange(-4.0, 10.0, 0.1)
    y = (-float(w[0]) - float(w[1]) * x) / float(w[2])
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
    return 0

def ltest(data,w):
    p=[]
    for d in data:
        r=definey(d,w)
        p.append(r)
    return p

def main():
    data,label,testdata,testlabel = readdata('./data2.csv')
    w,count=pocket(data,label)
    r=ltest(testdata,w)
    paint(w,data,label)
    print("迭代次数：", count)
    print("权重w：", w)
    print("划分结果：", r)
    num=0
    for i in range(len(r)):
        if r[i]==testlabel[i]:
            num+=1
    if num==len(r):
        print("测试集全部正确")
    else:
        print('测试集正确率为：',float(num/len(r)))

if __name__ == '__main__':
    main()