class Shaxs:
    def __init__(self, firstname, lastname, passport, year, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.passport = passport
        self.year = year
        self.gender = gender

    def __repr__(self):
        return f"{self.firstname} {self.lastname}, {self.year}-da tug'ilgan, jinsi {self.gender}"


class Talaba(Shaxs):
    def __init__(self, firstname, lastname, passport, year, gender, kurs):
        super().__init__(firstname, lastname, passport, year, gender)
        self.kurs = kurs
    def __eq__(self, kurs):
        return self.kurs == kurs.kurs
    def __lt__(self, kurs):
        return self.kurs < kurs.kurs
    def __le__(self, kurs):
        return self.kurs <= kurs.kurs

    def get_kurs(self):
        return self.kurs
talaba1 = Talaba("Izzat", "Raximov", "AB123456", 2003, "Erkak", 2)
talaba2 = Talaba("Azamat", "Jumabayev", "AD0019319", 2004, "Erkak", 3)
print(f"{talaba1},{talaba1.get_kurs()}-kurs talabasi")
print(f"{talaba2},{talaba2.get_kurs()}-kurs talabasi")
if talaba2 < talaba1: print(f"{talaba2.firstname} {talaba2.lastname} katta kurs talabasi")
else: print(f"{talaba2.firstname} {talaba2.lastname} kichik kurs talabasi emas")
