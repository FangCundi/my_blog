import numpy as np
import random
from sklearn import model_selection
import matplotlib
import matplotlib.pyplot as plt

#SMO解二次规划问题（松弛向量）
def selectJrand(i, m):
    '''
	随机选择 α
	:param i: α_i的索引值
	:param m: α参数个数
	:return:  α_j的索引值
	'''
    j = i  # 选择一个不等于i的j
    while (j == i):
        j = int(random.uniform(0, m))
    return j

def clipAlpha(aj, H, L):
    '''
	修剪α
	:param aj: α_j值
	:param H:  α上限
	:param L:  α下限
	:return:   α值
	'''
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

def SMO(dataMatIn, classLabels, C, toler, maxIter):
    '''
	SMO算法
	:param dataMatIn: 矩阵
	:param classLabels: 标签
	:param C:  松弛变量
	:param toler:  容错率
	:param maxIter: 最大迭代次数
	:return:
	'''
    # 转换为numpy的mat存储
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    # 初始化b参数，统计dataMatrix的维度
    b = 0
    m, n = np.shape(dataMatrix)
    # 初始化alpha参数，设为0
    alphas = np.mat(np.zeros((m, 1)))
    # 初始化迭代次数
    iter_num = 0
    # 最多迭代matIter次
    while (iter_num < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            # 步骤1：计算误差Ei
            fXi = float(np.multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T)) + b
            Ei = fXi - float(labelMat[i])
            # 优化alpha，设定一定的容错率。
            if ((labelMat[i] * Ei < -toler) and (alphas[i] < C)) or ((labelMat[i] * Ei > toler) and (alphas[i] > 0)):
                # 随机选择另一个与alpha_i成对优化的alpha_j
                j = selectJrand(i, m)
                # 步骤1：计算误差Ej
                fXj = float(np.multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[j, :].T)) + b
                Ej = fXj - float(labelMat[j])
                # 保存更新前的aplpha值，使用深拷贝
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                # 步骤2：计算上下界L和H
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H: continue
                # 步骤3：计算eta
                eta = 2.0 * dataMatrix[i, :] * dataMatrix[j, :].T - dataMatrix[i, :] * dataMatrix[i, :].T - dataMatrix[j,:] * dataMatrix[j, :].T
                if eta >= 0: continue
                # 步骤4：更新alpha_j
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                # 步骤5：修剪alpha_j
                alphas[j] = clipAlpha(alphas[j], H, L)
                if (abs(alphas[j] - alphaJold) < 0.00001): continue
                # 步骤6：更新alpha_i
                alphas[i] += labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
                # 步骤7：更新b_1和b_2
                b1 = b - Ei - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i, :] * dataMatrix[i, :].T - labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[i, :] * dataMatrix[j, :].T
                b2 = b - Ej - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i, :] * dataMatrix[j, :].T - labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[j, :] * dataMatrix[j, :].T
                # 步骤8：根据b_1和b_2更新b
                if (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif (0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                # 统计优化次数
                alphaPairsChanged += 1
                # 打印统计信息
                # print("第%d次迭代 样本:%d, alpha优化次数:%d" % (iter_num, i, alphaPairsChanged))
        # 更新迭代次数
        if (alphaPairsChanged == 0):
            iter_num += 1
        else:
            iter_num = 0
        print("迭代次数: %d" % iter_num)
    return b, alphas

# 计算 W
def get_w(dataMat, labelMat, alphas):
    alphas, dataMat, labelMat = np.array(alphas), np.array(dataMat), np.array(labelMat)
    w = np.dot((labelMat.reshape(1,len(dataMat)).T* dataMat).T, alphas)
    return w

def readdata(filename):#获得数据，标签在数据最后一列
    file_0=open(filename)
    a=file_0.read()
    a=a.split('\n')[:-1]
    # print(a)
    data_sum=[]
    label_sum=[]
    data_n=[]
    for i in a:
        data_n=i.split(',')
        data_n=[float(j) for j in data_n]
        data_sum.append(data_n[:-1])
        label_sum.append(data_n[-1])
    return data_sum,label_sum

def predictl(testdata,w,b):
    result=[]
    for i in testdata:
        if float(np.dot(w.T,i)+b)>0:
            result.append(1)
        else:
            result.append(-1)
        # result.append(float(np.dot(w.T,i)+b))
    return result

def testl(testdata,testlabel,w,b):
    num=0
    for i in range(len(testdata)):
        if (testlabel[i]>0 and np.dot(w.T,testdata[i])+b>0 )or (testlabel[i]<0 and np.dot(w.T,testdata[i])+b<0 )or(np.dot(w.T,testdata[i])+b<=0.01):
            num+=1
        else:
            print(testdata[i],' ',testlabel[i],' ',np.dot(w.T,testdata[i])+b)
    print('正确率为：',num/len(testdata))

def paint(w,x,y,b):
    # 确定坐标轴范围
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0维特征的范围
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1维特征的范围
    x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网络采样点
    grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点
    # 指定默认字体
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    plt.rc('axes', unicode_minus=False)
    # 设置颜色
    cm_light = matplotlib.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    cm_dark = matplotlib.colors.ListedColormap(['g', 'r', 'b'])

    grid_hat = predictl(grid_test,w,b)  # 预测分类值
    grid_hat=np.array(grid_hat)
    grid_hat = grid_hat.reshape(x1.shape)  # 使之与输入相同
    plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)  # 预测值得显示
    yy=[]
    for i in y:
        if i == -1:
            yy.append(0)
        else:
            yy.append(1)

    plt.scatter(x[:, 0], x[:, 1], c=yy[:], s=50, edgecolors='k', zorder=3,cmap=cm_dark)  # 圈中测试集样本点
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.show()

def IninDataSet(n):
    dataMat = []
    labelMat = []
    np.random.seed(7557)  # 使其生成相同的数据集，  666
    w = np.random.uniform(-1, 1, 2)  # 输出（w1,w2）数组
    b = np.random.uniform(-1, 1)  # 输出 （b）
    X = np.random.uniform(-1, 1, [n, 2])  # 输出 n个（x1,x2）个样本       输出的是元组
    y = np.sign(np.inner(w, X) + b)
    dataMat = X.tolist()  # 元组转变为列表
    labelMat = y.tolist()
    return dataMat, labelMat

if __name__ == '__main__':
    data,label=readdata('./data2.csv')
    # data,label=IninDataSet(500)
    x=np.array(data)#转换为数组
    y=np.array(label).transpose()
    train_data,test_data,train_label,test_label=model_selection.train_test_split(x,y, random_state=17, train_size=0.8,test_size=0.2)
    '''
    sklearn.model_selection.train_test_split随机划分训练集与测试集。train_test_split(train_data,train_label,test_size=数字, random_state=0)
　　 参数解释：
　    　train_data：所要划分的样本特征集
　    　train_label：所要划分的样本类别
　    　test_size：样本占比，如果是整数的话就是样本的数量.(注意：)
                   --  test_size:测试样本占比。 默认情况下，该值设置为0.25。 默认值将在版本0.21中更改。 只有train_size没有指定时， 
                        它将保持0.25，否则它将补充指定的train_size，例如train_size=0.6,则test_size默认为0.4。
                   -- train_size:训练样本占比。
　    　random_state：是随机数的种子。
    '''
    b,alphas=SMO(train_data,train_label,1,0.001,10)
    w = get_w(train_data, train_label, alphas)
    testl(train_data,train_label,w,b)
    paint(w,test_data,test_label,b)