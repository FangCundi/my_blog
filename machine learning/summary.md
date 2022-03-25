# 000 基础知识

1. 规律、技术：改变/改进某种性能度量
2. 机器学习组成：
   1. 数据集D，输入空间、输出空间
   2. 未知函数f
   3. 函数满足值g（假设空间H）
3. 用学习算法找一个最好的g，使g逼近f
4. f客观存在，但不可知；g有多个且不同，期望用g取表示f
<font color='red'><b>
5. 机器学习想找一个g，使g接近f。数据挖掘想用大量数据找一些有意思的规律。如果说规律就是假说g，那么DM=ML。一般DM专注于高性能计算，ML专注于g算法
6. 机器学习是帮助实现AI的手段，还有其他方法，比如逻辑

</font></b>

7. 统计是用数据对未知作推理，f可看做未知变量，g可看做推理结果。更加偏向理论

<div STYLE="page-break-after: always;"></div>

# 001 感知机算法PLA
<b>
实际上就是线性分类的感知机算法PLA和针对非线性的适用算法POCKET
</b>

## PLA
权重：$y(标签)={-1（bad）,1（good）}$
阈值：$h(x)=sign((\sum^d_{i=1}w_ix_i)-threshold(阀值))=sign(w^Tx)$
每一组权重，阈值都可以认为是一个g，都是直线/超平面$w\in R^d,b\in R^1$，这里的d是数据的维度
$w^T$是超平面的法向量，为$w=\{w_1,w_2,...,w_n,d\}$其中d为偏执量，w的维度与x样本的维度一致。同理，样本x=$\{x_1,x_2,...,x_n,1\}$。会多一个维度，多出来的d在图形上表示为直线的上下平移。
PLA的主要任务：找到一个w，使样本点可以正确二分类，即要求：
**已知理想直线$W_f$，求证$w_{t+1}$比$w_t$更接近$w_f$**

<b>

流程为：给一个初识解$g^0$，然后去调试，如果$w^t$对$(x_n(t),y_n(t))$不能正确分类，即$sign(w_t^T*x_n*(t))\ne y_n(t)$，则要求$w_{t+1}\Longleftarrow w_t+y_n(t)*x_n(t)$，不一定会再分类正确，但一定会向结果靠近
</b>

### 1 证明会向结果靠近

$w_{t+1}=w_t+y_n(t)x_n(t)$，其中$(x_n(t),y_n(t))$是一个错分点
更接近代表着向量的内积增大
即求证$w_f^T*w_{t+1}\ge w_f^T*w_t$
代入有$w_f^T*w_{t+1}=w_f^T*(w_f+y_n(t)x_n(t))
=w_f^T*w_t+y_n(t)*w_f^T*x_n(t)$
因为$w_f$是理想直线，表示在线性可分的时候全部分类正确
即$y_n(t)$与$w_f^T*x_n(t)$同符号
即$y_n(t)*w_f^T*x_n(t)\ge 0$，这里是由于非负相乘必为非负数
故$w_f^T*w_{t+1}\ge w_f^T*w_t+\min_ny_n(t)*w_f^T*x_n(t)$——**1式**
**<font color='red'>
此时，已经证明了向量内积会随着迭代次数而增加**
</font>
但虽然已知内积增大，但可能是夹角减小（即我们想要的靠近）或者是模增加
现在考虑模长的改变，即$||w_{t+1}||$与$||w_t||$的关系
$||w_{t+1}||^2=||w_t+y_n(t)*x_n(t)||^2$
$=||w_t||^2+2y_n(t)*w_t^T*x_n(t)+||y_n(t)*x_n(t)||^2$
因为对$w_t$而言，因假设$(x_n(t),y_n(t))$是错分点
则$sign(w_t^Tx_n(t))\ne y_n(t)$且符号相反
故$2y_n(t)*w_t^T*x_n(t)\le 0$
可有
$||w_{t+1}||^2\le ||w_t||^2+||y_n(t)x_n(t)||^2$
对第二项取极值可有
$||w_{t+1}||^2\le ||w_t||^2+\max_n ||y_n(t)x_n(t)||^2$——**2式**
其中$\max_n ||y_n(t)*x_n(t)||^2$表示变化上界
**<font color='red'>
此时，已经证明了模长会有一个变化上界**
</font>
现在可以考虑夹角$\theta$的$\cos$值
$\cos\theta=\frac{w_f^T*w_t}{||w_f||||w_t||}$
所以需要考虑$\cos\theta$的上界或下界
对1式求错位：初始化$w_0=0$
$w_f^Tw_1\ge w_f^Tw_0+\min_ny_nw_f^Tx_n$
$w_f^Tw_2\ge w_f^Tw_1+\min_ny_nw_f^Tx_n$
...
$w_f^Tw_t\ge w_f^Tw_{t-1}+\min_ny_nw_f^Tx_n$

错位后是：
$w_f^Tw_t\ge w_f^Tw_0+t\min_ny_nw_f^Tx_n$
即$w_f^Tw_t\ge t\min_ny_nw_f^Tx_n$
同理，对2式求错位：初始化w_0=0
$||w_1||^2\le||w_0||^2+\max_n||y_nx_n||^2$
$||w_2||^2\le||w_1||^2+\max_n||y_nx_n||^2$
...
$||w_t||^2\le||w_{t-1}||^2+\max_n||y_nx_n||^2$
错位后是：
$||w_t||^2\le||w_0||^2+t\max_n||y_nx_n||^2$
即$||w_t||^2\le t\max_n||y_nx_n||^2$
故可有$\cos\theta：$
$\cos\theta=\frac{w_f^Tw_t}{||w_f||||w_t||}$
$\ge \frac{\sqrt t\min_ny_nw_f^Tx_n}{||w_f||\sqrt{\max_n||y_nx_n||^2}}$
因为$y_n\in\{-1,1\}$
故可转化为
$\cos\theta\ge \frac{\sqrt t\min_ny_nw_f^Tx_n}{||w_f||\max_n||x_n||}$
其中，$\max_n||x_n||$表示距离圆点最远的点的距离R
而$\frac{\min_ny_nw_f^Tx_n}{||w_f||}$表示离理想直线最近的点$(x_n,y_n)$到直线的距离$\rho$
故$\cos \theta\ge \sqrt{t}\frac{\rho}{R}$
很明显，随着迭代次数t的增加，$\cos\theta$的下界逐渐增加，表示$\cos\theta$越来越大
**<font color='red'>
此时，已经证明了角度会越来越小，即越来越得到的直线与最终结果的直线的夹角会越来越小，直到重合**
</font>
但是，由于$\cos\theta$本身具有上界1，这个时候表示$w_t$与$w_f$完全重合

### 2 证明迭代可终止（有上界）

<font size='4'>

**根据这个就可以得到PLA算法的迭代上界，即我们的Radios-Margin Bound定理**

</font>

将$\cos$的上界带入，可有
$\sqrt t\frac{\rho}{R}\le1$
其中，$\max_n||x_n||$表示距离圆点最远的点的距离R
而$\frac{\min_ny_nw_f^Tx_n}{||w_f||}$表示离理想直线最近的点$(x_n,y_n)$到直线的距离$\rho$

即$t\le(\frac{R}{\rho})^2$

## POCKET

**PLA算法只能解决线性可分的情况，线性可分的时候是收敛的。**
只要PLA停机，就是线性可分的问题。
数据集D线性可分$\Longleftrightarrow$存在$w_f$使得$y_n=sign(w_f^T*x_n)$
至于POCKET算法，则是面对非线性分类的时候
有噪声时，$y_i$不一定是$x_i$的真实标签，无法线性可分。假设**噪声很少，此时目标函数f通常可以正常分类，此时需要尽可能去分类**，$w_g\leftarrow org\min_w \sum_{n=1}^N[y_n\ne sign(w^Tx_i)]$，即不一致的最少。

**<font color='red'>
当且仅当$w_{t+1}$分类的错误项比$w_t$分类的错误项少的时候，才会用$w_{t+1}$来代替$w_t$，然后人为设定一个最大迭代阈值即可。
</font>**

<div STYLE="page-break-after: always;"></div>

# 002 支持向量机与核算法SVM

## base

输入空间：$X\subseteq R^d$
输出空间（标签）：$Y=\{-1,+1\}$
未知的目标函数：$f:X\rightarrow Y$
训练集合：$S=\{(x_i,y_i)\}_{i=1}^n,y_i=f(x_i),\{x_i\}_{i=1}^n$从输入空间X中依据分布D采样得到，n为样本个数
假说集合：$H=\{x\rightarrow sign(w^Tx+b):w\in R^d,b\in R\}$
假设h是某个具体假设函数
经验误差：$R_S(h)=\frac 1n \sum_{i=1}^n[h(x_i)\ne f(x_i)]$ with $h\in H$，表示分类错误，是针对训练集的误分率
泛化误差：$R_D(h)=P_{x\in D}[h(x)\ne f(x)]$with$h\in H$，表示针对整个样本分布，错误分类的概率，类似于噪声，是在新样本集合上的错分率
分类问题：
&emsp;&emsp;给定样本$S=\{(x_1,y_1),...(x_n,y_n)\},\{x_i\}_{i=1}^n\subseteq X^n$独立同分布，$y_i=f(x_i)\in Y$
二分类问题基于数据S，从假说集合H中选择一个h，期望误差：
&emsp;&emsp;$E_{x-D}[h(x)\ne f(x)]=1*P_{x-D}[h(x)\ne f(x)]+0*P(x-D)[h(x)=f(x)]$，1表示错误分类代价

## SVM

考虑超平面$w^Tx+b=0$
给定$a>0$，要求其平面对正样本：$y=1,w^Tx+b\ge a$；对负样本：$y=-1,w^Tx+b\le -a$
样本$x_i$到超平面$w^T+b=0$的距离为：$\frac{|w^Tx_i+b|}{|w|}=\frac{y_i(w^Tx_i+b)}{|w|}$
样本集S到超平面$w^T+b=0$的距离$\rho$为：$\rho=\min_{(x_i,y_i)}=\frac{y_i(w^Tx_i+b)}{|w|}=\frac{a}{|w|}$，即距离超平面最近的点的距离
故优化目标为$\max_{w,b}\frac{a}{|w|},s.t.y_i(w^Tx_i+b)\ge a,\forall i$，即使距离超平面的点与超平面的距离a最大

### 线性可分

优化目标为$\max_{w,b}\frac{a}{|w|},s.t.y_i(w^Tx_i+b)\ge a,\forall i$
其中a未知，正样本$w^T+b\ge a$，负样本$w^T+b\le -a$
即要最近的点的距离最大化$y_i(w^Tx_i+b)\ge a$，这是因为正确分类的时候，$y$与$w^Tx+b$同符号
要求在$w,b$约束的条件下使$\frac{a}{|w|}$最大，最大几何间断
可以定义$\widehat{w}=\frac{w}{a},\widehat{b}=\frac{b}{a}$，可有$(w,b)\rightarrow(\widehat{w},\widehat{b})$
故原来的优化目标可变为$\max_{\widehat{w},\widehat{b}}\frac{1}{|\widehat{w}|},s.t. y_i(\widehat{w}^Tx_i+\widehat{b})\ge 1$
由于a不影响符号，都线性可分，所以不影响分类性能
而$\max_{\widehat{w},\widehat{b}}\frac{1}{|\widehat{w}|}$等价于$\min_{\widehat{w},\widehat{b}}|\widehat{w}|$
故可有$\min_{\widehat{w},\widehat{b}}\frac{1}{2}|\widehat{w}|,s.t.y_i(\widehat{w}^Tx_i+\widehat{b})\ge 1,\forall i$，其中加$\frac{1}{2}$是为了便于计算的系数
<font color='red'><b>
将约束条件融入到优化目标函数中，建立拉格朗日公式
</font></b>
可有：
$L(\widehat{w},\widehat{b},\alpha)=\frac{1}{2}|\widehat{w}|^2-\sum_{i=1}^n\alpha_i(y_i(\widehat{w}^Tx_i+\widehat{b})-1),s.t.\alpha_i\ge 0$
其中$\alpha$是拉格朗日系数，$\alpha=[\alpha_1,...,\alpha_n]^T$
此时优化目标变为$\min_{\widehat{w},\widehat{b}}(\max_{\alpha_i\ge 0}L(\widehat{w},\widehat{b},\alpha))$
即表示$L$先对$\alpha$求最大，后对$\widehat{w},\widehat{b}$求最小
进行展开可有
$L(\widehat{w},\widehat{b},\alpha)=\frac{1}{2}|w|^2-\sum_{i=1}^n\alpha_i y_i \widehat{w}^Tx_i-\sum_{i=1}^n\alpha_i y_i \widehat{b}+\sum_{i=1}^n\alpha_i$
<font color='red'><b>
需要转换为其对偶问题来求解。原始问题通过满足KKT(<font size=4>原始变量求偏导，最大时约束部分为0</font>)，已转化为对偶问题，后让$L(\widehat{w},\widehat{b},\alpha)$关于$\widehat{w},\widehat{b}$最小化，后对$\alpha$求极大，后用SMO求解
</font></b>
即求解$\max_{\alpha_i\ge 0}(\min_{\widehat{w},\widehat{b}}L(\widehat{w},\widehat{b},\alpha))$
此时可以考虑KKT条件
即先固定$\alpha$，然后对$\widehat{w},\widehat{b}$求导来求最小
故可有：
$\left \{ \begin{array}{c}\frac{dL}{d\widehat{w}}=|\widehat{w}|-\sum_{i=1}^n\alpha_iy_ix_i=0\\\frac{dL}{d\widehat{b}}=-\sum_{i=1}^n\alpha_iy_i=0\\ \alpha_i(y_i(\widehat{w}^Tx_i+\widehat{b})-1)=0\end{array} \right.$
代入原式后可有
$\max_{\alpha_i\ge 0}w_{(\alpha)}=\max_{\alpha_i\ge 0}(\sum_{i=1}^n\alpha_i-\frac{1}{2}\sum_{i=1,j=1}^n\alpha_i \alpha_j y_i y_j x_j^Tx_i)$
转为$\min$为
$\min_{\alpha}(\frac{1}{2}\sum_{i=1}^n\sum_{j=1}^n\alpha_i\alpha_j y_i y_j x_i^Tx_j-\sum_{i=1}^n\alpha_i,s.t.\sum_{i=1}^n\alpha_i y_i=0)$
得到$\alpha_i$之后，可有
$\widehat{w}=\sum_{i=1}^n\alpha_i y_i x_i$
又因为KKT要求$\forall i \alpha_i(y_i(\widehat{w}^Tx_i+\widehat{b})-1)=0$
所以要么$\alpha_i=0$或$y_i(\widehat{w}^Tx_i+\widehat{b})=1$
将$\widehat{w}=\sum_{i=1}^n\alpha_i y_i x_i$代入，可有
$\widehat{b}=\frac{1}{y_i}-\widehat{w}^Tx_i=\frac{1}{y_i}-\sum_{j=1}^n\alpha_j y_j(x_j^Tx_i)$
因为$y_i\in\{-1,1\}$
故可以有$\widehat{b}=y_i-\sum_{j=1}^n\alpha_j y_j (x_j^Tx_i)$
此时预测函数为：
<b>
$\widehat{h}(x)=sign(\widehat{w}^Tx+\widehat{b})$
对任何一个样本$x_i$有
$\widehat{h}(x_i)=sign(\widehat{w}^Tx_i+\widehat{b})$
即
$\widehat{h}(x_i)=sign(\sum_{j=1}^n\alpha_j y_j x_j^Tx_i+y_i-\sum_{j=1}^n\alpha_j y_j (x_j^Tx_i))$
</b>
<font color='red'><b>
可以看到，此时的预测函数对于任何一个样本，用该样本来更新权重的时候，都需要和其他全部样本进行比较，相当于每次的输入是一个<font size=5>样本对</font>
</font></b>

### 线性不可分

线性不可分的时候，引入松弛变量$\epsilon_i$，表示容许某个样本违反超平面，即优化目标变为：
$\min_{\widehat{w},\widehat{b}}(\frac{1}{2}|w|^2+C\sum_{i=1}^n\epsilon_i),s.t.y_i(w^Tx_i+b)\ge1-\epsilon_i,\epsilon_i\ge 0$
$\epsilon_i$为误差(松弛变量)，缩小间距，C是折中参数
将约束日傲剑融合到优化目标中，有拉格朗日
$L(\widehat{w},\widehat{b},\alpha,\beta)=\frac{1}{2}|\widehat{w}|^2+C\sum_{i=1}^n\epsilon_i-\sum_{i=1}^n\alpha_i(y_i(\widehat{w}^Tx_i+\widehat{b})-1+\epsilon_i)-\sum_{i=1}^n\beta_i\epsilon_i$
其中$\alpha,\beta$为拉格朗日系数，$s.t.\alpha\ge 0,\beta\ge 0,\epsilon_i\ge 0$
此时优化目标为
$\min_{\widehat{w},\widehat{b},\epsilon}(\max_{\alpha,\beta}(L(\widehat{w},\widehat{b},\epsilon,\alpha,\beta)))$
即对$\alpha,\beta$取最大，之后对$\widehat{w},\widehat{b},\epsilon$取最小
考虑KKT：
$\left \{ \begin{array}{c}\frac{dL}{d\widehat{w}}=|w|-\sum_{i=1}^n\alpha_i y_i x_i=0\\ \frac{dL}{d\widehat{b}}=\sum_{i=1}^n\alpha_i y_i=0\\ \frac{dL}{d\epsilon_i}=C-\alpha_i-\beta_i=0,注意这里是对某一个\epsilon_i求导 \\ \alpha_i(y_i(\widehat{w}^Tx_i+\widehat{b})-1+\epsilon_i)=0 \\ \beta_i\epsilon_i=0 \end{array} \right.$
由以上公式，可转化为对偶问题
$\max_{\alpha,\beta}(\min_{\widehat{w},\widehat{b},\epsilon}(L(\widehat{w},\widehat{b},\epsilon,\alpha,\beta)))$
代入原式可有
$L(\widehat{w},\widehat{b},\epsilon,\alpha,\beta)=-\frac{1}{2}\sum_{i=1}^n\sum_{j=1}^n\alpha_i\alpha_j y_i y_j x_i^Tx_j+\sum_{i=1}^n\alpha_i$
对$\alpha_i$求极大，可求得$\widehat{w},\widehat{b}$
$\widehat{w}=\sum_{i=1}^n\alpha_i y_i x_i,\widehat{b}=(1-\epsilon_i)y_i-\sum_{i=1}^n\alpha_i y_i x_i^Tx_j$
<font color='red'><b>
可以看到，仍然可以用<font size=5>样本对</font>来解决
</font></b>

## 核函数

采用样本对时就可以考虑使用核函数。
<b>
核函数可以处理即便引入松弛变量也不能处理的非线性问题，即升维到高维空间
</b>
特征映射：将数据从原始空间映射到高维空间的函数，如极坐标/二次多项式
决策函数：$h(x)=\widehat{w}^Tx+\widehat{b}\Longrightarrow h'(x)=\widehat{w}^T\phi(x)+\widehat{b}$
优化目标：$\min_{\widehat{w},\widehat{b},\epsilon} \frac{1}{2}|\widehat{w}|^2+C\sum_{i=1}^n\epsilon_i,s.t.y_i(\widehat{w}^T\phi(x_i)+\widehat{b})\ge1-\epsilon_i,\forall i$
当不知道特征映射的时候，就不可解
重点在于如何计算特征映射以及如何找到合适的特征映射
<font color='red'><b>
核函数：样本在特征空间中（特征映射决定的空间）的内积，即
$k(x_i,x_j)=<\phi(x_i),\phi(x_j)>=\phi(x_i)^T\phi(x_j)$
</font></b>
核函数会是一个矩阵，样本的内积矩阵
此时优化目标进行拉格朗日
$L(\widehat{w},\widehat{b},\epsilon,\alpha,\beta)=\frac{1}{2}|w|^2+C\sum_{i=1}^n\epsilon_i-\sum_{i=1}^n\alpha_i(y_i(\widehat{w}^T\phi(x_i)+\widehat{b})-1+\epsilon_i)$
其中$\alpha,\beta$是拉格朗日乘子
有KKT，即
$\left \{ \begin{array}{c}\frac{dL}{d\widehat{w}}=0\\ \frac{dL}{d\widehat{b}}=0\\ \frac{dL}{d\epsilon_i}=0\\ \alpha_i(y_i(\widehat{w}^T\phi(x_i)+\widehat{b})-1+\epsilon_i)=0\\ \beta_i\epsilon_i=0\end{array} \right .$
优化目标为
$\min_{\alpha,\beta(\beta可删去)}(\frac{1}{2}\sum_{i=1}^n\sum_{j=1}^n\alpha_i\alpha_j y_i y_j \phi(x_i)^T\phi(x_J))-\sum_{i=1}^n\alpha_i$
$s.t.\sum_{i=1}^n\alpha_i y_i=0,C\ge\alpha_i\ge 0$
即
$\min_{\alpha}(\frac{1}{2}\sum_{i=1}^n\sum_{j=1}^n\alpha_i\alpha_j y_i y_j k(x_i,x_j))-\sum_{i=1}^n\alpha_i$
$s.t.\sum_{i=1}^n\alpha_i y_i=0,C\ge\alpha_i\ge 0$
其中$\alpha$只与样本数n有关，与样本维度无关
通过选好的特征映射，找到好的核函数
<font color='red'>
对一个征订核函数，特征映射必然存在，保证正定，不一定唯一
正定函数：处零点外恒为正值的标量函数
</font>

<div STYLE="page-break-after: always;"></div>

# 003 计算学习理论PAC

## base

样例集：独立同分布$D={(x_1,y_1),...,(x_m,y_m)}$，其中$y\in\{1,-1\}$
h为x到y的一个映射
泛化误差：$E(h,D)=P_{x-D}(h(x)\ne y)$分类器的期望误差，分类器在新样本集上的误差
经验误差：$\widehat{E}(h,D)=\frac{1}{m}\sum_{i=1}^nI(h(x_i)\ne y_i)$，其中I表示相同时返回0，不同时返回$I$，一般为1.给定样例集上的平均误差，分类器在训练集上的误差
泛化误差小，经验误差大意味着没有完全学习；泛化误差大，经验误差小意味着过拟合
误差参数：$\epsilon$，是$E(h)$的上限，是认为给定的一个量，即我们期望的分类器对于测试样本的最大误分概率
一致性：$h$在$D$上的经验误差为0，则称$h$与$D$一致
不合：对两个映射$h_1,h_2\in X\rightarrow Y,D(h_1,h_2)=P_{x-D}(h(x_1)\ne h(x_2))$
概念：concept，样本空间X到标记空间Y的映射，决定X的真实标记Y
目标概念：对任何样例$(x_i,y_i)$，均有$C(x_i)=y_i$成立，则$C$为目标概念
概念类：目标概念的集合
假设空间：给定学习算法$L$，他所考虑的所有可能概念的集合$H$，对$h\in H$，由于不确定$h$是否接近或等于$C$，故为假设
学习过程为$L$在$H$中搜索过程，找一个$h$接近$C$或等于$C$
可分：若$C\in H$，即$H$中存在假设使所有实例完全分开，则该问题对学习算法$L$是可分的
不可分：$C\notin H$，即$H$中不存在能将所有样本完全分开的假设
$h$应该尽可能接近$C$而不能精确等于$C$：

1. $D$数据集不无限，故会有一些在$D$上等效的$h$，而算法$L$无法区分这些$h$
2. 对同样大小的不同$D$，会有偶然性

## PAC，probably approximately correct，概率相似正确

以较大把握能够学习到较好的模型，即能够以较大概率学习到误差满足预设上限的模型

### PAC辨识，PAC identify

对$0<\epsilon,\epsilon<1$，所有$c\in C$和分布$d\in D$，若存在学习算法$L$，其输出假设$h\in H$满足：
$P(E(h)\le \epsilon)\ge 1-\sigma$，即$E(h)$泛化误差小于$\epsilon$上限这个事件的概率不会小于$1-\sigma$
则称学习算法$L$能够从假设空间$H$中PAC辨识概念类$C$
在计算的时候可以直接计算$P(E(c)\le \epsilon)\ge 1-\sigma$
表示$L$能够以较大概率$1-\sigma$学得目标概念$c$的近似，误差最多为$\epsilon$

### PAC可学习，PAC learning

给$m$个样本，有$m\ge poly(\frac{1}{\epsilon},\frac{1}{\sigma},size(x),size(c))$
即表示$L$能从$H$中PAC辨识概念类$C$
则称$C$对$H$而言是PAC可学习的
即限定了学习所需要的样本个数

### PAC学习算法

若$L$使$C$为PAC可学习的，且$L$的运行时间也是多项式函数$poly(\frac{1}{\epsilon},\frac{1}{\sigma},size(x),size(c))$，则称$C$是高效PAC可学习的，$L$为$C$的PAC学习算法

### 样本复杂度sample complexity

满足PAC学习算法$L$所需要的$m\ge poly(\frac{1}{\epsilon},\frac{1}{\sigma},size(x),size(c))$中最小的m，即最少需要的样本个数
对$H$而言，随着$H$的增大，包含任意$c$的可能性也随之上升，但找到某个具体概念$c$的难度也越来越大。当$H$有限时为有限假设空间

### 恰PAC可学习properly PAC learnable

$H=C$，即学习算法能力与学习任务恰好匹配的理想情况，一般不等于

### rademacher复杂度

给定训练集$D=\{(x_1,y_1),...,(x_n,y_n)\}$
$\widehat{h}$的经验误差为$\widehat{E}(h)=\frac{1}{m}\sum_{i=1}^m I (h(x_i)\ne y_i)$
由于$I=1$，而$h(x_i),y_i\in\{-1,1\}$，故只有四种情况$(1,-1),(-1,1),(1,1),(-1,-1)$，即同符号为合格，此时$I$应该为0；反符号为不合格，此时$I$应该为1，即可以将$I$表示为：
$I(h(x_i)!=y_i)=\frac{1}{2}(1-y_i h(x_i))$\
故上式可写为$\widehat{E}(h)==\frac{1}{m}\sum_{i=1}^m\frac{1}{2}(1-y_i h(x_i))$
即$\widehat{E}(h)=\frac{1}{2}-\frac{1}{2m}\sum_{i=1}^my_i h(x_i)$
其中$\frac{1}{m}\sum_{i=1}^my_i h(x_i)$体现了$h(x_i)$与$(y_i)$的一致性(是否为1)，即预测与真实
若对所有的i，均有$h(x_i)=y_i$，则取最大值1
经验误差最小假设：$\argmax_{h\in H}\frac{1}{m}\sum_{i=1}^my_i h(x_i)$
若$y_i$随机，不再是真实标记，即加入了噪声，有$\sup_{h\in H}\frac{1}{m}\sum_{i=1}^m\sigma_i h(x_i)$，即遍历$h$使得尽可能大
其中$\sigma_i$为redemacher随机变量，以0.5的概率取-1，以0.5概率取1
<font color='red'>
这里的目的是挑战h的复杂度，看看最大复杂度是多少。挑战H的复杂度，对任意标签，都刻有一个f与之匹配
考虑$h\in H$，期望为$E_{\sigma}[\sup_{h\in H}\frac{1}{m}\sum_{i=1}^m\sigma_i h(x_i)]$
</font>
$\sigma=\{\sigma_1,...,\sigma_m\},E_{\sigma}\in [0,1]$，体现H的复杂度/表现能力
当$|H|=1$时，只有一个$h,E_{\sigma}=0$
当$|H|=2^m$且$H$能打散$D$时，对任意$\sigma$总有一个$h$使$h(x_i)=\sigma_i,E_{\sigma}=1$，即对某一个固定的$D$，不管其真实标签如何变化，在假设空间$H$中都有一个假设$h$使得预测标签和真实标签相匹配，即可以理解为这个假设空间对于这个数据集是充分的。

### 函数空间F关于训练集Z的经验redemacher复杂度

对实值函数空间$F:Z\rightarrow[0,1]$，根据分布$D$从$Z$中独立同分布采样得到数据集$Z=\{z_1,...,z_m\}$，已知：
经验误差的复杂度：$\widehat{R_z}(F)=E_{\sigma}[\sup_{f\in F}\frac{1}{m}\sum_{i=1}^m\sigma_i f(z_i)],\sigma_i=\{-1,1\} \forall i$
即这一步是给出初始的经验误差期望计算公式
函数空间的复杂度：$R_m(F)=E_z[\widehat{R_z}F]$
经验误差的复杂度表示针对某一样本集$Z$，函数空间(假设空间)$F$中最匹配的$f$的误差的期望
函数空间的复杂度表示对全部样本，经验误差的复杂度的期望，也可表示泛化误差的复杂度
<font color='red'><b>
由于我们需要估计一个分类器的泛化误差，故需要采样一个样本集Z，然后通过公式求出泛化误差的上界
证明：$E|f(z)|\le \frac{1}{m}\sum_{i=1}^mf(z_i)+2R_m(F)+\sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}}$
即泛化误差的上界是某样本集Z的经验误差+2倍函数空间复杂度+样本度量
<font size=4>
注意，样本度量中的参数$\sigma$与上文提到的标签$\sigma$是不一样的，一个是标量一个是向量
</font>
</font></b>
假设函数$\phi(Z)=\sup(E|f(z)|-\frac{1}{m}\sum_{i=1}^mf(z_i))$
即函数$\phi(Z)$是泛化误差-经验误差的关于$f$遍历的最大值
<b>
有mcdiarmid不等式：$设\forall i |f(x_1,...,x_i,...,x_n)-f(x_1,...,x'_i,...,x_n)|\le c_i$
则$P_r(|f(x_1,...,x_i,...,x_n)-E[f(x_1,...,x_i,...,x_n)]|\ge t)\le 2\exp(-\frac{2t^2}{\sum_{i=1}^nc_i^2})$
即某变量与其期望的偏差值大于参数$t$的概率小于$2\exp(-\frac{2t^2}{\sum_{i=1}^nc_i^2})$
</b>
可以假设$Z'=\{z_1,...,z'_i,...,z_m\}$
有$|\phi(Z)-\phi(Z')|=|\sup_{t\in F}(E_Z[f(z)]-\frac{1}{m}\sum_{i=1}^mf(z_i)-\sup_{t\in F}(E_{Z'}[f(z')]-\frac{1}{m}\sum_{i=1}^mf(z'_i))|$
因为$\sup_xf(x)+\sup_xp(x)\ge \sup_x(f(x)+g(x))$
所以$|\phi(Z)-\phi(Z')|\le |\sup_{t\in F}(E_{Z}[f(z)]-\frac{1}{m}\sum_{i=1}^mf(z_i)-E_{Z'}[f(z')]+\frac{1}{m}\sum_{i=1}^mf(z'_i))|$
由于$E_Z[f(z)]$代表泛化误差，与某一样本集无关
故可以有$|\phi(Z)-\phi(Z')|\le |\sup_{t\in F}(\frac{1}{m}(f(z'_i)-f(z_i)))|$
由于对此公式而言，$\sup$/不影响符号，所以可以拿出来
$|\phi(Z)-\phi(Z')|\le \sup_{t\in F}|(\frac{1}{m}(f(z'_i)-f(z_i)))|$
因为$f(z_i)$表示$z_i$的标签预测值$\in\{0,1\}$<font color='red'>这里注意对标签的修改</font>
所以可以有上界：
$|\phi(Z)-\phi(Z')|\le\frac{1}{m}$
所以可以把$\frac{1}{m}$设为参数$c_i$
根据macdiarmid不等式可有
$P_r(|\phi(Z)-E_Z[\phi(Z)]\ge t|)\le 2 exp(-2mt^2)$
这里可令$\sigma=exp(-mt^2)$
故可以有$t=\sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}}$
<b>
此时的$\sigma$就是我们求证的公式中的$\sigma$
</b>
代入可有$P_r(|\phi(Z)-E_Z[\phi(Z)]|\ge \sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}}|)\le 2\sigma$
将绝对值拆开可以有
$\left\{ \begin{array}{} P_r(\phi(Z)-E_Z[\phi(Z)]\le -\sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}})\le \sigma \\ P_r(\phi(Z)-E_Z[\phi(Z)]\ge \sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}})\le \sigma \end{array}\right.$

进行转换可有
$P_r(\phi(Z)-E_Z[\phi(Z)]\ge -\sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}})\ge 1-\sigma$
即$P_r(E_Z[\phi(Z)]\le \phi(Z)+\sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}})\ge 1-\sigma$
因为
$\phi(Z)=\sup_{f\in F}(E[f(Z)]-\frac{1}{m}\sum_{i=1}^mf(z_i))$
其中$E_Z[f(z)]$是泛化误差，$\frac{1}{m}\sum_{i=1}^mf(z_i)$是经验误差
又因为某函数必然小于该函数的上界
$E[f(Z)]-\frac{1}{m}\sum_{i=1}^mf(z_i)\le\sup_{f\in F}(E[f(Z)]-\frac{1}{m}\sum_{i=1}^mf(z_i))$
故可有
$E[f(Z)]\le\frac{1}{m}\sum_{i=1}^mf(z_i)+\sup_{f\in F}(E[f(Z)]-\frac{1}{m}\sum_{i=1}^mf(z_i))$
代入之前的不等式可有
$P_r(\sup_{f\in F}(E_Z[f(Z)])-\frac{1}{m}\sum_{i=1}^mf(z_i)\le E_Z[\phi(z)]+\sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}})\ge 1-\sigma$
所以有
$P_r(\sup_{f\in F}(E_Z[f(Z)])\le \frac{1}{m}\sum_{i=1}^mf(z_i)+E_Z[\phi(z)]+\sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}})\ge 1-\sigma$
因为$E_Z[\phi(z)]=E_Z[\sup_{f\in F}(E_{Z'}[f(z')]-\frac{1}{m}\sum_{i=1}^mf(z‘_i))]$
这里的$Z'$仅作为区分，无实际意义，表示将$\phi(z)$代入，因为是泛化误差，对样本集无要求
故可以用$\frac{1}{m}\sum_{i=1}^mf(z‘_i)$代替$f(z')$
即用期望代替函数，代入可以有
$E_Z[\phi(z)]=E_Z[\sup_{f\in F}(E_{Z'}[\frac{1}{m}\sum_{i=1}^mf(z'_i)]-\frac{1}{m}\sum_{i=1}^mf(z_i))]$
因为$\sup_x(E[f(x)])\le E[\sup_x(f(x))]$，期望的最大小于等于最大的期望
故可以有
$\sup_{f\in F}(E_{Z'}[\frac{1}{m}\sum_{i=1}^mf(z'_i)]-\frac{1}{m}\sum_{i=1}^mf(z_i))\le E_{Z'}[\sup_{f\in F}(\frac{1}{m}\sum_{i=1}^mf(z'_i)-\frac{1}{m}\sum_{i=1}^mf(z_i))]$
故可以有
$\sup_{f\in F}(E_{Z'}[\frac{1}{m}\sum_{i=1}^mf(z'_i)]-\frac{1}{m}\sum_{i=1}^mf(z_i))\le E_{Z'}[\sup_{f\in F}(\frac{1}{m}\sum_{i=1}^m(f(z'_i)-f(z_i)))]$
故可以得到
$E_Z[\phi(z)]\le E_ZE_{Z'}[\sup_{f\in F}(\frac{1}{m}\sum_{i=1}^m(f(z'_i)-f(z_i)))]$
令$\sigma_i\in\{+1,-1\}$，<b>注意这里的$\sigma_i$与概率中的参数$\sigma$无关</b>
因为$\sup_x\sum_{i=1}^mf(x_i)\le E_{\sigma}\sup_x\sum_{i=1}^n\sigma_if(x_i)$，可以把$f(x_i)$中的负转为正，因为有$\sup$取权值
所以有
$E_ZE_{Z'}[\sup_{f\in F}(\frac{1}{m}\sum_{i=1}^m(f(z'_i)-f(z_i)))]\le E_{\sigma}E_{Z}E_{Z'}[\sup_{f\in F}(\frac{1}{m}(\sum_{i=1}^m\sigma_i f(z'_i)+sum_{i=1}^m-\sigma_i f(z_i)))]$
因为$\sigma_i \in\{1,-1\}$且随机，且具有$\sup$取极值
故$-\sigma_i$与$\sigma_i$一致(仅限此时)
故可以有
$E_ZE_{Z'}[\sup_{f\in F}(\frac{1}{m}\sum_{i=1}^m(f(z'_i)-f(z_i)))]\le E_{\sigma}E_{Z'}[\sup_{f\in F}(\frac{1}{m}(\sum_{i=1}^m\sigma_i f(z'_i)))]+E_{\Sigma}E_{Z}[\sup_{f\in F}(\frac{1}{m}(sum_{i=1}^m\sigma_i f(z_i)))]$
因为样本经验误差的复杂度的计算公式为
$\widehat{R_Z}(F)=E_{\sigma}[\sup_{f\in F}\frac{1}{m}\sum_{i=1}^m\sigma_i f(z_i)]$
故可以代入有$E_ZE_{Z'}[\sup_{f\in F}(\frac{1}{m}\sum_{i=1}^m(f(z'_i)-f(z_i)))]\le E_{Z'}[\widehat{R_{Z'}}(F)]+E_Z[R_Z(F)]$
即可以用两个样本集$Z,Z'$的经验误差的复杂度的期望之和来表示上界
因为函数空间的复杂度为$E_Z[\widehat{R_Z}(F)]=R_m(F)$，且函数空间的复杂度对任意的样本集是一致的
故代入可以有$E_ZE_{Z'}[\sup_{f\in F}(\frac{1}{m}\sum_{i=1}^m(f(z'_i)-f(z_i)))]\le 2R_m(F)$
而$\phi(Z)=\sup_{f\in F}(E|f(z)|-\frac{1}{m}\sum_{i=1}^mf(z_i))$
即$\phi(Z)=E_Z[\sup_{f\in F}(f(z)-\frac{1}{m}\sum_{i=1}^mf(z_i))]$
即$\phi(Z)=E_Z[\sup_{f\in F}(\frac{1}{m}\sum_{i=1}^mf(z'_i)-\frac{1}{m}\sum_{i=1}^mf(z_i))]$
故可以有$E_Z[\phi(z)]=E_ZE_{Z'}[\sup_{f\in F}(\frac{1}{m}\sum_{i=1}^m(f(z'_i)-f(z_i)))]$，这里是因为$Z,Z'$是等价的，都是样本集
故可有$E_Z[\phi(z)]\le 2R_m(F)$
代入原始的不等式$P_r(\sup_{f\in F}(E_Z[f(Z)])\le \frac{1}{m}\sum_{i=1}^mf(z_i)+E_Z[\phi(z)]+\sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}})\ge 1-\sigma$
可有扩大后的公式
$P_r(\sup_{f\in F}(E_Z[f(Z)])\le \frac{1}{m}\sum_{i=1}^mf(z_i)+2R_m(f)+\sqrt{\frac{\ln(\frac{1}{\sigma})}{2m}})\ge 1-\sigma$

<div STYLE="page-break-after: always;"></div>

# 004 SGD 随机梯度下降

## base

如何快速找到最优解(迭代，从一个初始解开始，向正确方向努力)
<b>
即$k_{t+1}=k_t+\alpha g(k_t)$
其中$\alpha$为步长，$g(k_t)$为下降方向
</b>
$g(k_t)$条件：$\left \{ \begin{array}{} g(k_t)要让k_{t+1}向最优解逼近(判定)\\ k_t达到最优解时g(k_t)=0 \end{array} \right .$
即表示当$k_{t+1}=k_t$时有$g(k_t)=0$
核心问题：找一个满足条件的$g(k_t)$，这里选择的是函数$f(k)$的梯度
梯度优化：方向+步长，步长越大，可能发生徘徊；步长越小，找的越慢
大规模梯度优化中计算开销打，时间复杂度高

## 梯度下降法（针对可微函数）

$d f(w)=(\frac{d f(w)}{d w_1},\frac{d f(w)}{d w_2},...,\frac{d f(w)}{d w_d})^T$
要求$w_{t+1}=w_t-\eta df(w_t)$，用$-\eta$为的是梯度的反方向

### 求证收敛，即向结果偏移

<b>

求证$f(w_{t+1})\le f(w_t)$

</b>

因为$f(w_{t+1})=f(w_t-\eta df(w_t))$
进行泰勒展开可有
$f(w_{t+1})=f(w_t)+(w_t-\eta df(w_t)-w_t)^Td f(w_t)$
可有$f(w_{t+1})=f(w_t)-\eta df(w^t)^Td f(w_t)$
即$f(w_{t+1})=f(w_t)-\eta|d f(w_t)|^2,\eta>0$
因为$\eta|d f(w_t)|^2\ge 0$
故$f(w_{t+1})\le f(w_t)$

### 求证上限，即迭代上线

假设$|w_*|$为最优解，且$|w_*|\le B$
假设输出的权重$\widehat{w}$是当前T次迭代的所有权证权重的平均值，即$\widehat{w}=\frac{1}{T}\sum_{t=1}^Tw_t$
要求其有迭代上界，即找到输出权重找到的接与最优权重找到的解的差异，即$f(\widehat{w})-f(w_*)$的差异
<b>
这里是由于凸函数的性质，沿着梯度下降的方向迭代，偏差应该是下降的。
可以把$w_*$理解为最优解，$\widehat{w}$是当前解，$T$为迭代次数
</b>
$f(\widehat{w})-f(w_*)\le \frac{1}{T}\sum_{t=1}^T(f(w_t)-f(w_*))$
因为微分的时候，可以有$f(w_t)-f(w_*)\le <w_t-w_*,d f(w_t)>$
即梯度乘x的长度大于等于y的长度，之前已经证明了梯度会减小
又因为$w_{t+1}=w_t-\eta v_t,v_t=d f(w_t),\eta$为步长
代入可以有
$f(\widehat{w})-f(w_*)\le \frac{1}{T}\sum_{t=1}^T(f(w_t)-f(w_*))$
即
$f(\widehat{w})-f(w_*)\le \frac{1}{T}\sum_{t=1}^T(<w_t-w_*,d f(w_t)>)$
即
$f(\widehat{w})-f(w_*)\le \frac{1}{T}\sum_{t=1}^T(<w_t-w_*,v_t>)$
又因为可以乘一个$\eta$再除以一个$\eta$
$<w_t,w_*,v_t>=\frac{1}{\eta}<w_t-w_*,\eta v_t>$
因为矩阵乘法可以有：
$x^Ty=-\frac{1}{2}(|x-y|^2-|x|^2-|y|^2)$
故可有
$\frac{1}{\eta}<w_t-w_*,\eta v_t>=-\frac{1}{2\eta}(|w_t-w_*-\eta v_t|^2-|w_t-w_*|^2-|\eta v_t|^2)$
因为$w_{t+1}=w_t+\eta v_t$
代入可有
$\frac{1}{\eta}<w_t-w_*,\eta v_t>=-\frac{1}{2\eta}(|w_{t+1}-w_*|^2-|w_t-w_*|^2-|\eta v_t|^2)$
故可有，求和展开后
$\sum_{t=1}^T(<w_t-w_*,v_t>)=-\frac{1}{2\eta}(|w_{t+1}-w_*|^2-|w_1-w_*|^2)+\frac{\eta}{2}\sum_{t=1}^T|v_t|^2$
因为正常运行时，$w_{t+1}$很接近$w_*$，故可以近似
$\sum_{t=1}^T(<w_t-w_*,v_t>)\le \frac{1}{2\eta}(|w_1-w_*|^2)+\frac{\eta}{2}\sum_{t=1}^T|v_t|^2$
而因为$w_1$是初识给定的初始解$v$
故可有
$\sum_{t=1}^T(<w_t-w_*,v_t>)\le \frac{|w_*|^2}{2\eta}+\frac{\eta}{2}\sum_{t=1}^T|v_t|^2$
而之前给了一个上界最小值$B$，这里可以假设一个$\rho$，使
$|w_*|\le B,|v_t|\le \rho$
这里的$\rho$表示导数的上界，或者说梯度的上界
故有
$\sum_{t=1}^T(<w_t-w_*,v_t>)\le \frac{B^2}{2\eta}+\frac{\eta T}{2}\rho^2$
则可有
$\frac{1}{T}\sum_{t=1}^T(<w_t-w_*,v_t>)\le \frac{B^2+\eta^2T\rho^2}{2\eta T}$
其中只有一个变量$\eta$，即我们人为给定的步长，对其求导可以得到步长的最优解
$\eta=\sqrt{\frac{B^2}{\rho^2-T}}$
代入可有
$\frac{1}{T}\sum_{t=1}^T(<w_t-w_*,v_t>)\le \frac{BP}{\sqrt{T}}$
即
$f(\widehat{w})-f(w_*)\le \frac{BP}{\sqrt{T}}$
即误差有一个上界，当误差给定的时候，即
$f(\widehat{w})-f(w_*)\le \epsilon$，即要求与期望的结果相差小于某个给定的参数的时候，可有
$T\ge \frac{B^2P^2}{\epsilon^2}$
此时$T$为迭代次数/收敛速率，表示至少这么多次才能将误差降低到$\epsilon$，记为
$O(\frac{1}{\epsilon})$
比较慢，$O(\frac{1}{\epsilon})$比$O(\frac{1}{\sqrt{\epsilon}})$更快

## 子（次）梯度下降

函数不可微时，如何找下降方向
$\forall u,f(u)\ge f(w)+<u-w,d f(w)>$
只要满足上面的条件即可，即
$\forall u,f(u)\ge f(w)+<u-w,v>,v$是次梯度
含义是，对任意向量$v$，对任意的权重$u$都有上式成立，则$v$是在$u$点的次梯度

### 例：求$|x|$的次梯度

$|x| \left\{ \begin{array}{} 1&x>0\\-1&x<0\\?&x=0 \end{array} \right.$
令任意$u$满足$\forall u,|u|\ge |w|+<u-w,v>$
可有$|u|\ge <u,v>$
即$|u|\ge uv\Longrightarrow v\in[-1,1]$
故可有
$|x| \left\{ \begin{array}{} 1&x>0\\-1&x<0\\v\in[-1,1]&x=0 \end{array} \right.$

### 例：求$f(w)=\max\{0,1-y<w,x>\}$的次梯度

可给定$g_i(w)$均为凸函数，则可有
$d g_j(w)\in d g(w),j\in \argmax g_i(w)$
即$\forall i,g_i(w^Tx+b)\ge 1-\epsilon_i\Longrightarrow \epsilon_i\ge 1-g_i(w^Tx_i+b)$
<font color='red'><b>
个人理解为：当某一个点可以有多个函数表示的时候，选择其中最大的作为次梯度
</font></b>
故当$f(w)=\max\{0,1-y<w,x>\}$时，他需要进行分段
$\left \{ \begin{array}{} -y_ix_i & 1-y_i<w,x_i>> 0\\Co\{-y_ix_i,0\}&1-y_i<w,x_i>=0\\0&other \end{array}\right .$
<font color='red'><b>注意，第2个情况中是向量的凸包，是一个集合</font></b>

## SGD随机梯度下降

不要求下降方向是梯度方向，只需要每次下降一点点
$v$可以使随机变量，但要求$E(v)$必须是当前位置的次梯度里面的一个
一般不能求接待约束的问题，因为要求计算梯度后还要满足约束
$\eta>0,T>0,w=0$初始化

```python
for t=1,...,T:阈值
    选一个vt，要求E(vt)在次梯度中
    更新wt+1=wt-ηvt
```

输出$\widehat{w}=\frac{1}{T}\sum_{t=1}^Tw_t$

### 例：$\min_{w,\epsilon}\frac{\lambda}{2}|w|^2+\sum_{i=1}^n\epsilon_i,s.t.y_i(w^Tx_i)\ge 1-\epsilon_i,\epsilon_i\ge 0$

首先转化为无约束
$\min_{w,\epsilon}\frac{\lambda}{2}|w|^2+\sum_{i=1}^n\max\{0,1-y_i(w^Tx_i)\}$
这里是根据$\epsilon_i\ge 1-y_i(w^Tx_i)$得到的，个人感觉类似于拉格朗日方程的求法
然后观察，对于函数$f(w)=\frac{\lambda}{2}|w|^2+\sum_{i=1}^n\max\{0,1-y_i(w^Tx_i)$
前半部分是可微的$\frac{\lambda}{2}|w|^2$，后半部分是不可微的，需要用次梯度
求导可有$\frac{dw_t}{df}=\lambda w_t+v_t$
其中$v_t$就是次梯度
所以针对任意一个点，可有
$w_{t+1}=w_t-\frac{1}{\lambda t}(\lambda w_t+v_t)$
这里我们人为设定步长$\eta=\frac{1}{\lambda t}$，感觉只是为了简便计算，对结果无影响。
将上式拆开可有
$w_{t+1}=w_t-\frac{1}{\lambda t}\lambda w_t-\frac{1}{\lambda t}v_t$
即
$w_{t+1}=\frac{t-1}{t}w_t-\frac{1}{\lambda t}v_t$
将$w_t=w_{t-1}-\eta(\lambda w_{t-1}+v_{t-1})$代入可有
$w_{t+1}=\frac{t-1}{t}(w_{t-1}-\eta(\lambda w_{t-1}+v_{t-1}))-\frac{1}{\lambda t}v_t$
即$w_{t+1}=\frac{t-1}{t}(\frac{t-2}{t-1}w_{t-1}-\frac{1}{\lambda(t-1)}v_{t-1})-\frac{1}{\lambda t}v_t$
由此，可以一直推导到$w_0=0$初始解，可有
$w_{t+1}=-\frac{1}{\lambda t}\sum_{i=1}^tv_i$
即某一点的下一个迭代的权重$w_{t+1}$与之前的权重无关，只与每一次迭代的次梯度有关。
而选择步长为$\eta=\frac{1}{\lambda t}$只是为了约去每一次迭代的权重$w_i$

当约束条件拿不进去的时候，就进行缩放来解决

<div STYLE="page-break-after: always;"></div>

# 005 multi-class 多分类问题

## base

给定训练样本集$S=\{(x_1,y_1),...,(x_m,y_m)\},\{x_i\}_{i=1}^m\subseteq X^m$独立同分布，$y_i=f(x_i)\in Y(\forall i=1,...,m)$
目标是基于数据$S$，从假说集合$H$中选择一个$h$
$E_{x-D}[sign(h(x))\ne f(x)]$
找一个$h$使得$\forall x,f(x)=h(x)$或不同最小
对于多分类问题，则是$sign(argmax(h(x)))\ne f(x)$取可能性最大的一位
当$y=\{1,2,3,4,5\}$时，表示有多个标签，将会根据所有的标签计算一个值$h(x_i,y_1),...,h(x_i,y_5)$，取分数最大的
当$x_i$与$y_i$匹配时，要求：
$\left . \begin{array}{} \forall y\ne y_i&h(x_i,y_i)-h(x_i,y)\ge 0&测试\\\forall y\ne y_i&h(x_i,y_i)-h(x_i,y)\ge 1&训练 \end{array}  \right .$
其实就是
<font color='red'><b>
$h(x_i,y_i)=w_{y_i}^Tx_i$
是哪一类，则采用哪一类的法向量(权重),$w=\{w_1,...,w_k\}$
注意，k是标签的个数

要求是$w_{y_i}^Tx_i-w_y^Tx_i\ge \tau$
$\tau$是某一个变量，是人为设置的，上文设置的是1

故优化目标为
$\min_{w,\epsilon}\frac{1}{2}\sum_{l=1}^k|w_l|^2+C\sum_{i=1}^m\epsilon_i,s.t.\forall i\in[1,m],\forall l\in Y-\{y_i\},w_{y_i}^Tx_i\ge w_l^Tx_i+1-\epsilon_i$
</font>
其中$k$是标签的种类个数，$m$为样本个数
$y_i$是$x_i$的真实标签或者说期望标签
$l$是所有的不是真实标签的标签，或者说错误标签
$x_i$可以用核函数$\phi(x_i)$代替
$\epsilon_i$是松弛变量
注意，这里本应该是
$\forall i \in[1,m],\forall y ,y\ne y_i ,w_{y_i}^Tx_i\ge w_{y}^Tx_i+1-\epsilon_{iy}$
即应该针对每一个错误的y都应该与正确的$y_i$有一个松弛变量，但这里为了简化计算，取
$\epsilon_i=\max\epsilon_{iy}$
故有$\forall i \in[1,m],\forall y ,y\ne y_i ,w_{y_i}^Tx_i\ge w_{y}^Tx_i+1-\epsilon_{i}$

要求最大化每一个间距$\frac{1}{|w|}$
决策函数：$\argmax_{y_i\in y}w_{y_i}^Tx$取最大
</b>

### one-versus-all

多分类转二分类
两两坐庄，一个正类，剩下的全为负类，以此类推
$\forall x\in X,h(x)=\argmax_{l\in Y}f_l(x)$
代入k个，得分最高

正样本少，负样本多，不准

### one-versus-one

任选两个类做分类器，一正一负，剩下的暂时不管，有$C_{R}^2$个分类器
$\forall x\in X,h(x)=\argmax_{l‘\in Y}|l:h_{ll'}(x)=l|$
选择被分为正类最多的标签作为结果

决策时间长得多，没有充分利用样本关系，不准

## 错误修正编码

$$
\begin{array}{}
M&1&2&3&4&5&6\\
1&0&0&0&1&0&1\\
2&1&0&1&0&0&0\\
3&1&1&1&0&0&0\\
4&0&1&1&0&1&1\\
5&1&0&1&1&1&0\\
\end{array}
$$
每一行是某一种类别的编码
每一列代表一种小分类器，1为正0为负
每一行要有可区分行，且每一列不能全0或全1，尽量均衡
需要用代码找一个最优的M，即编码表
对一个$x_i$，先用每个小分类器获得$x_i$的编码$F(x_i)$，与$M$进行比对，找到最小汉明距离$h(x)=\argmin_{l\in y}d(M_l,F(x_i))$，相当于找到最大匹配
汉明距离，表示不一样的加一
使汉明距离最小的就是他的类别
<b>
迭代过程：
</b>
①给一个初始的M(k*m)，初始化或者上一轮迭代后

②根据M的每一列，得到$m$个小分类器$f(x_i),\forall i\in[1,m]$
对每个小分类器$f(x_i)$，都会对样本集(训练集)$X(n)$根据M每一列进行划分，并进行训练
$\min_{w_i,b_i,\epsilon_i}(\frac{1}{2}|w_i|^2+C_i\sum_{j=1}^n\epsilon_{ij}),s.t.y_j(w_i^Tx_j+b_i)\ge 1-\epsilon_{ij},\epsilon_{ij}\ge 0$
其中$w_i,b_i$是小分类器$f_i(x)$的权重和偏移量，$C_i$为该分类器的折中参数，$\epsilon_{ij}$表示该分类器$f_i(x)$对每一个样本$(x_j,y_j)$的误差

③根据获得的新的小分类器$f_i(x),\forall i\in[1,m]$获得对每个样本$(x_j,y_j)$的新的编码$F(x_j)$
即样本集从$(x_j,y_j)$变为了$(F(x_j),y_j)$
<b>注意，此时获得的相当于是用更新后的小分类器对样本集进行重新分类后的结果，每个样本集中的样本都会有一个相较于之前的新的编码</b>

④以得到的新的编码样本集，对M进行训练更新
即$\min_{M,\epsilon}|M|^2_F+C\sum_{i=1}^n\epsilon_i,s.t.\forall i\in[1,n],\forall l\in Y-\{y_i\},k(M_{y_i},F(x_i))-k(M_l,F(x_i))\ge1-\epsilon_i$
其中$|M|_F^2$表示对M的每一行$w_l$求平方后再相加的结果，即$\sum_{l=1}^k|w_l|^2$，$\epsilon_i$代表某一样本对每一行非正标签的误差的最大值$\epsilon_i=\max(\epsilon_{iy})$
代入可有
$\min_{M,\epsilon}\frac{1}{2}\sum_{l=1}^k|w_l|^2+C\sum_{i=1}^n\epsilon_i,s.t.\forall i\in[1,n],\forall l\in Y-\{y_i\},(w_{y_i}^TF(x_i)-w_l^TF(x_i))\ge1-\epsilon_i$
注意，这里的$1-\epsilon_i$中的1表示不区分错误的代价，可以用设定的变量进行替换
求拉格朗日：
$L(\{w_l\}_{l=1}^k,\epsilon,\alpha,\beta)=\frac{1}{2}\sum_{l=1}^k|w_l|^2+C\sum_{i=1}^n\epsilon_i-\sum_{i=1}^n\sum_{l\ne y_i}\alpha_{il}(w_{y_i}^TF(x_i)-w_l^TF(x_i)-1+\epsilon_i)-\sum_{i=1}^n\beta_i\epsilon_i$
优化问题：$\min_{\{w\}_l^k,\epsilon}(\max_{\alpha,\beta}(L(\{w_l\}_{l=1}^k,\epsilon,\alpha,\beta)))$
对偶问题：$\max_{\alpha,\beta}(\min_{\{w\}_l^k,\epsilon}(L(\{w_l\}_{l=1}^k,\epsilon,\alpha,\beta)))$
求KKT：
$\left \{ \begin{array}{} \frac{dL}{dw_l}=w_l+\sum_{i=1}^n\alpha_{il}F(x_i)=0 \\ \frac{dL}{d\epsilon_i}=C-\sum_{l\ne y_i}\alpha_{il}-\beta_i=0 \\ \alpha_{il}(w_{y_i}^TF(x_i)-w_l^TF(x_i)-1+\epsilon_i)=0 \\ \beta_i\epsilon_i=0 \end{array} \right .$
化简可有
$\left \{ \begin{array}{} w_l=\sum_{i=1}^n\alpha_{il}F(x_i) \\ C=\sum_{l\ne y_i}\alpha_{il}+\beta_i \\ \alpha_{il}(w_{y_i}^TF(x_i)-w_l^TF(x_i)-1+\epsilon_i)=0 \\ \beta_i\epsilon_i=0 \end{array} \right .$
<b>注意，这里是针对某一个$\epsilon_i$求导，所以会有n个第二式</b>
代入可化为只有$\alpha_{il}$的式子，进行优化
$L(\{w_l\}_{l=1}^k,\epsilon,\alpha,\beta)=\frac{1}{2}\sum_{l=1}^k\sum_{i=1}^n\sum_{j=1}^n\alpha_{il}\alpha_{jl}F(x_i)^TF(x_j)+\sum_{l\ne y_i}\sum_{i=1}^n\alpha_{il}\epsilon_i-\sum_{i=1}^n\sum_{l\ne y_i}\alpha_{il}\sum_{j=1}^n\alpha_{jy_i}F(x_j)^TF(x_i)+\sum_{i=1}^n\sum_{l\ne y_i}\alpha_{il}\sum_{j=1}^n\alpha_{jl}F(x_j)^TF(x_i)+\sum_{i=1}^n\sum_{l\ne y_i}\alpha_{il}-\sum_{i=1}^n\sum_{l\ne y_i}\alpha_{il}\epsilon_i$
通过合并可有
$L(\{w_l\}_{l=1}^k,\epsilon,\alpha,\beta)=\frac{1}{2}\sum_{l=1}^k\sum_{i=1}^n\sum_{j=1}^n\alpha_{il}\alpha_{jl}F(x_i)^TF(x_j)+\sum_{i=1}^n\sum_{l\ne y_i}\alpha_{il}\sum_{j=1}^n(F(x_j)^TF(x_i))(\alpha_{jl}-\alpha_{jy_i})+\sum_{i=1}^n\sum_{l\ne y_i}\alpha_{il}$
对$\alpha$求极大，可有$L$的解，并解出$w_l$
这个时候$w_l$代表$M$的每一行，但是是一个实数，需要对其进行离散化后得到新的$M$

⑤当达到最大迭代时，返回$M$

## 结构化预测

$f:X\rightarrow R$，X样本，输出为一个实数R
但有些时候，输出不再是一个实数$f:X\rightarrow y$，y是一个复杂的类别
图像分割：输入一个图片，抠出一个区域
优化目标为：
$\min_{w,\epsilon}(\frac{1}{2}|w|^2+C\sum_{i=1}^m\max_{y\ne y_i}\max(0,1-(w^T[\phi(x_i,y_i)-\phi(x_i,y)]))),s.t.w^T\phi(x_i,y_i)-w^T\phi(x_i,y)\ge1-\epsilon_{iy}$
注意，这里的1表示的是标签之间的差异，可以用$L(y_i,y)$代替
因为
$w^T\phi(x_i,y_i)-w^T\phi(x_i,y)\ge1-\epsilon_{iy}$
可有
$\epsilon_{iy}\ge1-w^T\phi(x_i,y_i)+w^T\phi(x_i,y)$
又因为
$\epsilon_{iy}\ge 0$
即
$\epsilon_{iy}=\max(0,1-w^T\phi(x_i,y_i)+w^T\phi(x_i,y))$
令$\epsilon_i=\max\epsilon_{iy}$
可有
$\epsilon_i=\max_{y\ne y_i}\epsilon_{iy}=\max_{y\ne y_i}\max(0,1-w^T\phi(x_i,y_i)+w^T\phi(x_i,y))$
故原式可化为：
$\min_{w\epsilon}\frac{1}{2}|w|^2+C\sum_{i=1}^n\epsilon_i,s.t.w^T\phi(x_i,y_i)-w^T\phi(x_i,y)\ge1-\epsilon_{iy},\forall y\ne y_i,\epsilon_{iy}\ge 0$
求梯度，次梯度或随机梯度
预测时要求$y=\max_{y\in Y}w^T\phi(x,y)$
当用$L(y_i,y)$代替1时，即
$\min_{w,\epsilon}(\frac{1}{2}|w|^2+C\sum_{i=1}^m\max_{y\ne y_i}\max(0,L(y_i,y)-(w^T[\phi(x_i,y_i)-\phi(x_i,y)])))$
可进行扩大来方便找$\max$
即
$\min_{w,\epsilon}(\frac{1}{2}|w|^2+C\sum_{i=1}^m\log\sum_{y\in T}\exp(L(y_i,y)-(w^T[\phi(x_i,y_i)-\phi(x_i,y)])))$
即先升上去，增大差距，然后求和，再求对数，近似求$\max$
如$log(e^1+e^{10})\approx 10$
也可以通过对损失加权的方式来简化求$\max$
即
$\min_{w,\epsilon}\frac{1}{2}|w|^2+C\sum_{i=1}^m\max_{y\ne y_i}L(y_i,y)\max\{0,1-(w^T[\phi(x_i,y_i)-\phi(x_i,y)])\}$

<div STYLE="page-break-after: always;"></div>

# 006 聚类分析

## base

是一种无监督学习，给数据集，自动分为k个簇，使同一个簇中的样本尽可能相同
可以根据距离定义相似度，有多种距离
<b>可用于图形分割</b>

## 层次聚类

自底向上或自顶向下

自底向上：每一次从样本集中抽出两个簇进行合并(相似度最好)，结合成一个簇，簇数从样本数依次递减，直到达到目标簇数(需求)
难点是如何计算两个簇之间的相似度，以及如何快速计算最相似的簇
从$n*n$到$n-1*n-1$时，有$n-2*n-2$个值不会发生改变，所以可以加一行一列，扔掉之前合并的两行两列，即单独进行计算即可

自顶向下：一开始所有的样本属于一个簇，每次都有一个簇从当前样本中分出去，难点是如何选择分割簇的大小

簇相似度：最小距离、最大距离、平均距离

## k均值

给n个样本点，k个簇个数
求k个均值，每个均值指代每个簇，即中心。每个样本找最小距离的中心，属于那个簇
得到聚类之后再重新计算中心，用样本均值代替k均值，再重新划分，交替执行：
$初始化\mu_k\rightarrow划分x\rightarrow计算样本均值\overline{x_k}\rightarrow均值更新\mu_k$
$\mu_k=\frac{1}{|C_k|}\sum_{j\in C_k}x_j$即样本均值
其中$C_k$代表第k组的样本个数

### 求证：是否收敛

$\mu:\mu_1,...,\mu_k$，k均值
定义$r_{ik}\in\{0,1\}$，表示$x_i$是否属于$k$簇
目标：最小化$J(\mu,r)=\sum_{i=1}^n\sum_{k=1}^Kr_{ik}|x_i-\mu_{k}|^2$
要求$r_i=[r_{i1},...,r_{ik}]^T,r_{ik}\in \{0,1\},r_i^T*1=1,\forall i$即要求每行(列)求和=1，$\sum_{k=1}^Kr_{ik}=1$
调整$\mu,r$使$J(\mu,r)$最小，由于交替更新$\mu,r$，所以要固定一个

①给定$\mu$，优化$r,r\in\{r_1,...,r_k\},r_i^T1=1,\forall i,r_i,r_j$不存在关联，可拆分
这里相当于固定k个均值，而去调整优化每个样本的簇分类，相当于上文中的<b>划分</b>过程
$\forall i,\min_{r_i}\Longrightarrow\sum_{k=1}^Kr_{ik}|x_i-\mu_k|^2,s.t.\sum_{k=1}^Kr_{ik}=1,r_{ik}\in\{0,1\}$
即要求每个样本被划分到距离他最近的均值中
令$d_{ik}=|x_i-\mu_k|^2,d_i=\left( \begin{array}{} d_{i1}\\.\\.\\.\\d_{iK} \end{array} \right)$
相当于找到了最小的$d_{ik}$就确定了$r_{ik}$的序列

②给定$r$，优化$\mu,\forall i\min_{\mu_i}\sum_{i=1}^n\sum_{k=1}^Kr_{ik}|x_i-\mu_k|^2$
优化目标不变，相当于固定样本的簇分类不变，而去调整均值，相当于上文中的<b>均值更新</b>过程
直接求导可有
$\frac{dJ}{d\mu_{k}}=\sum_{i=1}^nr_{ik}(2x_i-2\mu_k)=0$
这里注意，是针对某一个$\mu_k$求导，相当于会有K个式子
可有$\sum_{i=1}^nr_{ik}x_i=\sum_{i=1}^n\mu_kr_{ik}$
即$\mu_k=\frac{\sum_{i=1}^nr_{ik}x_i}{\sum_{i=1}^nr_{ik}}$
<font color='red'><b>即分子是属于第k簇的样本之和，分母是属于第k簇的样本个数</font></b>
对每个$\mu_k$都要进行更新，就相当于用样本均值$\overline{x}$代替$\mu_k$

①②算一轮迭代，交替多次，相当于阶梯型前进
假设t轮时，有$\left. \begin{array}{} J(\mu_t,r_t)&证明J(\mu_t,r_t)\ge J(\mu_t,r_{t+1})\\J(\mu_t,r_t)&证明J(\mu_t,r_{t+1})\ge J(\mu_{t+1},r_{t+1}) \end{array} \right.$
即可证明经过一次迭代，目标在下降

还要证明有下界，即样本均值最终会和k均值重合

k均值初始化的时候：第一个$\mu$随机，第二个选择距离现有$\mu$最远的样本点，加松弛的时候，就进行软划分，使$r_{ik}\in(0,1)$

## 谱聚类

<b>谱：矩阵的最大特征值</b>
将样本看做高维图中的点，边看做样本的相似度(权重)，可有$graph:G(V,E,W)$
其中$w_{ij}=\exp\{-\frac{|x_i-x_j|^2}{2\sigma^2}\}$
令$cut(A,B)$表示分割簇A与簇B所需要切断的边的权重

<font color='red'><b>
目标：$\min cut(A,B)=\sum_{i\in A,i\in B}w_{ij}$
此时为二分类问题
</font></b>
化为了最小生成树问题
为了简便，化为有加权的最小分割
$Ncut(A,B)=cut(A,B)(\frac{1}{vol(A)}+\frac{1}{vol(B)})$
这一步是为了让A,B中元素的个数的差距不要太大
其中$vol(A)=\sum_{i\in A}d_i,d_i=\sum_{j=1}^nw_{ij}$
即$d_i$表示第$i$行的行和，可以理解为点$i$与其他所有样本点的权重之和
而$vol(A)$则表示同属于A类的点距离除他之外所有点的权重之和的和
当然，也可以直接用$|A|$代替$vol(A)$

目标：$\min Ncut(A,B)=cut(A,B)(\frac{1}{vol(A)}+\frac{1}{vol(B)})$

为了化简计算，定义$f=[f_1,...,f_n]^T,f_i=\left\{ \begin{array}{} \frac{1}{vol(A)}&if.i\in A\\-\frac{1}{vol(B)}&if.i\in B \end{array} \right.$
可以理解为将$r_i$的信息与权重结合起来成了$f_i$，用正负来区分$A,B$类
令$w1_n=求行和=列向量=w_i=\left( \begin{array}{} d_1\\.\\.\\.\\d_n \end{array} \right)$
$D=diag(w1_n)$，即将$w1_n$扩展为对角矩阵$D=\left( \begin{array}{} d_1,0,...,0\\0,d_2,...,0\\.,.,...,.\\0,0,...,d_n \end{array} \right)$
$L=D-W$
则可有
$f^TLf=\sum_{ij}w_{ij}(f_i-f_j)^2$，即求列和、再求行和，两次求和
根据求和定义可有
$f^TLf=\sum_{ij}f_if_jL_{ij}$
将$L=D-W$代入可有
$f^TLf=\sum_{ij}f_if_j(D_{ij}-w_{ij})=f^T(D-w)f$
展开有
$f^TLf=f^TDf-f^Twf$
因为$d_i=\sum_{j=1}^nw_{ij}$
所以可有
$f^TLf=\sum_{i=1}^nd_if_i^2-f^Twf$
故可有
$f^TLf=\sum_{i=1}^nd_if_i^2-\sum_{i=1}^n\sum_{j=1}^nf_if_jw_{ij}$
将$\sum_{i=1}^n$拆开，为$\frac{1}{2}\sum_{i=1}^n+\frac{1}{2}\sum_{j=1}^n$
故可以有
$f^TLf=\frac{1}{2}\sum_{i=1}^nd_if_i^2+\frac{1}{2}\sum_{j=1}^nd_jf_j^2-\sum_{i=1}^n\sum_{j=1}^nf_if_jw_{ij}$
由于$w_{ij}$是对称的，有$w_{ij}=w_{ji}$
故
$f^TLf=\frac{1}{2}\sum_{i=1}^n\sum_{j=1}^nw_{ij}f_i^2+\frac{1}{2}\sum_{j=1}^n\sum_{i=1}^nw_{ji}f_j^2-\sum_{i=1}^n\sum_{j=1}^nf_if_jw_{ij}$
可有
$f^TLf=\sum_{i=1}^n\sum_{j=1}^n(\frac{1}{2}w_{ij}f_i^2+\frac{1}{2}w_{ij}f_j^2-f_if_jw_{ij})$
可见，这为一个完全平方式
$f^TLf=\frac{1}{2}\sum_{i=1}^n\sum_{j=1}^nw_{ij}(f_i-f_j)^2$
其中$f_i,f_j$是标量
由于只有当$i,j$不同簇的时候$f_i-f_j$不为0，有意义，故可有
$f^TLf=\frac{1}{2}(\sum_{i\in A}\sum_{j\in B}w_{ij}(\frac{1}{vol(A)}+\frac{1}{vol(B)})^2+\sum_{i\in B}\sum_{j\in A}w_{ij}(\frac{1}{vol(A)}+\frac{1}{vol(B)})^2)$
由于$i,j$是等价的，所以可以合并为
$f^TLf=\sum_{i\in A}\sum_{j\in B}w_{ij}(\frac{1}{vol(A)}+\frac{1}{vol(B)})^2$
故
$f^TLf=\sum_{i\in A,j\in B}w_{ij}(\frac{1}{vol(A)}+\frac{1}{vol(B)})
^2$

而考虑$f^TDf$，有
$f^TDf=\sum_{i=1}^nd_if_i^2=\sum_{i\in A}\frac{d_i}{vol(A)^2}+\sum_{i\in B}\frac{d_i}{vol(B)^2}$
又因为$\sum_{i\in A}d_i=\frac{1}{vol(A)}$
故可化简为
$f^TDf=\frac{1}{vol(A)}+\frac{1}{vol(B)}$

故可以有
$\frac{f^TLf}{f^TDf}=\sum_{i\in A,j\in B}w_{ij}(\frac{1}{vol(A)}+\frac{1}{vol(B)})=Ncut(A,B)$
<b>
相当于将目标转化为了求一个$f$，使得$\min_fNcut(A,B)=\frac{f^TLf}{f^TDf}$
</b>
而对应一个$f$都有一个划分向量$r$，但由于$f$是连续的，而$r$是离散的，需要想个办法将松弛转为连续
由于
$f^TD1=\sum_{i=1}^nf_id_i=\sum_{i\in A\cup B}f_id_i=\sum_{i\in A}f_id_i+\sum_{i\in B}f_id_i=\sum_{i\in A}\frac{d_i}{vol(A)}-\sum_{i\in B}\frac{-d_i}{vol(B)}=1+(-1)=0$
故在离散的时候，由于$f$只有$\frac{1}{vol(A)}$和$\frac{-1}{vol(B)}$两个值，所以默认了$f^TD1=0$成立
但当我们需要进行优化的时候，需要对f进行松弛，$f$可取$(\frac{-1}{vol(B)},\frac{1}{vol(A)})$中的任何值，所以需要强制要求$f^TD1=0$成立，相当于有一个约束条件
<font color='red'><b>
故优化目标转化为$\min_f\frac{f^TLf}{f^TDf},s.t.f^TD1=0$
</font></b>
在求解的时候，先不考虑约束，直接求导计算一个值，然后看在该值的情况下是否会满足约束条件即可
$\frac{d(\frac{f^TLf}{f^TDf})}{df}=\frac{2Lff^TDf-f^TLf2Df}{(f^TDf)^2}$
要求导数等于0，且由于$\frac{d(\frac{1}{2}x^TAx)}{dx}=Ax$，可有
$2Lff^TDf-f^TLf2Df=0$
可有
$Lff^TDf=f^TLfDf$
可有
$Lf=\frac{f^TLf}{f^TDf}Df$
令$\lambda=\frac{f^TLf}{f^TDf}$，可有
<font color='red'>
$Lf=\lambda Df$
</font>
这就是一个特征方程$D^{-1}Lf=\lambda f$
其中$\lambda$是个标量，即为特征值，$f$是特征向量
即$\frac{f^TLf}{f^TDf}$最优应满足$D^{-1}Lf=\lambda f$

先求证此时约束条件$f^TD1=0$是否依然满足
有$Lf=\lambda Df$，两边转置有$\lambda f^TD^T=f^TL^T$
由于$D,L$均对称，故有$\lambda f^TD=f^TL$
即
$\lambda f^TD1=f^TL1=f^T(D-w)1$
可有
$\lambda f^TD1=f^T(D1-w1)$
因为$D1-w1=0$求行和，即$L1=0$
故可有$\lambda f^TD1=0$
又因为$\lambda \ne 0$，否则根据$\lambda=\frac{f^TLf}{f^TDf}$，有$f^TLf=0,f=1$，没有意义
所以有
$Lf=\lambda Df$时，$f^TD1=0$也成立，自动满足

所以这个结果可以用，取$\lambda$是一个非零的最小特征值对应的特征向量$f$作为分类依据，对$f$离散化，根据$>0,<0$，可有分类$r$

## 谱聚类k个簇

求$Lf=\lambda Df$的前k个最小特征值对应的特征向量(此时可以选0，没有影响，因为0是均分)
可以得到一个$V\in R^{n*k}$的矩阵
$$
V=\left( \begin{array}{}
V&v_1&v_2&...&v_k\\
z_1&v_{11}&v_{12}&...&v_{1k}\\
.&.&.&...&.\\
z_n&v_{n1}&v_{n2}&...&v_{nk}
\end{array} \right)
$$
其中每一列为一个特征向量，每一行是一个样本点采用不同的k个分类器分类的结果，相当于<b>k次二分类结果矩阵</b>
将这个$n*k$矩阵作为$k$均值的输入，可以得到一个$k$均值的解，作为样本分类情况。
相当于$n*n\rightarrow n*k$或$n*m\rightarrow n*k$，类似于降维，将数据进行了抽象

<div STYLE="page-break-after: always;"></div>

# 007 深度学习

## base

流程图：通过传感器获得数据，经过预处理、特征提取、特征选择({$x_i,y_i$})、再到推理、预测或识别
机器学习关注识别的过程
特征表达：预处理、特征提取、特征选择，一般人工，相当于打标签，得到数据集

深度学习：自动的学习特征，也叫<b>表示学习</b>，是一个不断迭代、不断抽象的过程
信息处理是分级的，倾向性不断增加，语义信息越来越明显
高层特征是低层特征的组合，从底层到高层特征越来越抽象，越来越能表现语义或意图
抽象越高，可能猜测越少，越利于分类

## 神经网络

网络拓扑结构(连接方式)
相当于通过拓扑结构定义了假设空间中的函数是如何选择的
不同拓扑，则假说集不同，函数结构不同
神经元权重由数据决定
①前馈神经网络：多层感知机
②反馈神经网络：网络内神经元间有反馈，信息处理是状态交换

## 神经元

人工神经元用一个非线性激活函数，输出一个活性值a
d维输入$x=[x_1,...,x_d]^T$，有
$z=w^Tx+b,a=f(z)$
$w$是一个d维度的权重向量，b是偏置量，z为状态，表示x输入的加权和，f是激活函数，如sigmod

对神经元组合后，即符合运算，问题是如何找权重(数据调)
修正线性单元：用rectifer函数(rectifier(x)=max(0,x))的单元，有单侧已知、宽兴奋边界、稀疏激活性
sigmod函数是一类S型曲线函数
logistics函数$\sigma(x)=\frac{1}{1+e^{-x}},\sigma'(x)=(1-\sigma(x))\sigma(x)$
tanh函数$tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}$

前馈网络参数：
$L$：网络层数
$n^l$：第l层神经元个数
$f_l()$：第l层激活函数
$w^l\in R^{n^l*n^{l-1}}$：l-1与l层的权重矩阵
$b^l\in R^{n^l}$：第l层的偏置量
$z^l\in R^l$：第l层的状态
$a^l\in R^l$：第l层的活性值
可有
<font color='red'><font size=5>
$z^l=w^{lT}a^{l-1}+b^l,a^l=f_l(z^l)$
</font></font>
输入是上一层的输出
也可以合并写为
$z^l=w^{lT}f_{l-1}(z^{l-1})+b^l$
即每一层的信息为
$x=a^0\rightarrow z^1\rightarrow a^1\rightarrow z^2\rightarrow...\rightarrow a^{L-1}\rightarrow z^{L}\rightarrow a^{L}=y$

样本$\{(x_i,y_i)\}_{i=1}^n$，输出为$f(x|w,b)$
目标：$J(w,b)=\sum_{i=1}^n l(f(x_i|w,b),y_i)+\frac{\lambda}{2}|w|_F^2=\sum_{i=1}^n J(w,b,x_i,y_i)+\frac{\lambda}{2}|w|_F^2$
其中$l$是训练误差，$\frac{\lambda}{2}|w|_F^2$表示正则化学习，正则化项，用来剪枝
其中$|w|_F^2=\sum_{l=1}^L\sum_{i=1}^{n^{l+1}}\sum_{j=1}^{n^l}(w_{ij}^l)^2$

要求最小化$J(w,b)$，采用梯度下降的方法，可有
$w^l=w^l-\alpha(\frac{d J(w,b)}{dw^l})=w^l-\alpha(\sum_{i=1}^n(\frac{dJ(w,b,x_i,y_i)}{dw^l})+\lambda w^l)$
同理可有
$b^l=b^l-\alpha(\frac{d J(w,b)}{db^l})=b^l-\alpha(\sum_{i=1}^n(\frac{dJ(w,b,x_i,y_i)}{db^l}))$
$\alpha$是参数的更新(学习)率，即步长
$\frac{dT(w,b)}{dw^l}$是方向

根据链式法则，有
$\frac{dJ(w,b,x,y)}{dw_{ij}^l}=(\frac{dJ(w,b,x,y)}{dz^l})^T\frac{dz^l}{dw_{ij}^l}$

则对于第$l$层，定义一个误差项$\sigma^l=\frac{dJ(w,b,x,y)}{dz^l}\in R^{n^l}$为目标函数关于第$l$层的神经元$z^l$的偏导数，即第$l$层神经元对最终误差的影响
因为$z^l=w^{lT}a^{l-1}+b^l$
则有$\frac{dz^l}{dw_{ij}^l}=\frac{d(w^la^{l-1}+b^l)}{dw_{ij}^l}=\left[ \begin{array}{} 0\\...\\a_j^{l-1}\\...\\0 \end{array} \right]$
故有$\frac{dJ(w,b,x,y)}{dw_{ij}^l}=\sigma_i^la_j^{l-1}$
故有$\frac{dJ(w,b,x,y)}{dw^l}=\sigma^l(a^{l-1})^T$
同理$\frac{dJ(w,b,x,y)}{db^l}=\sigma^l$
则第$l$层的误差项为
$\sigma^l=\frac{dJ(w,b,x,y)}{dz^l}=\frac{d a^l}{d z^l}\frac{dz^{l+1}}{d a^l}\frac{dJ(w,b,x,y)}{dz^{l+1}}$
代入激活函数后有
$\sigma^l=diag(f_l'(z^l))(w^{l+1})^T\sigma(l+1)$
可以定义向量点积，表示每个元素相乘，就有
$\sigma^l=f_l'(z^l)\odot ((w^{l+1})^T\sigma^{l+1})$
可以看到，第$l$层的误差可由第$l+1$得到，相当于错误反向传递，可由后层的误差计算前层的误差
由每一层的误差，可得每一层参数的梯度

训练过程：

1. 先前馈样本计算每一层的$z$与$a$
2. 反向传播$\sigma^l$计算每一层的$\sigma^l$
3. 通过$\sigma^l$计算每一层的偏导，更新参数$w,b$

## 卷积神经网络

局部连接、权重共享，空间或事件上的次采样
平移、缩放、扭曲不变形

卷积：给定输入序列$x_t(t=1,...,n)$，滤波器$\sigma_k(k=1,...,m)$(移动窗口)，输出$y_t=\sum_{k=1}^mf_kx_{t-k+1}$
<font color='red'><b>实际上就是一个窗口内的加权求和</b></font>
当$f_k=\frac{1}{m}$时，卷积相当于信号序列的移动平均
宽卷积：输出n+m-1，对不在$[1,n]$内的$x_t$补零
窄卷积：输出n-m+1，不补零
二维：图像$x_{ij}(1<i<m,1<j<n)$，滤波器$f_{ij}(1<i<m,1<j<n)$
即$y_{ij}=\sum_{u=1}^m\sum_{v=1}^nf_{uv}x_{i-u+1,j-v+1}$
用卷积取代替全连接，第$l$层每个神经元只与第$l-1$层的一个局部窗口内的神经元相连，局部连接

则第$l$层的第$i$个神经元的输入定义为：
$a_i^l=f_l(\sum_{j=1}^mw_j^{lT}a_{i-m+j}^{l-1}+b^l)=f_l(w^{lT}a_{i-m+1:i}^{l-1}+b^l)$
其中$w^l\in R^m$为$m$维滤波器，$a_{i-m+1:i}^{l-1}=[a_{i-m+1}^{l-1},...,a_i^{l-1}]^T$
也可写为$a^{l}=f_l(w^l\otimes a^{l-1}+b^l)$
其中$\otimes$表示卷积运算

<b>可以看到，$w^l$对于所有的神经元都是相同的，可以理解为一层只有一个卷积核</b>
在图像处理中，需要二维矩阵的形式输入到神经网络中，因此需要二维卷积，假设$x^l\in R^{w_l*h_l}$和$x^{l-1}\in R^{w_{l-1}*h_{l-1}}$分别表示第$l$层和$l-1$层的神经元活性值，其中$x^l$的每一个元素为
$x_{s,t}^{l}=f_l(\sum_{i=1}^{u}\sum_{j=1}^{v}w_{ij}^lx_{s-i+u,t-j+v}^{l-1}+b^l)$
其中$w^l\in R^{u*v}$为两维滤波器，$b^l$为第$l$层偏置，第$l$层的神经元个数为$w_l*h_l$，并且$w_l=w_{l-1}-u+1,h_{l}=h_{l-1}-v+1$
可有
$x^l=f_l(w^l\otimes x^{l-1}+b^l)$

但对每一层，有多组卷积核：$x^{l,k}=f_l(\sum_{p=1}^{n_l-1}(w^{l,k,p}\otimes x^{l-1,p})+b^{l,k})$
其中$w^{l,k,p}$表示第$l-1$层的第$p$组特征向量到第$l$层的第$k$组特征映射所需要的滤波器，即卷积核

连接表：第$l$层的每一组特征映射依赖$l-1$层的所有特征映射，即不同层的特征映射之间是全连接，但这种全连接关系不是必须的，可用表来表示怎么连接，即第$l$层的每一组特征映射都依赖于前一层的少数几组特征映射

池化层：pooling，即子采样(sub-sampling)，有max/min/aver三种，用max/min/aver代替某一区域的值，降低维度，减少神经元个数

### 例 输入为32*32*1的灰度图片

|输入32*32|核大小均为6*5*5，即6个|池化2*2*1|补充|
|--|--|--|--|
|第一层卷积|$32*32*1\rightarrow 28*28*6$|32-5+1=28||
|第二层池化|$28*28*6\rightarrow 14*14*6$|28/2=14||
|第三层卷积|$14*14*6\rightarrow 10*10*16$|14-5+1=10|有连接表，不再全连接|
|第四层池化|$10*10*16\rightarrow 5*5*16$|10/2=5||
|第五层卷积|$5*5*16\rightarrow 1*1*120$|5-5+1=1|全连接，120个核，16相加得1|
|第六层卷积|$1*1*120\rightarrow 1*1*84$|人为设置84|全连接|
|第七层卷积|$1*1*84\rightarrow 1*1*10$|全连接|输出层10个欧式径向基函数|

## GAN生成对抗网络

概率生成模型，学习概率分布(数据)采样得到新的数据
生成器，判别器
$\left. \begin{array}{} 真实的图像\rightarrow采样得到X-P_{data}\\隐随机变量(噪声)z-P_z\rightarrow生成网络G\rightarrow采样得到G(z)-Q \end{array} \right\}判别网络D\rightarrow P$
判定为假时更新生成网络
判定为真时更新判断网络
个人理解：这里可以理解为人为认为所有的生成结果都是错的，所以如果能够判别出来是假的，相当于是真值，要生成更好的；如果判别是真的，相当于是假值，需要修正判定网络
最后会平衡
目标为：$\min_G\max_DV(D,G)=E_{x-P_{data}}(x)[log D(x)]+E_{z-P_{z}(z)}[log(1-D(G(z)))]$
其中$D(x)$表示$x$来自真实样本的概率
