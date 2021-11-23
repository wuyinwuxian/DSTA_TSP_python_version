
import numpy as np
np.random.seed(1)

class DSTA():
    # 初始化
    def __init__(self,fun,Best,SE,MaxIter):
        self.fun = fun
        self.Best = Best
        self.fBest = self.fun(Best)
        self.SE = SE
        self.MaxIter = MaxIter

    
    # 交换算子，产生候选解
    def op_swap(self):
        n = self.Best.size
        State = np.zeros((self.SE,n),dtype = int)
        for i in range(self.SE):
            temp = self.Best.copy()
            R = np.random.permutation(n)
            a = R[0]
            b = R[1]
            temp[b],temp[a] =   temp[a],temp[b]
            State[i,:] = temp
        return State
   
    # 对称算子，产生候选解
    def op_symmetry(self):
        n = self.Best.size
        State = np.zeros((self.SE,n),dtype = int)
        for i in range(self.SE):
            temp = self.Best.copy()
            R = np.random.permutation(n)
            a = R[0]
            b = R[1]
            if a < b:
                temp[list(range(a,b+1))] = temp[list(range(b,a-1,-1))]
            else:
                temp[list(range(b,a+1))] = temp[list(range(a,b-1,-1))]
            State[i,:] = temp
        return State
        
    # 平移算子，产生候选解
    def op_shift(self):
        n = self.Best.size
        State = np.zeros((self.SE,n),dtype = int)
        for i in range(self.SE):
            temp = self.Best.copy()
            R = np.random.permutation(n)
            a = R[0]
            b = R[1]
            if a < b:
                temp[a:b],temp[b] = temp[a+1:b+1],temp[a]
            else:
                temp[b:a],temp[a] = temp[b+1:a+1],temp[b]
            State[i,:] = temp
        return State
    
    # 选择更新当前最优解
    def selection(self,State):
        fState = np.zeros((self.SE,1))
        for i in range(self.SE):
            fState[i] = self.fun(State[i,:])
        index_newBest = np.argmin(fState)
        newBest = State[index_newBest,:]
        fnewBest = fState[index_newBest,:]
        if fnewBest < self.fBest:
            self.Best = newBest
            self.fBest = fnewBest
    
    # 迭代优化
    def run(self,draw):
        for i in range(self.MaxIter):
            State = self.op_swap()
            self.selection(State)
            State = self.op_shift()
            self.selection(State)
            State = self.op_symmetry()
            self.selection(State)
            # print()
            draw(i,self.Best,self.fBest)
            
    

        