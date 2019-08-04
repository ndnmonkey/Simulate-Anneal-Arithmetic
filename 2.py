#别人的方法
import numpy as np
import matplotlib.pyplot as plt
import math
#define aim function
def aimFunction(x):
     #y=x**3-60*x**2-4*x+6
     y = (x - 2) * (x + 3) * (x + 8) * (x - 9)
     return y
x=[i/10 for i in range(1000)]
y=[0 for i in range(1000)]
for i in range(1000):
     y[i]=aimFunction(x[i])

print("最优解是：",min(y))
index_num = min(y)
print("最优解对应横坐标是：",y.index(index_num)/10)


# fig, ax = plt.subplots()  # 我们的数据是一个0~2π内的正弦曲线
# line, = plt.plot(x, y)
# point, = plt.plot(index_num, min(y), 'o')

plt.plot(x, y, label='NM')
#plt.plot(x2, y2, label='Second Line')
plt.xlabel('X')  #横坐标标题
plt.ylabel('Y')  #纵坐标标题
#plt.title('Interesting Graph\nCheck it out',loc="right")   #图像标题
#plt.title('Interesting Graph\nCheck it out')
plt.legend()    #显示Fisrt Line和Second Line（label）的设置
plt.savefig('C:/Users/zhengyong/Desktop/1.png')
plt.show()
