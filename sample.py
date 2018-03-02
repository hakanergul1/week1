f = int(input("İşlem Kaç Defa Tekrar Etsin : "))
if f<=0:
    print ("Döngü sıfırdan tekrar edemez. : ")
for i in range (0,f) :
    sayi1 = int(input("1. Sayıyı Girin :"))
    sayi2 = int(input("2. Sayıyı Girin :"))
    islem = input("İşlem Operatörü Seçiniz (+,-,*,/):")


    if islem == "+" :
        print (sayi1+sayi2)

    elif islem == "-" :
        print (sayi1-sayi2)

    elif islem == "*" :
        print (sayi1*sayi2)

    elif b==0 :
        print ("Sıfır ile bölme işlemi yapamazsınız.")
    elif islem =="/" :
        print (sayi1/sayi2)

    elif islem == "exit":
        break
    else:
        print("İşlem operatörü giriniz")
