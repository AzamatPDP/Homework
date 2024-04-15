def kalkulyator(belgi,*numbers):
    kop = 1
    ayirma = numbers[0]
    bolinma = numbers[0]
    if belgi == '+':
        return sum(numbers)
    elif belgi == '*':
        for n in numbers:
            kop *= n
        return kop
    elif belgi == '-':
        for n in numbers:
            ayirma -= n
        return ayirma + numbers[0]
    elif belgi == '/':
        for n in numbers:
            bolinma /= n
        return bolinma * numbers[0]

belgi = input("('+', '-', '*', '/') shulardan bittasini tanlang!:")
# number = float(input("Son kiriting:"))
print(kalkulyator(belgi,6,9,3))