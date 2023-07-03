import sqlite3

con = sqlite3.connect('library.sqlite')

cur = con.cursor()


def create_p():
    text = """Qaysi amalni bajarasiz: :
        1.Qo'shish
            2.O'chirish
                3.Yangilash
        """
    choose = int(input(text))
    if choose == 1:
        print('Creat books table')
        n = int(input('Nechta qo\'shmoqchisiz '))
        for i in range(n):
            id1 = int(input('id: '))
            name1 = input('name: ')
            author1 = input('author: ')
            year1 = int(input('year: '))
            query = "insert into books(id,name,author,year) values(id1,name1,author1,year1) "
            cur.execute(query)
            con.commit()
            create_p()

    elif choose == 2:
        m = input('ID bo\'yicha qaysini o\'chirsin:   ')
        query = "delete from books where id = m"
        cur.execute(query)
        con.commit()
        create_p()
    elif choose == 3:
        data = input('O\'zgartirish: ')
        id2 = int(input('ID: '))
        update2 = input('qaysi so\'z bilan yangilansin: ')
        query = f"update books set name = update2 where id = id2"
        cur.execute(query)
        con.commit()
        create_p()


def admin_panel():
    print('Hush kelibsiz: ')
    t =1
    if t==1:
        create_p()


def reader_panel():
    print('Tahrirlash')


def main():
    text = """
        1.Admin
        2.Tahrirlash
        """
    choose = int(input(text))
    if choose == 1:
        admin_panel()
        # username = input('username:')
        # password = input('password:')

    elif choose == "2":
        reader_panel()
        # fullname = input('fullname:')
        # password = input('password:')


main()