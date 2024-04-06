#HomeWork
# uzb = ['TOSHKENT', 'NAMANGAN', 'ANDIJON', 'SIRDARYO', 'JIZZAX', 'XORAZIM', 'BUXORO', 'NAVOIY', 'SAMARQAND', 'QASHQADARYO', "FARG'ONA", 'SURXONDARYO']
# print("Asl ro'yxat:",uzb)
# print(f"O'zbekistonda {len(uzb)} ta viloyat bor")
# print("Tartiblangan ro'yxat:", sorted(uzb))
# print("Teskari tartiblangan ro'yxat:", sorted(uzb, reverse=True))
# print("Asl ro'yxat:",uzb)
# uzb.reverse()
# print(uzb) #Asl ro'yxatning tezkarisi
# uzb.sort()
# print("Alifbo tartibidagi ro'yxat", uzb)
# print(sorted(uzb, reverse=True)) #Teskari alifbo tartibi

juft_sonlar = list(range(180,1800,2))
print(juft_sonlar)
summa = sum(juft_sonlar)
print("Summa:",summa)
maxx = max(juft_sonlar)
minn = min(juft_sonlar)
ayirma = maxx - minn
yigindi = maxx + minn
print(f"{maxx} - {minn} = {ayirma}")
print(f"{maxx} + {minn} = {yigindi}")
print(f"Ro'yxatda jami {len(juft_sonlar)} ta sonlar bor")
print(juft_sonlar[:10])
print(juft_sonlar[400:410])
print(juft_sonlar[800:])