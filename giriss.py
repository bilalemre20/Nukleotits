import re
import json

def valid_email(email):
    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(pattern, email))

def kayit_ol():
    print("Kayıt Olma Formu")
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")

    while True:
        email = input("E-posta Adresiniz: ")
        if valid_email(email):
            break
        else:
            print("Hata: Geçersiz e-posta formatı. Lütfen doğru bir e-posta adresi girin.")

    while True:
        sifre = input("Şifre (En az 8 karakter): ")
        sifre_tekrar = input("Şifreyi Tekrar Girin: ")

        if len(sifre) >= 8:
            if sifre == sifre_tekrar:
                user_info = {
                    "Ad": ad,
                    "Soyad": soyad,
                    "E-posta": email,
                    "Şifre": sifre  # Storing plain text password
                }

                with open("kullanicilar.json", "a") as json_file:
                    json.dump(user_info, json_file)
                    json_file.write('\n')

                break
            else:
                print("Hata: Şifreler eşleşmiyor. Tekrar deneyin.")
        else:
            print("Hata: Şifre en az 8 karakterden oluşmalı. Tekrar deneyin.")

    print("\nKayıt Başarılı!")
    print("Ad: ", ad)
    print("Soyad: ", soyad)
    print("E-posta: ", email)
    print("Şifre: ", sifre)

kayit_ol()

def giris_yap():
    print("\nGiriş Yapma Formu")
    while True:
        email = input("E-posta Adresiniz: ")
        sifre = input("Şifreniz: ")

        with open("kullanicilar.json", "r") as json_file:
            for line in json_file:
                user_info = json.loads(line)
                if user_info["E-posta"] == email and user_info["Şifre"] == sifre:
                    print("\nGiriş Başarılı!")
                    print("Hoş geldiniz, {} {}".format(user_info["Ad"], user_info["Soyad"]))
                    return

            print("\nHata: Giriş başarısız. Kullanıcı adı veya şifre hatalı. Tekrar deneyin.")

giris_yap()
