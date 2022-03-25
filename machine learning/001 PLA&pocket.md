# 感知机算法PLA
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