class Shaxs:
    odamlar_soni = 0
    def __init__(self, ism, familya, passport, tYil):
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tYil = tYil
        Shaxs.odamlar_soni += 1

    @classmethod
    def get_odam_count(cls):
        return cls.odamlar_soni
    def get_info(self):
        info = f"{self.ism} {self.familya},"
        info += f"passport:{self.passport}, {self.tYil}-yilda tug'ilgan"
        return info
    def get_age(self, thisYear):
        return thisYear - self.tYil

person = Shaxs("Azamat", "Jumabayev", "AD0019319", 2004)
print(f"{person.get_info()}, {person.get_age(2024)} yoshda.")

class Talaba(Shaxs):
    talabalar_soni = 0
    def __init__(self, ism, familya, passport, tYil, idRaqam,):
        super().__init__(ism, familya, passport, tYil)
        self.__idRaqam = idRaqam
        Talaba.talabalar_soni += 1

    @classmethod
    def talaba_count(cls):
        return cls.talabalar_soni
    def get_idRaqam(self):
        return self.__idRaqam
    def update_idRaqam(self, new_idRaqam):
        newID = self.__idRaqam = new_idRaqam
        return newID


talaba1 = Talaba("Azamat", "Jumabayev", "AD0019319", 2004, 123001)
print(talaba1.get_info())
print(talaba1.get_idRaqam())
print(talaba1.update_idRaqam(123002))