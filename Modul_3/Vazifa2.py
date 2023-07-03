#leetcode

#1 242    chiqmadi

class Solution():
    def __init__(self, s1, s2):
        self.s1=s1
        self.s2=s2

    def myfunc(self):
        arr=[]
        arr2=[]
        for i in range(len(self.s1)):
            arr.append(self.s1[i])
        for i in range(len(self.s2)):
            arr2.append(self.s2[i])
        for i in range(len(arr)):
            for j in range(len(arr2)):
                if arr[i]==arr2[j]:
                    arr.pop(i)
                    arr2.pop(j)
        m=False
        if len(arr)==0 and len(arr2)==0:
            m=True
        return m
s1=input('s1=')
s2=input('S2=')
ob=Solution(s1,s2)
print(ob.myfunc())