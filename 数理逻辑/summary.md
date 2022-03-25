# 001 形式系统

## base

形式系统（研究对象），是逻辑的载体；逻辑是数学的基础
<b>把学科建立在可靠严谨的公理系统之上，是现代数学乃至科学的基本特征之一</b>

## 形式系统定义

一个形式系统是一个<b>五元偶</b>，$FS=(\Sigma,Term,Formula,Axiom,Rule)$

1. 非空集合$\Sigma$是FS的字母表，其元素称为FS的符号，如$0-9,x,=$
2. $Term\subseteq \Sigma^*$，称为FS的项集，其元素称为FS的项，项集可为空集
$\Sigma^*$表示以$\Sigma$为字母表，构成的有穷串组成的集合，包含空串，串为序列，元素可重复
3. $Formula\subseteq\Sigma^*,Formula\cap Term=\varnothing$，称为FS的字母集，其元素称为FS的公式，一般不允许Formula为空，公式具有真假性。
Formula中有子集Atom，为FS的原子公式
4. $Axiom\subseteq Formula$，称为FS的公理（永真）集合，其元素称为FS的公理，一元规则
5. $Rule\subseteq \cup_{n=2}^{\infty}2^{(Formula)^n}$，是FS的演绎规则的集合，元素为演绎规则（序列），即规则
<b>若A为集合，$2^A$是A的幂集=$\{B|B\subseteq A\}$，A的全部子集构成的集合</b>
$B^A$表示以A为定义域，以B为值域的函数构成的集合
<b>$\Sigma,Term,Formula$是语言部分，定义语言；$Axiom,Rule$是推理部分</b>

**例：初等数式系统FSEN**
$\Sigma=\{0,'(后继),=(等于)\}$
$Term=\{0,0',0'',...\}$
$Formula=Atom=\{t_1=t_2|t_1,t_2\in Term\}$
$Axiom=\{0=0\}$
$Rule=\{r\}$，其中$r=\{<t_1=t_2,t_1'=t_2'>|t_1,t_2\in Term\}$

## 语法语义

**语法**：构成形式系统$Term,Formula$等语言成分的规则，字符串的规则
定义方法：集合描述法、归纳定义法、BNF定义法
<b>归纳定义步骤：
>定义基础元素、无条件承认
定义通过已有元素构成新元素的规则
极小化，所有元素可用有限次应用前两步规则得到
</b>

**例：归纳定义FSEN中的项**
在FSEN中，项集采用集合描述为$\{0,0',0'',...\}$，则其可以归纳定义如下
>0是FSEN中的项
若t是FSEN中的项，则t'是项
除上述元素外，FSEN中不含有其他项

BNF是一种归纳定义的文法，一般用相同的符号标识相同类型的语法成分

**例：用BNF范式定义FSEN中的项和公式**
>t::=0|t'
f::=t~t

考虑形式系统FSDM=$<\Sigma,\varnothing,Formula,\varnothing,\varnothing>$，其中$\Sigma=\{a,b,\#,@\}$，公式集定义如下
>a和b都是公式
若f是公式，则@f也是公式
若$f_1,f_2$是公式，则$f_1\#f_2$也是公式

则其等价的BNF描述为$f::=a|b|@f|f\#f$

**语义**：给项、公式值的过程，把项/公式映射到给定集合的过程，该集合称为语义值集合

**例：FSDM一类语义定义方式**
取定整数集合Z作为语义值集合，其公式的语义由一个函数$\sigma:\{a,b\}\rightarrow Z$确定，即语义函数$V_{\sigma}:Formula\rightarrow Z$如下
>$V_{\sigma}(a)=\sigma(a)且V_{\sigma}(b)=\sigma(b)$
$V_{\sigma}(@f)=-V_{\sigma}(f)$
$V_{\sigma}(f_1\#f_2)=V_{\sigma}(f_1)\#V_{\sigma}(f_2)$

**个人理解，这里相当于定义了加法和取反操作的语义，公式中的变量a，b可以根据一个特征映射$\sigma$取到值域Z中的值**

若FS不满足唯一可读性，则会导致语义计算的二义性
<font color='red'>语义与形式系统无关，形式系统是语法上的东西</font>

**<font color='red'>归纳证明：</font>**
设形式系统$FS=<\Sigma,Term,Formula,Axiom,Rule>$，集合$\Gamma\subseteq Formula$以及$A\in Formula$。若存在公式序列$A_0,A_1,...,A_m\in Formula$，满足$A_m=A$，且当$0\le i\le m$时以下三个条件之一成立
①$A_i\in \Gamma$
②$A_i\in Axiom$
③存在$r\in Rule$，以及$i_0,i_1,...,i_n<i$使得$<A_{i_0},A_{i_1},...,A_{i_n},A_i>\in r$
则称A由$\Gamma$可证，记为$\Gamma\vdash_{FS}A$，并称$<A_{i_0},A_{i_1},...,A_{i_n},A_i>$为A的一个从$\Gamma$出发的证明
**个人理解：首先判断$A_i$是不是给定的$\Gamma$集合中的定理(条件)，其次判断$A_i$是不是公理，最后判定能不能通过某些规则r来得到$A_i$。这里也说明规则集不是抽象的，而是不可数的公式序列组成的。当公式序列中的每一位都可证的时候，最后一位A作为公式序列的一部分，自然可证，这就是归纳。<font color='red'>注意，在证明$A_i$的时候默认$A_{i-1}已证$</font>**

若A由$\Gamma$（已知公式集合，假设的系统）可证，记为$\Gamma\vdash_{FS(系统)}A$，其中FS可以省略，若$\Gamma$为空则$\vdash A$，代表A恒成立

若$\Gamma\vdash A$，则称A为$\Gamma$的演绎结果，<font color='red'>演绎是语法层面</font>，不依赖语义，即可狭隘理解为不解释公式的真假性，只是从字符串层面上存在推理过程。

记$Th(FS\cup \Gamma)=\{A\in Formula|\Gamma\vdash_{FS}A\}$，简记为$Th(\Gamma)$，表示$\Gamma$系统的一切可证（演绎）定理的集合。任何一个公式$A$的证明步数是有限的
>$Axiom\subseteq TH(FS)\subseteq TH(\Gamma)$，表示一切公理可由最开始的FS系统证明，FS可证明的一切定理可由增加了新条件$\Gamma$后的系统证明
$\Gamma\subseteq TH(\Gamma)$，表示增加的新条件可由增加了新条件后的系统证明
$TH(\varnothing)=TH(FS)$，不增加新条件时证明能力不变
若$\Gamma_1\subseteq\Gamma_2$则$TH(\Gamma_1)\subseteq TH(\Gamma_2)$，增加新条件越多，可证明的定理越多
$TH(TH(\Gamma))=TH(\Gamma)$，将可证明的定理作为条件，不会再证明出新的定理

**例：证明$TH(TH(\Gamma))=TH(\Gamma)$**
将$TH(\Gamma)视为\Gamma_0，即比较TH(\Gamma_0)与\Gamma_0$
因为$\Gamma_0\subseteq TH(\Gamma_0)$，故$TH(\Gamma)\subseteq TH(TH(\Gamma))$
从$TH(TH(\Gamma))$中任取A，即$A\in TH(TH(\Gamma))$
则有$TH(\Gamma)\vdash A$，即$A\in TH(\Gamma_0)$，即$\Gamma_0\vdash A$
求证任一个$A\in TH(\Gamma_0)$，均有$\Gamma\vdash A$即$A\in TH(\Gamma)，即A\in \Gamma_0$
取一个序列$<A_0,A_1,...A_m=A>$
对其中每一个$A_i$求证①②③
①：已证，$Axiom\subseteq TH(\Gamma_0)\subseteq TH(\Gamma)$
②：已证，$\Gamma\subseteq TH(\Gamma)$
③：证明$\Gamma\vdash A_{ij}$
对$\forall i<m$，皆有$\Gamma_0\vdash A$
即必存在$<A_{i00},A_{i01},...,A_{i0}>\in Rule(\Gamma_0)$
即已证$<A_{i00},A_{i01},...,A_{i0}>,<A_{i10},A_{i11},...,A_{i1}>,...,<A_{i0},A_{i1},...,A_{i}>$
可提取$<A_{i0},A_{i1},...,A_{i}>\in Rule(\Gamma_0)$
所以有对$\forall i<m,\Gamma\vdash A$
所以有$A\in TH(\Gamma)，即A\in \Gamma_0$
即对任意$A\in TH(TH(\Gamma))$，有$A\in TH(\Gamma)$
双向证明，则说明$TH(\Gamma)=TH(TH(\Gamma))$

## 形式系统的扩张

设形式系统$FS_i=<\Sigma_i,Term_i,Formula_i,Axiom_i,Rule_i>$，其中$i=1,2$，若$FS_1,FS_2$满足
①$\Sigma_1\subseteq \Sigma_2$
②$Term_1\subseteq Term_2$
③$Formula_1\subseteq Formula_2$
④$Axiom_1\subseteq TH(FS_2)$
⑤$Rule_1\subseteq Rule_2$
则称$FS_2$是$FS_1$的一个扩张，记为$FS_1\subset FS_2$，当不相等时，记为$FS_1\subset FS_2$

<div STYLE="page-break-after: always;"></div>

# 002 命题逻辑

## $\mathcal{P}$系统定义

$\mathcal{P}=<\Sigma_p,Term_p,Formula_p,Axiom_p,Rule_p>$
$\Sigma_p$包括通用符号$\thicksim,\cup,(,)$及特殊符号（原子变元）
$Term_p=\varnothing$，命题逻辑中没有项，相当于符号组合而成的都是公式
$Formula_p$为满足下列条件的集合
①若P为命题变元（原子命题），则$P\in Formula$
②若$A\in Formula$则$\thicksim A\in Formula$
③若$A,B\in Formula$则$(A\cup B)\in Formula$
$Axiom=AS_1\cup AS_2 \cup AS_3$
①$AS_1:A\cup A\rightarrow A$
②$AS_2:A\rightarrow B\cup A$
③$AS_3:A\rightarrow B\rightarrow (C\cup A\rightarrow B\cup C)$
$Rule_P=\{MP\}$
$MP:\frac{A,A\rightarrow B}{B}$
注意，以上的公理和规则都是按照<font color='red'>模式</font>写的，必要时可以写成公式集合的形式
所以，Formula是包含所有的命题变元，且关于$\thicksim,\cup,(,)$构造封闭的最小集合。
Atom就是由全部原子命题构成的集合
$\cap:(A\cap B\longrightarrow \thicksim(\thicksim A\cup\thicksim B))$
$\rightarrow:(A\rightarrow B)\longrightarrow (\thicksim A \cup B)$
$\equiv:(A\equiv B)\longrightarrow ((A\rightarrow B)\cap(B\rightarrow A))$
<font color='red'><b>注意，这些都是在语法层面的，语义还没有涉及到</b></font>

### 公式结构归纳法

要证明$P$的公式集Formula满足某个性质R，可以按照如下方法进行证明
①若$p$为命题变元，则$p$满足R
②若A满足R，则$\thicksim A$满足
③若B，C满足R，则$(B\cup C)$满足

### 代入操作

设函数$\theta:\Sigma^*\rightarrow \Sigma^*$，即是一个从符号集构成的有穷串组成的集合映射到符号集构成的有穷串组成的集合，且满足
①若$x\in \Sigma$，则$\theta(x)\ne \epsilon$
②对任意的$x,y\in \Sigma^*$有$\theta(xy)=\theta(x)\theta(y)$，注意，不可以交换成$\theta(xy)=\theta(y)\theta(x)$
就称$\theta$是$\Sigma^*$上的一个代入，可写为$\theta=S_{A}^{p}$，指将$p$替换为$A$

假设$\theta$是一个$\Sigma^*_{\mathclap{P}}$上的一个代入，可有
①若$\{x\in \Sigma_{P}|\theta(x)\ne x\}$为有穷集，则称$\theta$是一个有穷代入
②若$\theta$不改变P中的通用符号，则称$\theta$是一个变元代入
③若存在命题变元$p_1,p_2,...,p_n\in \Sigma_{P}$以及公式$A_1,A_2,...,A_n\in Formula_P$，使得
$\theta(x)=\left\{ \begin{array}{} A_i&x\in \{p_1,p_2,...,p_n\}\\x&x\notin\{p_1,p_2,...,p_n\} \end{array} \right.$，可记为$\theta=S_{A_1,A_2,...,A_n}^{p_1,p_2,...,p_n}$
可以理解为对单个变元的替换而已

<font color='red'>注意$S_{p,q}^{q,p}$与$S_p^qS_q^p$不同，前者是针对一个公式进行的同时替换，后者不是同时</font>

### 公式的命题变元集

就是变量，查看一个公式的变量是什么。
定义函数$Var:Formula\rightarrow 2^{\Sigma_p}$
若p是命题变元，则$Var(p)=\{p\}$
若$A\in Formula$，则$Var(\thicksim A)=Var(A)$，指的是组成这两个公式的变量是一致的
若$B\cup C\in Formula$，则$Var(B\cup C)=Var(B)\cup Var(C)$
若命题变元$p\in Var(A)$则p在A中出现

## 定理与导出规则

①$\in:若A\in\Gamma则\Gamma\vdash A$
②$\in_{+}:若\Gamma_1\vdash A且\Gamma_1\subseteq\Gamma_2则\Gamma_2\vdash A$
③$\overline{MP}:若\Gamma_1\vdash A,\Gamma_2\vdash A\rightarrow B,\Gamma_1\cup\Gamma_2\subseteq\Gamma则\Gamma\vdash B$
<font color='red'>④$sub:设\Gamma\vdash A且B_1,...,B_n\in Formula,若p_1,...,p_n\notin\Gamma,则\Gamma\vdash S_{B1,...,B_n}^{p_1,...,p_n}A$</font>

<b>证：设$\Gamma\vdash A,且B_1,...,B_n\in Formula,若p_1,...,p_n\notin \Gamma,求证\Gamma\vdash S_{B1,...,B_n}^{p_1,...,p_n}A$</b>
取序列$<A_0,...,A_m>,A_m=A$，记$\theta=S_{B1,...,B_n}^{p_1,...,p_n}$，即求证对每个$i\le m$，均有$\Gamma\vdash\theta(A_i)$
①若$A_i\in\Gamma$，由于$p_1,...,p_n\notin\Gamma$，故没有发生代入，$\theta(A_i)\in\Gamma$
②若$A_i\in Axiom$，则$\theta(A_i)$也是公理，改变变量不改变公理
③若存在$j,k<i,A_j=A_k\rightarrow A_i$，则有
$\Gamma\vdash\theta(A_j),\Gamma\vdash\theta(A_k)$，此为归纳
可有$\theta(A_j)=\theta(A_k)\rightarrow\theta(A_j)$，代入不对通用符号起作用
根据MP规则可有$\Gamma\vdash\theta(A_i)$
综上可有对任意满足条件的A，有$\Gamma\vdash\theta(A)$

⑤$DR_1:若\Gamma_1\vdash C\cup A,\Gamma_2\vdash A\rightarrow B,\Gamma_1\cup\Gamma_2\subseteq\Gamma,则\Gamma\vdash B\cup C$

<b>证：$若\Gamma_1\vdash C\cup A,\Gamma_2\vdash A\rightarrow B,\Gamma_1\cup\Gamma_2\subseteq\Gamma,则\Gamma\vdash B\cup C$</b>
因为$\Gamma_2\vdash A\rightarrow B$
又因为$\vdash A\rightarrow B\rightarrow (C\cup A\rightarrow(B\cup C))$
所以可有MP规则：$\Gamma_2\vdash (C\cup A\rightarrow(B\cup C))$
又因为$\Gamma_1\vdash C\cup A$
而$\Gamma_1\cup\Gamma_2\subseteq\Gamma$
所以可有$\Gamma\vdash(B\cup C)$

## 语义和连接词

变量语义的值域，令$B=\{t,f\}$，分别表示逻辑真和逻辑假，有真值运算符号（连接词）及其对应的语义：<font color='red'>$\thicksim,\cup,\cap,\rightarrow,\equiv$</font>
$\left\{ \begin{array}{} \thicksim t=f\\ \thicksim f=t \end{array} \right.$ $\left\{ \begin{array}{} f\cup f=f\\ f\cup t=t\cup f=t\cup t=t \end{array} \right.$ $\left\{ \begin{array}{} t\cap t=t\\f\cap f=t\cap f=f\cap t=f \end{array} \right.$ $\left\{ \begin{array}{} t\rightarrow f=f\\f\rightarrow f=f\rightarrow t=t\rightarrow t=t \end{array} \right.$ $\left\{ \begin{array}{} t\equiv t=f\equiv f=t\\f\equiv t=t\equiv f=f \end{array} \right.$

### 真值指派

一个指派$\phi$是一个从$Atom$原子命题到$B:\{t,f\}$的函数（特征映射）
关于A的指派$\phi:Var(A)\rightarrow\{t,f\}$为A的指派或者赋值。若$\Gamma\subseteq Formula,则\phi:Var(\Gamma)\rightarrow\{t,f\}$为$\Gamma$的指派或者赋值。简单地说，我可以对一个公式进行指派，也可以对一个公式集合进行指派

设$\phi$是P上的一个指派，则存在唯一的函数$V_{\phi}:Formula\rightarrow \{t,f\}$满足
①若$p$为原子命题，则$V_{\phi}=\phi(p)$
②若$A\in Formula$，则$V_{\phi}(\thicksim A)=\thicksim V_{\phi}(A)$，指派不针对通用符号
③若$B,C\in Formula$，则$V_{\phi}(B\cup C)=V_{\phi}(B)\cup V_{\phi}(C)$

设$\phi$是P上一个指派，$A\in Formula且\Gamma\subseteq Formula$
①称$\phi(A)$是A关于$\phi$指派的真值（赋值），可理解为将A=d
②若$\phi(A)=t$，则称$\phi$满足A，记为$\vDash_{\phi}A$，相当于从语义层面，某个解释可让公式A为真值
③若$\phi(A)=f$，则称$\phi$不满足A
④若对每个$B\in \Gamma$都有$\vDash B$，则称$\phi$满足$\Gamma$，记为$\vDash\Gamma$，可以理解为公式集合$\Gamma$均可被指派解释为真

### 指派定义：
①若每个指派都满足A，则称A为永真式或重言式，记为$\vDash A$，例如$A\cup \thicksim A$
②若每个指派都不满足A，则称A为永假式或矛盾式，例如$A\cup \thicksim A$
③若$A\rightarrow B$为永真式，则称A蕴含B，可以理解为若满足A则B默认满足，自然满足；反之不成立
④若$A\equiv B$为永真式，则称A与B等价，A与B必然同时满足
⑤若每个满足$\Gamma$的指派均满足A，则称A为$\Gamma$的逻辑结果，记为$\Gamma\vDash A$。可以理解为$\Gamma\rightarrow A$在每个满足$\Gamma$的时候必然成立，所以根据MP可有A在$\Gamma$满足时必然成立
⑥若有指派满足$\Gamma$，则称$\Gamma$是可满足的。理解为存在指派使得公式集合$\Gamma$中的每个公式都为真。<font color='red'>如果公式集合不满足，则说明公式集合内存在矛盾</font>
⑦若有指派满足A，则称A是可满足的
<font color='red'>
$\varnothing$的逻辑结果永真，因为在没有任何前提条件下可证的公式为永真式
永真的逻辑结果永真，永真式对推理能力没有帮助
$\Gamma\vDash A$但$A不一定\in \Gamma$，即$\Gamma$条件下可能证明出来原来证明不了的公式
</font>

### 命题连接词

设$n\ge 1$，函数$\phi:\{t,f\}^n\rightarrow\{t,f\}$为一个n元真值函数，相当于把n个变元映射到不同的值。
一个n元真值函数对应一个n元连接词
特别约定：$t,f$为0元真值函数
<font color='red'>共有$2^{2^n}$个不同的n元真值函数</font>
2元连接词包括$\cap,\cup.\rightarrow,\equiv$等16个

用$P_i^{(n)}$表示第i个n元投影函数，即$P_i^{(n)}(x_1,...,x_i,...,x_n)=x_i$
设S为一个真值函数集合，用$\widecheck{S}$表示S的合成闭包，其为满足下面条件的最小集合
①$S\subseteq\widecheck{S}$
②对任意n以及任意m$\le$n，投影函数$P_m^{(n)}\in \widecheck{S}$
③若m元真值函数$\phi\in\widecheck{S}$，并且n元真值函数$\phi_1,...,\phi_m\in\widecheck{S}$，则$\phi o(\phi_1,...,\phi_m)\in \widecheck{S}$
<font color='red'>
若$\phi\in\widecheck{S}$，则称$\phi$可由S定义。若每个真值函数$\phi_i$均可由S定义，则称S是完全的。
可以理解为，表示了全部的可能函数</font>
<b>
下面的命题连接词集合都是完全的，即可以表示全部的可能公式
$\{\thicksim,\cup\},\{\thicksim,\cap\},\{\thicksim,\rightarrow\},\{\uparrow\},\{\downarrow\}$
</b>

### 公式的指定出现与替换

设$A,M,N\in Formula$。若存在$\alpha_1,...,\alpha_n\in\Sigma^*$使得$A=\alpha_1 M\alpha_2 M...\alpha_n$，则称M在A中有一个$\alpha_1,...,\alpha_n$出现
若M在A中有一个$\alpha_1,...,\alpha_n$出现，则令$A_N^M$为$\alpha_1 N\alpha_2...\alpha_{n-1}N\alpha_n$
为用N替换A中所有M的制定出现的结果
<b>个人理解，替换是字符串层面的操作，而代入则是变元层面的操作</b>

## 元性质

### 可靠性

<font size=4>$若\Gamma\vdash A则\Gamma\vDash A$</font>
即如果是演绎结果，则一定是逻辑结果
因为$\Gamma\vdash A$，所以必然存在证明序列$<A_0,A_1,...,A_m>,A_m=A$
现归纳证明对于每个$i\le m$均有$\Gamma\vDash A_i$
①若$A_i\in \Gamma$则显然$\Gamma\vDash A_i$
②若$A_i\in Axiom$则显然$\Gamma\vDash A_i$
③若存在$j,k<i,A_k=A_j\rightarrow A_i$，则由归纳假设
因为$\Gamma\vDash A_j,\Gamma\vDash A_k$
即可有$\Gamma\vDash A_j\rightarrow A_i$
根据MP规则可有
$\Gamma\vDash A_i$成立
综上，可有$若\Gamma\vdash A则\Gamma\vDash A$

### 协调性

设P是一个逻辑系统，Formula为P的公式集且$\Gamma\subseteq Formula$，即$\Gamma$是一个公式子集
①若$Th(P)\ne Formula$，则称P是绝对协调的。<b>可以理解为P无法证明出超出其公式集能够表示的公式</b>。P的一切公式均可证，无矛盾
②若$A\in Formula$，则$A\notin Th(P)$或$\thicksim A\notin Th(P)$则称P关于否定协调。<b>可以理解为对于P中的任何一个公式，P只能证出该公式或者证明出该公式的否定，即不能证明出矛盾</b>
③若$Th(\Gamma)\ne Formula$，则称$\Gamma$是协调的。<b>若P关于否定是协调的，则P是绝对协调的</b>

<font color='red'><b>若公式集$\Gamma$不协调，当且仅当他的某个有穷子集不协调</b></font>
<b>一个公式集合协调$\longrightarrow$一个公式集合推不出所有公式，只能推出$A$或$\thicksim A\longrightarrow$一个公式集合证不出矛盾</b>

### 完全性

#### 公式集的完全性

设$\Gamma$是公式集合，若对每个公式A都有：$A\in \Gamma$或者$\thicksim A\in \Gamma$，则称$\Gamma$是完全的。<b>可以理解为$\Gamma$有能力表示每一个公式，一个公式A必然能在$\Gamma$中找到他的反或者他本身</b>

<b>若$\Gamma$既是完全的又是协调的，则称$\Gamma$是极大协调的</b>

#### 保协扩张

假设命题逻辑公式集Formula=$\{A_0,A_1,...\}$，$\Gamma$是协调集
①令$\Delta_0=\Gamma$
②令$\Delta_{i+1}=\left\{ \begin{array}{} \Delta_i\cup\{A_i\}&\Delta_i\vdash A_i\\\Delta_i\cup\{\thicksim A_i\}&\Delta_i\nvdash A_i \end{array} \right.$
③令$\Delta_r=\cup_{i=0}^{\infty}\Delta_i$
则$\Delta_r$必然为<b>极大协调集</b>
因为他的每个有穷子集都协调，所以本身必然协调
又因为取到了极限，所以必然包含所有的公式的本身或其反其中一个，所以完全
<font color='red'>不是所有的性质都可以在取极限的情况下保持性质
<b>一个极大协调集确定一个唯一的指派</b>
</font>

#### 证：若$\Gamma\nvdash A$，则$\Gamma\cup\{\thicksim A\}$协调

假设$\Gamma\cup\thicksim A$不协调，
则$\Gamma\cup\thicksim A\vdash A$，此为不协调的定义，即可以证出矛盾
但因为$\Gamma\cup A\thicksim A$，此为显然，A为条件
所以可有$\Gamma\vdash A$
但条件要求$\Gamma\nvdash A$
矛盾
所以$\Gamma\cup\thicksim A$协调

#### 协调性与可满足性

<b>极大协调集$\Gamma_{mc}$必然是可满足集</b>
令指派$\phi$满足$\phi(p)=t$当且仅当$p\in\Gamma$
下面归纳证明对任意一个公式A，都有$\phi(A)=t$当且仅当$A\in \Gamma$
①若$A=p\in Atom$，即原子公式，则由定义自然成立
②若$A=\thicksim B$，则$\phi(A)=t\leftrightarrow \phi(B)=f\leftrightarrow B\notin\Gamma\leftrightarrow\thicksim B\in \Gamma\leftrightarrow A\in \Gamma$，成立，这里有归纳假设
③若$A=B\cup C$，则$\phi(A)=t\leftrightarrow \phi(B)=t\cup\phi(C)=t\leftrightarrow B\in\Gamma\cup C\in\Gamma$，由归纳可证
考虑正向$B\in\Gamma\cup C\in\Gamma\rightarrow B\cup C\in \Gamma$
若$B\in\Gamma\cup C\in\Gamma$
又因为$B\rightarrow B\cup C$
故有$B\cup C\in\Gamma$
考虑反向$B\cup C\in \Gamma\rightarrow B\in\Gamma\cup C\in\Gamma$
若$B\cup C\in \Gamma$且$B\notin\Gamma\cap C\notin\Gamma$反证法
则有$\thicksim B\in\Gamma\cap\thicksim C\in\Gamma$
而$B\cup C\in\Gamma$等价于$\thicksim B\rightarrow C\in\Gamma$
根据MP规则可有$C\in\Gamma$
不协调，矛盾
故有$B\cup C\in \Gamma\rightarrow B\in\Gamma\cup C\in\Gamma$
故不管A是极大协调集中的什么样的公式，都必然满足
故极大协调集是可满足集

#### 完全性定理

<b>若$\Gamma\vDash A则\Gamma\vdash A$</b>

证明真命题等价于证明逆否命题
即求证$若\Gamma\nvdash A则\Gamma\nvDash A$

①首先证明若$\Gamma\nvdash A则\Gamma\cup\{A\}$协调
假设不协调，反证法
则$\Gamma\cup\thicksim A\vdash A$，不协调的定义
但由于$\Gamma\cup A\vdash A$
可有$\Gamma\vdash A$
矛盾
所以$\Gamma\cup\{\thicksim A\}$是协调的

②证明$\Gamma\cup\{\thicksim A\}$是可满足的
前面已证，极大协调集是可满足
而由于协调集的任意一个有穷子集是协调的，故必然存在指派$\phi$使子集满足
所以$\Gamma\cup\thicksim A$是可满足的

③所以可以把$\thicksim A$拿到右边
即$\Gamma\vDash\thicksim A$
即$\Gamma\nvDash A$

逆否定理可证，则原命题可证
<b>故若$\Gamma\vDash A则\Gamma\vdash A$</b>

#### 紧致性定理

<b>语法紧致性</b>：公式集$\Gamma$是协调的当且仅当$\Gamma$的每一个有穷子集是协调的（任一系统）
<b>语义紧致性</b>：公式集$\Gamma$是可满足的当且仅当$\Gamma$的每个有穷子集是可满足的（命题、一阶）

若$\Gamma$是析取有效的，则对任何一个指派$\sigma$，都有一个公式$A\in\Gamma$使得$\sigma(A)=t$。相当于是不管是什么指派，将公式解释为什么，公式集$\Gamma$不是全假

$\Gamma$是析取有效的当且仅当$\Gamma$的某个有穷子集是析取有效的

$\Gamma$是析取有效的当且仅当$\overline{\Gamma}$是不可满足的
$\overline{\Gamma}$表示$\Gamma$的对偶，即将所有的公式取非

$\overline{\Gamma}$是不可满足的即有一个有穷子集是不可满足的

### 独立性

#### 公理/规则的独立性：
称形式系统FS中某条公理或规则是独立的，如果将其在原系统中删除后$(FS')$，则必然有$Th(FS')\subsetneq Th(FS)$
即删除某条公理后，会存在原来的部分公式不可证（语法层面）

#### 独立性证明方法：
①寻找某个性质P，证明在不使用该公理/规则的情况下所有定理都满足P
②但是原系统中的某些定理并不都满足P
例如去除某个公理后所有的定理都是单命题公式，但原来可证的定理不全是单命题公式

#### 例：证明AS1的独立性

考虑代数指派
$\begin{array}{} &\thicksim\\0&1\\1&0\\2&2 \end{array}$  $\begin{array}{} \cup&0&1&2\\0&0&0&0\\1&0&1&2\\2&0&2&0 \end{array}$
可发现
在只使用$AS_2,AS_3,MP$的时候，定理在该指派下恒为0
而$AS_1$不恒为0

## 消解&DPLL

### 定义

**①文字：命题变元及其否定，L
②短句：若干个文字的析取，C
③合取范式：若干个短句的合取
④互补文字：形如$p,\thicksim p$的一对文字
⑤空短句：0个文字的析取，$\square$
$\square$代表永假式，不可满足**

短句的集合表示：
如$p\cup\thicksim q\cup r$可表示为$\{p,\thicksim q,r\}$

合取范式的集合表示：
如$(p\cup\thicksim q\cup r)\cap(\thicksim r\cup q)$可表示为$\{\{p,\thicksim q,r\},\{\thicksim r,q\}\}$
即双层集合

$C-\{L\}表示为C-L$

### 消解

<b>消解式：</b>
设$C_1,C_2$为短句，若$L_1\in C_1,L_2\in C_2$为两个互补文字（一正一反），则称$(C_1-L_1)\cup(C_2-L_2)$为$C_1$和$C_2$的一个消解式，$L_1,L_2$为消解基，$C_1,C_2$为消解母式
例如，$C_1=\{p,q\}=p\cup q,C_2=\{\thicksim p,r\}=\thicksim p\cup r$，则$\{q,r\}=q\cup r$是一个消解式
$\phi(C_1\cap C_2)$可满足当且仅当$\phi(C)$可满足

<b>消解结果、消解序列：</b>
设$\Gamma$为短句集，C为短句，若存在短句序列
$C_0,...,C_m,C_m=C$
对任意$i\le m$满足下列条件之一
①$C_i\in \Gamma$
②存在$j,k<i$使得$C_i$是$C_j,C_k$的消解式
则称$C$为$\Gamma$的一个消解结果，记为$\Gamma\Vdash C$，并称$C_0,...,C_m$是一个从$\Gamma$导出$C$的消解序列

<b>$\Gamma$导出$\square$的消解序列称为$\Gamma$的反驳或否证，即证明$\Gamma$不可满足</b>

#### 消解可靠性

若$\Gamma\Vdash C$则$\Gamma\vdash C$

若$\Gamma\Vdash\square$则$\Gamma$不可满足

#### 消解完全性

若$\Gamma$不可满足，则$\Gamma\Vdash\square$

<b>证：若$\Gamma$不可满足，则$\Gamma\Vdash\square$</b>

设秩函数$f(\Gamma)=\sum_{i=1}^n\#C_i-\#\Gamma$，#表示集合中元素的数目。相当于集合中所有短句的文字个数之和-集合中短句数目。$\Gamma=\{C_1,...,C_n\}$
①当$f(\Gamma)=0$，则一定包含了一组互补的文字，短句均为一个文字。此时一定能够消解为$\square$，例如$\{\{p\},\{\thicksim p\}\}$
②当$f(\Gamma)\le k$时，假设消解序列存在，求证$k+1$时也可以构建一个消解序列
则$f(\Gamma)=k+1$时，必然存在一个短句$C\in\Gamma$使得$C\ge 2$
进一步，假设一个文字$L\in C$，则可有$\#(C-L)\ge 1$，表示L可能多次出现可能只出现一次
令$\Gamma_1=(\Gamma-C)\cup(C-L),\Gamma_2=(\Gamma-C)\cup\{L\}$，即一个是减去C中的L，一个是减去C加上L
因为$\Gamma$是不可满足的，这是给的条件
所以$\Gamma_1,\Gamma_2$都是不可满足的
且$f(\Gamma_1)\le f(\Gamma),f(\Gamma_2)\le f(\Gamma)$
可有$f(\Gamma_1)\le k,f(\Gamma_2)\le k$
归纳可有，$\Gamma_1,\Gamma_2$可以消解到$\square$，这里是因为前提是假设k之前的都成立
不妨设$\Gamma_1$的消解序列为$C_1,...,C_m$
将$C_1,...,C_m$中的$C-L$换为$C$，则此时这个消解序列要么消解到$L$，表示L在序列中没有互补出现；要么消解到$\square$，表示L在序列中存在互补出现
此时就是$\Gamma$的消解序列
则可知$\Gamma\Vdash L或\Gamma\Vdash\square$
同理，$\Gamma_2$可以消解到$\square$
即$(\Gamma-C)\cup\{L\}\Vdash\square$
因为上式可有$\Gamma\cup\{L\}\Vdash\square$
又因为$\Gamma\Vdash L$已证
故可有$\Gamma\cup\{L\}\Vdash\square$
最终可有$\Gamma\Vdash\square$

### DPLL

①<b>重言式（永真式）规则</b>：从当前语句$\Gamma$删除所有包含互补文字的短句得到$\Gamma'$，则$\Gamma$可满足当且仅当$\Gamma'$可满足，相当于剔除了$A\cup\thicksim A$的永真式

②<b>单文字规则</b>：若某个短句只有一个文字$L$，则此文字为单文字（其真假性可以直接判定）。从$\Gamma$中删除包含$L$的短句，删除每个短句中与$L$互补的文字得到$\Gamma''$。$\Gamma$可满足当且仅当$\Gamma''$可满足，相当于剔除了确定为假的文字

③**纯文字规则**：若文字$L$的互补文字在短句集中没有出现，则$L$称为纯文字，其真值可以直接确定。在$\Gamma$中删除所有包含$L$的短句后得到$\Gamma'''$，$\Gamma$可满足当且仅当$\Gamma'''$可满足，相当于剔除了确定为真的短句

④**分裂规则**：设$L,\overline{L}$互为互补文字，设当前短句集中（只）包含$L$的短句为$C_1,...,C_n$，（只）包含$\overline{L}$的短句为$C_1',...,C_m'$，两者都不包含的为$C_1'',...,C_k''$
令$\Gamma'=\{C_1-L,...,C_n-L\}\cup\{C_1'',...,C_k''\}$
令$\Gamma''=\{C_1'-\overline{L},...,C_m'-\overline{L}\cup\{C_1'',...,C_k''\}$，则$\Gamma$可满足当且仅当$\Gamma',\Gamma''$两者之一可满足，相当于在讨论文字$L$的真假性

#### 例：$\Gamma=\{\{\thicksim p,q\},\{\thicksim p,r,s\},\{\thicksim q,\thicksim r\},\{p\},\{\thicksim s\}\}$

①使用关于$p$的单文字规则，可有
$\{q\},\{r,s\},\{\thicksim q,\thicksim r\},\{\thicksim s\}\}$
②使用关于$q$的单文字规则，可有
$\{\{r,s\},\{\thicksim r\},\{\thicksim s\}\}$
③使用关于$\thicksim r$的单文字规则，可有
$\{s\},\{\thicksim s\}$
④使用关于$s$的单文字规则
$\square$
故不可满足

<div STYLE="page-break-after: always;"></div>

# 003 一阶逻辑

## $F$系统定义

一阶逻辑也叫谓词演算或量化理论，基本上相当于加了全称量词和存在量词的命题逻辑，写作$\mathcal{F}=<\Sigma_f,Term_f,Formula_f,Axiom_f,Rule_f>$

$\Sigma_{f}$字母表包括通用逻辑符号和特殊符号
通用逻辑符号包括：连接词$\thicksim,\cup$；量词$\forall$；辅助符号$(,)$
特殊符号包括常元和变元
常元可分为个体常元（0元函词）、函数常元（函词：函数）、命题常元（0元谓词）、谓词常元（谓词：真假）
变元可分为个体变元、函数变元、命题变元、谓词变元
变元的数目是可数无穷多的，和自然数一个量级；常元是任意多的
**个人理解，函词表示有多个可能值（语义层面）的变元/常元，如年龄、集合；谓词表示只有真假两种情况（语义层面）的变元/常元。**

$Term$：项，是没有真假性的，归纳定义为
①若x为个体变元或常元，则$x\in Term$
②若f为n元<font color='red'><b>函数</b></font>常元或变元，$t_1,...t_n$为项，则$f(t_1,...,t_n)$为项
③任何项可由①②得到
**函词是没有真假性的，只是陈述性语句；谓词是具有真假性的**
例：A是某一个人，是个体变元，f(x)表示个体变元x的爸爸,f(x)是1元函数变元?，则$f(A)$表示A的爸爸

$Atom$：原子公式，由下列公式组成：
设$p$是n元谓词常元或变元，$t_1,...,t_n$为项，则$p(t_1,...,t_n)$是一个公式（原子公式）
**谓词表示一个关系，具有真假性**
$P(x,y)$表示x比y年纪大
$Formula$：公式：可归纳定义为
①原子公式都是公式
②$\thicksim$原子公式都是公式
③原子公式$\cup$原子公式都是公式
**④A是原子公式，x是个体变元，则$\forall x,A$也是公式**
⑤任意一个公式可以跟据有限次的①-④得到
<font color='red'><b>公式称为f系统的语言，记为$L(f)$</b></font>
**公式具有真假性**

$Axiom$：公理：
①$AS_1:A\cup A\rightarrow A$
②$AS_2:A\rightarrow B\cup A$
③$AS_3:A\rightarrow B\rightarrow (C\cup A\rightarrow B\cup C)$
④$AS_4:\forall x,A\rightarrow S_t^x A$，要求项$t$对A中的$x$是自由的，个人理解是项$t$中不存在$x$。
例：$\forall x,A\rightarrow A;\forall x,p(x,y)\rightarrow S_t^xp(x,y)\rightarrow p(t,y)$
⑤$AS_5:\forall x,(A\cup B)\rightarrow A\cup \forall x,b$，其中x在A中没有自由出现。个人理解是x在A中不作为自由变元，所以约束不到。
例：$\forall x,(\exist x,p(x)\cup Q(x))\rightarrow \exist x,P(x)\cup \forall x,Q(x)$

$Rule$：规则
①$MP:\frac{A\rightarrow B,A}{B}$
②$Gen:\frac{A}{\forall x,A}$
<font color='red'><font size=5><b>无前提依赖的证明，即没有前提条件$\Gamma$的证明：只用公理和规则
有前提依赖的证明：可能包含共公设集中$\Gamma$的公式，需要对$Gen$规则进行限制，并且有一条额外的$\alpha\beta$规则。公设集分有穷和无穷两种</b></font></font>

### 派生符号

$A\cap B\rightarrow \thicksim(\thicksim A\cup \thicksim B)$
$(A\rightarrow B)\rightarrow (\thicksim A\cup B)$
$A\equiv B\rightarrow ((A\rightarrow B)\cap(B\rightarrow A))$
$\exist x,A\rightarrow \thicksim x,\thicksim A$
存在x就是不是所有的x都不成立

### 个体变元的自由/约束出现

设x为个体变元
①称x在A中形如$\forall x,B或\exist x,B$的子公式称为约束出现，即x在公式A中会被量词约束
②变元的非约束出现称为自由出现
③若x在A中有约束出现，则x为A的约束边缘
④若x在A中有自由出现，则x为A的自由变元
<b>⑤A中无自由的个体变元，则A为闭公式
⑥A中除了约束个体变元没有其他变元（如函数变元等）则A为句子
注意：闭公式中可能包含函数变元、命题变元、谓词变元
</b>
例：$Q(x)\cup\thicksim P(x)\rightarrow\forall x,R(x)$中，前面的Q和P中的x为自由变元，而R中的x为约束边缘

### 对项的代入

设$x_1,...,x_n$是个体变元，$t_1,...,t_n$是项，令$\theta=S_{t_1,...,t_n}^{x_1,...,x_n}$
①若$a$为个体常元，则$\theta(a)=a$，表示对变元的代入没有影响到常元
②若x为个体变元，则$\theta(x)=\left\{ \begin{array}{} x&x\notin\{x_1,...,x_n\}\\t_i&x=x_i \end{array} \right.$，即个体变元的代入直接带入即可
③若$f$为函数常元，则$\theta(f(t_1',...,t_m'))=f(\theta(t_1'),...,\theta(t_m'))$，即对函数常元的代入等价于对函数的变量的代入
④若$F$为函数变元，则$\theta(F(t_1',...,t_m'))=F(\theta(t_1',...,\theta(t_m')))$，即对函数变元的代入等价于对函数参数的代入

### 对公示的代入

<b>带入到个体变元</b>
设$x_1,...,x_n$是个体变元，$t_1,...,t_n$是项，令$\theta=S_{t_1,...,t_n}^{x_1,...,x_n}$
①对原子公式$P(t_1',...,t_m')$，有$\theta(P(t_1',...,t_m'))=P(\theta(t_1'),...,\theta(t_m'))$，对原子公式的代入等价于对原子公式中每一项的代入
②$\theta(\thicksim A)=\thicksim\theta(A)$，即代入操作对操作符无意义
③$\theta(B\cup C)=\theta(B)\cup\theta(C)$
④$\theta(\forall x,A)=\left\{ \begin{array}{} \forall x,\theta(A)&x\notin\{x_1,...,x_n\}\\ \forall x,S_{t_1,...,t_{i-1},t{i+1},...,t_n}^{x_1,...,x_{i-1},x_{i+1},...,x_n}A&x=x_i \end{array} \right.$，即代入操作对约束边缘无效

<b>带入到命题变元</b>
设$p_1,...,p_n$是命题变元，$A_1,...,A_n$是公式，令$\theta=S_{A_1,...,A_n}^{p_1,...,p_n}$
①$\theta(p)=\left\{ \begin{array}{}p&p\notin\{p_1,...,p_n\}\\A_i&p=p_i \end{array}\right.$
②$\theta(p(t_1',...,t_m'))=p(t_1',...,t_m')$
③$\theta(\thicksim A)=\thicksim\theta(A)$
④$\theta(B\cup C)=\theta(B)\cup\theta(C)$
⑤$\theta(\forall x,A)=\forall x,\theta(A)$

### 可代入

#### 项的可代入

称项$t$对公式$A$中的个体变元$x$可代入（为自由的），如果对$t$中的每个个体变元$y$，变元$x$在$\forall y/\exist y$，辖域内无自由出现。即不被约束。
<b>代入后会增加约束变元
不可代入不是不能代入，而是代入之后会影响公式的语义</b>
例：$A=\exist y,(x<y)$，则$z$对A中的x可代入，$y+1$对A中的x不可代入

#### 公式的可代入

公式$B$对A中的命题变元p是可代入（为自由）的，说明B中的每个自由变元y而言，p不出现在$\forall y/\exist y$辖域内。即公式B中的每个自由变元在公式A中都没有约束出现
<b>代入前后变元约束出现的次数不改变</b>

## F的定理与导出规则

<b>无前提依赖</b>：不使用公设集中的公式，证明序列中仅出现公理以及通过应用规则得到的公式，即没有前提条件
<b>带前提以来</b>：证明序列中可能包含公设集中的公式
在带前提依赖的证明中，对Gen规则的使用增加了相应的限制，并需要增加一条额外的$\alpha\beta$规则，同时，还要区分公设集为有穷和无穷的情况

### p永真

存在命题逻辑中永真式B，使得A=$\sigma(B)$代入是永真的。
例：
$\thicksim\forall x,p(x)\cup \forall x,p(x)$是p中永真式$\thicksim A\cup A$进行$S_{\forall x,p(x)}^A$代入后的结果
$p\rightarrow p\cup\forall x,q(x)$是对p中永真式$A\rightarrow A\cup B$进行$S_{p,\forall x,q(x)}^{A,B}$代入后的结果

①若A是$P$系统的永真式，则有$\vdash_{F}A$
②若A是P永真的，则$\vdash_{F}A$，注意，p永真式包含p中的永真式，可以使经过代入的
③若$\vdash_{f}A_1,...,\vdash_{f}A_n，且A_1\cap...\cap A_n\rightarrow B$是p永真的，则$\vdash_{f}B$，MP规则依然有效

### 无前提依赖证明的协调性

取$q\in Atom$，即原子公式，定义映射$\phi:Formula\rightarrow Formula如下$
①若$A\in Atom$，即原子公式，则$\phi(A)=\phi$
②$\phi(\thicksim A)=\thicksim\phi(A)$
③$\phi(B\cup C)=\phi(B)\cup\phi(C)$
④$\phi(\forall x,A)=\phi(A)$
若$\vdash_{f}A$则$\vdash_{f}\phi(A)$
可以都转换成命题逻辑然后正常运算
$f$关于无前提依赖证明满足绝对协调以及关于否定协调

### 肯定出现及否定出现

设$A,B\in Formula_{f}$，并将A中的派生连接词、量词全部用原始符号$\thicksim,\cup,\forall$替换，则
①若B在A中的某个指定出现位于偶数个$\thicksim$的辖域中，则称B的该次出现为正出现或肯定的。可以理解为不影响其值
②若B在A中的某个指定出现位于奇数个$\thicksim$的辖域中，则称B的该次出现为负出现或否定的，可以理解为公式会对该值取反
③若B在A中的所有指定出现都是肯定的，则B在A中是肯定的
④若B在A中的所有制定出现都是否定的，则B在A中是否定的
例：$\thicksim \forall xp(x)\cup(\thicksim\thicksim\forall y\thicksim q(y)\cup \thicksim\forall z\thicksim(\thicksim p(z)\cup q(z)))$
其中的x,y,z,y分别是否定出现(1)，肯定出现(4)，否定出现(3)，肯定出现(2)

### $\rightarrow_{sub}$定理

设$A,M,N\in Formula_f,且y_1,...,y_n$为出现在M和N中的所有自由个体变元，则
①若M在A中是肯定的，则$\vdash\forall y_1,...,\forall y_n.(M\rightarrow N)\rightarrow(A\rightarrow A_{N}^M)$，可以理解为在M能够推出N的情况下，A可以推出将A中的M换为N后的公式，这是因为当A成立的时候，由于M在A中是肯定的，相当于默认了M成立。
②若M在A中是否定的，则$\vdash\forall y_1,...,\forall y_n.(M\rightarrow N)\rightarrow(A_N^M)\rightarrow A$，<font color='red'>？怎么理解</font>
③若M在A中是肯定的，且$\vdash M\rightarrow N$，则$\vdash A\rightarrow A_N^M$
④若M在A中是否定的，且$\vdash M\rightarrow N$，则$\vdash A_N^M\rightarrow A$

### $\equiv_{sub}$定理

设$A,M,N\in Formula,且y_1,...,y_n$为出现在M和N中的所有自由变元集合，则
①$\vdash \forall y_1,...,\forall y_n.(M\equiv N)\rightarrow(A\equiv A_N^M)$
②若$\vdash M\equiv N$，则$\vdash A\equiv A_N^M$
③若$\vdash M\equiv N且\vdash A$，则$\vdash A_N^M$

### $\alpha\beta$规则

<b>$\alpha\beta$条件</b>：
设$C\in Formula,y$不是C的自由变元且$y$对$C$中的$x$是自由的，则称$x,y$关于$C$满足$\alpha\beta$条件，记作$(C,x,y)$
<b>个人理解：关于x的公式代入y后原式中不包含剩余的y，且原式中本就没有y，代入后是完全一样的关于y的公式
例：$C=\forall x.P(x)/P(x)$</b>
设$(C,x,y)$，则：

<b>代入可逆性</b>：$C=S_x^yS_y^xC$，即先换x再换y仍然是原结果

<b>换名等价性</b>：$\vdash\forall x.C\equiv\forall y.S_y^xC$，即对一个公式，将其中的某个变元约束后，再代入时不会影响原式

<b>$\alpha\beta$规则</b>：若$\vdash A$则$\vdash A_{\forall y.S_y^xC}^{\forall x.C}$，即将公式A中的一个量词子公式中的约束变元进行替换后，不会影响公式的可满足性

#### 证：$\vdash C=S_x^yS_y^xC$，y不是C的自由变元且$y$对$C$中的$x$是自由的

先证明对任意一个项$t$有$S_x^yS_y^xt=t,y$在$t$中不出现
①当$t=a$个体常元，则代入没有效果，自然成立
②当$t=x$个体变元，则代入后无影响，仍为自身
③当$t=z$个体变元，则$t$中不存在$x$，代入无效，仍为自身
④$t\ne y$，前提条件
⑤当$t=f(t_1,...,t_n)$，即是n元函词变元，则$S_x^yS_y^xt=S_x^yS_y^xf(t_1,...,t_n)=f(S_x^yS_y^xt_1,...,S_x^yS_y^xt_n)$
此时可以用归纳，自然得出$=f(t_1,...,t_n)=t$
⑥求证对任意一个公式$C$，有$S_x^yS_y^xC=C$，这里相当于要考虑谓词部分
>(1)当$C=P=P(t_1,...,t_n)$，即是一个原子公式，有$S_x^yS_y^xC=S_x^yS_y^xP(t_1,...,t_n)=P(S_x^yS_y^xt_1,...,S_x^yS_y^xt_n)=C$
注意，这里处理的是n元谓词变元的情况，上面处理的是n元函词的情况
(2)当$C=\thicksim B$，则$S_x^yS_y^xC=S_x^yS_y^x(\thicksim B)=\thicksim(S_x^yS_y^xB)$
根据归纳可有$S_x^yS_y^xB=B$
故可有$S_x^yS_y^xC=\thicksim B=C$
(3)当$C=B\cup D$，则$S_x^yS_y^xC=S_x^yS_y^x(B\cup D)=S_x^yS_y^xB\cup S_x^yS_y^xD$
根据归纳可有$S_x^yS_y^xC=B\cup D=C$
(4)当$C=\forall z.D$，则$S_x^yS_y^xC=S_x^yS_y^x(\forall z.D)$
需要分情况
>>1)当$z=x$时，$S_x^yS_y^xC=S_x^yS_y^x(\forall x.D)$
因为原始式子中没有x的自由出现，所以$S_x^yS_y^x\forall x.D=S_x^y\forall x.D$
而对于y，前提条件中说明y在t中没有自由出现，所以y在D中没有自由出现，故$S_x^yD=D$
故成立
2）当z=y时，说明y在t中有约束出现，即$C=\forall y.D$
因为y对C中的x是自由的，此时D中必然没有自由出现的x ?
所以对x的代入没有意义，而对y的代入是无效的
3)当$z\ne x\And z\ne y$，此时$C=\forall z,D$，可能D中有自由的x，但不可能有y，因为y不能为自由变元
y对D中的x是可代入的，同时D中没有自由的y，此时<D,x,y>构成了一个新的$\alpha\beta$对
故可有$S_x^yS_y^xC=C$

#### 证：$若(C,x,y)则\forall x.C\equiv\forall y.S_y^xC$

①证明$\forall x.C\rightarrow\forall y.S_y^xC$
因为$AS_4$定义了$\forall x.C\rightarrow S_y^xC$
又因为当x在A中自由的时候，$A\rightarrow B\leftrightarrow A\rightarrow\forall x.B$成立
可有$\forall x.C\rightarrow\forall y.S_y^xC$，因为y在C中没有自由出现（$\alpha\beta$对）
成立

②证明$\forall y.S_y^xC\rightarrow\forall x.C$
根据$AS_4$可有$\forall x.C\rightarrow S_y^xC$
代入可有$\forall y.S_y^x\rightarrow S_x^yS_y^xC$
由于前面已证$S_x^yS_y^xC=C$
故可有$\forall yS^x_yC\rightarrow C$
又因为x在$\forall y.S_y^xC$中没有自由出现，全都被替换为了y
故可有$\forall y.S_y^xC\rightarrow\forall x.C$

### 带前提依赖证明

给定有穷公式集$\Gamma$，如果存在有穷序列$A_0,...,A_m,A_m=A$，且对每个$i\le m$必定有以下几种情况成立：
①Hyp：$A_i\in\Gamma$，即$A_i$是给定的前提中的公式
②Ax：$A\in Axiom$，公理
③MP：存在$j,k<i$，使得$A_k=A_j\rightarrow A_i$，即可以通过$MP$规则得到$A_i$
④Gen：存在$j<i$，使得$A_i=\forall x.A_j$，其中$x$在$\Gamma$中不自由，即可以通过现有公式构成
⑤$\alpha\beta$：存在$j<i$，公式$C$，个体变元$x,y$满足$(C,x,y)$且$A_i=A_{j\forall y.S_{y}^xC}^{\forall x.C}$。即y对C是约束的，没有自由变元，对于x是自由的，那么将$A_j$中的与x有关的子公式替换为y代入x的子公式之后，就变成了$A_i$，此时$A_i$和$A_j$的可满足性相同

则称$A$由$\Gamma$可证，$\Gamma\vdash A$，并称$A_0,...,A_m$是由$\Gamma$导出A的证明

<b>⑥若$\Gamma$前提是无穷集，则$\Gamma\vdash A$是指存在$\Gamma$的一个有穷子集$\Delta$使$\Delta\vdash A$</b>
<font color='red'>
个人理解：
相较于无前提的证明，对Gen规则增加了一个要求x在$\Gamma$前提中不自由，有约束的条件。因为如果x在前提中有自由出现，就不能说对任意变量都可以满足某公式，前提中存在对变量的要求，可能会产生冲突
增加了一条$\alpha\beta$规则，这就相当于规定了在x是$\Gamma$中自由的情况向下如何进行代入操作，即可以理解为部分代入
</font>

### 变元替换引理

设$X=\{x_1,...,x_n\}$，公式集$\Gamma$为有穷集合，$\Gamma\vdash A$且每个$x_i$均在$\Gamma\cup\{A\}$中不自由，则存在证明序列$A_0,...,A_m=A$满足：
①$X$中每个变元在证明序列中都没有自由出现
②证明序列中不对$X$中的变元使用$Gen$规则

<b>单调性定理</b>：$若\Gamma\vdash A且\Gamma_1\subseteq \Gamma_2则\Gamma_2\vdash A$

## 语义和前束范式

### 函数的单点取代操作

设$f:X\rightarrow Y$，则任取$x_0\in X及y_0\in Y$，可以得到一个新的函数$f[x_0/y_0]:X\rightarrow Y$，定义为：
$f[x_0/y_0](x)=\left\{ \begin{array}{} f(x)&x\ne x_0\\y_0&x=x_0 \end{array} \right.$
相当于直接强制将函数中的某个变量用另一个变量取代

①若$x_1\ne x_2$则$f[x_1/y_1][x_2/y_2]=f[x_2/y_2][x_1/y_1]$，即可以互换顺序
②$f[x_0/y_1][x_0/y_2]=f[x_0/y_2]$，即多次取代只有第一个有效
③$f[x_0/f(x_0)]=f$，即用函数值取代不变

<b>解释：给定二元偶$I=<D,I_0>$为$F$的一个解释，其中$D$是一个非空集合，称为论域，$I_0$为如下定义的一个映射：</b>
①若$a$为个体常元，则$I_0(a)\in D$，即$I_0$是一个常元到论域的映射
②若$f$为n元函词常元，则$I_0(f):D^n\rightarrow D$，即$I_0$是一个从n元常元到论域的映射
③若$p$为命题常元，则$I_0(p)\in B,B=\{t,f\}$，$I_0$是一个从命题常元到真假值的映射
④若$P$为n元谓词常元，则$I_0(P):D^n\rightarrow B$，即是一个n元常元到论域的映射
<b>个人理解：解释就是给<font color='red'>常元</font>一个赋值，个体常元和函词常元从论域$D$中取，命题常元和谓词常元从$B$中取</b>

<b>指派：给定解释$I=<D,I_0>$，若映射$\sigma$满足</b>
①若$x$为个体变元，则$\sigma(x)\in D$，即$\sigma$是一个变元到论域的映射
②若$g$为n元函词变元，则$\sigma(g):D^n\rightarrow D$，即$I_0$是一个从n元变元到论域的映射
③若$q$为命题变元，则$\sigma(q)\in B,B=\{t,f\}$，$\sigma$是一个从命题变元到真假值的映射
④若$Q$为n元谓词变元，则$\sigma(Q):D^n\rightarrow B$，即是一个n元变元到论域的映射
则称$\sigma$是$I$下的一个指派，通常，$\sum_{I}$表示$I$下的所有指派构成的集合
<b>个人理解：指派就是给<font color='red'>变元</font>一个赋值，个体变元和函词变元从论域$D$中取，命题变元和谓词变元从$B$中取</b>

### 项的语义

设$I=<D,I_0>$以及$\sigma\in\sum_I$，对每个$t\in Trem$，即项，可归纳定义其语义$I(t)(\sigma)$如下：
①若$t=a$为个体常元，则$I(t)(\sigma)=I_0(a)$，即没有用到指派
②若$t=x$为个体变元，则$I(t)(\sigma)=\sigma(x)$，即没有用到解释
③若$t=f(t_1,...,t_n)$，即f为n元函数常元，则$I(t)(\sigma)=I_0(f)(I(t_1)(\sigma),...,I(t_n)(\sigma))$，即将函词进行赋值之后将函词的每个变量进行指派或解释，这是个迭代
④若$t=g(t_1,...,t_n)$，即g为n元谓词常元，则$I(t)(\sigma)=\sigma(g)(I(t_1)(\sigma),...,I(t_n)(\sigma))$，即将谓词进行赋值之后对谓词的每个变量进行指派或解释，这是个迭代

因此，可以将$I$看做$Term\rightarrow(\sum_I\rightarrow D)$上的一个泛函

### 公式的语义

设$I=<D,I_0>$以及$\sigma\in\sum_{I}$，对每个$A\in Formula$，可归纳定义其语义$I(A)(\sigma)$为：
①若$A=P(t_1,...,t_n)$，其中P是n元函词常元，则$I(A)(\sigma)=I_0(P)(I(t_1)(\sigma),...,I(t_n)(\sigma))$，即对函词进行解释，然后进行迭代
②若$A=Q(t_1,...,t_n)$，其中Q是n元谓词常元，则$I(A)(\sigma)=\sigma(Q)(I(t_1)(\sigma,...,I(t_n)(\sigma)))$，即对谓词进行指派，然后进行迭代
③若$A=\thicksim B$，则$I(A)(\sigma)=\left\{ \begin{array}{} t&I(B)(\sigma)=f\\f&I(B)(\sigma)=t \end{array} \right.$
④若$A=B\cup C$，则$I(A)(\sigma)=\left\{ \begin{array}{} f&I(B)(\sigma)=I(C)(\sigma)=f\\t&other \end{array}\right.$
⑤若$A=\forall x.B$，则$I(A)(\sigma)=\left\{ \begin{array}{} f&\exist d\in D.I(B)(\sigma[x/d])=f \\t&other \end{array}\right.$，这里的意思是如果存在一个论域中的值，能够让$B$的指派（令B中的x为值d）为$f$，则说明任意的条件不满足

#### 例：假设某一阶系统语言中仅包含一个个体变元x，一个命题变元q，一个二元谓词常元P，一个一元函数常元f以及两个个体常元a，b，求1）论域D={$\alpha,\beta,\gamma$}，则有多少个解释。2）对任意一个以D为论域的解释$I$，$\Sigma_I$中有多少个指派<font color='red'>?</font>

1）依次查看即可
①对一个二元谓词常元，有$2^1$种结果，有$3^2$种输入方式，共计$2^{3^2}$种可能
②对一个一元函数常元，有$3^1$种结果，有$3^1$种输入方式，共计$3^1*3^1$种可能
③对两个个体常元，有$3^2$种可能
总计$2*3^2*3*3*3^2$中可能

2）查看对于变元有多少个指派即可
①对一个个体变元，有$3^1$种可能
②对一个命题变元，有$2^1$种可能
总计$3*2$种指派

### 代入定理

设$A\in Formula$，项$t$对A中的x可代入，即项t中的每个个体变元在A中没有对x进行约束，公式B对A中的命题变元p可代入，即公式B中的每个自由变元在A中没有对p进行约束，则对任意解释$I$以及指派$\sigma\in\sum_{I}$，有
<font size=4><b>①对任意的项$t'$有$I(S_t^xt')(\sigma)=I(t')(\sigma[x/d])$，其中$d=I(t)(\sigma)$，即将任意项中的某个个体变元代入为另一个项t之后，其结果等同于将该个体变元强制赋值为该项t</b></font>
例：对项$P(x)$，可有$I(S_t^xP(x))(\sigma)=I(P(t))(\sigma)=\sigma(P(t))$
而$I(P(x))(\sigma[x/I(t)(\sigma)])=I(P(t))(\sigma)=\sigma(P(t))$

<font size=4><b>②$I(S_t^xA)(\sigma)=I(A)(\sigma[x/d]),d=I(t)(\sigma)$，即将公式中的某个个体变元代入为项t之后，效果等同于将公式中的x强制赋值为t在同一指派下的值。要求项t对于A中的x是可代入的，即项中的每个个体变元没有对x进行约束</b></font>

<font size=4><b>③$I(S_B^pA)(\sigma)=I(A)(\sigma[p/v]),v=I(B)(\sigma)$，即将公式中的某个命题变元代入为公式B之后，效果等同于将公式中的p强制赋值为B在同一指派下的值。要求公式B对于A中的p是可代入的，即公式B中的每个自由变元没有对p进行约束</b></font>

<b>证：对任意的项$t'$有$I(S_t^xt')(\sigma)=I(t')(\sigma[x/d])$，其中$d=I(t)(\sigma)$</b>
分情况考虑项$t'$的可能取值
①$t'=z,z\ne x$，此时代入操作无效，可有
$I(S_t^xt')(\sigma)=I(S_t^xz)(\sigma)=I(z)(\sigma)=\sigma(z)$
而$I(t')(\sigma[x/d])=I(z)(\sigma[x/d])$，由于没有x，指派无效
故$I(t')(\sigma[x/d])=I(z)(\sigma)=\sigma(z)$相等
②$t'=x$，此时代入操作有效，可有
$I(S_t^xt')(\sigma)=I(S_t^xx){\sigma}=I(t)(\sigma)=d=\sigma[x/d](x)=I(x)(\sigma[x/d])=I(t')(\sigma[x/d])$
③$t'=a$，为个体常元，此时代入操作无效，可有
$I(S_t^xt')(\sigma)=I(a)(\sigma)=I_0(a)=I(a)(\sigma[x/d])=I(t')(\sigma[x/d])$，当无变元时，指派$\sigma$随便取
④$t'=f(t_1,...,t_n)$，即是n元函数常元，此时指派对f不起作用，可能对f的变量$t_1,...,t_n$起作用
$I(S_t^xt')(\sigma)=I_0(f)(I(S_t^xt_1)(\sigma),...,I(S_t^xt_n)(\sigma))(\sigma)$，此时根据归纳可有，
$I(S_t^xt')(\sigma)=I_0(f)(I(t_1)(\sigma[x/d]),...,I(t_n)(\sigma[x/d]))(\sigma)=I(f(t_1,...,t_n))(\sigma[x/d])$，这一步是因为满足了迭代，可以拿到外面来
最终可有$I(S_t^xt')(\sigma)=I(t')(\sigma[x/d])$
⑤$t'=g(t_1,...,t_n)$，即是n元函数变元，此时解释对g不起作用，可能对g的变量起作用
$I(S_t^xt')(\sigma)=I(S_t^xg(t_1,...,t_n))(\sigma)=I(g(S_t^xt_1,...,S_t^xt_n))(\sigma)=\sigma(g)(I(S_t^xt_1)(\sigma),...,I(S_t^xt_n)(\sigma))$
根据归纳可有$=\sigma(g)(I(t_1)(\sigma[x/d]),...,I(t_n)(\sigma[x/d]))$
又因为$\sigma(g)=\sigma[x/d](g)$
所以可以拿出来$=I(g(t_1,...,t_n))(\sigma[x/d])=I(t')(\sigma[x/d])$

<b>证：对任意的公式$A$有$I(S_t^xA)(\sigma)=I(A)(\sigma[x/d]),d=I(t)(\sigma)$</b>
考虑公式的几种情况
①$A=P(t_1,...,t_n)$原子公式的情况，且是n元谓词常元，此时指派对P不起作用
$I(S_t^xA)(\sigma)=I(S_t^xP(t_1,...,t_n))(\sigma)=I(P)(S_t^xt_1,...,S_t^xt_n)(\sigma)=I_0(P)(I(S_t^xt_1)(\sigma),...,I(S_t^xt_n)(\sigma))$
此时可以用归纳
$=I_0(P)(I(t_1)(\sigma[x/d]),...,I(t_n)(\sigma[x/d]))$
可以提出来
$=I(P(t_1,...,t_n))(\sigma[x/d])=I(A)(\sigma[x/d])$从成立
②$A=Q(t_1,...,t_n)$原子公式的情况，且是n元谓词变元，此时指派对Q有作用，解释无作用
$I(S_t^xA)(\sigma)=I(S_t^xQ(t_1,...,t_n))(\sigma)=I(Q)(S_t^xt_1,...,S_t^xt_n)(\sigma)=\sigma(Q)(I(S_t^xt_1)(\sigma),...,I(S_t^xt_n)(\sigma))$
此时可以用归纳
$=\sigma(Q)(I(t_1)(\sigma[x/d]),...,I(t_n)(\sigma[x/d]))=\sigma[x/d](Q)(I(t_1)(\sigma[x/d]),...,I(t_n)(\sigma[x/d]))$
故可有$=I(Q(t_1,...,t_n))(\sigma[x/d])$成立
③$A=\thicksim B$
$I(S_t^xA)(\sigma)=I(\thicksim S_t^xB)(\sigma)=\thicksim I(S_t^xB)(\sigma)$
采用归纳，可有$=\thicksim I(B)(\sigma[x/d])=I(\thicksim B)(\sigma[x/d])=I(A)(\sigma[x/d])$
④$A=B\cup C$
$I(S_t^xA)(\sigma)=I(S_t^x(B\cup C))(\sigma)=I(S_t^xB\cup S_t^xC)(\sigma)=I(S_t^xB)(\sigma)\cup I(S_t^xC)(\sigma)$
根据归纳，可有
$=I(B)(\sigma[x/d])\cup I(C)(\sigma[x/d])=I(B\cup C)(\sigma[x/d])=I(A)(\sigma[x/d])$成立
⑤$A=\forall z.B,z\ne x$，此时，代入操作对A无效，对B可能有效
$I(S_t^xA)(\sigma)=I(S_t^x\forall z.B)(\sigma)=I(\forall z.S_t^xB)(\sigma)=\forall z.I(S_t^xB)(\sigma)$
由归纳可有$=\forall z.I(B)(\sigma[x/d])$
即$=I(\forall z.B)(\sigma[x/d])=I(A)(\sigma[x/d])$
⑥$A=\forall x.B$，此时，由于是约束边缘，代入无效
$I(S_t^xA)(\sigma)=I(S_t^x\forall x.B)(\sigma)=I(\forall x.B)(\sigma)$
根据归纳，可有
$=I(\forall x.B)(\sigma[x/d])=I(A)(\sigma[x/d])$
这里我只是单纯地不想用黑板那个证，不知道对不对，太麻烦了。

<b>若x在A中不自由，则对任意的$d_1,d_2\in D$，有$I(A)(\sigma[x/d_1])=I(A)(\sigma[x/d_2])$</b>
即
<font size=4><b>
闭公式：没有自由个体变元的公式
句子：没有自由变元的公式
若A为句子，则A的真值只与解释（对常元的赋值）相关，而与指派（对变元的赋值）无关</b></font>

### 关于语义的定义

①<b>可满足的公式：</b>给定公式$A\in Formula$，若存在解释$I$以及指派$\sigma\in\Sigma_I$，使得$I(A)(\sigma)=t$，则称A是可满足的，记作$\vDash_{I,\sigma}A$
②<b>公式模型：</b>对公式A，存在解释$I$使得每个$指派\sigma\in\Sigma_I$都有$\vDash_{I,\sigma}A$成立，则$I$是A的模型，记作$\vDash_{I}A$，即有一个对常元的解释使得A在当前解释下永真
③<b>永真/有效：</b>每个解释都是A的模型，记作$\vDash A$
④<b>可满足的公式集合：</b>给定公式集合$\Gamma$，若存在解释$I$以及指派$\sigma\in \Sigma_{I}$，使得对每个$A\in\Gamma$都有$\vDash_{I,\sigma}A$成立，即有一个解释和指派能够让所有的公式同时为真
⑤<b>公式集模型：</b>对公式集$\Gamma$，若对每个$A\in \Gamma$都有$\vDash_{I}A$，则称$I$是$\Gamma$的一个模型，记为$\vDash_{I}\Gamma$，即存在一个解释，对任意指派，都可以使公式集中的任意公式成立
⑥<b>公式集的逻辑结果：</b>若对每个解释$I$和指派$\sigma\in\Sigma_I$，若$\vDash_{I,\sigma}\Gamma则\vDash_{I,\sigma}A$，就称$A$是$\Gamma$的逻辑结果，记为$\Gamma\vDash A$，即任意一对可以让公式集满足的解释和指派，都会同时让某个公式A成立，则说明公式集成立的情况下，公式A必然成立

### 前束范式

设$A\in Formula$是公式，$\exists\forall=\{\forall,\exists\},x$为个体变元
①若$\exists\forall x.C$是A的子公式，且x在C中没有自由出现，则称$\exists\forall x$是空量词，即他没有任何作用，没有限制到任何东西
例：$\exists x.(\forall x.P(x))$，对于P(x)中的x，外层的$\exists$没有任何作用，因为可以直接将x换成y，而此时P(y)中便不再有x
②若A中无空量词，且量词均不出现在$\thicksim,\cup$的辖域内，则称A为<b>前束范式</b>
即当且仅当A形如$\exists\forall_1 x_1,...,\exists\forall_n x_n.B$
其中B不含有量词，$x_1,...,x_n$是彼此不同的个体变元，即量词提前

#### 矫正的

若$A\in Formula$满足：
①A中没有空量词
②A中的自由变元与约束变元不同名
③A中不同的约束变元之间不同名
则称A是矫正的

假设A是矫正的公式，那么对其中的每一个量词$\exists\forall_i$，A的前束范式为$\widecheck{\exist\forall_1}x_1,...,\widecheck{\exist\forall_n}x_n.B$，其中
$\widecheck{\exist\forall_i}=\left\{ \begin{array}{} \forall_i&\exist\forall_i=\forall并且在A中是肯定的 或者 \exist\forall_i=\exist并且在A中是否定的\\\exist_i&\exist\forall_i=\exist并且在A中是肯定的 或者 \exist\forall_i=\forall并且在A中是否定的 \end{array} \right.$

#### 前束范式存在性定理

设$A\in Formula$，则存在前束范式$A'\in Formula$使得$\Vdash A\equiv A'$，即任意一个公式必然存在与之对应的前束范式
 
## 元性质

### 可靠性

①若$\vdash A$则$\vDash A$
②若$\Gamma\vdash A$则$\Gamma\vDash A$
推论：若公式集$\Gamma$是可满足的，则必然是协调的

#### 证明若$\Gamma\vdash A$则$\Gamma\vDash A$

证明存在序列$A_0,...,A_m=A$，分情况归纳
①若$A_i\in\Gamma$，显然成立
②若$A_i\in Axiom$，公理，显然成立
③若存在$A_j=A_k\rightarrow A_i$，MP规则，成立
④若存在x在$\Gamma$中不自由，$A_i=\forall x.A_j$，则
$任取解释I和指派\sigma$，可有归纳，$A_j$成立
$I(A_j)(\sigma)=t$
任取$d\in D$，由于x在$\Gamma$中不自由
所以$I(A_j)(\sigma[x/d])=t$成立，因为，$A_j$中必然没有$x$的自由出现
又因为是对任意$d$，所以可有$I(\forall x.A_j)(\sigma[x/d])=t$
即$I(A_i)(\sigma)$成立
⑤若存在$(C,x,y)$满足$\alpha\beta$规则，即y在x中没有自由出现，y不是C的自由变元，即$A_i=A_{j\forall y.S_y^xC}^{\forall x.C}$
因为$\forall x.C\equiv\forall y.S_y^xC$
又因为$A_j$满足，归纳可有$A_i$满足

#### 证明$\Gamma$可满足则协调

反证，若$\Gamma$不协调
则$\Gamma\vdash A\rightarrow \Gamma\vDash A$
同时$\Gamma\vdash\thicksim A\rightarrow \Gamma\vDash\thicksim A$
矛盾，故原式不成立

### 协调性

首先，定义$L_0(F),L_1(F),L_2(F)=L(F)$分别表示$F$中的全体句子（没有自由变元）、闭公式（没有自由个体变元）、公式构成的集合
定义$Term_0$为$F$中的全体闭项（不含变元的项）构成的集合

设$F$为一阶系统
①若$Th(F)\ne L(F)$，则称$F$是绝对协调的，即F一定能证出比自身多的公式
②若对每个$A\in L(F)$都有$A\notin Th(F)$或者$\thicksim A\notin Th(F)$，则称$F$是关于否定协调的，即系统能够证出的公式中不存在互补文字，即矛盾
③对公式集$\Gamma$，若$Th(\Gamma)\ne L(F)$，则称$\Gamma$是协调的

<b>若$\Gamma\cup\Gamma'$是协调的，则$\Gamma$与$\Gamma'$协调</b>

$A_1,...,A_n$与$\Gamma$不协调当且仅当$\Gamma\vdash \thicksim A_1\cup,...,\cup\thicksim A_n$

<b>A与$\Gamma$不协调当且仅当$\Gamma\vdash\thicksim A$，即当公式集能够推出A的反的时候，公式集必然与A不能协调，会存在矛盾</b>

### 独立性

#### $AS_1-AS_3$的独立性

同命题逻辑，找到代数指派即可

#### $AS_4$的独立性

给全称量词$\forall$一个全新的定义
$I(\forall x.A)(\sigma)=\left\{ \begin{array}{} t&存在d\in D使I(A)(\sigma[x/d])=t\\f&other \end{array} \right.$
能够证明出其他公式均会产生永真式，而公理中有不永真的存在，即其他公式证不出非永真式

#### $AS_5$的独立性

仍然是找一个定义，使得其他规则只能证出永真式

#### MP规则的独立性

考虑在F中有$\vdash p\cup\thicksim p$成立，但
$AS_1-AS_5$中任一公理的长度均大于$p\cup \thicksim p$的长度
Gen与$\alpha\beta$规则均不能减少已证定理的长度
因此MP规则独立

### 完全性

#### 完全集

设$\Gamma\subseteq L(F)$，若对每一个$A\in L(F)$，或者有$A\in \Gamma$或者$\thicksim A\in \Gamma$，则$\Gamma$是完全的
<b>注意区分公式集的完全性和形式系统的完全性，公式集的完全性是指每个变元/原子命题都能找到自身或自身的反；形式系统的完全性则是语义与语法之间的连接</b>

#### Godel完全性定理

①若$\vDash A$则$\vdash A$

②若$\Gamma\vDash A$则$\Gamma\Vdash A$

语义可证则语法可证

#### 势

$\# A$，也叫A的基数，表示A集合中包含多少个元素

<b>等势则#A=#B，说明存在一一映射</b>

#### 极大协调集

若公式集$\Gamma$既是完全的又是协调的，则称$\Gamma$是极大协调的

设$\Gamma\subseteq L(F)$为极大协调集，则
①对任意公式A，$A$或者$\thicksim A$只能有一个在$\Gamma$中
②若$A\notin\Gamma$，则A与$\Gamma$不协调

若$\Gamma$是协调集，则存在极大协调集使得$\Gamma\subseteq\Gamma'$

#### 形式系统的膨胀（公式变多）

设$F_1,F_2$是两个一阶形式系统
①<b>膨胀：</b>若$L(F_1)\subseteq L(F_2)$，则称$F_2$是$F_1$的膨胀，记作$\Gamma_1\le \Gamma_2$，即系统1的公式比系统2的少，可能一样
②<b>真膨胀：</b>若$L(F_1)\subsetneq L(F_2)$，则称$F_2$是$F_1$的真膨胀，记作$\Gamma_1<\Gamma_2$，即系统1的公式比系统2的少

#### 形式系统的扩张（推出的定理变多）

设$F_1,F_2$是两个一阶形式系统，$\Gamma_i\subsetneq L(F_1),i=1,2$
①若$F_1\le F_2$且$Th(F_1\cup\Gamma_1)\subseteq Th(F_2\cup\Gamma_2)$，则称$F_2\cup\Gamma_2$为$F_1\cup\Gamma_1$的**扩张**，记作$F_1\cup\Gamma_1\subseteq F_2\cup\Gamma_2$
②若$F_1\cup\Gamma_1\subseteq F_2\cup\Gamma_2$，且$Th(F_1\cup\Gamma_1)\cap L(F_1)=Th(F_2\cap\Gamma_2)\cap L(F_1)$，则称$F_2\cup\Gamma_2$为$F_1\cup\Gamma_1$的**保守扩张**，记作$F_1\cup\Gamma_1\preceq F_2\cup\Gamma_2$，即在扩张的情况下，原先证不出来的公式依然证不出来，增加的公式完全来自公式集$\Gamma_1,\Gamma_2$

<b>只增加若干常元，一定是保守扩张</b>

<b>若$F_1\cup\Gamma_1\preceq F_2\cup\Gamma_2$，则$F_1\cup\Gamma_1$为协调的当且仅当$F_2\cup\Gamma_2$是协调的

若$F_1\supseteq F_2$，且二者的差别只有个体常元，$\Gamma\supseteq L(F_1)$，则$F_1\cup\Gamma\preceq F_2\cup\Gamma$

若$\Gamma\vdash S_a^xA$且$a$为不在$\Gamma\cup\{A\}$的个体常元，则$\Gamma\vdash\forall x.A$
</b>

#### 节省解释与节省模型


<b>节省：若解释$I=<D,I_0>$满足$\#D<\#L(F)$，则称$I$是节省的。即论域中的元素个数小于F系统的公式个数，该模型是节省模型</b>

<b>保势扩张</b>：给定两个一阶形式系统，若$F_1\subseteq F_2且\#(\Sigma_2-\Sigma_1)=\#L(F_1)$，则$\#L(F_2)=\#L(F_1)$

<b>协调集的可满足性</b>：若$\Gamma\subseteq L(F)$是协调的，则必有节省解释$I$满足$\Gamma$

#### Goddel完全性定理

①若$\vDash A则\vdash A$
②若$\Gamma\vDash A则\Gamma \vdash A$

#### 紧致性定理

语法紧致性：一阶逻辑公式集$\Gamma$是协调的当且仅当其每个有穷子集是协调的

语义紧致性：一阶逻辑公式集$\Gamma$是可满足的当且仅当每个有穷子集是可满足的

<div STYLE="page-break-after: always;"></div>

# 004 等词系统

## 一阶等词系统$F^{\approx}$

一阶等词系统$F^{\approx}$由一阶系统添加如下成分组成
①语言部分：加入了二元谓词常元$\approx$
②推理部分：引入了两条关于$\approx$的公理
$AS_6:x\approx x$，个人理解，这一步是对谓词常元的语义进行定义
$AS_7:x\approx y\rightarrow (S_x^zA\rightarrow S_y^zA)$，即如果$x\approx y$，那么将z分别代入为x和y，得到的公式**等价**，注意我这里用的是等价，需要证明。个人理解，这一步是增强谓词常元的能力，从只能对个体变元的操作通过代入扩展到了对公式的影响。**这一步是等价，例如3和7可以等价，奇偶性相同；恒等只能3=3**

由于$\Gamma\vdash_{F^{\approx}}A$当且仅当$\Gamma,AS_6,AS_7\vdash_{F}A$，所以$Th(F)\supseteq Th(F^{\approx})$，即是一个膨胀，公式变多了

若一阶理论$J$含有等词$\approx$并含有$AS_6,AS_7$，则称$J$为带等词的一阶理论，注意这里是理论，不一定是完整的系统

### 对称性$x\approx y\rightarrow y\approx x$

令A为$z\approx x$
由$AS_7$可有$x\approx y\rightarrow(S_x^zz\approx x\rightarrow S_y^zz\approx x)$
即$x\approx y\rightarrow(x\approx x\rightarrow y\approx x)$
可有$x\approx y\vdash(x\approx x\rightarrow y\approx x)$
拿到左边$x\approx y,x\approx x\vdash y\approx x$
再拿到右边$x\approx x\vdash(x\approx y\rightarrow y\approx x)$
继续$\vdash x\approx x\rightarrow(x\approx y\rightarrow y\approx x)$
由$AS_6$可有MP$x\approx y\rightarrow y\approx x$

<b>推论：$x\approx y\equiv y\approx x$</b>

### 传递性$x\approx y\rightarrow (y\approx z\rightarrow x\approx z)$

令A为$u\approx z$
$AS_7$可有$y\approx x\rightarrow(S_y^uA\rightarrow S_x^uA)$
代入$y\approx x\rightarrow(y\approx z\rightarrow x\approx z)$
又因为$x\approx y\rightarrow y\approx x$
故MP$x\approx y\vdash (y\approx z\rightarrow x\approx z)$
故$\vdash x\approx y\rightarrow(y\approx z\rightarrow x\approx z)$

### 若t为项，则$x\approx y\rightarrow S_x^zt\approx S_y^zt$

令$A为S_x^zt\approx t$
$x\approx y\rightarrow(S_x^z(S_x^zt\approx t)\rightarrow S_y^z(S_x^zt\approx t))w$
即$x\approx y\rightarrow(S_x^zt\approx S_x^zt\rightarrow S_X^Zt\approx S_y^zt)$
因为$AS_6:x\approx x$
故$S_x^z\rightarrow S_x^zt\approx S_y^zt$
即$x\approx y\rightarrow S_x^zt\approx S_y^zt$

### 等词替换定理

在$F^{\approx}$中，可以归纳证明
①$x_1\approx y_1\cap x_2\approx y_2\cap...\cap x_n\approx y_n\rightarrow f(x_1,...,x_n)\approx f(y_1,...,y_n)$
②$x_1\approx y_1\cap x_2\approx y_2\cap...\cap x_n\approx y_n\rightarrow P(x_1,...,x_n)\approx f(y_1,...,y_n)$

<b>推论</b>
①$t_1\approx t_1'\cap t_2\approx t_2'\cap...\cap t_n\approx t_n'\rightarrow f(t_1,....,t_n)\approx f(t_1',...,t_n')$
②$t_1\approx t_1'\cap...\cap t_n\approx t_n'\rightarrow S_{t_1,...,t_n}^{x_1,...,x_n}A=S_{t_1',...,t_n'}^{x_1,...,x_n}A$
其中要求$t_1,...,t_n与t_1',...,t_n'$均对$A的x_i$可代入

## 等词模型

设$J$是带等词的一阶理论，$I=<D,I_0>$为$J$的模型，注意到
①$\vdash_Jx\approx x$
②$\vdash_Jx\approx y\rightarrow y\approx x$
③$\vdash_Jx\approx y\rightarrow(y\approx z\rightarrow x\approx z)$
因此对于$J$的解释$I=<D,I_0>,I_0(\approx)$必然是$D$上的**等价关系**，即相似三角形。

### 等词解释，是对等词系统更严格的规定

考虑D上的特殊等价关系$I_D$，其定义为
$I_D(d_1,d_2)=\left\{ \begin{array}{} t&d_1=d_2\\f&d_1\ne d_2 \end{array} \right.$
称为D上的**恒等关系**，即全等三角
对于含等词的一阶理论J，若其解释$<D,I_0>$满足$I_0(\approx)=I_{D}$，则称该解释为等词解释

若$I$是公式A（公式集合$\Gamma$）的模型，则称其为$A(\Gamma)$的等词模型

<font color='red'><b>等词关系不仅要求满足$AS_6,AS_7$，还要求满足恒等关系</b></font>

### 初等等价

设$I$和$I'$为一阶系统$F$的两个解释。若对每个句子A，都有
$\vDash_{I}A当且仅当\vDash_{I'}A$
则称$I$和$I'$初等等价，记作$I\equiv I'$

若$I$是$\Gamma$满足$AS_6+AS_7$的一个解释，则必然存在关于$\Gamma$的等词解释$I'$，使$I\equiv I'$

若$I$是$\Gamma$的一个等词解释，则必然存在$\Gamma$的一个满足$AS_6+AS_7$的非等词解释$I'$使得$I\equiv I‘$

### 全称闭包

设A中所有的自由变元均为个体变元，且$x_1,...,x_n$为A中全部的自由变元，则令$\overline{A}=\forall x_!,...,\forall X_n.A$为$A$的全称闭包。
个人理解为就是对A中原本的自由变元都加了约束。

<b>节省：若解释$I=<D,I_0>$满足$\#D<\#L(F)$，则称$I$是节省的。即论域中的元素个数小于F系统的公式个数</b>

<b>$F^{\approx}$中协调句子集的性质：</b>
设$\Gamma\subseteq L(F^{\approx})$为句子集，则$\Gamma$为协调的当且仅当$\Gamma$有节省的等词模型

<b>$F^{\approx}$系统的完全性：</b>
设$\Gamma\subseteq L(F^{\approx})$为句子集，则$\Gamma\vdash_{F^{\approx}}A$当且仅当$\Gamma\vDash_{F^{\approx}}A$，表示每个等词模型均是A的模型

<b>设$\Gamma\subseteq L(F^{\approx})$为一个句子集，则下列条件等价
①$\Gamma$是协调的
②$\Gamma$的每个有穷子集都是协调的
③$\Gamma$有等词模型
④$\Gamma$的每个有穷子集都有等词模型
⑤$\Gamma$有节省的等词模型
⑥$\Gamma$的每个有穷子集都有节省的等词模型
</b>

## 描述能力

设$\Gamma\subseteq L(F^{\approx})$为一个句子集，若对每个$n\in N,\Gamma$都有基数大于n的有穷等词模型，则$\Gamma$必然有无穷等词模型

<b>LST定理</b>：设$\Gamma\subseteq L(F^{\approx})$为一个句子集，若$\Gamma$有无穷等词模型，则对每个更大的无穷基数$\alpha$，皆存在关于$\Gamma$的基数为$\alpha$的等词模型

$F^{\approx}$不能表达“有限集”的概念，即：不存在公式集$\Gamma$使$I=<D,I_0>$是$\Gamma$的模型当且仅当$\#D<\infty$
个人理解：我们不能用有限个句子来描述一个等词系统，也没办法用有限个公式来描述一个等词系统，因为$AS_7$公理，从一个自由的个体变元代入到了任何一个公式？

无穷集不能用有限多个公式刻画

<div STYLE="page-break-after: always;"></div>

# 005 证明与反驳

公式A的反驳，就是找到关于$\thicksim A$的一个证明

## 自然演绎系统N

### 问题的定义

问题：家乡的集合，所有元素均已编码为特定格式的串
对一个问题，关心能否判定某个给定的串是否属于该集合
例：最大公约数-GCD问题，实例为三元组$(a,b,c)\in Z^3$，如$(12,8,4)\in GCD$

**过程不一定种植，终止的过程为算法**

可判定问题：存在一个判定算法
半可判定问题：对一个输入，若属于则是，否则否或者不停机

对偶问题：Q与对偶问题$\overline{Q}$：对符合输入格式的串q有$q\in Q\leftrightarrow q\notin \overline{Q}$

定理：若$Q,\overline{Q}$问题均半可判定，则两者均可判定（交替运行）

## 永真式的判定

### Herbrand方法

两个步骤：
①计算公式A的$Skolem$标准型，即一种标准的前束范式
②利用$Herbrand$定理判断公式的永真性

#### skolem标准型

给定一阶逻辑公式A，A是前束范式$A=\exist\forall_1x_1,...,\exist\forall_nx_n.B$
B中不含有量词，目的是去除存在量词转为全称量词
①首先令$A_0=A$
②对当前公式$A_i=\exist\forall_{i1}x_{i1},...,\exist\forall_{ik}x_{ik}.B_i$，设$\exist_{ij}$是最左边第一个等于$\exist$的量词
·若$ij=i1$，即是最外层的量词，则选取新的个体常元$a_i$，并且令$A_{i+1}=\exist\forall_{i2}x_{i2},...,\exist\forall_{ik}x_{ik}.S_{a_i}^{x_{i1}}B_i$
·否则，选取新的$j-1$元函数常元$f_i$，令$A_{i+1}=\exist\forall_{i1}x_{i1},...,\exist\forall_{ij-1}x_{ij-1},\exist\forall_{ij+1}x_{ij+1},...,\exist\forall_{ik}x_{ik}.S_{f_i(x_{i1},...,x_{ij-1})}^{x_{ij}}B_i$
③当$A_i$中不含有存在量词，则过程停止

例：$A=\thicksim\forall x.(P(x)\rightarrow(\exist y.P(y)\cup \forall z.P(z)))$
首先化为前束范式$\exist x\forall y\exist z.(P(x)\cap\thicksim P(y)\cap \thicksim P(z))$
$A_0=A=\exist x\forall y\exist z.(P(x)\cap\thicksim P(y)\cap \thicksim P(z))$
$A_1=\forall y\exist z(P(a)\cap\thicksim P(y)\cap\thicksim P(z))$
$A_2=\forall y.(P(a)\cap\thicksim P(y)\cap\thicksim P(f(y)))$

<b>设B是A的skolem标准型，则A可满足当且仅当B可满足</b>

#### herbrand定理

对句子的不可满足性问题的判定只需要考虑特定论域上的特定常元解释，进而将一阶句子集的不可满足性判定问题转化为无两次公式集的不可满足判定问题

##### herbrand域

给定已经化为skolem标准型的句子A，其herbrand域$D_H$是满足下列条件的最小集合
①若a是A中的个体常元，则$a\in D_H$
②若A中不包含任何个体常元，则将某个特定的个体常元b置于$D_H$
③若f是A中的n元函数，$t_1,...,t_n\in D_H$，则$f(t_1,...,t_n)\in D_H$

例：$\forall y.(P(a)\cap\thicksim P(y)\cap\thicksim P(f(y)))$的herbrand域为
首先，个体常元a是，根据定义1
其次f是A中的1元函数，则$f(a)$是，根据定义3
递归可有$f(f(a))$是
最终可有$\{a,f(a),f(f(a)),...\}$

例：$\forall y.(P(a)\cap\thicksim P(y)\cap\thicksim P(b))$的herbrand域为
首先，个体常元a是，根据定义1
其次，个体常元b是，根据定义1
没了，即$\{a,b\}$

##### herbrand解释

给定句子A已经化为skolem标准型，他的一个herbrand解释$I_H=<D_H,I_{H0}>$，其中$D_H$论域是herbrand域，并且
①对每个n元函数常元f及$t_1,...,t_n\in D_H$，有
$I_{H0}(f)(t_1,...,t_n)=f(t_1,...,t_n)$，这里由于不考虑变元，故没有考虑指派，只考虑解释。相当于n元函数常元的解释不会影响到函数的变量
②对每个n元谓词常元P及$t_1,...,t_n\in D_H$，有
$I_{H0}(P)(t_1,...,t_n)\in \{t,f\}$，即直接映射到真假性上

**定理：写成skolem标准型的句子A是可满足的，当且仅当A被它的某个herbrand解释所满足**

设$A=\forall x_{1},...,\forall x_n.B$，则A在其herbrand域上可满足当且仅当公式集合$\Gamma_A=\{ S_{t_1,...,t_n}^{x_1,...,x_n}B|t_1,...,t_n\in D_H \}$可满足

例：$\forall y.(P(a)\cap\thicksim P(y)\cap\thicksim P(b))$
其herbrand域为$\{a,b\}$
其中只三个1元谓词常元P，但由于只有一个参数是变元，可有当且仅当$\{ S_{t_1}^{y}B|t_1\in \{a,b\} \}$可满足，此时已经转变为了命题逻辑公式集合

若$\Gamma_A$不可满足，根据禁止性定理，必存在$\Gamma_A$的某个有穷子集不可满足

## 合一化与消解

用herbrand定理判断的时候，一方面代入计算比较耗时，另一方面一般针对某一条公式，无法处理公式集的可满足性问题

### 合一化算法

将变元代入$\theta=S_{t_1,...,t_n}^{x_1,...,x_n}$写为$\theta=\{t_1/x_1,...,t_n/x_n\}$

当n=0时，记为$\theta=\epsilon$，即空代入

对公式A和项t的代入$\theta(A),\theta(t)$分别简记为$A\theta,t\theta$

设$\theta=\{t_1/x_1,...,t_n/x_n\},\gamma=\{u_1/y_1,...,u_m/y_m\}$为两个代入，则两者的合成定义为
$\theta \circ \gamma=\{t_i\gamma/x_i|1\le i\le n\}\cup\{u_i/y_i|y_i\notin\{x_1,...,x_n\}\}$
①$\theta\circ\epsilon=\epsilon\circ\theta=\theta$
②$(\theta_1\circ\theta_2)\circ\theta_3=\theta_1\circ(\theta_2\circ\theta_3)$
③$A(\theta\circ\gamma)=(A\theta)\gamma且t(\theta\circ\gamma)=(t\theta)\gamma$

#### 合一化

设$\Gamma$为有穷公式集，$\theta$是一个代入，令$\Gamma\theta=\{A\theta|A\in \Gamma\}$
①若$\Gamma\theta$中只含有一个公式，则称$\theta$合一化$\Gamma$，并称$\theta$是$\Gamma$的一个合一子
②若$\Gamma$存在合一子，则称$\Gamma$是可以合一化的
例：$\Gamma=\{P(f(a)),P(x),P(y)\}$是可以合一化的，合一子为$\{f(a)/x,y/x\}$
$\Gamma=\{P(f(x)),P(x),P(y)\}$是不可以合一化的

<b>更一般</b>：若存在$\gamma_1\circ\theta=\gamma_2$，则称$\gamma_1$比$\gamma_2$更一般，记作$\gamma_1\preceq\gamma_2$
<b>等价</b>：若$\gamma_1\preceq\gamma_2,\gamma_2\preceq\gamma_1$，则两者等价，记作$\gamma_1\simeq\gamma_2$
<b>最一般合一子</b>：对$\Gamma$的任意一个合一子$\gamma$都有$\theta\preceq\gamma$，记作$mgu(\Gamma)$，当只有两个公式的时候可以直接记为$mgu(A_1,A_2)$
例：$mgu(P(f(x)),P(y))=\{f(x)/y\}$

<b>最左差异集</b>：$lmd(A_1,A_2)$，分别是取自$A_1,A_2$最左的不同符号所在的公式或项
例：$A_1=P(x,f(y,z)),A_2=P(x,a)$
$lmd(A_1,A_2)=\{f(y,z),a\}$
可以推广到多个公式的情形

#### 求最一般合一子算法

输入：无量词原子公式$A_1,A_2$
输出：若可合一化，输出$mgu(A_1,A_2)$，否则报告不存在
①$k\leftarrow 0;\Gamma_k\leftarrow\{A_1,A_2\};\sigma_k\leftarrow \epsilon$
②若$\Gamma_k$为单元素集，停止，返回$\sigma_k$，否则，求出$lmd(\Gamma_k)$
③若$lmd(\Gamma_k)=\{v_k,t_k\}$，其中$v_k$是变元，$t_k$是项，且$t_k$中没有$v_k$，则令$\rho_k=\{t_k/v_k\}$，跳转到4.否则，$\Gamma$不可合一化，停止
④令$\sigma_{k+1}\leftarrow\sigma\circ\rho_{k},\Gamma_{k+1}\leftarrow\Gamma_k\circ\rho_k,k\leftarrow k+1$，跳转到2

若算法能够进行，公式集中每次至少减少一种变元

### 一阶公式消解算法

给定$L(F)$中的有穷句子集$\Gamma$及句子$A$，目标是判断是否有$\Gamma\vDash A$成立
等价于求证$\Gamma\cup\{\thicksim A\}$不可满足

首先，将$\Gamma\cup\{\thicksim A\}$中的公式化为skolem标准型，然后去掉所有的量词，并将每个公式等价的转化为若干个断句的形式，称为$\Gamma\cup\{\thicksim A\}$的消解形式集$\Delta$
**相当于拆成合取范式的情况**

设$A\cup C$与$B\cup \thicksim D$是该公式集中的两个短句，其中C与D是两个原子公式，则$A\theta\cup B\theta'$是这两个公式的消解结果，其中$C\theta=D\theta'$
例：$\Delta=\{\thicksim P(x)\cup Q(x),P(f(y)),\thicksim Q(f(a)),\thicksim Q(f(z))\}$
①$\thicksim P(x)\cup Q(x)$与$P(f(y))$可以发生消解，有互补文字P
此时$\theta=f(y)/x,\theta'=\epsilon$
代入后有$\thicksim P(f(y))\cup Q(f(y))$与$P(f(y))$
消解得到$Q(f(y))$
②$\thicksim Q(f(z))$与$\thicksim Q(f(a))$，同类型，可以统一为$\thicksim Q(f(a))$
③$Q(f(y))$与$\thicksim Q(f(z))$可以发生消解，有互补文字Q
此时$\theta=y/z,\theta'=\epsilon$
代入后有$Q(f(z))$与$\thicksim Q(f(z))$，消解后得到$\square$
④此时$\Delta$中只剩下$\square$，证明原公式集存在矛盾，不可满足

#### 消解的可靠性

若$\Gamma\cup\{\thicksim A\}$对应的消解形式集存在关于$\square$的消解序列，则$\Gamma\vDash A$

#### 消解的完全性

若$\Gamma\vDash A$，则$\Gamma\cup\{\thicksim A\}$对应的消解形式集存在关于$\square$的消解序列
