# Break ve Continue

"""
Break:

Break ifadesi döngülerde programcılar tarafından en çok kullanılan ifadedir.

* Döngu herhangi bir yerde ve herhangi bir zamanda break ifadesiyie zaman çalışmasını bir anda durdurur. Böylelikle döngu hiçbir koşula bağlı kalmadan sonlanmış olur.

break ifadesi sadece ve sadece içindeki bulunduğu döngüyü sonlandırır. Eğer iç içe döngüler bulunuyorsa ve en içteki döngüde break kullanılmışsa sadece içteki döngü sona erer. Örneklere break ifadesini anlamaya çalışalım.

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
continue ifadesi

continue ifadesi break'e göre biraz daha az kunanllan bit ifadedir. Anlamı şu şekildedir.

- Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığı zaman geri kalan işlemlerini yapmadan direk bloğunun başına döner.

contjnue ifadesini anlamak örneklerimize bakalım.
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
