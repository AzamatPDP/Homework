# def kalkulyator(belgi,*numbers):
#     kop = 1
#     ayirma = numbers[0]
#     bolinma = numbers[0]
#     if belgi == '+':
#         return sum(numbers)
#     elif belgi == '*':
#         for n in numbers:
#             kop *= n
#         return kop
#     elif belgi == '-':
#         for n in numbers:
#             ayirma -= n
#         return ayirma + numbers[0]
#     elif belgi == '/':
#         for n in numbers:
#             bolinma /= n
#         return bolinma * numbers[0]
#     else:
#         result = "Iltimos! quyidagi belgilardan bittasini tanlang:('+','-','*','/')"
#         return result
#
# belgi = input("('+', '-', '*', '/') shulardan bittasini tanlang!:")
# # number = float(input("Son kiriting:"))
# print(kalkulyator(belgi,6,9,3))

def birlashtiruvchi(*royxatlar):
    umumiy_royxat = []
    for royxat in royxatlar:
        umumiy_royxat.append(royxat)
    return umumiy_royxat

royxat1 = [1,2,3,4,5]
royxat2 = [6,7,8,9,10]
royxat3 = [11,12,13,14,15]
royxat4 = [16,17,18,19,20]
print(birlashtiruvchi(royxat1,royxat2,royxat3,royxat4))