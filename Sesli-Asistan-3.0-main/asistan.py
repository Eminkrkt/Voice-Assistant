# Gerekli olan kütüphanelerimizi projeye dahil ediyoruz.
from speech_recognition import * ; from gtts import *
from playsound import * ; from datetime import *
from pyfiglet import Figlet ; import colorama ; import webbrowser
import time ; import time ; import random ; import os
from threading import Thread # Aynı anda birden fazla işlem yapabilmek için thread'ları kullanacağız.
import requests # İnternet bağlantısını kontrol etmek için kullanacağız.


colorama.init()

roman = Figlet(font='roman')
rectangles = Figlet(font='rectangles')
pawp = Figlet(font='pawp')

# Gerekli Olan Değişkenler Tanımlanır.
system_type = "win" # Default Windows Ayarlı.
username = None
age = None
internet_connection = True # İnternet bağlantısı olup olmadığını kontrol eden değişken.

# Windows sistemlerde bildirim gönderme fonksiyonu.
def notification(title,msg):
    if (system_type == "win"):
        try :
            from win10toast import ToastNotifier
        except ImportError:
            pass
        notifi = ToastNotifier()
        notifi.show_toast(title=title,msg=msg,duration=3)
    elif (system_type == "linux"):
        try :
            import subprocess
            from beepy import beep

            subprocess.run(
            ["notify-send", "-u", "normal", "-t", "4000",
            title, msg],
            check=True)
            beep(sound=1)
        except ImportError :
            pass

# Programın geliştirilebilmesi için duyulan sözcükler kayıt altına alınır.
def old_words_write(text):
    with open("old_words.txt","a",encoding="utf-8") as file :
        file.write(text)
        file.write("\n")
    file.close()

# Log dosyasına veri yazmak için kullan fonksiyon.
def data_write(new_user_name,new_age):
    global username,age
    with open("log.txt" , "a+" , encoding="utf-8") as file:
        file.truncate(0)
        if(new_user_name != username):
            file.write(new_user_name)
        else :
            file.write(username)
        if(new_age != age):
            file.write("\n{0}".format(new_age))
        else :
            file.write(age)
    file.close()

# Log dosyasından veri çekmek için kullanılan fonksiyon.
def data_read():
    global username,age
    with open("log.txt" , "a+" , encoding="utf-8") as file:
        try :
            username = (file.readline())
            username = username.replace('"'," ") # Tırnakdan kurtarıyoruz.
            age = (file.readline())
            age = age.replace('"'," ")# Tırnakdan kurtarıyoruz.
        except :
            assistant_event("Maalesef kullanıcı bilgisi bulunamadı !")
    file.close()

# Kullanıcı bilgileririn değiştiği fonksiyondur.
def change_user_information():
    print(colorama.Fore.RED)
    terminal_clear()
    print(rectangles.renderText('EK - SA'))
    word = "Kullanıcı adı ve yaşı değiştirilecek onaylıyor musunuz ? \n"
    assistant_event(word)
    wait(word)
    decision = input("İşlemi onaylıyor musunuz ? [E/H] ")
    if (decision == "e" or decision == "E"):
        word = "Yeni kullanıcı adını giriniz : "
        assistant_event(word)
        wait(word)
        new_user = input()
        word = "Yeni yaşı giriniz : "
        assistant_event(word)
        wait(word)
        new_age = input()
        word = "Kullanıcı adı : {0} \nYaş : {1} \nOnaylıyor musunuz ? \n".format(new_user,new_age)
        assistant_event(word)
        wait(word)
        decision2 = input("İşlemi onaylıyor musunuz ? [E/H] ")
        if(decision2 == "e" or decision2 == "E"):
            data_write(new_user,new_age)
            wait(word)
            notification("Bildirim","Kullanıcı adı ve yaşı sisteme kaydedildi.Programı yeniden başlatın.")
        elif(decision2 == "h" or decision2 == "H"):
            word = "İşlem kullanıcı tarafından iptal edildi"
            assistant_event(word)
            wait(word)
        else :
            word = "Maalesef yanlış bir veri girşi oldu"
            assistant_event(word)
            wait(word)
    elif (decision == "h" or decision == "H"):
        word = "İşlem kullanıcı tarafından iptal edildi"
        assistant_event(word)
        wait(word)
    else :
        word = "Maalesef yanlış bir veri girşi oldu"
        assistant_event(word)
        wait(word)

def internet_control():
    global internet_connection
    url = "https://www.google.com/"
    timeout = 5
    try :
        request = requests.get(url, timeout=timeout)
        internet_connection = True
    except (requests.ConnectionError, requests.Timeout) as exception:
        internet_connection = False


def computer_shutdown():
    print(colorama.Fore.RED)
    terminal_clear()
    print(rectangles.renderText('EK - SA'))
    word = "Bilgisayarınız 3 saniye içinde kapanıcaktır"
    assistant_event(word)
    wait(word)
    decision = input("\nİşlemi onaylıyor musunuz ? [E/H] ")
    if(decision == "e" or decision == "E"):
        word = "Bilgisayarınız 1 dakikadan az süre içinde kapanacaktır."
        assistant_event(word)
        wait(word)
        if(system_type == "win") :
            os.system("shutdown -s") # Bilgisayarın kapanması için gerekli olan komut
        elif (system_type == "linux") :
            os.system("sudo shutdown now") # Linux bilgisayarın kapanması için gerekli komut,Kullanıcı şifresi gerektirir.
    elif(decision == "h" or decision == "H"):
        word = "İşlem kullanıcı tarafından iptal edildi"
        assistant_event(word)
        wait(word)
    else :
        word = "Yanlış bir veri girişi oldu"
        assistant_event(word)
        wait(word)

def computer_restart():
    print(colorama.Fore.RED)
    terminal_clear()
    print(rectangles.renderText('EK - SA'))
    word = "Bilgisayarınız 3 saniye içinde yeniden başlatılacak"
    assistant_event(word)
    wait(word)
    decision = input("\nİşlemi onaylıyor musunuz ? [E/H] ")
    if(decision == "e" or decision == "E"):
        word = "Bilgisayarınız 1 dakikadan az süre içinde yeniden başlatılacak."
        assistant_event(word)
        wait(word)
        if(system_type == "win") :
            os.system("shutdown -r") # Bilgisayarın kapanması için gerekli olan komut
        elif (system_type == "linux") :
            os.system("sudo shutdown -r now") # Linux bilgisayarın kapanması için gerekli komut,Kullanıcı şifresi gerektirir.
    elif(decision == "h" or decision == "H"):
        word = "İşlem kullanıcı tarafından iptal edildi"
        assistant_event(word)
        wait(word)
    else :
        word = "Yanlış bir veri girişi oldu"
        assistant_event(word)
        wait(word)

# İşletim Sistemi Tanıma Fonksiyonu
def system_recognition():
    global system_type
    if(os.name == 'nt'):
        system_type = "win"
    elif(os.name == 'posix'):
        system_type = "linux"
  
# Konuşma Fonksiyonu.
def assistant_speech(text):
    tts = gTTS(text = text , lang='tr')
    file = "speek.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

# Yazma Fonksiyonu.
def assistant_write(text):
    for x in text:
        print(x,end='',flush=True)
        time.sleep(0.08)

# Programın hataya düşmemesi için bekleme fonksiyonu.
def wait(word):
    word_len = len(word)
    if(word_len >35):
        time.sleep(5.1)
    elif(word_len >30):
        time.sleep(4.7)
    elif(word_len >25):
        time.sleep(4.2)
    elif(word_len >20):
        time.sleep(3.5)
    elif(word_len >15):
        time.sleep(2.7)
    elif(word_len >10):
        time.sleep(2.4)
    elif(word_len >5):
        time.sleep(1.7)
    
# Kullanıcıdan alınan sesin ekrana ekrana yazıdırıldığı fonksiyon.
def user_write(text):
    text = text.capitalize() # Gelen verinin ilk harfini büyük yaparız.
    print("\n","                                           {0}".format(text))

# Terminal temizleme fonksiyonu.
def terminal_clear():
    if(system_type == 'linux'):
        os.system('clear')
    elif(system_type == 'win'):
        os.system('cls')

# Selamlama fonksiyonu,Program ilk çalışığında 1 kere çalışır.
def greeting():
    notification("Bildirim","EK-SA asistan hazır.")
    global username,age
    print(colorama.Fore.CYAN)
    terminal_clear()
    print(pawp.renderText('EK - SA'))
    word = "Merhaba ben bir sesli asistanım ,Size yardım etmek için buradayım."
    assistant_event(word)
    wait(word)

    if((username is None) or (age is None)):
        word = "\nKullanıcı bilgisi bulunamadığı için kayıt olmanız gerekiyor."
        assistant_event(word)
        wait(word)
        change_user_information()
    
# Threadlerin görevleri belirtilir.
def thread_write_fun(text):
    thread_write = Thread(target=assistant_write,args=(text,))
    thread_write.start()
def thread_speech_fun(text):
    thread_write = Thread(target=assistant_speech,args=(text,))
    thread_write.start()

# Asistanın olaylarının gerçekleştiği asıl fonksiyondur.
def assistant_event(text):
    thread_speech_fun(text)
    time.sleep(0.66)
    thread_write_fun(text)

# Asistanla-Kullanıcı arasında geçen konuşmaların olduğu bölüm.
def listening():
    while True :
        print(colorama.Fore.CYAN)
        terminal_clear()
        assistant_event("Sizi dinliyorum")
        time.sleep(1.5) # Asistanın lafı bitmeden dinleme olayına geçmemek için 1.5 saniye bekletilir.
        r = Recognizer()
        with Microphone() as source :                     
            audio=r.listen(source)             
            voice=" "             
            try :
                voice=r.recognize_google(audio,language="tr-TR")
                user_write(voice)
                old_words_write(voice)
                voice = voice.lower()
                if "günaydın" in voice or "günaydın asistan" in voice:
                    word = ["Günaydınlar efendim","Günaydın Efendim"]
                    word = random.choice(word)
                    assistant_event(word)
                    wait(word)
                if "tünaydın" in voice or "tünaydın asistan" in voice :
                    word = ["Tünaydınlar efendim","Tünaydın Efendim"]
                    word = random.choice(word)
                    assistant_event(word)
                    wait(word)
                if "selam" in voice or "selamlar" in voice:
                    word = ["Selam efendim","Selamlar"]
                    word = random.choice(word)
                    assistant_speech(word)
                    wait(word)
                if "merhaba" in voice or "merhabalar" in voice:
                    word=["Sana da merhaba","Merhabalar efendim","Merhaba nasıl yardımcı olabilirim"]
                    word=random.choice(word)
                    assistant_event(word)
                    wait(word) 
                if "nasılsın" in voice or "iyi misin" in voice :
                    word=["İyiyim sen nasılsın","İyi ,siz nasılsınız"]     
                    word=random.choice(word)
                    assistant_event(word)
                    wait(word)
                if "ne haber" in voice :
                    word=["İyidir sizden naber","İyi efendim"]    
                    word=random.choice(word)
                    assistant_event(word) 
                    wait(word)
                if "adın ne" in voice or "adın nedir" in voice:
                    word="EK-SA asistan diyebilirsin"
                    assistant_event(word)
                    wait(word)
                if "sesli asistan" in voice or "asistan" in voice:
                    word=["Buyurun benim","Efendim ..."]
                    word=random.choice(word)
                    assistant_event(word)
                    wait(word)
                if "seni yapan kim" in voice or "seni kim yaptı" in voice or "yapımcının kim" in voice:
                    word = "Emin Korkut tarafından geliştirildim"
                    assistant_event(word)
                    wait(word)
                if "benim adım ne" in voice or "benim yaşım kaç"in voice or "kullanıcı bilgileri" in voice :
                    data_read()
                    word = "{0} adınız {1} yaşınız sisteme kayıtlıdır.".format(username,age)
                    assistant_event(word)
                    wait(word)
                if "bilgilerimi değiştir" in voice or "kullanıcı bilgilerini değiştir" in voice or "bilgileri değiştir" in voice or "bilgilerimi sıfırla" in voice:
                    word = "Hemen yönlendiriyorum"
                    assistant_event(word)
                    wait(word)
                    change_user_information()
                    break    
                if "dediklerimi tekrarla" in voice or "dekdiklerimi tekrarlar mısın" in voice :
                    assistant_event("Tekrar etmemi istediğin şeyi söyle") 
                    time.sleep(2.3)
                    r = Recognizer()
                    with Microphone() as source :            
                        audio=r.listen(source)  
                        voice="" 
                        try :
                            voice=r.recognize_google(audio,language="tr-TR")
                            user_write("'{0}'".format(voice))
                            assistant_event("{0} dedin".format(voice))
                            wait(voice)
                            time.sleep(1.2) # Hataya düşmemek için ek süre
                        except :
                            assistant_event("Seni anlamadım") 
                            time.sleep(1.7)

                if "wikipedia" in voice or "wikipedia da ara" in voice :
                    assistant_event("Wikipedia da ne aramamı istersin")
                    time.sleep(2.7)
                    r = Recognizer()
                    with Microphone() as source :                     
                        audio=r.listen(source)  
                        voice="" 
                        try :
                            voice=r.recognize_google(audio,language="tr-TR")
                            user_write(voice)
                            word = "{} için Wikipedia da arama yapıyorum".format(voice)
                            assistant_event(word)
                            url ="https://tr.wikipedia.org/wiki/{}".format(voice)
                            webbrowser.get().open(url)
                            wait(word)
                        except :
                            word = "\nMaalesef Söylediğini anlamadım"
                            assistant_event(word)
                            wait(word)
                if "internette ara" in voice or "google'da ara" in voice or "chrome'da ara" in voice or "web'de ara" in voice or "İnternet'te arama yap" in voice:
                    assistant_event("Google de ne arayım")
                    time.sleep(2.1)
                    r = Recognizer()
                    with Microphone() as source :                     
                        audio=r.listen(source)  
                        voice="" 
                        try :
                            voice=r.recognize_google(audio,language="tr-TR")
                            user_write(voice)
                            word = "{} İçin Google De Arama Yapıyorum".format(voice)
                            assistant_event(word)
                            url ="https://www.google.com.tr/search?q={}".format(voice)
                            webbrowser.get().open(url)
                            wait(word)
                        except :
                            word = "\nGoogle de Aramak İstediğini Anlamadım"
                            assistant_event(word)
                            wait(word)
                if "youtube aç" in voice or "youtube" in voice or "youtube açar mısın" in voice:
                    assistant_event("Youtube da ne aramamı istersiniz")
                    time.sleep(2.6)
                    r = Recognizer()
                    with Microphone() as source :                     
                        audio=r.listen(source)  
                        voice="" 
                        try :
                            voice=r.recognize_google(audio,language="tr-TR")
                            user_write(voice)
                            word = "{} için Youtube Müzik De Arama Yapıyorum".format(voice)
                            assistant_event(word)
                            url ="https://youtube.com/search?q={}".format(voice)
                            webbrowser.get().open(url)
                            wait(word)
                        except :
                            word = "\nMaalesef Söylediğini anlamadım"
                            assistant_event(word)
                            wait(word)  
                if "instagram aç" in voice or "instagram" in voice:
                    word = "İnstagramı açıyorum."
                    assistant_event(word)
                    wait(word)
                    url = "https://www.instagram.com/"
                    webbrowser.get().open(url)
                    time.sleep(2)



                if "saat kaç" in voice or "saati söyler misin" in voice :
                    saat=datetime.now().strftime("%H:%M")
                    assistant_event("Saat Şuanda {}".format(saat))
                    wait("Saat şuan 00:00")
                if "hangi gündeyiz" in voice or "bugün günlerden ne" in voice  :
                    day=time.strftime("%A")  
                    if day=="Monday" :
                        assistant_event("Pazartesindeyiz")
                        wait("Pazartesindeyiz")
                    elif day=="Tuesday" :
                        assistant_event("Salıdayız")
                        wait("Salıdayız")
                    elif day=="Wednesday" :
                        assistant_event("Çarşambadayız")    
                        wait("Çarşambadayız")
                    elif day=="Thursday" :
                        assistant_event("Perşembedeyiz")
                        wait("Perşembedeyiz")
                    elif day=="Friday" :
                        assistant_event("Cumadayız") 
                        wait("Cumadayız")
                    elif day=="Saturday" :
                        assistant_event("Cumartesindeyiz")
                        wait("Cumartesindeyiz")
                    elif day=="Sunday" :
                        assistant_event("Pazardayız")     
                        wait("Pazardayız")

      
                if "teşekkürler" in voice or "teşekkür ederim" in voice or "çok teşekkür ederim" in voice :
                    word=["Rica ederim her zaman","Senin için burdayım"]
                    word=random.choice(word)
                    assistant_event(word)
                    wait(word)
                # Kapatma Olayları
                if "görüşürüz" in voice :
                    word=["Görüşürüz efendim","Görüşürüz"]
                    word=random.choice(word)
                    assistant_event(word)
                    wait(word)
                    notification("Bildirim","EK-SA asistan kapatıldı.")
                    break
                if "güle güle" in voice or "bay bay" in voice:
                    word=["Güle güle","Güle güle efendim","Bay bay","Bay bay efendim"]
                    word=random.choice(word)
                    assistant_event(word)
                    wait(word)
                    notification("Bildirim","EK-SA asistan kapatıldı.")
                    break
                if "kendini kapat" in voice or "uygulamayı kapat" in voice :
                    word=["Tamamdır kendine iyi bak","Bay bay efendim"]
                    word=random.choice(word)
                    assistant_event(word)
                    wait(word)
                    notification("Bildirim","EK-SA asistan kapatıldı.")
                    break                     

                # Bilgisayar İşlemleri
                if "bilgisayarı kapat" in voice or "bilgisayar kapat" in voice :
                    word = "Hemen yönlendiriyorum"
                    assistant_event(word)
                    wait(word)     
                    computer_shutdown()
                    break    
                if "bilgisayarı yeniden başlat" in voice or "bilgisayar yeniden başlat" in voice :
                    word = "Hemen yönlendiriyorum"
                    assistant_event(word)
                    wait(word)     
                    computer_restart()
                    break 

            except UnknownValueError:
                terminal_clear()
                word = "Maalesef sizi anlamadım"
                assistant_event(word)
                wait(word)
            except RequestError:
                terminal_clear()
                word = "Maalesef İnternet Bağlantısı Kurulamadı"
                assistant_event(word)
                wait(word)
                notification("Bildirim","EK-SA asistan internet bağlantısı olmadığı için kapatıldı.")
                break

# Programın başlaması .

internet_control()
system_recognition() # Terminalin temizlenmesi için işletim sistemi tanınır.
if(internet_connection == True):
    terminal_clear()
    try :
        data_read()
        greeting()
        time.sleep(6.5) # Programın hataya düşmemesi için selamlama fonksiyonun bitmesi beklenir.
        listening()
    except RequestError :
        thread_write_fun("Maalesef internet bağlantısı bulumadı.")
else :
    notification("Bildirim","EK-SA asistan internet bağlantısı olmadığı için açılmadı.")
    