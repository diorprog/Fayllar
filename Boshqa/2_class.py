# type,  value

# xotira 2 xil: 
#stack -- qiymat joylashadigan xotira
#heap -- qiymat joylashadigan xotira

# a:int=9        obj : A=A()          o'zgaruvchi : type = qiymat      o'zgaruvchi tipini oldindan ko'rsatish   dastur nisbatan tezroq ishlaydi

                
                #class
                
# class A:
#                         # class attribute{
#     a=7
#     b=9
                        #}
#     def __init__(self,a,b):
#                         # instance attribute {
#         self.a=a
#         self.b=b
                        #}
# obj=A(11,9)
# print(obj.a)


                                #method

# class Number:
#         def __init__(self, a: int, b: int):
#                 self.a = a
#                 self.b = b
#
#         def add(self):
#             summa = self.a + self.b + self.test
#             return summa
#
#         def sep(self):
#             result = self.a - self.b
#             return result
#
#         test = 10
#
#
# obj = Number(10, 20)
#
# print(obj.add())
# print(obj.sep())

                            # Inheritance -> (Vorislik) 5 turi bor:


# class A:
#     pass
#
#
# class B:
#     pass
#
#
# class C(A,B):             # 2 ta A va B class lardan funksiyalarni C ga o'zlashtirib oladi
#     pass
#



                            # Encapsulation


# class A:
#     def __init__(self, a, b, c):
#         self.a = a        # public
#         self._b = b        # Protected -->  not change value
#         self.__c = c        # private  --> not see, not change value
#
#     @property
#     def b(self):               #  <----  protected to'g'ri ishlashi uchun
#         return self._b
#
#     @property
#     def __dict__(self):                 # <---- koddagi  himoyalangan kodlarni aniqlashni cheklash  __dict__     yashirin kodlarni nomlarini chiqarib beradi
#         raise AttributeError("__dict__ orqali ko'rishni iloji yo'q")
#
# obj = A(1, 2, 3)
#
# print(obj.b)
# print(obj.__dict__)