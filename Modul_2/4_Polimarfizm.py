            # Polimarfizm    len() kiradi      M:   a=len('text1', 'text2', 'text3') a ning qiymati 3 bo'ladi va len har bir ichki elemtlar(m: a[1]=len(text1) a[2]=len(text2) ... ) uchun ham ishlatiladi bu polimarfizm

# import datetime
#
# class Animal:
#     def __init__(self,turi:str, nomi:str, t_yili:int):
#         self.turi=turi
#         self.nomi=nomi
#         self.t_yili=t_yili
#
#     def get_age(self, year):
#         return year - self.t_yili
#
#     def get_info(self):
#         print(f'{self.turi}  |  {self.nomi}  |  {self.t_yili}')
#
# class Bird(Animal):
#     def __init__(self,turi:str, nomi:str, t_yili:int, uchadimi: bool):
#         super().__init__(turi, nomi, t_yili)
#         self.uchadimi=uchadimi
#
#     def get_info(self):
#         print(f'{self.turi}  |  {self.nomi}  |  {self.t_yili}  |  {"Ha" if self.uchadimi else "Yo`q"}')
#
# bird1=Animal('Yovvoyi', 'Burgut', 2020)
# print(bird1.get_age(datetime.datetime.now().year))
# bird1.get_info()
#
# bird2=Bird('Yovvoyi', 'Pingvin', 2015, False)
# print(bird2.get_age(datetime.datetime.now().year))
# bird2.get_info()