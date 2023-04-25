# 题目

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230235332110.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

# 实验知识点

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230235519798.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

# 题目一

## 1、设置变量

```python
num=[3]
den=[2,1]
```

## 2、单位阶跃相应

```python
sys=tf(num,den)
step(sys)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201231000108550.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

## 3、单位冲激相应

```python
impulse(sys)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201231000218131.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

# 题目二

## 1、设置变量

```python
A=[-0.5572,-0.7814;0.7814,0;];
B=[1;0];
C=[1.9691,6.4493;];
D=[0]
```

## 2、单位阶跃响应

```
step(A,B,C,D)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020123023572860.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

## 3、单位冲激相应

```
impulse(A,B,C,D)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020123100024269.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

## 4、零输入响应

```python
x0=[0,1];
initial(A,B,C,D,x0)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201231000940335.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

## 5、斜坡输入相应

```python
[num,den]=ss2tf(A,B,C,D)
 t=0:0.01:5
u=t;
lsim(num,den,u,t)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201231001034557.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

## 6、simulink

### （1）绘图，分别是step模块，state-space模块，scope模块

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230195212297.png)

### （2）step模块设置

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230195223260.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

### （3）state-space模块设置

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230195231570.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)

### （4）scope模块设置时间为25，结果如下

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020123019524110.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)
==PS：抱歉，由于撰写时时间仓促，出现了很多错误，现进行修改2020.12.31==
