#自己的解法
import random
import matplotlib.pyplot as plt

list_x = []
# for i in range(1):
#     #print(random.randint(0,100))
#     for i in range(0,100):
#         print("sss",i)
#
#     list_x.append(random.randint(0,100))
for i in range(-100,100):
    list_x.append(i/10)

print("横坐标为：",list_x)
print(len(list_x))


list_y = []
for x in list_x:
    # print(x)
    #y = x*x*x - 60*x*x -4*x +6
    y = (x - 2) * (x + 3) * (x + 8) * (x - 9)
    list_y.append(y)
print("纵坐标为：",list_y)

#经验证，这里算出来的结果6.5和最优解1549都是对的
print("最小值为：",min(list_y))
num = min(list_y)
print("最优解：",list_y.index(num)/10-10)
print("第",list_y.index(num)/10-10,"个位置取得最小值")

plt.plot(list_x, list_y, label='TuiHuo')
#plt.plot(x2, y2, label='Second Line')
plt.xlabel('X')  #横坐标标题
plt.ylabel('Y')  #纵坐标标题
#plt.title('Interesting Graph\nCheck it out',loc="right")   #图像标题
#plt.title('Interesting Graph\nCheck it out')
plt.legend()    #显示Fisrt Line和Second Line（label）的设置
plt.savefig('C:/Users/zhengyong/Desktop/1.png')
plt.show()
