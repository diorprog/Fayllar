

# inkapsulatsiya 3 turga bo'linadi: 

# public <--ochiq  
# protected <--yarim himoya    kodda:  _ 1 probel orqali
# provide <--  to'liq himoyalangan     kodda:   __ 2 probel orqali


class Human:
    def __init__(self, full_name, year, address):
        self._full_name = full_name
        self.year = year
        self.__address = address
    
    def pechat(self):
        print(self.full_name, self.address, self.year)
    
    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address


class Student(Human):
    def __init__(self, full_name, year, address, study):
        super().__init__(full_name, year, address)
        self.study = study

student = Human('ogijeoijeerg', 1000, 'peorgkperogkerpgo')
print(student.full_name, student.year, student.getAddress())
student.setAddress('Toshkent')
print(student.full_name, student.year, student.getAddress())