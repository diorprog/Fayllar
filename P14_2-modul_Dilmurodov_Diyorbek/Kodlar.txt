#1-savol


# f=open('P14_2-modul_Dilmurodov_Diyorbek\savol1.txt','r')
# txt=f.read().split()
# arr=[]
# for i in range(len(txt)):
#     if i%2==1:
#         arr.append(txt[i].replace(txt[i],'00'))
#     else:
#         arr.append(txt[i])
# print(arr)



#2-savol


# f=open('P14_2-modul_Dilmurodov_Diyorbek\savol2.txt','r')
# txt=f.read().split()
# arr=[]
# for i in range(len(txt)):
#     if i%2==0:
#         arr.append(txt[i].replace(txt[i],txt[i]+txt[i]))
#     else:
#         arr.append(txt[i])
# print(arr)


#3-savol


# f=open('P14_2-modul_Dilmurodov_Diyorbek\savol3.txt','r')
# txt=' '.join(f.read().split())

# if txt.endswith==" ":
#     txt.replace(txt[len(txt)-1],'')
# print(txt)
        
        

#4-savol


# s=input('s=')
# s1=input('s1=')
# s2=input('s2=')

# txt=s.replace(s1,s2,1)
# print(txt)


#5-savol


# class numm:
#     def __init__(self,n:int):
#         self.n=n
#         self.arr=[]
                
#     def ten(self):
#         y=int(self.n)//100
#         b=int(self.n)%10
#         o=int(self.n)//10%10
        
#         if int(self.n)>99 and int(self.n)<1000:
#             m=int(self.n)%100
#             if y==1:
#                 self.arr.append('bir yuz')
#             elif y==2:
#                 self.arr.append('iKKi yuz')
#             elif y==3:
#                 self.arr.append('uch yuz')
#             elif y==4:
#                 self.arr.append('to\'rt yuz')
#             elif y==5:
#                 self.arr.append('besh yuz')
#             elif y==6:
#                 self.arr.append('olti yuz')
#             elif y==7:
#                 self.arr.append('yetti yuz')
#             elif y==8:
#                 self.arr.append('saKKiz yuz')
#             elif y==9:
#                 self.arr.append('to\'qqiz yuz')
        
#         if int(self.n)>9 & int(self.n)<100:
#             if o==1:
#                 self.arr.append('o\'n')
#             elif o==2:
#                 self.arr.append('yigirma')
#             elif o==3:
#                 self.arr.append('o\'ttiz')
#             elif o==4:
#                 self.arr.append('qirq')
#             elif o==5:
#                 self.arr.append('elliK')
#             elif o==6:
#                 self.arr.append('oltmish')
#             elif o==7:
#                 self.arr.append('yettmish')
#             elif o==8:
#                 self.arr.append('saKson')
#             elif o==9:
#                 self.arr.append('to\'qson')
        
#         if int(self.n)>0 & int(self.n)<10:
#             if b==0:
#                 self.arr.append('nol')
#             elif b==1:
#                 self.arr.append('bir')
#             elif b==2:
#                 self.arr.append('iKKi')
#             elif b==3:
#                 self.arr.append('uch')
#             elif b==4:
#                 self.arr.append('to\'rt')
#             elif b==5:
#                 self.arr.append('besh')
#             elif b==6:
#                 self.arr.append('olti')
#             elif b==7:
#                 self.arr.append('yetti')
#             elif b==8:
#                 self.arr.append('saKKiz')
#             elif b==9:
#                 self.arr.append('to\'qqiz')
#         return ' '.join(self.arr)
# n=input('n=')
      
# res=numm(n)

# print(res.ten())



#6-savol


class Sanoq_Sistema_10:
    def __init__(self,n:int):
        self.n=n
        self.arr=[]
        self.arr2=[]
        self.arr3=[]

class Sanoq_Sistema_2(Sanoq_Sistema_10):
    def __init__(self, n: int):
        super().__init__(n)
        
    def sanoq(self):
        while int(self.n)!=0:
            self.arr.append(int(self.n)%2)
            self.n=int(self.n)//2
        self.arr.reverse()
        return self.arr
    
class Sanoq_Sistema_8(Sanoq_Sistema_10):
    def __init__(self, n: int):
        super().__init__(n)
        
    def sanoq8(self):
        while int(self.n)!=0:
            self.arr2.append(int(self.n)%8)
            self.n=int(self.n)//8
        self.arr2.reverse()
        return self.arr2
    
class Sanoq_Sistema_16(Sanoq_Sistema_10):
    def __init__(self, n: int):
        super().__init__(n)
        
    def sanoq16(self):
        while int(self.n)!=0:
            self.arr3.append(int(self.n)%16)
            self.n=int(self.n)//16
        for j in range(len(self.arr3)):
            if self.arr3[j]==10:
                self.arr3[j]='A'
            elif self.arr3[j]==11:
                self.arr3[j]=='B'
            elif self.arr3[j]==12:
                self.arr3[j]=='C'
            elif self.arr3[j]==13:
                self.arr3[j]=='D'
            elif self.arr3[j]==14:
                self.arr3[j]=='E'
            elif self.arr3[j]==15:
                self.arr3[j]=='F'
        self.arr3.reverse()   
        return self.arr3

n=input('n=')

res=Sanoq_Sistema_2(n)
res1=Sanoq_Sistema_8(n)
res2=Sanoq_Sistema_16(n)

print(res.sanoq(), res1.sanoq8(), res2.sanoq16())