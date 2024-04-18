# numbers = list(range(-5,5))
# print(numbers)
# musbat_numbers = list(filter(lambda num: num > 0,numbers))
# print(musbat_numbers)

# numbers = list(range(1,6))
# teskari_list = lambda num : num[::-1]
# print(teskari_list(numbers))

numbers = list(range(-5,5))
print(numbers)
juft_numbers = list(filter(lambda num : num % 2 == 0,numbers))
print(juft_numbers)
kvadrat = list(map(lambda num : num * num, juft_numbers))
print(kvadrat)