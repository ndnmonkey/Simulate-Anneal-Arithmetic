import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import animation

#设置基本参数
#T初始温度，T_stop，iter_num每个温度的迭代次数，Q温度衰减次数
class Tuihuo_alg():
    def __init__(self,T_start,iter_num,T_stop,Q,xx,init_x):
        self.T_start = T_start
        self.iter =iter_num
        self.T_stop = T_stop
        self.Q = Q
        self.xx = xx
        self.init_x = init_x
    # def cal_x2y(self):
    #     return (x - 2) * (x + 3) * (x + 8) * (x - 9)


if __name__ == '__main__':

    def cal_x2y(x):
        #print((x - 2) * (x + 3) * (x + 8) * (x - 9))
        return (x - 2) * (x + 3) * (x + 8) * (x - 9)
    T_start = 1000
    iter_num = 1000
    T_stop = 1
    Q = 0.95
    K = 1
    l_boundary = -10
    r_boundary = 10
    #初始值
    xx = np.linspace(l_boundary, r_boundary, 300)
    yy = cal_x2y(xx)
    init_x =10 * ( 2 * np.random.rand() - 1)
    print("init_x:",init_x)

    t = Tuihuo_alg(T_start,iter_num,T_stop,Q,xx,init_x)

    val_list = [init_x]
    while T_start>T_stop:
        for i in range(iter_num):
            init_y = cal_x2y(init_x)
            new_x = init_x + (2 * np.random.rand() - 1)
            if l_boundary <= new_x <= r_boundary:
                new_y = cal_x2y(new_x)
        #print("new_x:",new_x)
        #print('new_y:',new_y)
                delta = new_y - init_y  #新减旧
                if delta < 0:
                    init_x = new_x
                else:
                    p = np.exp(-delta / (K * T_start))
                    if np.random.rand() < p:
                        init_x = new_x
            #print("new_x:",new_x)
            #print("当前温度：",T_start)
        T_start = T_start * Q

print("最优解x是：", init_x)   #这里最初写的是new_x,所以结果一直不对
print("最优解是：", init_y)
#比如我加上new_x，真假之间的误差实际就是最后一次的赋值“init_x = new_x”
print("假最优解x是：", new_x)   #这里最初写的是new_x,所以结果一直不对
print("假最优解是：", new_y)

xx = np.linspace(l_boundary,r_boundary,300)
yy = cal_x2y(xx)
plt.plot(xx, yy, label='Tuihuo')
#plt.plot(x2, y2, label='Second Line')
plt.xlabel('X for tuihuo')  #横坐标标题
plt.ylabel('Y for tuihuo')  #纵坐标标题
#plt.title('Interesting Graph\nCheck it out',loc="right")   #图像标题
#plt.title('Interesting Graph\nCheck it out')
plt.legend()    #显示Fisrt Line和Second Line（label）的设置
plt.savefig('C:/Users/zhengyong/Desktop/1.png')
plt.show()
