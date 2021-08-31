import gtts
from playsound import playsound
from datetime import datetime
import random

sekarang = datetime.now()
time = sekarang.strftime("%H.%M.%S")
tanggal = sekarang.strftime("%d")
bulan = sekarang.strftime("%m")
tahun = sekarang.strftime("%Y")
nama = "Kintan Puti Alami"
default = [
  "au ah gelap"
]

# perlu pip3 install gTTS pyttsx3 playsound
# text to speech 

tts = gtts.gTTS("Halo Kintan", lang="id")
tts.save("halo.mp3")
playsound("halo.mp3")

# referensi https://www.thepythoncode.com/article/convert-text-to-speech-in-python


# list message
   
# Just Examples
# list jawaban untuk pertanyaan tentang nama
jawaban_nama = [
      "nama saya {0}".format(nama),
      "orang-orang memanggil saya {0}".format(nama),
      "panggil saja saya {0}".format(nama)
   ]

# Just Examples
# list jawaban untuk pertanyaan tentang tanggal
jawaban_tanggal = [
      "hari ini tanggal {0}".format(tanggal),
      "ya ampun masa tidak tahu, hari ini tanggal {0}".format(tanggal)
    ]
   
# Just Examples
# opsi pertanyaan yang bisa dijawab
pertanyaan = {
  "nama kamu siapa?": jawaban_nama,
  "kamu siapa?" : jawaban_nama,
  "tanggal berapa hari ini?": jawaban_tanggal,
  "hari ini tanggal berapa?" : jawaban_tanggal,
  "default": default
}

# Just Examples
# list jawaban untuk sebuah argument selain pertanyaan
statement =  [
                  'sangat senang',
                  'aku baik-baik saja',
                  'aku sangat bahagia hari ini'
              ]
   
# Just Examples tambahkan sesuai selera
# respon keseluruhan
responses = {
    'pertanyaan' : pertanyaan,
    'statement' : statement
}

# Task
# ----
# bot dapat membalas sapaan
# bot dapat memberikan informasi dirinya
# bot juga daapt menjawab beberapa informasi umum atau informasi yang anda inginkan
# bot menjawab dengan mencari pattern pada kalimat
# bot menjawab dengan kata yang tidak sama untuk setiap kalinya
# bot menjawab sesuai dengan senang atau tidak
# bot dapat menjawab dengan suara
# optional file suara setelah dipakai auto dihapus
# gunakan file ini sebagai module , buat file testing.py dan jalankan bot pada file testing.py
# bebas berkreasi :)
   
# Just Examples
def chatbot(message):
  respon1 = responses['pertanyaan']
  cerita = responses['statement']
  if 'siapa' in message:
    respon2 = random.choices(jawaban_nama)
    return (respon2)
  elif 'tanggal' in message:
    respon2 = random.choices(jawaban_tanggal)
    return (respon2)
  elif 'bagaimana kabarmu?' in message:
        return random.choices(cerita)
  else:
    return respon1['default']

def main():
  print ("Halo senang bertemu dengan kamu :)")
  print ("Kalau mau keluar tekan x ya")
  while True:
    q = str(input("Kamu mau tanya apa : "))
    if q == "x" :
      print("Sampai Jumpa :)")
      break
    a = chatbot(q)
    print (a)
    print ("============================")

if __name__ == "__main__" :
  main()
