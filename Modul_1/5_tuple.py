# tuple ni o'zgartirish mumkin emas son o'chirish qo'shish mumkin emas. o'zgartirish list orqali amalga oshiriladi.
tpl=(1,2,3,5,7,9)

for i in tpl:
    print(i,end=' ')
print()

for i in range(len(tpl)):
    print(tpl[i],end=' ')
print()

for i in range(0, len(tpl), 2):
    print(tpl[i],end=' ')
print()

tpl=(1,2,3,5,7,9)
print(tpl[::-1])

tpl=(1,2,3,5,7,9)
print(tpl[1:5])

       #

tpl=(1,2,3,5,7,9)
arr=list(tpl)

arr.append(4)
arr.sort()
tpl2=tuple(arr)

print(tpl2)