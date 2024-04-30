# with open("ilm.txt") as file:
#     ilm = file.read()
# print(ilm)
import pickle
def oneday(n):
    with open("pi_million_digitss.txt") as file:
        number = file.read()
        if n in number: return True
        else: return False


n = input("Tug'ilgan kuningzini kiriting:")
if oneday(n):
    print("Bu son π ning qiymati ichida bor")
else:
    print("Bu son π ning qiymati ichida yo'q")
number = float(n)
with open("pi.pickle", "wb") as file1:
    pickle.dump(number,file1)

