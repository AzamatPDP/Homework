class User:
    def __init__(self, username,fullname,age,email):
        self.username = username
        self.toliqism = fullname
        self.yosh = age
        self.email = email

    def maxAge(self):
        pass
    def get_age(self):
        return f"Yosh:{self.yosh}"
    def get_fullname(self):
        print(f"Username:{self.username}")
    def get_email(self):
        return f"Email:{self.email}"
    def get_info(self):
        print(f"Github username '{self.username}', to'liq ismim '{self.toliqism}' va menga murojaat qilishingiz uchun => {self.email}")

user1 = User("AzamatPBD","Azamat Jumabayev", 20, "azamatjumabayev8774@gmail.com")
user2 = User("juma_developer","Aziz Jumabayev", 21, "azizbek@gmail.com")
user3 = User("Onedeveloper","Afzalbek Jumabayev", 23, "onedevelopernaik@gmail.com")
user1.get_info()
user1.get_fullname()
print(user1.get_age())
print(user1.get_email())
user2.get_info()
user3.get_info()
