#Sayı tahmin oyunu
#python 3.7.7500
import random
MAX=1000
aranan=random.randint(1,MAX)
say=0
while True:
    mesaj="1 ile "+str(MAX)+ "ARASINDA BİR SAYI TAHMİN ET"
    stahmin=input(mesaj)
    tahmin=int(stahmin)
    say+=1
    if tahmin == aranan:
        print("BRAVO! ARANAN SAYI {} ADIMDA BULUNDU".format(say))
        break
    elif tahmin < aranan:
        print("GİRDİĞİN SAYI KÜÇÜK")
    else:
        print("GİRDİĞİN SAYI ARANANDAN BÜYÜK")
