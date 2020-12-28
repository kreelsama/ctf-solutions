## Coppersmith Attack for Short Padding Messages

https://en.wikipedia.org/wiki/Coppersmith%27s_attack

### Related Message Attack

$e=3$，有两个明文，$m_1, m_2$，且$m_2=\alpha m_1+\beta$且$\alpha、\beta$已知。若知道$c_1=m_1^e\bmod N$和$c_2=m_2^e\bmod N$。则攻击者可以直接得到$m_1$：
$$
\frac{\beta\left(c_{2}+2 \alpha^{3} c_{1}-\beta^{3}\right)}{\alpha\left(c_{2}-\alpha^{3} c_{1}+2 \beta^{3}\right)}=\frac{3 \alpha^{3} \beta m_{1}^{3}+3 \alpha^{2} \beta^{2} m_{1}^{2}+3 \alpha \beta^{3} m_{1}}{3 \alpha^{3} \beta m_{1}^{2}+3 \alpha^{2} \beta^{2} m_{1}+3 \alpha \beta^{3}}=m_{1} \bmod N
$$

### Resultant

意为结式（百度百科上是eliminant），指的是两个多项式$f(x)$和$g(x)$的（由高到低）系数组成的西尔韦斯特（Sylvester）行列式，记$h=res_x(f, g)$是$f$和$g$对系数$x$的结式，则$h$由以下性质：

* 若$f(x)$和$g(x)$由同一个零点，则$h=0$；若没有相同的零点，则$h\not=0$。

sage中可以直接计算两个行列式的结式，若有$f(x,y)$和$g(x,y)$，则$f$和$g$关于$x$的结式是：

```python
h = g.polynomial(x).resultant(f.polynomial(x))
```

### This Problem

用$e=3$加密了$m_1, m_2$，且$m_2=m_1+\beta$，其中$m_1、m_2、\beta$均未知，但是$\beta$足够小（比特长度为104，小于$\lfloor\frac{n}{e^2}\rfloor$，$n$为$N$的比特长度），密文分别为$c_1,c_2$。

首先设两个多项式：
$$
\begin{align}
f(x,y) &= x^e - c_1\\
g(x,y) &= (x+y)^e - c_2
\end{align}
$$
则$x=m_1$是上述两个多项式的公共零点，而$y=\beta$是第二个多项式的零点，是我们想要得到的。由于两个多项式由公共零点$x=m_1$，所以两个多项式对于$x$的结式应该为0。设两个多项式的结式为$h(y)=res_x(f, g)$，则$h(\beta)=0$，即$\beta$是$h\equiv 0\bmod N$的一个小根，使用Coppersmith定理直接求解即可。
