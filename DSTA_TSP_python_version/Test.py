from DSTA import DSTA
from otherlib import distance
from otherlib import draw
import numpy as np

# 读取数据
data = np.loadtxt('eil101.txt')
A = data[:,1:]

#初始化
fun1 = lambda Best: distance(Best,A)
Best = np.arange(A.shape[0])
SE = 30   
MaxIter = 500
dsta = DSTA(fun1,Best,SE,MaxIter)

#迭代优化
fun2 = lambda iter_k,Best,fBest: draw(iter_k,Best,fBest,A)
dsta.run(fun2)

