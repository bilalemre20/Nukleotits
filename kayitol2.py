import re
import hashlib
import json


def hash_sha256(sifre):
    hash_obj = hashlib.sha256(sifre.encode())
    return hash_obj.hexdigest()


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
                hashlenmis_sifre = hash_sha256(sifre)

                user_info = {
                    "Ad": ad,
                    "Soyad": soyad,
                    "E-posta": email,
                    "Hashlenmiş Şifre": hashlenmis_sifre
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
    print("Hashlenmiş Şifre: ", hashlenmis_sifre)

kayit_ol()

def giris_yap():
    print("\nGiriş Yapma Formu")
    while True:
        email = input("E-posta Adresiniz: ")
        sifre = input("Şifreniz: ")

        hashlenmis_sifre = hash_sha256(sifre)

        with open("kullanicilar.json", "r") as json_file:
            for line in json_file:
                user_info = json.loads(line)
                if user_info["E-posta"] == email and user_info["Hashlenmiş Şifre"] == hashlenmis_sifre:
                    print("\nGiriş Başarılı!")
                    print("Hoş geldiniz, {} {}".format(user_info["Ad"], user_info["Soyad"]))
                    return

            print("\nHata: Giriş başarısız. Kullanıcı adı veya şifre hatalı. Tekrar deneyin.")

giris_yap()
