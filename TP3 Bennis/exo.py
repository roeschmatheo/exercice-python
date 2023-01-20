a = 5
b = 8
c = 5

while b < 7 :
    if a < c :
        a += 3
    else:
        c -= 1
    b += 1

if a < b and (a + c) > b :
    print(1)
else :
    print(2)

if (a < c) :
    print(3)
else :
    print(4)
    if (a + c) > 2 * b :
        print(5)





