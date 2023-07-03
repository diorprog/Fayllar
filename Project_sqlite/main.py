from model import User, Book
session_user: User = None
session_book: Book = None

def register():
    d = {
        "name": input("Name:"),
        "username": input("Username:"),
        "password": input("Password:"),
    }
    user = User(**d)
    if user.check_username():
        print("Your username already exists!")
        return
    user.save_user()
    print("Registration successful !")


def login():
    global session_user

    d = {
        "username": input("Username:"),
        "password": input("Password:"),
    }

    obj = User(**d)
    session_user = obj.login_check()
    if not session_user:
        print("Wrong username or password !")
        return
    print(f"Welcome {session_user.name}")
    if session_user.role == "ADMIN":
        admin_menu()
    else:
        user_menu()


def category_crud():
    text = """
        1) Read category
        2) New category
        3) Delete category
        4) <- back
        >>>>  """

    key = input(text)
    match key:
        case 1:
            pass
            # read_category()
        case 2:
            pass
            # new_category()
        case 3:
            pass
            # delete_category()
        case 4:
            admin_menu()


def book_crud():
    text = """
    1.Yangi kitob qo'shish
    2.Kitob infosini yangilash
    3.O'chirish
    4.<- Back
            >>>"""
    key = int(input(text))
    match key:
        case 1:
            d = {
                'name': input('name'),
                'category_id': int(input('category_id:')),
                'count': int(input('count:'))
            }
            obj_book = Book(**d)
            obj_book.save_book()
        case 2:
            taxt = """
            1.Nomi
            2.Kategoriyasi
            3.Soni
                  >>>"""
            key = int(input(taxt))
            item = input('New_item:')
            obj = Book()

        case 3:
            delete_name = input('O\'chiriladigan kitob nomi: ')
            obj = Book()
            obj.delete_book(delete_name)
        case 4:
            return
    book_crud()


def admin_menu():
    menu = """
    1) Kategoriya
    2) Kitob
    3) Admin qo'shish
    4) Sozlanmalar
    5) Profildan chiqish
        >>>"""
    # C  create
    # R  remove
    # U  update
    # D  delete
    key = int(input(menu))
    match key:
        case 1:
            category_crud()
        case 2:
            book_crud()
        case 3:
            add_admin()
        case 4:
            settings()
        case 5:
            return


def add_admin():
    text = """
    Admin qo'shish uchun username kiriting: 
           """
    new_admin = input(text)
    session_user.add_new_admin(new_admin)


def settings():
    menu = """
    1) change info
    2) delete account
    3) <- back
    """
    key = int(input(menu))
    match key:
        case 1:
            menu_col = """
                1) name
                2) username
                3) password
                4) <- back
                    >>>"""
            key = int(input(menu_col))
            if key != 4:
                new_val = input("New value: ")
            match key:
                case 1:
                    session_user.change_info("name", new_val)
                case 2:
                    session_user.change_info("username", new_val)
                case 3:
                    session_user.change_info("password", new_val)
                case 4:
                    settings()
            settings()

        case 2:
            acc_name = (input('Enter username'))
            session_user.delete_account(acc_name)
        case 3:
            admin_menu()
    admin_menu()


def user_menu():
    text = """
           1.Kitoblar
           2.Qidirish
           3.Sozlanmalar
           4.Profildan chiqish
           >>>"""
    key = int(input(text))
    match key:
        case 1:
            obj = Book()
            for i in obj.select_books():
                d = {
                    'id': i[0],
                    'name': i[1],
                    'category_id': i[2],
                    'count': i[3],
                    'created_time': i[4],
                }
                print(d)
        case 2:
            book_name = input('name:')
            category_id = input('category_if')
            obj = Book()
            data = obj.search_book(book_name)
            for i in data:
                d = {
                    'id': i[0],
                    'name': i[1],
                    'category_id': i[2],
                    'count': i[3],
                    'created_time': i[4],
                }
                print(d)
        case 3:
            manu = """
            1.Nomni o'zgartirish
            2.username ni o'zgartirish
            3.Parolni o'zgartirish
            4.Profilni o'chirish
            5. <- Back
                   >>>"""
            key = int(input(manu))
            match key:
                case 1:
                    change_name = input('Yangi nom:')
                    session_user.change_name(change_name)
                case 2:
                    change_username = input('Yangi username')
                    session_user.change_username(change_username)
                case 3:
                    change_password = int(input('Yangi parol: '))
                    session_user.change_password(change_password)
                case 4:
                    session_user.delate_self_account()
                    return
                case 5:
                    user_menu()

        case 4:
            return
    return


def UI():
    while True:
        text = """
        1) Register
        2) Login
        3) exit
            >>>"""
        key = int(input(text))
        match key:
            case 1:
                register()
            case 2:
                login()
            case 3:
                break


UI()


# class
"""
    AdminUI
    UserUI
    BookUI
    CategoryUI
    """
