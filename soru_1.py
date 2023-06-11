from collections import defaultdict
import io
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import Counter
from zemberek import (
    TurkishMorphology,
)
import os
import pandas as pd
import matplotlib.pyplot as plt

# Stop words kelimeleri değişkene aktarır
stop_words_tr = []    
file=io.open("./stop-words_turkish_1_tr.txt", mode="r", encoding="utf-8")
for read in file.readlines():
     text = read.split("\n")
     text = ''.join(text)
     stop_words_tr.append(text)

# # Alt sayfaları bulur
# base_url = "https://www.deu.edu.tr/"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
# }

# # Ana sayfanın HTML içeriğini getirir
# response = requests.get(base_url, headers=headers)
# html_content = response.text

# soup = BeautifulSoup(html_content, "html.parser")

# # Tüm a etiketlerini bulur
# links = soup.find_all("a")

# # Alt URL'leri depolamak için bir liste oluşturur
# sub_urls = list()

# # Her bir link için alt URL'yi bulur ve listeye ekler
# for link in links:
#     href = link.get("href")
#     if href:
#         absolute_url = urljoin(base_url, href)

#         # İçinde edu bulunmayan ve pdf uzantılı olan url'leri filtreler
#         filter = str(absolute_url).replace("."," ")
#         if "edu" in filter and "pdf" not in filter:
#             sub_urls.append(absolute_url)


# # Text dosyalarının isimleri için oluşturuldu
# index = 0
# for sub_url in sub_urls:
#    try:
#         index += 1 
       
#         # Web sayfasından içeriği alır
#         headers = {
#             "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
#             }
#         response = requests.get(sub_url,headers=headers)
#         content = response.text

#         # HTML etiketlerini kaldırır ve metni düzeltir
#         soup = BeautifulSoup(content, 'html.parser')
#         text = soup.get_text()

#         # Metni küçük harfe çevirir, sayıları temizler ve noktalama işaretlerini temizler
#         text = text.lower()
#         text = re.sub(r'[^\w\s]', '', text)
#         text = re.sub(r'\d+', '', text)

#         # Kelimeleri köklerine ayırır
#         morphology = TurkishMorphology.create_with_defaults()
#         words = text.split()
        
#         # Sitelerden kelimleri ayıklama uzun sürdüğü için stop words'lardan temizlediğim ve zemberek ile köklerine ayırdığım  kelimleri text dosyasına kaydeder
#         file = open(f"./Words/{index}.txt", "w")
#         for word in words:
#             results = morphology.analyze(word)
#             for result in results:
#                 if result.get_stem() not in stop_words_tr:
#                     file.write(result.get_stem() + "\n")
#         file.close()    
                    
#    except Exception as e:
#        print(e)
#        index -= 1
#        pass



# Kelimeleri gerekli listelere aktarır
all_words = list()
words_of_pages= defaultdict(int)
index2=0
with os.scandir(f"./Words") as tarama:
    for belge in tarama:   
        index2 += 1
        file = open(f"./Words/{index2}.txt", "r")
        
        temp=list()
        for line in file:
            text = file.readline()
            text=text.split('\n')[0]
                        
            # Stop words'lerde eklemeler yaptım bu yüzden tekrar filtreleme yaparak ekledim
            if text not in stop_words_tr:
             all_words.append(text)
             temp.append(text)
             
        
        words_of_pages[index2]=temp
        

# Kelimelerin frekanslarını hesaplar
number_of_word = Counter(all_words)


sorted_dict = dict(sorted(number_of_word.items(), key=lambda x: x[1],reverse=True))

how_many_different_pages = defaultdict(str)
for word in sorted_dict.keys():
    count=0
    for page in range(1,len(words_of_pages)):
        if word in words_of_pages[page]:
            count+=1    
    how_many_different_pages[word] = count     

# Verileri dataframe'e dönüştürür
data = {
    'Sözcük': sorted_dict.keys(),
    'Frekans': sorted_dict.values(),
    'Web_sayfasi': how_many_different_pages.values(),
}

# Verileri kullanarak bir DataFrame oluşturun
df = pd.DataFrame(data)

df.to_csv("./sonuc.csv", encoding='utf-8-sig', index=False)


# İlk 100 kelime için verileri seçme
df_top_100 = df.head(100)

# Sözcük-Frekans grafiği
plt.figure(figsize=(12, 6))
plt.bar(df_top_100['Sözcük'], df_top_100['Frekans'])
plt.xticks(rotation=90)
plt.xlabel('Sözcük')
plt.ylabel('Frekans')
plt.title('İlk 100 Sözcüğün Frekansları')
plt.tight_layout()
plt.show()

# Sözcük-Web Sayfası grafiği
plt.figure(figsize=(12, 6))
plt.bar(df_top_100['Sözcük'], df_top_100['Web_sayfasi'])
plt.xticks(rotation=90)
plt.xlabel('Sözcük')
plt.ylabel('Web Sayfası Sayısı')
plt.title('İlk 100 Sözcüğün Geçtiği Web Sayfalarının Sayısı')
plt.tight_layout()
plt.show()