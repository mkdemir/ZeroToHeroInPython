"""
# Metodlar

Bugüne kadar Python'da birçok veri tipini gördük ve bu veri tipleri üzerinde bazı metodları kullandık. Aslında, bu veri tipleriyle oluşturulan her bir değişken Python'da bir nesne (object) olarak düşünülür ve Python geliştiricileri bu nesnelere birçok metod tanımlamıştır.

Metodlar, bir nesne üzerinde belirli işlemleri gerçekleştiren, o nesneye özgü fonksiyonlardır. Nesnelerin üzerinde metodlar aşağıdaki şekilde kullanılır:

`obje.herhangi_bir_metod(değerler(opsiyonel))`

Python'da metodlar, nesne yönelimli programlama paradigmalarında kullanılan önemli bir kavramdır. Bir nesne, bir sınıfın bir örneğidir ve bir sınıfın örneği olan nesneler, o sınıfın tanımladığı metodları kullanabilirler. Metodlar genellikle nesnenin durumunu değiştiren veya özelliklerini işleyen fonksiyonlardır.

Python'da metodlar, sınıfların içinde tanımlanır ve genellikle nesne üzerinde çağrılırlar. Bu şekilde nesnenin belirli bir işlem yapması sağlanır.
"""

liste = [1,2,3,4,5] # liste objesi oluşturdum.
print(type(liste))
liste.insert(1,"Mustafa")
print(liste)

liste.append("Python")
print(liste)

liste.pop()
print(liste)