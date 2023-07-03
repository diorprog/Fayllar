            #
            
# iterator=iter([1,2,3,4,5,6,7,8,9])
# print(iterator)


            #

# iterator=iter([1,2,3,4,5,6,7,8,9])
# print(iterator.__next__())

            #

# iterator=iter([1,2,3,4,5,6,7,8,9])
# while True:
#     print(iterator)

            #

iterator=iter([1,2,3,4,5,6,7,8,9])
while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        break