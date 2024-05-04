def maxnumber(n1, n2, n3):
    if n1 > n2 and n1 > n3: maxx = n1
    elif n2 > n1 and n2 > n3: maxx = n2
    else: maxx = n3
    return maxx

# print(maxnumber(6,5,9))
def stringTitle(matn = []):
    matnlar = []
    for i in matn:
        matnlar.append(i.title())
    return matnlar
# print(stringTitle(['azamat','jumabayev']))

def juftNumbers(*num):
    numbersArray = []
    for i in num:
        if i % 2 == 0:
            numbersArray.append(i)
    return numbersArray
# print(juftNumbers(1, 2, 3, 4, 5, 6))

def fiboNumber(fNum, num):
    numbers = [0, 1]
    i = 2
    while i < fNum:
        numbers.append(numbers[-1] + numbers[-2])
        i += 1
    ishora  = True
    for i in numbers:
        if i == num:
            ishora = True
            break
        else:
            ishora = False

    return ishora
print(fiboNumber(8,13))

