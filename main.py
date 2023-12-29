

import random
import time

class kumanda():
    def __init__(self,tv="kapali",tvses=0,kanali=["trt"],kanal="trt"):
        self.tv=tv
        self.tvses=tvses
        self.kanali=kanali
        self.kanal=kanal
    def tvac(self):
        if(self.tv=="acik"):
            print("tv acik")
        else:
            print("aciliyor tv...")
            self.tv="acik"
    def tvkapat(self):
        if(self.tv=="kapali"):
            print("tv zaten kapali")
        else:
            print("tv kapaniyor")
            self.tv="kapali"
    def ses(self):
        while True:
            cevap=input("tv ses ac> azalt< ")
            if(cevap=="<"):
                if(self.tvses!=0):
                    self.tvses-=1
                    print("ses",self.tvses)
            elif(cevap==">"):
                if(self.tvses!=30):
                    self.tvses+=1
                    print("ses",self.tvses)
            else:
                print("ses guncellendi",self.tvses)

    def kanalek(self,kanalis):
        print("kanal ekleniyor")
        time.sleep(1)
        self.kanali.append(kanalis)
        print("kanal eklendi")
    def rast(self):
        rastgele=random.randint(0,len(self.kanali)-1)
        self.kanal=self.kanali[rastgele]
        print("suanki kanal",self.kanal)
    def __len__(self):
        return len(self.kanali)
    def __str__(self):
        return "tv durumu{}\n tv ses{}\n kanal listesi{}\n suanki{}\n".format(self.tv,self.tvses,self.kanali,self.kanal)

kumanda=kumanda()
print("""

Televizyon Uygulaması


1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
""")
while True:
    islem=input("işlemi seçin")
    if(islem=="q"):
        print("cikiliuor")
        break
    elif(islem=="1"):
        kumanda.tvac()
    elif(islem=="2"):
        kumanda.tvkapat()
    elif(islem=="3"):
        kumanda.ses()
    elif(islem=="4"):
        kanalisim=input("girin kanal")
        kanalist=kanalisim.split(",")
        for eleman in kanalist:
            kumanda.kanalek()
    elif(islem=="5"):
        print("kanal sayisi",len(kumanda))
    elif(islem=="6"):
        kumanda.rast()
    else:
        print("geçersiz işlem...")