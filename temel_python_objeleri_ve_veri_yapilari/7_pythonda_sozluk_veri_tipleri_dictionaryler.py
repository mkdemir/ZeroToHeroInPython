"""
Sözlükler

Sözlüğün içindeki her bir eleman indeks ile değil, anahtar (key), değer (value) olarak tutulur. Bu anlamda gerçek hayattaki sözlüklere oldukça benzerler.

"""

# Sözlük Oluşturma

sozluk1 = {
    "bir": 1,
    "iki": 2,
    "üç": 3,
    "dört": 4,
    "beş": 5,
    "altı": 6,
    "yedi": 7
}
print(type(sozluk1))  # <class 'dict'>

# Boş bir sözlük oluşturma

# 1
sozluk2 = {}
print(type(sozluk2))
print(sozluk2)

# 2
sozluk2 = dict()
print(type(sozluk2))
print(sozluk2)

# Sözlük Değerlerine Erişmek ve Sözlüğe Değer Eklemek: Sözlük veritipinin gerçek hayattaki sözlüklere çok benzediğini söylemiştik. Öyleyse bir değeri (value) elde etmek için, indeksleri değil anahtarları (key) kullanacağız.
print(f"sozluk1['bir']: {sozluk1['bir']}")
try:
    print('sozluk1["on"]: {}'.format(sozluk1["on"]))
except KeyError as e:
    print(
        f"KeyError {e} hatası almaktayız nedeni ise böyle bir key'in sözlük içerisinde olmaması")

# Dinamik olarak eleman ekleme
sozluk1['sekiz'] = 8
print(f"sozluk1['sekiz']: {sozluk1}")

x = {
    "bir": [1, 2, 3, 4],
    "iki": [[1, 2], [3, 4], [5, 6], [7, 8]],
    "üç": [9, 10, 11, 12]
}

print(f'x["iki"] :{x["iki"]}')
print(f'x["iki"][1] :{x["iki"][1]}')
print(f'x["iki"][1][0] :{x["iki"][1][0]}')
print(sozluk1)

sozluk1["beş"] = 6
print(sozluk1["beş"])

uzun = {
    "sayılar": {
        "bir": 1,
        "iki": 2
    },
    "meyveler": {
        "kiraz": "yaz",
        "portakal": "kış"
    }
}
print(f"uzun['sayılar']['bir']: {uzun['sayılar']['bir']}")

# Temel Sözlük Metodları
yeni_sozluk = {
    "bir": 1,
    "iki": 2,
    "üç": 3
}
# dict_keys(['bir', 'iki', 'üç']), sadece sözlükteki anahtarları alır (Python bunu normal bir liste olarak kabul ediyor).
print(f'yeni_sozluk.keys(): {yeni_sozluk.keys()}')

# dict_values([1, 2, 3]), sadece sözlükteki değerleri alır.
print(f'yeni_sozluk.values(): {yeni_sozluk.values()}')

# 2 değeri tuple şeklinde alabiliriz.
# dict_items([('bir', 1), ('iki', 2), ('üç', 3), ('dört', 4), ('beş', 6), ('altı', 6), ('yedi', 7), ('sekiz', 8)]), python kendisine veri yapısı kurmuş bu veri yapısıda listeler içerisinde demetler olarak karşımıza çıkmış
print(sozluk1.items())

for k, v in sozluk1.items():
    print(k, v)
