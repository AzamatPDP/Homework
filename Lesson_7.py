# Homewrok
# kompyuter = {
#     'model':'Hp',
#     'Turi':'Victus',
#     'Protsessor':'Intel',
#     'Price': 700
# }
# kompyuter['Protsessor'] = 'AMD'
# print(kompyuter)
# year = kompyuter.get('year','Bunday ma\'lumot yo\'q')
# print(year)

# kompyuterQQ = {
#     'protsessor':'Intel',
#     'miyaus':'sichqoncha',
#     'printer':'chop qiliuvchi',
#     'kalonka':'ovoz chiqaruvchi',
#     'veb-kamera':'kamera',
#     'ssd':'doimiy xotira',
#     'hdd':'doimiy xotira',
#     'ram':'tezkor xotira'
# }
# for keys in kompyuterQQ.keys():
#     print(keys.upper())

# Davlatlar = {
#     'O\'zbekistan':'Tashkent',
#     'Rossiya':'Moskva',
#     'AQSH':'Vashington',
#     'Turkiya':'Istanbul',
#     'Xitoy':'Pekin',
#     'Yaponiya':'Tokiyo',
#     'Janubiy Korea':'Seul'
# }
# print(sorted(Davlatlar.items()))
# print(sorted(Davlatlar.keys()))
# print(sorted(Davlatlar.values()))
# for d, p in Davlatlar.items():
#     print(f"Davlat: {d}")
#     print(f"Poytaxt: {p}\n")

# davlatlar = {
#     'O\'zbekiston':'Taohkent',
#     'Rossiya':'Moskva',
#     'AQSH':'Vashington',
#     'Turkiya':'Istanbul',
#     'Xitoy':'Pekin',
#     'Yaponiya':'Tokiyo',
#     'Hindiston':'Dehli',
#     'Germaniya':'Berlin'
# }
# davlat = input("Davlat nomini kiriting:").lower()
# poytaxt = ""
# for key in davlatlar:
#     if key.lower() == davlat:
#         poytaxt = key
# # poytaxt  = davlatlar.get(davlat.lower(),'')
# if poytaxt:
#     print(f"Poytaxt=> {davlatlar[poytaxt]}")
# else:
#     print("Bizda bunday ma'lumot yo'q")