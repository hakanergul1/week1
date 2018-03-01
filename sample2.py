# week1

N = int(input("Sayi Giriniz : "))


x = 1
print (1)
while x <= N:
    i = 2
    while i*i <= x:
        if x % i == 0:
            break
        i += 1
    else:
        print(x)
    x += 1
