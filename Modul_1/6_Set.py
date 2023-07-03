            #
st={7,8,9,6,3,2,1,5,4}
print(st)
            #
st={7,8,9,6,3,2,1,5,4}
for i in st:
    print(i,end=" ")
print()
print(len(st))

            # Intersection    update
st1=set((7,8,9,6,3,2,1,5,4))
st2=set((1,8,10,11,12,13))

st1.intersection_update(st2)            #kesishma
print(st1)

            #
st1=set((7,8,9,6,3,2,1,5,4))
st2=set((1,8,10,11,12,13))

st3=st1.intersection(st2)
print(st3)
          
            # Difference      update
st1=set((7,8,9,6,3,2,1,5,4))
st2=set((1,8,10,11,12,13))

st1.difference_update(st2)
print(st1)

            #
st1=set((7,8,9,6,3,2,1,5,4))
st2=set((1,8,10,11,12,13))

st3=st1.difference(st2)
print(st3)

            #  Update
st1=set((7,8,9,6,3,2,1,5,4))
st2=set((1,8,10,11,12,13))
st1.update(st2)     #Birlashma
print(st1)

            #
st1=set((7,8,9,6,3,2,1,5,4))
st2=set((1,8,10,11,12,13))

st3=st2-st1
print(st3)    #Ayirma