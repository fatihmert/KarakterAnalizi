#-*- coding: cp1254 -*-

#DEVELOPER: Fatih Mert DOĞANCAN
#MAIL:      fatihmertdogancan@hotmail.com
#GITHUB:    @fatihmert

#KAYNAK:
#http://onedio.com/haber/isminize-gore-karakter-tahlili-340313

KARAKTER = {
    "a":[u"arzulu"],
    "b":[u"becerikli"],
    "c":[u"cana yakın"],
    "ç":[u"çapkın"],
    "d":[u"deli dolu",u"değişken"],
    "e":[u"elit",u"egolu"],
    "f":[u"farklı"],
    "g":[u"girişken",u"girişimci"],
    "h":[u"harbi",u"hayta",u"hayvan sever"],
    "ı":[u"ışıl ışıl"],
    "i":[u"inandırıcı"],
    "j":[u"janjanlı",u"jön"],
    "k":[u"kaprisli"],
    "l":[u"lakayit"],
    "m":[u"mert"],
    "n":[u"narsist",u"nazlı"],
    "o":[u"optimist",u"oyun bozan"],
    "ö":[u"özgün",u"özgür"],
    "p":[u"politik"],
    "r":[u"renkli",u"rengarenk"],
    "s":[u"sahtekar"],
    "ş":[u"şahsiyetli"],
    "t":[u"teknolojik"],
    "u":[u"utangaç",u"uslu"],
    "ü":[u"üstün zekalı"],
    "v":[u"vicdanlı",u"vicdansız"],
    "y":[u"yaramaz"],
    "z":[u"zarif"]
    }

import random
from PIL import Image, ImageDraw, ImageFont


def itemLength(i):
    return len(KARAKTER[i])

#RANDOM DICT VALUE LIST ITEM
def rastgele(itemLen):
    return random.randint(0,itemLen-1)

def hex2rgba(deger):
    return tuple(int(deger.lstrip('#')[i:i+2], 16) for i in range(0, 6, 2))+(1,)

ARKAPLAN_RENGI = hex2rgba("#e74c3c") #BACKGROUND_COLOUR
BOYUT = (1024,768) #SIZE
BASLIK = (230,8) #TITLE START COORDINATE
BASLIK_N = u"İSİME GÖRE KARAKTER ANALİZİ" #TITLE NAME
FONT_SIZE = 50
BASLANGIC_SOL = (130, 30 + FONT_SIZE + BASLIK[1]) #START COORDINATE
FONT_SIZE2 = 42
FONT_SIZE3 = 32


mainImg = Image.new("RGB",BOYUT,ARKAPLAN_RENGI)
cizimLayer = ImageDraw.Draw(mainImg) #DRAW LAYER
cizimFont = ImageFont.truetype("arial.ttf",FONT_SIZE)

harfFont = ImageFont.truetype("arial.ttf",FONT_SIZE2)
chrFont = ImageFont.truetype("arial.ttf",FONT_SIZE3)

#INIT FOR DRAW
mainImg.load()

#TITLE DRAW
cizimLayer.text(BASLIK,BASLIK_N,font=cizimFont,fill=hex2rgba('#ecf0f1'))

isim = raw_input("Isminizi girin: ").lower()

Y_BASLANGIC = 74
X_BASLANGIC = 160

for harf in isim:
    cizimLayer.text((X_BASLANGIC,Y_BASLANGIC),harf.upper(),font=harfFont,fill=hex2rgba('#ecf0f1'))
    for karakterOzellikHarf in KARAKTER[harf][rastgele(itemLength(harf))][1:]:
        Y_BASLANGIC += FONT_SIZE3 + 5
        cizimLayer.text((X_BASLANGIC,Y_BASLANGIC),karakterOzellikHarf.lower(),font=chrFont,fill=hex2rgba('#ecf0f1'))
    X_BASLANGIC += FONT_SIZE2 + 5
    Y_BASLANGIC = 74
    
mainImg.save('isle.jpg')
