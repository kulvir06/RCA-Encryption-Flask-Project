from operator import indexOf


file1 = open("static\\uploads\\keys.txt", "r")
text = file1.read().split()
i1 = text.index("Kc")
# print(i1)
i2 = text.index("ITER_MAX")
# print(i2)
for i in range (3,i1-1):
    Kr.append(int(text[i])) 
# print(kr)
for i in range (i1+2, i2):
    Kc.append(int(text[i]))
# print(kc)



