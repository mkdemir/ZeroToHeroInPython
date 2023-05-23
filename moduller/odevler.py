def problem1():
    """
    # Proje 1

    Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.
    """

    import math

    # while True:
    #     expr = input("İfadeyi girin (q ile çıkış yapın): ")

    #     if expr.lower() == "q":
    #         break

    #     try:
    #         result = eval(expr)
    #         print("Sonuç:", result)
    #     except (SyntaxError, NameError, ZeroDivisionError, TypeError) as e:
    #         print("Geçersiz ifade:", e)

    while True:
        operation = input("İşlemi seçin (+, -, *, /, q ile çıkış yapın): ")

        if operation.lower() == "q":
            break

        try:
            num1 = float(input("Birinci sayıyı girin: "))
            num2 = float(input("İkinci sayıyı girin: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            else:
                print("Geçersiz işlem!")
                continue

            print("Sonuç:", result)
        except ValueError:
            print("Geçersiz sayı girişi!")
        except ZeroDivisionError:
            print("Sıfıra bölme hatası!")


def problem2():
    """
    # Proje 2
    
    Math modülünde kullandığınız fonksiyonları kendiniz de ayrı bir modüle (Python dosyasına) yazmaya çalışın ve bu yazdığınız modülü kullanarak gelişmiş bir hesap makinesi yazın.
    """

    import math

    while True:
        operation = input("İşlemi seçin (pow, sqrt, sin, cos, tan, q ile çıkış yapın): ")

        if operation.lower() == "q":
            break

        try:
            if operation == "pow":
                num1 = float(input("Taban sayıyı girin: "))
                num2 = float(input("Üs sayıyı girin: "))
                result = math.pow(num1, num2)
            elif operation == "sqrt":
                num = float(input("Karekökünü almak istediğiniz sayıyı girin: "))
                result = math.sqrt(num)
            elif operation == "sin":
                angle = float(input("Açıyı girin (radyan cinsinden): "))
                result = math.sin(angle)
            elif operation == "cos":
                angle = float(input("Açıyı girin (radyan cinsinden): "))
                result = math.cos(angle)
            elif operation == "tan":
                angle = float(input("Açıyı girin (radyan cinsinden): "))
                result = math.tan(angle)
            else:
                print("Geçersiz işlem!")
                continue

            print("Sonuç:", result)
        except ValueError:
            print("Geçersiz sayı girişi!")

def main():
    problem1()
    

if __name__  == '__main__':
    main()