#下面网站的代码
#https://my.oschina.net/ahaoboy/blog/1822157
# https://www.imooc.com/article/details/id/30160
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import animation


def inputfun(x):
    return (x - 2) * (x + 3) * (x + 8) * (x - 9)
    #return (x+10) * (x - 2) * (x + 3) * (x + 8) * (x - 8)


initT = 1000  # 初始温度
minT = 1  # 温度下限
iterL = 1000  # 每个T值的迭代次数,这里初始值是1000
delta = 0.95  # 温度衰减系数
k = 1

#initx是-10到10的区间
initx = 10 * (2 * np.random.rand() - 1)


nowt = initT
print("初始解initx为：", initx)

#形成300个-10到10的numpy.ndarray
xx = np.linspace(-10, 10, 300)
yy = inputfun(xx)

#val_list 算了一个为[6.370639452766955]的数
val_list = [initx]
# 模拟退火算法寻找最小值过程
while nowt > minT:
    for i in range(iterL):
        funVal = inputfun(initx)
        #xnew是-11到11之间的
        xnew = initx + (2 * np.random.rand() - 1)
        if -10 <= xnew <= 10:
            funnew = inputfun(xnew)
            #挑选出随机的几个对应值（通过余数来挑选）
            #这里两句貌似没用
            # if i % 100 == 0:
            #     val_list.append(xnew)
            # #这里就是deltaE
            res = funnew - funVal
            #这里是核心的精华部分
            if res < 0:
                initx = xnew
            else:
                p = np.exp(-res / (k * nowt))
                if np.random.rand() < p:
                    initx = xnew
        print(initx)

    nowt = nowt * delta
    #print(nowt)
print("第",i,"次",len(val_list))
#print(val_list)

fig, ax = plt.subplots()  # 我们的数据是一个0~2π内的正弦曲线
line, = plt.plot(xx, inputfun(xx))
point, = plt.plot(initx, inputfun(initx), 'o')


def animate(i):
    point.set_ydata(inputfun(val_list[i]))
    point.set_xdata(val_list[i])


ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              repeat=False,
                              frames=len(val_list),
                              interval=20,
                              blit=False)
plt.show()
print("最优解：", initx)
print("最优值：", inputfun(initx))