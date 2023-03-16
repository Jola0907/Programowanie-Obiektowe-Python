import matplotlib.pyplot as plt
from datetime import datetime
from math import gcd


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def nalezy_do(self, pr):
        return self.y == pr.a * self.x + pr.b


class Prosta:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def miejsce_zerowe(self):
        if self.a == 0:
            print("Miejsce zerowe nie istnieje")
            return None
        else:
            return -self.b / self.a


class Prostokat:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def bok_a(self):
        if self.p1.x > self.p2.x:
            return self.p1.x - self.p2.x
        else:
            return self.p2.x - self.p1.x

    @property
    def bok_b(self):
        if self.p1.y > self.p2.y:
            return self.p1.y - self.p2.y
        else:
            return self.p2.y - self.p1.y

    def pole(self):
        return self.bok_a * self.bok_b

    def obwod(self):
        return 2 * (self.bok_a + self.bok_b)

    def rysuj(self):
        plt.scatter([self.p1.x, self.p2.x], [self.p1.y, self.p2.y])
        plt.plot([self.p1.x, self.p1.x, self.p2.x, self.p2.x, self.p1.x],
                 [self.p1.y, self.p2.y, self.p2.y, self.p1.y, self.p1.y])
        plt.grid()
        plt.show()

class Note:
    def __init__(self, autor, tresc):
        self.autor = autor
        self.tresc = tresc
        czas = datetime.now()
        self.czas = str(czas.hour) + ':' + str(czas.minute)


class Notebook:
    def __init__(self):
        self.lista = []

    def dodaj_nowa(self, autor, tresc):
        nowa = Note(autor, tresc)
        self.lista.append(nowa)

    def dodaj(self, nowa):
        self.lista.append(nowa)

    def ile(self):
        return len(self.lista)

    def wyswietl_wszystko(self):
        i = 1
        for n in self.lista:
            print(i, '. ', n.autor, ': "', n.tresc, '" o godzinie ', n.czas, sep='')
            i += 1


class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        nwd = gcd(a, b)
        self.__a = int(a / nwd)
        self.__b = int(b / nwd)

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def __add__(self, other):
        a1 = self.__a
        b1 = self.__b
        a2 = other.a

        m1, m2 = self.__b, other.b
        a1 *= m2
        b1 *= m2
        a2 *= m1

        return Fraction(a1 + a2, b1)

    def __sub__(self, other):
        a1 = self.__a
        b1 = self.__b
        a2 = other.a

        m1, m2 = self.__b, other.b
        a1 *= m2
        b1 *= m2
        a2 *= m1

        return Fraction(a1 - a2, b1)

    def __mul__(self, other):
        return Fraction(self.__a * other.a, self.__b * other.b)

    def __truediv__(self, other):
        return Fraction(self.__a * other.b, self.__b * other.a)

    def __abs__(self):
        return Fraction(abs(self.__a), abs(self.__b))

    def __repr__(self):
        return 'Fraction(' + str(self.__a) + ', ' + str(self.__b) + ')'

    def __eq__(self, other):  # ==
        return self.__a == other.a and self.__b == other.b

    def __ne__(self, other):  # !=
        return self.__a != other.a or self.__b != other.b

    def __lt__(self, other):  # <
        a1 = self.__a
        a2 = other.a

        m1, m2 = self.__b, other.b
        a1 *= m2
        a2 *= m1

        return a1 < a2

    def __gt__(self, other):  # >
        a1 = self.__a
        a2 = other.a

        m1, m2 = self.__b, other.b
        a1 *= m2
        a2 *= m1

        return a1 > a2

    def __le__(self, other):  # <=
        a1 = self.__a
        a2 = other.a

        m1, m2 = self.__b, other.b
        a1 *= m2
        a2 *= m1

        return a1 <= a2

    def __ge__(self, other):  # >=
        a1 = self.__a
        a2 = other.a

        m1, m2 = self.__b, other.b
        a1 *= m2
        a2 *= m1

        return a1 >= a2

    def __float__(self):
        return self.__a / self.__b

    def __int__(self):
        return int(self.__a / self.__b)

    def __bool__(self):
        if self.__a != 0:
            return True
        else:
            return False

    def __round__(self, n=0):
        return round(float(self), n)

    def __str__(self):
        wynik = ''
        if self.__a >= self.__b:
            wynik += str(self.__a // self.__b) + ' '
        if self.__a % self.__b != 0:
            wynik += str(self.__a % self.__b) + '/' + str(self.__b)
        return wynik
