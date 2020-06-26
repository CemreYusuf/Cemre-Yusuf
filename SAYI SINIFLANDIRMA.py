sayi1=float (input("BİR SAYI GİR.KÜSÜRATLI OLABİLİR:  "))
sayi2=int(sayi1)
if sayi2!=sayi1:
    print(sayi1, "KÜSÜRTLI BİR SAYI ")
elif sayi2%2==0:
    print(sayi2, "EKRANA YAZDIRILAN SAYI ÇİFTTİR")
elif sayi2%3==0:
    print(sayi2, "EKRANA YAZDIRILAN SAYI 3 VEYA 3'ÜN KATIDIR")
else:
    print(sayi2, "EKRANA YAZDIRILAN SAYI TAM SAYIDIR")
