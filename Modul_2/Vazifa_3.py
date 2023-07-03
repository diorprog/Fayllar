            #1

class Butun:
    def __init__(self, arr):
        self.arr=arr
    def yig(self):
        s=0
        for i in self.arr:
            s+=i
        return f' {s} '

    # def kop(self):
    #     s = 1
    #     for i in range(len(self.arr)):
    #         s *= self.arr[i]
    #     return f' {s} '
    #
    # def maxx(self):
    #     m = self.arr[0]
    #     for i in range(len(self.arr)):
    #         if m<self.arr[i]:
    #             m=self.arr[i]
    #     return f' {m} '
    #
    # def minn(self):
    #     m = self.arr[0]
    #     for i in range(len(self.arr)):
    #         if m>self.arr[i]:
    #             m=self.arr[i]
    #     return f' {m} '

arr=list(map(int,input('Massiv: ').split()))
result=Butun(arr)
print(f'{result.yig()}')

                #2

# class Butun:
#     def __init__(self, arr):
#         self.arr=arr
#     def maxx(self):
#         m=0
#         for i in range(len(self.arr)):
#             if self.arr[m]<self.arr[i]:
#                 m=i
#         return m+1
#
# arr=list(map(int,input('massiv: ').split()))
# res=Butun(arr)
# print(f'{res.maxx()}')

                #3

# class Butun:
#     def __init__(self, arr):
#         self.arr=arr
#     def man(self):
#         arr2=[]
#         for i in self.arr:
#             if i<0:
#                 arr2.append(i)
#         for i in self.arr:
#             if i==0:
#                 arr2.append(i)
#         for i in self.arr:
#             if i>0:
#                 arr2.append(i)
#         return  arr2
#
# arr=list(map(int,input('Massiv: ').split()))
# rs=Butun(arr)
# print(rs.man())

                #4

# class Butun:
#     def __init__(self, arr, t1, t2):
#         self.arr=arr
#         self.t1=t1
#         self.t2=t2
#     def man(self):
#         for i in self.arr:
#             if i<0:
#                 self.t2+=1
#         for i in self.arr:
#             if i>0:
#                 self.t1+=1
#         return  f'Musbatlar {self.t1}  Manfiylar {self.t2}'
#
# arr=list(map(int,input('Massiv: ').split()))
# rs=Butun(arr,0,0)
# print(rs.man())

                #5

# class Butun:
#     def __init__(self, arr):
#         self.arr=arr
#     def man(self):
#         arr2=[]
#         for i in range(len(self.arr)):
#
#         return  f'Musbatlar {self.t1}  Manfiylar {self.t2}'
#
# arr=list(map(int,input('Massiv: ').split()))
# rs=Butun(arr)
# print(rs.man())


                #8

# class Tovar:
#     def __init__(self, soni, narxi, sot):
#         self.