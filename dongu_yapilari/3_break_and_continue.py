# Break ve Continue

"""
Break:

- Break ifadesi, programcılar tarafından en sık kullanılan ifadedir döngülerde.

Herhangi bir döngüde, herhangi bir zamanda break ifadesi kullanılarak, döngünün aniden durdurulması sağlanır. Böylece döngü, herhangi bir koşula bağlı kalmadan sonlanmış olur.

Break ifadesi, sadece içinde bulunduğu döngüyü sonlandırır. Eğer iç içe döngüler bulunuyorsa ve en içteki döngüde break kullanılıyorsa, sadece içteki döngü sona erer. 
Break ifadesini anlamaya yönelik örneklerimize bir göz atalım.
"""

i = 0

while (i<10):
    print(f"i: {i}")
    i+=1


i = 0

while (i<10):
    if (i == 5):
        break
    print(f'i: {i}')
    i+=1

liste = [1,2,3,4,5]

for i in liste:
    if (i == 3):
        break
    print(f"i: {i}")


while True:
    isim = input("Enter your name:")
    if (isim == "q"):
        print("Exiting the program...")
        break
    print("Names:",isim)


"""
continue İfadesi:

continue ifadesi, break ifadesine göre biraz daha az kullanılan bir ifadedir.

Anlamı şu şekildedir:

Bir döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığında, geri kalan işlemleri yapmadan doğrudan bloğunun başına döner.
continue ifadesini anlamak için örneklerimize bakalım.
"""


liste = [1,2,3,4,5,6,7,8,9,10]

for i in liste:
    print("i:",i)


for i in liste:
    if (i ==3 or i ==5):
        continue # Alttaki işlemi yapma döngünün en başına git
    print("i:",i)

# Sonsuz bir döngü oluşturuyoruz.
# i = 0

# while (i<10):

#     if (i==2):
#         continue
#     print(i)
#     i+=1


i = 0

while (i<10):

    if (i==2):
        i += 1
        continue
    print(i)
    i+=1
