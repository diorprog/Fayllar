            #

# def my_decor(func):
#     def wrapper():
#         print('Funksiyadan oldin')
#         func()
#         print('Funksiyadan keyin')
#     return wrapper()

# def prnt():
#     print('decorator')

# my_decor(prnt)

            #
            
# def my_decor(func):
#     def wrapper():
#         print('Funksiyadan oldin')
#         func()
#         print('Funksiyadan keyin')
#     return wrapper()

# @my_decor
# def prnt():                                                       # printsiz ishlatish
#     print('decorator')

            #
            
# def check_email(func):                                      #    @ bor yoki yo'qlikka tekshiradi
#     def wrapper(email):
#         if '@' in email:
#             func(email)
#         else:
#             raise Exception("Emailda @ belgi bo'lishi kerak.")
#     return wrapper

# @check_email
# def pechat(email):
#     print(email)
    
# pechat('abcd@gmail.com')

            #
            
# def phone(func):
#     def wr(num):
#         if num.startswith('+998') and len(num)==13:
#             func(num)
#         else:
#             raise Exception("998 bilan boshlanishi kerak.")
#     return wr

# @phone
# def prnt(num):
#     print(num)
    
# prnt('+998943331161')