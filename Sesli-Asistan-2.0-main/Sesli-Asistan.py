from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from playsound import *
from gtts import *
from speech_recognition import *
from datetime import *
import webbrowser
import time
import random 
import sys
import os


print("▌ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ▌")
print("▌ ███████████████████████  ▌")
print("▌   𝓔 𝓜 𝓘 𝓝   𝓚 𝓞 ℜ 𝓚 ∪ T  ▌")
print("▌ ███████████████████████  ▌")
print("▌ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▌")

print("")
print("")
print("")

print("▌ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ▌")
print("▌ ███████████████████████  ▌")
print("▌          𝓔𝓚-𝓢𝓐          ▌")
print("▌ ███████████████████████  ▌")
print("▌ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▌")

def konuşma (text) :
    tts=gTTS(text=text,lang="tr")
    file="cvp.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def selamlama() :
    saat=int(datetime.now().strftime("%H"))
    if 5<saat<=10 :
        konuşma("Günadyın Hoş Geldiniz")
    elif 10<saat<=20 :
        konuşma("İyi Günler Hoş Geldiniz ")
    elif 20<saat<=24 :
        konuşma("İyi Geceler Hoş geldiniz")
    else :
        konuşma("Uyumanız Gerekiyor")          

class asıl_pencere(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("𝓢𝓮𝓼𝓵𝓲 𝓐𝓼𝓲𝓼𝓽𝓪𝓷")
        self.setFixedSize(400,400)
        self.setStyleSheet("background-color : #cdcdc1")

        self.sesli_asistan_yazısı=QLabel("𝓔𝓚-𝓢𝓐 \n 𝓢𝓮𝓼𝓵𝓲 𝓐𝓼𝓲𝓼𝓽𝓪𝓷",self)
        self.sesli_asistan_yazısı.setFont(QFont("Ariel",15))
        self.sesli_asistan_yazısı.setGeometry(50,50,300,60)
        self.sesli_asistan_yazısı.setStyleSheet("border-radius : 5;border : 2px solid black")
        self.sesli_asistan_yazısı.setAlignment(Qt.AlignCenter)

        self.dinleme_butonu=QPushButton("🎙",self)
        self.dinleme_butonu.setGeometry(75,300,250,50)
        self.dinleme_butonu.setFont(QFont("Ariel",20))
        self.dinleme_butonu.setStyleSheet("border-radius : 5;border : 2px solid black")
        self.dinleme_butonu.setToolTip("Sesli Asistan İle Konuşmak İçin Tıklayınız")

        self.dinleme_butonu.clicked.connect(self.dinleme)

    def dinleme(self) :
        while True :
            print("Seni Dinliyorum ")
            r = Recognizer()
            with Microphone() as source :                     
                audio=r.listen(source)             
                voice=" "             
                try :                      
                    voice=r.recognize_google(audio,language="tr-TR")
                    self.close()
                    if "günaydın" in voice :
                        seçim=["Günaydınlar efendim","Günaydın canım","Günün aydın olsun","Seni gördüm Günüm Aydınlandı"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)   
                    if "Selam" in voice :
                        seçim=["Sana da selam olsun","Selamlar","Selam sana nasıl yardımcı olabilirim"]    
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "Merhaba" in voice :
                        seçim=["Sana da merhaba","merhabalar efendim","merhaba nasıl yardımcı olabilirim"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)   
                    if "nasılsın" in voice :
                        seçim=["Bi Yapay Zeka Her zaman iyidir dostum ","İyiyim sen nasılsın","Çok naziksin sen nasılsın","Ben iyiyim ama önemli olan sensin"]     
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "ne yapıyorsun" in voice :
                        seçim=["Seni bekliyordum sen ne yapıyorsun","Beni çalıştırmanı bekliyordum ","oturuyordum sen ne yapıyorsun"]    
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "ne haber" in voice :
                        seçim=["iyidir senden naber","İyi efendim"]    
                        seçim=random.choice(seçim)
                        konuşma(seçim)    
                    if "sesli asistan" in voice or "asistan" in voice:
                        seçim=["Biri bana mı seslendi","buyurun benim","hemen geliyorum    , geldim","efendim"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "adın ne" in voice or "adın nedir" in voice:
                        seçim=["EK SA asistan diyebilirsin"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)  
                    if "ne iş yapıyorsun" in voice :
                        seçim=["Şuanda bir sesli asistanım ","asistanlık yapıyorum","insanlara yardım ediyorum sen ne yapıyorsun"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "Aklından ne geçiyor" in voice or "ne düşünüyorsun" in voice  :
                        seçim=["Senin Bana Sorucağın Soruları Düşünüyordum","asistanlık yapıyorum","insanlara yardım ediyorum sen ne yapıyorsun"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "sıkıldım" in voice or "çok sıkıldım" in voice :
                        seçim=["İstersen Espiri yapabilirim","Seni eğlendirebilmek için ne yapabilirim"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "kötüyüm" in voice or "kendimi kötü hissediyorum" in voice :
                        seçim=["Çok üzüldüm Problem nedir","Üzülme geçicektir","Üzüldüm Senin için yapabileceğim bir şey varmı"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "iyiyim" in voice or "kendimi iyi hissediyorum" in voice :
                        seçim=["Çok mutlu oldum","çok sevindim ","Çok Mutlu Oldum Senin için yapabileceğim bir şey varmı"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "seni yapan kim" in voice or "seni kim yaptı" in voice :
                        konuşma("Emin Korkut Tarafından geliştirildim")  
                    if "espri yap" in voice or "espri yaparmısın" in voice :
                        seçim=["Bağırsak Kurtları bağırsakta yaşar bağırmasak ta .. ","Allah bana yürü kulum dedi , arabayı sattım"]  
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "Fıkra anlat" in voice or "Fıkra anlatırmısın" in voice :
                        seçim=["Bir gün Ela sınıftayken öğretmeni Ela'ya sormuş: 5 elma 7 portakal daha ne yapar? diye.Ela cevap vermiş: vitamin yapar öğretmenim demiş.","Yoldan Geçen Biri -Bunlar taze mi?, diye sormuş. Balıkçı: - Yok abla, pil takıp oynatıyoruz, demiş."]          
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "Pi'nin değeri kaçtır" in voice or "Pi'nin değeri nedir" in voice : 
                        konuşma("3,14159 dur")  
                    if "tekerleme söyle" in voice or "tekerleme söyler misin" in voice :
                        seçim=["Adem madene gitmiş.Adem madende badem yemiş.Madem ki Adem madende badem yemiş,Niye bize getirmemiş.","Şu yoğurdu nane ile birlikte sarımsaklasak da mı saklasak nane ile sarımsaklamasak da mı saklamasak Nanesiz sarımsaklasak da mı saklamasak?","İbibiklerin ibiklerini iyice iyileştirmek için İstinyeli istifçi İbiş´in istif istiridyeleri mi, yoksa, İskilipli İspinoz işportacı İshak´ın işliğindeki ibrişimleri mi daha iyi, bilemiyorum.","Şu köşe yaz köşesi, şu köşe kış köşesi, ortadaki su şişesi.","Dal sarkar kartal kalkar, kartal kalkar dal sarkar."]    
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "şaka yaptım" in voice or "şaka yapmıştım" in voice :
                        seçim=["Gülmekten devrelerim yandı ...","o kadar komikti ki gülmeyi unuttum"] 
                        seçim=random.choice(seçim)
                        konuşma(seçim)   
                    if "sus artık" in voice  :
                        konuşma("Bir daha ağzımı açmıyıcam")    
                    if "Özlü söz söyler misin?" in voice or "özlü söz söyle" in voice :
                        seçim=["Açıklamalarla vaktini harcama; İnsanlar sadece duymak istediklerini duyarlar.Paulo Coelho","Hayatta hep mutlu olursam, Hayalini kuracak neyim kalır. Dostoyevski","Yanında olduğum zaman değerimi bilmezsen, değerimi bildiğin gün beni yanında bulamazsın. Necip Fazıl Kısakürek"]                          
                        seçim=random.choice(seçim)
                        konuşma(seçim) 
                    if "dediklerimi tekrarla" in voice or "dekdiklerimi tekrarlar mısın" in voice :
                        konuşma("Tekrar etmemi istediğin şeyi söyle") 
                        r = Recognizer()
                        with Microphone() as source :                     
                            audio=r.listen(source)  
                            voice="" 
                            try :
                                voice=r.recognize_google(audio,language="tr-TR")
                                konuşma("{} dedin".format(voice))
                            except :
                                konuşma("Seni anlamadım")        
                    if "Gökyüzü neden mavi" in voice or "gökyüzü neden mavi" in voice :
                        konuşma("Güneş gökyüzünde yükseldiği zamanlarda Güneş'ten gelen kısa dalga boylu mavi ışık daha uzun dalga boylu renklere göre çok daha fazla saçılarak her yöne dağılır ve bu durum gökyüzünün mavi görünmesine sebep olur.")                  
                    if "Hangi gündeyiz" in voice or "Bugün günlerden ne" in voice  :
                        gün=time.strftime("%A")  
                        if gün=="Monday" :
                            konuşma("Pazartesindeyiz")
                        elif gün=="Tuesday" :
                            konuşma("Salıdayız")
                        elif gün=="Wednesday" :
                            konuşma("Çarşambadayız")    
                        elif gün=="Thursday" :
                            konuşma("Perşembedeyiz")
                        elif gün=="Friday" :
                            konuşma("Cumadayız") 
                        elif gün=="Saturday" :
                            konuşma("Cumartesindeyiz")
                        elif gün=="Sunday" :
                            konuşma("Pazardayız")      
                    if "saat kaç" in voice or "saati söyler misin" in voice :
                        saat=datetime.now().strftime("%H:%M")
                        konuşma("Saat Şuanda {}".format(saat))  
                    if "internette ara" in voice :
                        konuşma("Google de ne arayım")
                        print("Aramak İstediğinizi Söyleyiniz")
                        r = Recognizer()
                        with Microphone() as source :                     
                            audio=r.listen(source)  
                            voice="" 
                            try :
                                voice=r.recognize_google(audio,language="tr-TR")
                                url ="https://www.google.com.tr/search?q={}".format(voice)
                                webbrowser.get().open(url)
                                konuşma("{} İçin Google De Arama Yapıyorum".format(voice))
                            except :
                                konuşma("Google de Aramak İstediğini Anlamadım")
                    if "hava durumu" in voice or "hava nasıl" in voice :
                        konuşma("Hangi Şehrin Hava Durumunu İstersin")
                        print("Aramak İstediğiniz Şehrin Adını Söyleyiniz ")
                        r = Recognizer()
                        with Microphone() as source :                     
                            audio=r.listen(source)  
                            voice="" 
                            try :
                                voice=r.recognize_google(audio,language="tr-TR")
                                url ="https://mgm.gov.tr/?il={}".format(voice)
                                webbrowser.get().open(url)
                                konuşma("{} İçin Hava Durumuna Bakıyorum".format(voice))
                            except :
                                konuşma("Söylediğin Şehri Anlamadım ")
                    if "Wikipedia" in voice or "Wikipedia da ara" in voice :
                        konuşma("Wikipedia Da Ne Aramamı İstersin")
                        print("Wikipedia Da Aramak İstediğiniz Kelimeyi Söyleyiniz")
                        r = Recognizer()
                        with Microphone() as source :                     
                            audio=r.listen(source)  
                            voice="" 
                            try :
                                voice=r.recognize_google(audio,language="tr-TR")
                                url ="https://tr.wikipedia.org/wiki/{}".format(voice)
                                webbrowser.get().open(url)
                                konuşma("{} için Wikipedia Da Arama Yapıyorum".format(voice))
                            except :
                                konuşma("Maalesef Söylediğini anlamadım ")
                    if "haber aç" in voice or "haberler" in voice or "haberleri aç" in voice :
                        url ="https://www.ensonhaber.com/"
                        webbrowser.get().open(url)
                        konuşma("Haberleri Açıyorum")
                    if "müzik aç" in voice or "şarkı aç" in voice  :
                        konuşma("Youtube Müzik de ne aramamı istersiniz")
                        print("Youtube Müzik De Ne Aramak İstiyorsanız Söyleyiniz")
                        r = Recognizer()
                        with Microphone() as source :                     
                            audio=r.listen(source)  
                            voice="" 
                            try :
                                voice=r.recognize_google(audio,language="tr-TR")
                                url ="https://music.youtube.com/search?q={}".format(voice)
                                webbrowser.get().open(url)
                                konuşma("{} için Youtube Müzik De Arama Yapıyorum".format(voice))
                            except :
                                konuşma("Maalesef Söylediğini anlamadım")   
                    if "ders takvimini aç" in voice  or "dersleri aç" in voice  or "ders programını aç" in voice :
                        url= "http://www.capokul.com/ogrenci/egitim_takvimi.php"
                        webbrowser.get().open(url)
                        konuşma("Çap Okulu açıyorum") 
                    if "kendinden bahset" in voice or "kendini anlat" in voice :
                        seçim=["Python Dili Kullanılarak Yapıldım","Python Dili İle Hazırlanmış Kodlardan Oluşuyorum"]
                        seçim=random.choice(seçim)
                        konuşma(seçim) 
                    if "hangi dilleri biliyorsun" in voice or "başka bir dil biliyor musun" in voice :
                        seçim=["Sadece Türkçe Biliyorum","Türkçe hariç başka bir dil bilmiyorum"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "Kalbin var mı?" in voice or "kalbin var mı" in voice :
                        seçim=["Bir Yapay Zekanın kalbi yoktur ancak benim renk renk var :)","evet hemde renk renk"]    
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "versiyon" in voice :
                        seçim=["versiyon 2.0"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)      
                    if "beni arka planda dinlemeyi bırak" in voice or "dinlemeyi bırak" in voice :
                        seçim=["Tamamdır bırakıyorum, Dinleme Düğmesine basarak geri açabilirsin","Tamamdır Görüşürüz"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)   
                        break 
                    if "arka planda neden dinliyorsun" in voice or "neden sürekli dinliyorsun" in voice :
                        seçim=["Arka planda dinlemem senin söylediklerini daha iyi anlamam ve sürekli düğmeye tıklamaman için istersen kapatabilirsin"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "arka planda dinlemeni nasıl kapatabilirim" in voice or "arka planda dinlemeni nasıl kapatırım" in voice :
                        seçim=["Arka Planda Dinlememi kapatmak için arka planda dinlemeyi bırak diyebilirsin veya dinlemeyi bırak diyebilirsin"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)        
                    if "hayal kurar mısın" in voice  :
                        seçim=["Tabiki bi Yapay Zekada olsam Hayal Kurarım","Yapay Zekalar hayal kuramaz diye bi şey yok :)"]
                        seçim=random.choice(seçim)
                        konuşma(seçim) 
                    if "Neler yapabilirsin" in voice or "benim için neler yapabilirsin" in voice :
                        konuşma("Google de arama yapabilirim,Youtube Müzikte arama yapabilirim,Haberleri Açabilirim,Wikipedia da arama yapabilirim,hava durumuna bakabilirim ve seninle sohbet edebilirim")            
                    if "teşekkürler" in voice or "teşekkür ederim" in voice or "çok teşekkür ederim" in voice :
                        seçim=["Rica ederim her zaman","Senin için burdayım","Ne demek başka yardımcı olabiliceğim bir şey var mı"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "Aferim" in voice or "Aferin sana" in voice :
                        seçim=["Teşekkür ederim","her zaman en iyisi olmaya çalışıyorum"] 
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                    if "Görüşürüz" in voice or "görüşürüz" in voice :
                        seçim=["Gitmene Üzüldüm ama Sonra tekrar buluşalım","görüşürüz canım"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                        self.close()
                        break
                    if "Güle güle" in voice or "güle güle" in voice :
                        seçim=["Güle güle ...","güle güle efendim"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                        self.close()
                        break
                    if "Kendini kapat" in voice or "Uygulamayı kapat" in voice :
                        seçim=["Tamamdır kendine iyi bak","Bay bay efendim"]
                        seçim=random.choice(seçim)
                        konuşma(seçim)
                        self.close()
                        break

                except  :
                    konuşma("Maalesef Seni Anlıyamadım ")

uygulama=QApplication(sys.argv)
pencere=asıl_pencere()
pencere.show()
uygulama.exec()
