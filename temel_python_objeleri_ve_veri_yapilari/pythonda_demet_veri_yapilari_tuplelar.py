"""
Demetler (Tuplelar):

Demetler veya ingilizce ismiyle tuplelar listelere oldukça benzer ancak farkları demetlerin değiştirilemez oluşudur. Bu yüzden programlarımızda değiştirilmesini  istemediğimiz değerleri bir demek içinde depolayabiliriz. İsterseniz konumuza demetlerin oluşturulmasıyla başlayalım.

- Demetler read only (Sadece Okuma) bir veri tipi olduğundan listelere göre biraz daha hızlı çalışırlar.
"""

# Demet Oluşturma

# Demet elemanları parantez içine alınarak demet oluşturulabilir.
demet = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print('demet: {}'.format(demet))
print(f'{type(demet)}')
print(f'{demet[-1]}')
print(demet[:4])
print(demet[::-1])

# Demetlerin Temel Metodları
# Index metoduyla için verdiğimiz elemanın hangi indekste olduğunu bulabilirsiniz (Demetlerin yanlızca 2 metodu bulunuyor).

demet2 = (1, 2, 3, 4, 1, 6, 7, 8, 9)
# count fonk. demetin içersinde kaç tane "1" geçiyor ona bakıyor.
print(f"demet2.count(1): {demet2.count(1)}")

demet3 = ("Python", "Php", "C", "Java")
# index fonk. "Python" string'inin hangi index'te olduğunu söylüyor eğer varsa.
print(f'demet3.index("Python"): {demet3.index("Python")}')

# Değiştirişmeme Özelliği: Demetlerin değiştirilemez olduğunu artık biliyoruz.

demet = (1, 2, 3, 4, 5)
# demet[-1] = "x" # TypeError: 'tuple' object does not support item assignment (Hatasını aldık).
