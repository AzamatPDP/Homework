#Homework
# Dost = {
#     'azamat':['lol', 'sir', 'men','aso'],
#     'izzat':['men', 'andalus fotihlari'],
#     'suroj':['atom odatlari', 'dor ostidagi odam'],
#     'umid':['tungi suhbatlar', 'tongi suhbatlar']
# }
# ism = ''
# name = input("Ismni kiriting:").lower()
# for key, value in Dost.items():
#     if key.lower() == name:
#         ism = key
#         break
# if ism:
#     print(f"{name.title()}ni sevimli kitoblari quyidagilar:",end="")
#     for book in Dost[ism]:
#         print(f"{book}, ",end="")

davlatlar = {
    'uzbekistan':{
        'poytaxt':'Toshkent',
        'dTil':'uzbek tili',
        'joylashuv':'o\'rta osiyo',
        'aholi':'37 mln'
    },
    'rossiya':{
        'poytaxt':'Moskva',
        'dTil':'rus tili',
        'joylashuv':'yevropa',
        'aholi':'350 mln'
    },
    'Xitoy':{
        'poytaxt':'Pekin',
        'dTil':'xitoy tili',
        'joylashuv':'osiyo',
        'aholi':'1 mlrd 450 mln'
    },
    'Germaniya':{
        'poytaxt':'Berlin',
        'dTil':'nemis tili',
        'joylashuv':'yevropa',
        'aholi':'84 mln'
    }
}

# for d,info in davlatlar.items():
#     print(f"{d.title()}:"
#           f" Poytaxti {info['poytaxt']} shaxri,"
#           f"davlat tili {info['dTil']}, "
#           f"{info['joylashuv']}da joylashgan, "
#           f"aholisi {info['aholi']} hisoblanadi")

davlat = input("Davlat nomini kiriting:").lower()
d = ""
for key,value in  davlatlar.items():
    if key.lower()==davlat:
        d = key
        break
# lugat = {}
if d:
    # print(davlatlar[d])
    # lugat = davlatlar[d]
    print(f"{davlat.title()}:", end="")
    print(f" Poytaxti {davlatlar[d]['poytaxt']} shaxri,"
          f"davlat tili {davlatlar[d]['dTil']}, "
          f"{davlatlar[d]['joylashuv']}da joylashgan, "
          f"aholisi {davlatlar[d]['aholi']} hisoblanadi")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")
