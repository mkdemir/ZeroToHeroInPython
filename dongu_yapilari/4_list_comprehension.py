"""
# Liste Kapsamı (List Comprehension)

Bu konuda, Pythonda listeleri üretmek ve oluşturmak için oldukça pratik bir yöntem olan "List Comprehension" konusunu öğreneceğiz. Biliyorsunuz, Python'da birçok işi kısa kodlarla halledebiliyoruz. Ancak kodları daha da kısaltmak ve pratik yöntemler kullanmak her zaman tercih edilir. Şimdi, öğreneceklerimizle list comprehension'ı anlamaya çalışalım.
"""

# Listelerdeki append metodunu hatırlayalım.
liste = [1,2,3,4]
liste.append(5)
print(liste)

####

liste1 = [1,2,3,4,5]
liste2 = list() # Boş bir liste oluşturduk.

for i in liste1:
    liste2.append(i)
print(liste2)

# List comprehension

liste3 = [1,2,3,4,5]
liste4 = [i for i in liste3]
print(liste4)


liste = [3,4,5]
liste1 = [i*2 for i in liste]
print(liste1)


liste = [(1,2),(3,4),(5,6)]
liste1 = [i*j for i,j in liste]
print(liste1)


s = "Python"
liste1 = [i*3 for i in s]
print(liste1)


liste = [[1,2,3], [4,5,6,7,8], [9,10,11,12,13,14,15]]
liste1 = list()

for i in liste:
    for x in i:
        liste1.append(x)
print(liste1)


liste = [[1,2,3], [4,5,6,7,8], [9,10,11,12,13,14,15]]
liste1 = [x for i in liste for x in i]
print(liste1)
