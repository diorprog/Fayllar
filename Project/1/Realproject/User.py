import json
import time


class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            return data

    def write(self, data):
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=3)


class User1:
    def __init__(self, fullname: str,
                 email: str,
                 password: str,
                 role: str,
                 username: str):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.role = role
        self.username = username
        # self.number = number
        # self.created_at = created_at if created_at else time.strftime("%Y-%m-%d %H:%M")

    def check_data(self):
        if not self.fullname:
            raise Exception('Full name kiritilmadi! ')
        obj = File('user.json')
        data = obj.read()
        for i in data:
            if i.get('username') == self.username:
                raise Exception('Bunday username ishlatilgan: ')
        if len(self.password) < 4:
            raise Exception('Parol 4 belgidan kop bolishi zarur')

    def save(self):
        obj = File("user.json")
        data = obj.read()
        data.append(self.__dict__)
        obj.write(data)

    def log_gin(self):
        obb = File('user.json')
        date3 = obb.read()
        for i in date3:
            if i.get('fullname') == self.fullname and i['email'] == self.email and i['password'] == self.password:
                print('Dastur bo\'limi ko\'rsatildi ')
