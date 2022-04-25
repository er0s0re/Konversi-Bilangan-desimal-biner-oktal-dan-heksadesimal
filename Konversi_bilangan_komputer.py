# Konversi bilangan desimal, biner, oktal, dan hexadesimal


class dec :
    def __init__(self, x):
        self.x = x

    def decimal(x):
        decimal = " "
        while x > 0:
            decimal = str(x % 2) + decimal
            x = x // 2
        return decimal

    def biner(x):
        biner = " "
        while x > 0:
            biner = str(x % 2) + biner
            x = x // 2
        return biner

    def oktal(x):
        oktal = " "
        while x > 0:
            oktal = str(x % 8) + oktal
            x = x // 8
        return oktal

    def hexa(x):
        hexa = " "
        while x > 0:
            hexa = str(x % 16) + hexa
            x = x // 16
        return hexa

    def tampil1(x):
        print("Bilangan Desimal:", x)
        print("Bilangan Biner:", dec.biner(x))
        print("Bilangan Oktal:", dec.oktal(x))
        print("Bilangan Hexadesimal:", dec.hexa(x))

class bin :
    def __init__(self, x):
        self.x = x

    def decimal(x):
        decimal = 0
        for i in range(len(x)):
            decimal = 2 * decimal + int(x[i])
        return decimal

    def biner(x):
        return x

    def oktal(x):
        x = bin.decimal(x)
        oktal = " "
        while x > 0:
            oktal = str(x % 8) + oktal
            x = x // 8
        return oktal

    def hexa(x):
        x = bin.decimal(x)
        hexa = " "
        while x > 0:
            hexa = str(x % 16) + hexa
            x = x // 16
        return hexa

    def tampil2(x):
        print("Bilangan Desimal:", bin.decimal(x))
        print("Bilangan Biner:", x)
        print("Bilangan Oktal:", bin.oktal(x))
        print("Bilangan Hexadesimal:", bin.hexa(x))

class oct :
    def __init__(self, x):
        self.x = x

    def decimal(x):
        decimal = 0
        for i in range(len(x)):
            decimal = 8 * decimal + int(x[i])
        return decimal

    def biner(x):
        x = oct.decimal(x)
        biner = " "
        while x > 0:
            biner = str(x % 2) + biner
            x = x // 2
        return biner

    def oktal(x):
        return x

    def hexa(x):
        x = oct.decimal(x)
        hexa = " "
        while x > 0:
            hexa = str(x % 16) + hexa
            x = x // 16
        return hexa

    def tampil3(x):
        print("Bilangan Desimal:", oct.decimal(x))
        print("Bilangan Biner:", oct.biner(x))
        print("Bilangan Oktal:", x)
        print("Bilangan Hexadesimal:", oct.hexa(x))

class hexa :
    def __init__(self, x):
        self.x = x

    def decimal(x):
        decimal = 0
        for i in range(len(x)):
            if x[i] == "A":
                decimal = 16 * decimal + 10
            elif x[i] == "B":
                decimal = 16 * decimal + 11
            elif x[i] == "C":
                decimal = 16 * decimal + 12
            elif x[i] == "D":
                decimal = 16 * decimal + 13
            elif x[i] == "E":
                decimal = 16 * decimal + 14
            elif x[i] == "F":
                decimal = 16 * decimal + 15
            else:
                decimal = 16 * decimal + int(x[i])
        return decimal

    def biner(x):
        x = hexa.decimal(x)
        biner = " "
        while x > 0:
            biner = str(x % 2) + biner
            x = x // 2
        return biner

    def oktal(x):
        x = hexa.decimal(x)
        oktal = " "
        while x > 0:
            oktal = str(x % 8) + oktal
            x = x // 8
        return oktal

    def hexa(x):
        return x

    def tampil4(x):
        print("Bilangan Desimal:", hexa.decimal(x))
        print("Bilangan Biner:", hexa.biner(x))
        print("Bilangan Oktal:", hexa.oktal(x))
        print("Bilangan Hexadesimal:", x)

print("==========================================================")
x = int(input("Masukkan bilangan desimal: "))
dec.tampil1(x)
y = input("\nMasukkan bilangan biner: ")
bin.tampil2(y)
z = input("\nMasukkan bilangan oktal: ")
oct.tampil3(z)
w = input("\nMasukkan bilangan hexadesimal: ").upper()
hexa.tampil4(w)
print("==========================================================")


