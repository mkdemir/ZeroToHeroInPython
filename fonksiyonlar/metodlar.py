"""
# Metodlar

Şimdiye kadar Pythonda kullanabildiğimiz bir çok veri tipi gördük ve bazı veritipleri üzerinde bu veritiplerinin metodlarını kullandık. Aslında bu veritiplerin oluşturulan her bir değişken Pythonda obje( object) olarak düşünülür ve Python geliştiricileri bu objelere birçok metod tanımlamıştır.

Metodlar bir obje üzerinde belli işlemleri gerçekleştiren objelere özgü fonksiyonlardır ve objelerin üzerinde metodlar şu şekilde kullanılır.

obje.herhangi_bir_metod(değerler(opsiyonel)) 

Python'da metodlar, nesnelerin - obje (object) üzerinde çalışan ve belli bir işlevi yerine getiren fonksiyonlardır. Bir nesne, bir sınıfın bir örneğidir ve bir sınıfın örneği olan nesneler, o sınıfın tanımladığı metodları kullanabilirler. Metodlar, nesnel programlama paradigmalarında kullanılan önemli bir kavramdır.

Python'da metodlar, sınıfların içerisinde tanımlanır ve genellikle nesnenin durumunu değiştiren veya özelliklerini işleyen fonksiyonlardır. Sınıfın içinde tanımlanan metodlar, nesne üzerinde çağrılabilir ve bu şekilde nesnenin belirli bir işlem yapması sağlanır.

"""

liste = [1,2,3,4,5] # liste objesi oluşturdum.
print(type(liste))
liste.insert(1,"Mustafa")
print(liste)

liste.append("Python")
print(liste)

liste.pop()
print(liste)