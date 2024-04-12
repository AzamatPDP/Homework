def tub_son(son):
    """Ixtiyoriy butun sonni tublikga tekshiruvchi funksiya"""
    i, k = 1, 0
    while i <= n:
        if n % i == 0:
            k += 1
        if k > 2: break
        i += 1
    if k == 2:
        print(f"{n} tub son")
    else:
        print(f"{n} tub son emas")

#Quyidagicha funksiyaga murojat qilinadi
n = int(input("Ixtiyoriy butun son kiriting=>"))
tub_son(n)
tub_son(7) #to'g'ridan to'g'ri qiymat berishimiz ham mumkin


# def EKUB(a,b):
#     """2 ta musbat butun sonning EKUBini hisoblovchi funksiya"""
#     x = a
#     y = b
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     print(f"EKUB({x},{y}) = {a} ")
#
# # #Quyidagicha funksiyaga murojat qilinadi
# n = int(input("1-sonni kiriting:"))
# m = int(input("2-sonni kiriting:"))
# EKUB(n,m)
# # EKUK(12,8) #to'g'ridan to'g'ri qiymat berishimiz ham mumkin
# #Quyidagicha funksiyaga murojat qilinadi
# n = int(input("Ixtiyoriy butun son kiriting=>"))
# tub_son(n)
# tub_son(7) #to'g'ridan to'g'ri qiymat berishimiz ham mumkin


def EKUB(a,b):
    """2 ta musbat butun sonning EKUBini hisoblovchi funksiya"""
    x = a
    y = b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(f"EKUB({x},{y}) = {a} ")

# #Quyidagicha funksiyaga murojat qilinadi
n = int(input("1-sonni kiriting:"))
m = int(input("2-sonni kiriting:"))
EKUB(n,m)
# EKUK(12,8) #to'g'ridan to'g'ri qiymat berishimiz ham mumkin

