#HomeWork
# age = int(input("How old are you?=>"))
# if age <= 5 or age > 60:
#     price = 0
# elif age <= 18:
#     price = 15000
# else:
#     price = 25000
# print(f"Sizga chipta narxi {price} so'm")

# print("Ixtiyoriy 2 ta son kiriting")
# n1 = float(input("1-son:"))
# n2 = float(input("2-son:"))
# if n1 > n2:
#     print(f"1-son katta ya'ni {n1}")
# elif n1 < n2:
#     print(f"2-son katta ya'ni {n2}")
# else:
#     print("Bu ikki son teng")

# number = int(input("Ixtiyoriy son kiriting:"))
# numbers = []
# for i in range(3,15):
#     if (i % number) == 0:
#         numbers.append(i)
# print(f"{number} shu sonlarga qoldiqsiz bo'linadi: {numbers}")

users = ['ajumabayev', 'developer', 'backend', 'android', 'ios', 'qwerty', 'youtube', 'python', 'jumabayev', 'azamat']
login = input("Yangi login kiriting:")
if login in users:
    print("Hurmatli foydalanuvchi login band, yangi login kiriting!")
else:
    print("Hurmatli foydalanuvchi login muvaffaqiyatli qabul qilindi")