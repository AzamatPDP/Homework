import datetime as dt
import re
# today = dt.date.today()
# print(today)
# kun = today.day
# day2 = dt.date(2024,5, kun+14)
# print(day2)

# 1 - topshiriq
# from datetime import datetime, timedelta
#
# today = datetime.today()
#
# for i in range(10):
#     date = today + timedelta(weeks=2*i)
#     print(date.strftime("%Y-%m-%d"))

# 2 - topshiriq
# qurbanEidDay = dt.date(2024,6,16)
# ramadanEidDay = dt.date(2025, 3, 31)
# today = dt.date.today()
# print(f"Qurbon haytiga {(qurbanEidDay - today).days} kun qoldi")
# print(f"Ramazon haytiga {(ramadanEidDay - today).days} kun qoldi")

# 3 - topahiriq
# def birthDay(year ,month, day):
#     today = dt.date.today()
#     birthday = dt.date(year, month, day)
#     Day = today - birthday
#     yDm = Day.days
#     return f"{yDm // 365} yil, {yDm // 30 } oy, {yDm} kun"
# print(birthDay(2004,3,6))

# 4 - topshiriq
# andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# numMSG = "Telefon raqam kiriting:"
# while True:
#     number = input(numMSG)
#     if re.match(andoza,number):
#         print("To'gri telefon raqam")
#         break
#     else:
#         print("Bu telefon raqam emas")


from datetime import datetime
def yosh_hisobla(tugilgan_sana):
    tugilgan_sana = datetime.strptime(tugilgan_sana, '%Y-%m-%d')
    hozirgi_sana = datetime.now()
    farq = hozirgi_sana - tugilgan_sana
    kunlar = farq.days
    yillar = kunlar // 365
    oy = (kunlar % 365) // 30
    kun = (kunlar % 365) % 30
    return f"Siz {yillar} yil, {oy} oy va {kun} kun yashadingiz."

# Foydalanish misoli:
print(yosh_hisobla('2004-08-06'))
