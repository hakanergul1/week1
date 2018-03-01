# week1
for x in range(3):
        sayi1=int(input("sayi gir : "))
        sayi2=int(input("sayi gir : "))
        s=0
        print("Toplama Islemi(+)")
        print("Cikarma Islemi(-)")
        print("Bolme   Islemi(*)")
        print("Carpma  Islemi(/)")
        islem=input("islem : ")
        if islem == "+" :
            s=sayi1+sayi2

            print("sonuc", s)
        elif islem=="-":
            s=sayi1-sayi2
            print("sonuc",s)
        elif islem=="*":
            s=sayi1*sayi2
            print("sonuc",s)
        elif islem=="/":
            s=sayi1/sayi2
            print("sonuc",s)
