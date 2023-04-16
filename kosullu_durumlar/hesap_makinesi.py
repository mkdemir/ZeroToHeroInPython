print("""
****************************************************
Hesap Makinesi Programı

İşlemler;
1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi 
4. Bölme İşlemi
****************************************************
""")

sayi1 = int(input("Birinci Sayı:"))
sayi2 = int(input("İkinci Sayı:"))
islem = input("İşlemi Giriniz:")

if islem == "1":
    print(f'sayi1 + sayi2 : {sayi1 + sayi2}')
elif islem == "2":
    print(f'sayi1 - sayi2 : {sayi1 - sayi2}')
elif islem == "3":
    print(f'sayi1 * sayi2 : {sayi1 * sayi2}')
elif islem == "4":
    print(f'sayi1 / sayi2 : {sayi1 / sayi2}')
else:
    print("Yanlış işlem kodu girdiniz lütfen işlemi tekrardan giriniz...")
