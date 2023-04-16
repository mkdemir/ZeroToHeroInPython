"""
Stringler: Bu veri tipi aslında her bir karakter olan bir dizidir.

Örnek: ali stringini düşünecek olursak. "a", "l", "i" harflerinden veya karakterlerinden oluşmaktadır.
"""

# String Oluşturma

# Tek Tırnak ile
'mkdemir'

# Çift Tırnal ile
"mkdemir"

# 3 Tırnak ile
"""mkdemir"""

print("Mustafa'nın bugün dersi var.")
# Python'da bulunan kaçış dizileri vardır.
print("Mustafa\'nın bugün dersi var.")

isim = 'Mustafa'
print(isim)

"""
String Indeksleme ve Parçalama:
    - ali stringinde a,l,i karakterlerinin yerleri indeks olarak adlandırılır. Pythonda ve genellikle çoğu programlama dilinde (Octave hariç) stringlerin indekslenmesi "0" dan başlamaktadır. 
"""

# Indeksleme:

# 0. elemana ulaşalım. Bunun için [] operatörünü kullanacağız.
a = 'ali'
print(f'a[0]: {a[0]}')
print(f'a[1]: {a[1]}')
print(f'a[1]: {a[2]}')

# Python'da stringler baştan olduğu gibi sondan da indekslenebilirler. Sondan başlayarak -1, -2.. şeklinde indeksleniriler.
metin = 'mkdemir'
print(f'metin[-1]: {metin[-1]}')
print(f'metin[-2]: {metin[-2]}')
print(f'metin[-3]: {metin[-3]}')
print(f'metin[-4]: {metin[-4]}')
print(f'metin[-5]: {metin[-5]}')
print(f'metin[-6]: {metin[-6]}')
print(f'metin[-7]: {metin[-7]}')

# Parçalama: [başlama indeksi : bitiş indeksi : atlama değeri]
yazi = 'Python Programlama Dili'

# 4. indeskten başla 10. indekse kadar (dahil değil) al.
print(f'yazi[4:10]: {yazi[4:10]}')

# Başlangıç değeri belirtilmemişse en baştan başlayarak alır.
print(f'yazi[:10]: {yazi[:10]}')

# Bitiş değeri belirtilmemişse en sonuna kadar alır.
print(f'yazi[4:]: {yazi[4:]}')

# İki değer de belirtilmemişse tüm stringi al.
print(f'yazi[:]: {yazi[:]}')

# Son karaktere kadar al.
print(f'yazi[:-1]: {yazi[:-1]}')

# Baştan sona 2 değer atlaya atlaya stringi al.
print(f'yazi[::2]: {yazi[::2]}')

# Başta sona 2 değer atlaya atlaya stringi al.
print(f'yazi[4:12:2]: {yazi[4:12:2]}')

# Baştan sona -1 atlayarak stringi ak. (String'i ters çevirme)
print(f'yazi[::-1]: {yazi[::-1]}')

# String Özellikleri

# Bir stringin uzunluğunu bulma
uzun_metin = 'Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 1500\'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır. Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek değişmeden elektronik dizgiye de sıçramıştır. 1960\'larda Lorem Ipsum pasajları da içeren Letraset yapraklarının yayınlanması ile ve yakın zamanda Aldus PageMaker gibi Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler olmuştur.'
# Toplam -> 590 tane karakter var.
print('len(uzun_metin): {}'.format(len(uzun_metin)))

string = 'Merhaba'
# string[3] = 't' # TypeError: 'str' object does not support item assignment (Sen bir objeyi assignment edemezsin karakteri değiştiremezsin) yani bir bir stringi direk olarak değiştiremiyoruz.

# Stringleri Toplama
a = 'Python '
b = 'Programlama '
c = 'Dili'
print(f'a + b + c: {a+b+c}')

print('Python ' * 3)  # Stringi çarpma

# Mülakatlarda Çıkıyor.
a = 'Mustafa '
a = a + 'Kaan'
print(f'a = a + "Kaan" : {a}')
