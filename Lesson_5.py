#HomeWork
# foydalaunuvchi_ismi = input("Login kiriting:")
# if foydalaunuvchi_ismi.lower() == 'root':
#     print("Xush kelibsiz Rootjon. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {foydalaunuvchi_ismi}")

# print("Ikkita son kiriting")
# n1 = float(input("1-son:"))
# n2 = float(input("2-son:"))
# if n1 == n2: print("Bu sonlar teng!")
# else: print("Bu sonlar teng emas!")

# number = float(input("Ixtiyoriy son kiriting:"))
# if number > 0: print("Musbat son")
# elif number == 0: print("Bu son 0 ga teng")
# else: print("Manfiy son")

# number = float(input("Ixtiyoriy son kiriting:"))
# if number > 0: print(number**(1/2))
# else: print("Musbat son kiriting")

numbers = []
n = int(input("Nechta son kiritasiz:"))
for num in range(n):
    numbers.append(int(input(f"{num+1}-sonni kiriting:")))
print(numbers)
musbat = []
manfiy = []
for i in numbers:
    if i >= 0:
        musbat.append(i)
    else:
        manfiy.append(i)
print(f"Musbat sonlar: {musbat}")
print(f"Manfiy sonlar: {manfiy}")