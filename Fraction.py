

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = (self.num * other.den) + (self.den * other.num)
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        return (self.num * other.den) == (self.den * other.num)

if __name__ == '__main__':

    # Test __str__
    myf = Fraction(3, 5)
    print(myf)

    # Test __add__
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    f3 = f1 + f2
    print(f3)

    # Test __eq__
    f4 = Fraction(1, 2)
    f5 = Fraction(3, 6)
    print(f4 == f5)


