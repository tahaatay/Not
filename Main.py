import os
import json
def show_menu():
    print("""
    -----------------------
    ---Hoşgeldin yarraam---
    -----------------------
    -------1:not yaz-------
    -----------------------
    -----2:notlara bak-----
    -----------------------
    -------3:not sil-------
    -----------------------
    ------4:Düzeltme-------
    -----------------------
    ---5:siktir olup git---
    -----------------------
    """)
def bilgi():
    if os.path.exists("notlar.json"):
     with open ("notlar.json","r") as json_file:
      data = json.load(json_file)
      return data
    else:
      print("dosya yok aq malı")
      data={}
      return data
def yazma(data):
  try:
    baslik=input("Başlığı giriniz")
    icerik=input("iceriği giriniz")
    if baslik in data:
        print("ULAN ZATEN BU NOT VAR PİÇ")
        return
    data[baslik]=icerik
    with open ("notlar.json","w") as json_file:
        json.dump(data,json_file)
    print("Bilgileriniz Allah izin verdiyse kaydedilmiştir"
        "\n eğer edilmemişse ilahi adalettir kodda hata yok!!!")
  except Exception as e:
      print(f"Dosyada hata var amk {e}")
def gosterme(data):
 try:
  if not data:
    print("Ulan köpek not yok neyi göstersin!")
    return

  print("\n----NOTLARINIZ----")
  for baslik,icerik in data.items():
    print(f"Baslik: {baslik} | icerik: {icerik}\n"+ "-" *20)
 except Exception as e:
     print(f"Dosyada hata var amk {e}")
def silme(data):
    try:
     if not data:
        print("Hangi notu sil biliyormusun amındaki notu sil göt")
        return
     else:
      gosterme(data)
      baslik = input("Başlığı giriniz")
      if baslik in data:
        del data[baslik]
        with open ("notlar.json","w") as json_file:
         json.dump(data,json_file)
      else:
         print("Mercimek geliyormu yanında menünün")
         return
    except Exception as e:
     print(f"Dosyada hata var amk {e}")
def duzeltme(data):
    if not data:
        print("Data yok!")
        return
    gosterme(data)
    baslik = input("Basliğı giriniz!")
    if baslik not in data:
       print("Öyle bir başlık yok!!")
       return
    elif baslik in data:
     yeni_icerik=input(f"Başlık {baslik} için yeni içeriği giriniz")
     data[baslik]=yeni_icerik
     try:
         with open ("notlar.json","w") as json_file:
          json.dump(data,json_file)
         print("Kaydedilmiştir herhalde 2 ye basıp kontrol et!")
     except Exception as e:
      print(f"Dosyada hata var amk {e}")
data=bilgi()
try:
    while True:

     show_menu()
     _=input("birini seç yoksa evine zurna döner gelir")
     if _=="1":
         yazma(data)
     elif _=="2":
         gosterme(data)
     elif _=="3":
        silme(data)
     elif _=="4":
        duzeltme(data)
     elif _=="5":
        break
     else:
        print("1 ile 5 amk 1 ile 5 arası aptal!!!\n")
except KeyboardInterrupt:
    print("\n")
    print("*"*25)
    print("PROGRAM ZORLA KAPATILDI! Çok cani bir insansın...")
    print("*"*25)