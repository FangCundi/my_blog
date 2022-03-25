# multi-class 多分类问题

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
