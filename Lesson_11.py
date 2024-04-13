def aylana(radius):
    uzunlik = 2 * 3.14 * radius
    yuza = 0
    diametr = 2 * radius
    
    aylana_info = {
        'radius':radius,
        'uzunlik':uzunlik,
        'yuza':yuza,
        'diametr':diametr
    }
    return aylana_info

radius = float(input("Radius kiriting:"))
aylana_info = aylana(radius)
print(aylana_info)


# def tub_sonlar(n, m):
#     """Berilgan n va m butun musbat sonlar orasidagi tub sonlar"""
#     tub = []
#     while n <= m:
#         i = n
#         j = 1
#         boluvchi = 0
#         while j <= i:
#             if i % j == 0:
#                 boluvchi += 1
#             j += 1
#         if boluvchi == 2:
#             tub.append(i)
#         n += 1
#     return tub
# n = int(input("n=>"))
# m = int(input("m=>"))
# tublik = tub_sonlar(n, m)
# print(f"Tub sonlar: {tublik}")

# def fibonachi(n):
#     fibo = [0, 1]
#     i = 2
#     while i < n:
#         fibo.append(fibo[-1] + fibo[-2])
#         i += 1
#     return fibo
# son = int(input("Nechta fibonachi sonlari kerak:"))
# print(fibonachi(son))

# def fibonachi(n):
#     fibo = [0, 1]
#     for i in range(2, n):
#         fibo.append(fibo[-1] + fibo[-2])
#     return fibo
# son = int(input("Nechta fibonachi sonlari kerak:"))
# print(fibonachi(son))



