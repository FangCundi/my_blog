# 一、实验目的

1．掌握数字PID控制的编程方法
2．实现连续系统与离散系统PID控制的MATLAB编程

# 二、实验原理

PID控制器是一种线性控制器，它根据给定值r(t)与实际输出值c(t)构成偏差：e(t)=r(t)-c(t)。将偏差的比例(P)、积分(I)和微分(D)通过线性组合构成控制量，对受控对象进行控制。PID控制系统结构框图下图所示。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184619742.png)

PID控制系统结构框图
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184623797.png)为系统的输入信号，![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184627320.png)为系统的输出，控制器的输出信号![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184638707.png)。
其控制规律为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184647590.png)

KP是比例系数，KI是积分常数，KD是微分常数。
PID控制器由比例（P）环节、积分（I）环节和微分（D）环节组合而成。比例（P）环节：将控制系统的给定输入与系统反馈所形成的偏差信号成比例的放大，偏差一旦产生，控制器立即产生控制作用，以减少偏差。比例环节能够提高控制系统的响应速度，增大比例系数KP，可以加快调节，但KP过大，控制系统会产生较大的超调，甚至导致系统不稳定。积分（I）环节：主要是消除系统的静态误差，提高系统的无差度，同时提高控制系统的响应速度。积分作用的强弱取决于积分常数KI，积分常数KI越大，积分作用越强，反之则越弱。微分（D）环节：反映偏差信号的变化率，调节误差的微分输出，能够在系统误差突变时，在系统中引入一个有效的早期修正信号，以加快系统的动作速度，减少调节时间，从而改善系统的动态性能。

# 三、实验内容

## 1．连续系统的数字 PID 控制仿真：

假设被控对象为电机模型，其传递函数为![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184704552.png)，其中![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184716285.png) 。输入信号为![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184723472.png)，采用PID控制，请根据如下代码选择合适的KP、KD参数，使得跟踪曲线误差尽可能小，并记录最小误差情况下的KP和KD值。

## 2．设被控对象为

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184756475.png)

采样时间为1ms，对其进行离散化。针对离散系统的阶跃信号、正弦信号和方波信号的位置响应，设计离散PID控制器。其中S为信号选择变量，S=1是阶跃跟踪，S=2是方波跟踪，S=3是正弦跟踪。请根据如下代码选择合适的Kp、Ki、Kd参数，观察三组信号跟踪曲线响应速度、超调量和稳态误差的变化，选择最好的一组跟踪效果最好阶跃跟踪、方波跟踪和正弦跟踪曲线，并记录下各自对应的Kp、Ki、Kd值。

# 四、实验过程

## 1．数字PID控制仿真

（1）首先新建函数文件，用于创建连续函数对象的微分方程函数
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184826169.png)

（2）初始化界面如图
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184829136.png)

（3）将指导书中提供的代码粘贴到文件中

```python
function dy=chap1_1f(t,y,flag,para)
u=para;
J=0.0067;B=0.1;

dy=zeros(2,1);
dy(1) = y(2);
dy(2) = -(B/J)*y(2) + (1/J)*u;
```

（4）保存，文件类型为m文件，注意需要放到环境路径文件夹，或者将文件夹路径设置为环境路径
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184841424.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

（5）将指导书中的主程序代码复制到命令行窗口中并执行

```python
% chap1_1.m
%Discrete PID control for continuous plant
clear all;
close all;
ts=0.001;  %Sampling time
xk=zeros(2,1);
e_1=0;
u_1=0;

for k=1:1:2000
time(k) = k*ts;

rin(k)=0.50*sin(1*2*pi*k*ts);
  
para=u_1;              % D/A
tSpan=[0 ts];
[tt,xx]=ode45('chap1_1f',tSpan,xk,[],para);
xk = xx(length(xx),:);    % A/D
yout(k)=xk(1); 

e(k)=rin(k)-yout(k);
de(k)=(e(k)-e_1)/ts; 

u(k)=KP*e(k)+KD*de(k);
%Control limit
if u(k)>10.0
   u(k)=10.0;
end
if u(k)<-10.0
   u(k)=-10.0;
end

u_1=u(k);
e_1=e(k);
end
figure(1);
plot(time,rin,'r',time,yout,'b');
xlabel('time(s)'),ylabel('rin,yout');
figure(2);
plot(time,rin-yout,'r');
xlabel('time(s)'),ylabel('error');
```

（6）产生如图报错
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184852164.png)

（7）修改代码中KP,KD的值，令KP=20,KD=0.5
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184855449.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184857872.png)

（8）运行后得到图像如图，此时KP=20,KD=0.5
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020123018490253.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184905363.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

（9）分析：输出跟随输入，PD控制中，微分控制可以改善动态性能，调节时间缩短，允许加大比例控制，使稳态误差减小，提高了控制精度

## 2．被控对象

（1）在主程序中添加KP,KI,KD的具体数值
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184921325.png)

（2）令KP=1.5,KI=2,KD=0.05

```python
% chap1_1.m
%Discrete PID control for continuous plant
clear all;
close all;

ts=0.001;
sys=tf(5.235e005,[1,87.35,1.047e004,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0.0;u_2=0.0;u_3=0.0;
y_1=0.0;y_2=0.0;y_3=0.0;
x=[0,0,0]';
error_1=0;
for k=1:1:1500
time(k)=k*ts;

%S=input('?s= ');%
S=1;
if S==1
    kp=1.5;ki=2;kd=0.05;        
    rin(k)=1;                            %Step Signal
elseif S==2
    kp=1.5;ki=2;kd=0.05;        
    rin(k)=sign(sin(2*2*pi*k*ts));  %Square Wave Signal
elseif S==3
    kp=1.5;ki=2;kd=0.05;             %Sine Signal
    rin(k)=0.5*sin(2*2*pi*k*ts);         
end

u(k)=kp*x(1)+kd*x(2)+ki*x(3);   %PID Controller
%Restricting the output of controller
if u(k)>=10     
   u(k)=10;
end
if u(k)<=-10
   u(k)=-10;
end
%Linear model
yout(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(2)*u_1+num(3)*u_2+num(4)*u_3;

error(k)=rin(k)-yout(k);

%Return of parameters
u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=yout(k);
   
x(1)=error(k);                 %Calculating P
x(2)=(error(k)-error_1)/ts;  %Calculating D
x(3)=x(3)+error(k)*ts;        %Calculating I
error_1=error(k);
end
figure(1);
plot(time,rin,'k',time,yout,'k');
xlabel('time(s)'),ylabel('rin,yout'); 
```

（3）运行主程序，结果如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230184936329.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)
