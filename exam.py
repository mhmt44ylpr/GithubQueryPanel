import requests
import json

class GITHUB(object):
    def __init__(self):
        self.url = "https://api.github.com/users"

    def Sorgu(self,kullanıcı_adı):
        k_S = self.url + "/" + kullanıcı_adı
        k_sr = requests.get(k_S)
        js = json.loads(k_sr.text)
        txt = f"Adı: {js["login"]} , Repositories {js["public_repos"]} , Takip : {js["following"]}"
        return txt

    def Repos(self,kullanıcı_adı):
        res = requests.get(f"https://api.github.com/users/{kullanıcı_adı}/repos")
        res = res.json()
        num = 1
        for i in res:
            print(f"{num} - ",i["name"])
            num += 1

    def ReposAdd(self,token,name,read):

        new_url = f"https://api.github.com/user/repos"
        headers =  {"Authorization": f"token {token} "}
        data = {"name" : f"{name}",
                "description" : f"{read}"}

        res = requests.post(new_url, headers=headers, json=data)

        print("Repo Olşuturldu")
github = GITHUB()

while True:
    print("1-Kullanıcı Sorgu\n2-Kullanıcıya dair repositories\n3-Repositories Ekle\n4-Çıkış")
    sec = input("Seçiminiz: ")

    if sec == "4":
        break
    else:
        if sec == "1":
            kullanıcı_adı = input("Kullanıcı Adı: ")
            islem = github.Sorgu(kullanıcı_adı)
            print(islem)
        elif sec == "2":
            kullanıcı_adı = input("Kullanıcı Adı: ")
            github.Repos(kullanıcı_adı)
        elif sec == "3":
            token = input("Token: ")
            isim = input("Isim: ")
            yorum = input("Yorum: ")
            github.ReposAdd(token = token,
                            name=isim,
                            read=yorum)
        else:
            print("Yanlış Seçim ...")