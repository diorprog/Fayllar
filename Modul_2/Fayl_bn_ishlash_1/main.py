             #
# f=open('D:\Python\Modul_2\Fayl_bn_ishlash_1\input.txt','r')   #  o'qish uchun 'r'
# print(f.read())

            #
            
# f=open("D:\Python\Modul_2\Fayl_bn_ishlash_1\input.txt",'a')
# f.write(' P14 Group')                                                 # txt file ga shu matnni qo'shib boradi


            #
            
# f=open('D:\Python\Modul_2\Fayl_bn_ishlash_1\input.txt','r')
# arr=list(map(int,f.read().split()))
# print(arr)


            #
            
            #    {      n inputdan olib fibonachi sonlarni outputga chiqaradi
            
f=open('D:\Python\Modul_2\Fayl_bn_ishlash_1\input.txt')
n=int(f.read())
f.close()
f=open('D:\Python\Modul_2\Fayl_bn_ishlash_1\output.txt','w')

a1=a2=1
while a1<=n:
    a3=a1+a2
    f.write(f'{a1} ')
    a1,a2=a2,a3
f.close

            # chiqarilgan outputdagi qiymatni dictga yuklab printda chiqaradi
            
f=open('D:\Python\Modul_2\main\output.txt','r')
arr=list(map(int,f.read().split()))
f.close()

arr2=[]

for i,j in enumerate(arr):
    arr2.append(
        {
            'index':  i+1,
            'valuse': j
        }
    )
    
print(arr2)             #      }