from User import User1


def main():
    text = """
        Welcome to pdp
        1) register
        2)login
        3)exit
    """
    choice = input(text)
    print(choice)
    if choice == '1':
        role_txt = """
                    Role: 
                    1) Client
                    2)Merchant
                    >>> """

        data = {'fullname': input('full name: '),
                # 'number': int(input('number: ')),
                'email': input('email: '),
                'username': input('username: '),
                'password': input('password: '),
                # 'created_at': input('created time: '),
                'role': input(role_txt)}
        obj = User1(**data)
        try:
            obj.check_data()
            obj.save()
            # main()
        except Exception as d:
            print(d)
            main()
    elif choice == '2':
        data2 = {"fullname": input('full name: '),
                 "email": input('email: '),
                 "password": input('password: '),
                 "role": input('role'),
                 "username": input('username: ')}
        obj2 = User1(**data2)
        try:
            obj2.log_gin()
        except Exception as e:
            print(e)


    elif choice == '3':
        print('Dastur toxtadi!')
        return


main()
