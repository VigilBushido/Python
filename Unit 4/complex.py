"""Illustration of concepts from Chapter 11 and 12 using the Complex number class"""

import math


class Complex(object):
    """Complex represents complex numbers. The object is immutable.
    Use the public functions re(), im().
    """

    def __init__(self, real, imag=0):
        self.__real = float(real)
        self.__imag = float(imag)

    def re(self):
        """Part of the public interface: return real part"""
        return self.__real


    def im(self):
        """Part of the public interface: return imaginary part"""
        return self.__imag

    def zero():
        """a class method representing number 0"""
        return Complex(0,0)   

    def jay():
        """a class method representing imaginary 1 (square root of -1)"""
        return Complex(0,1)    

    def _closeto(x, y, eps=1E-15):
        """class method; returns true if x and y are very close to each other. Used for __eq__."""
        return abs(x - y) < eps
    
    def exp(z):
        """class function: Complex.exp(z) = exp(z.re()+j*z.im()) =
              exp(z.re()) * Complex(cos(z.im()),sin(z.im())), using Euler's formula"""
        return math.exp(z.re()) * Complex(math.cos(z.im()), math.sin(z.im()))

    def sqrt(x):
        if isinstance(x, int) or isinstance(x, float):
            if x >= 0:
                return math.sqrt(x)
            return Complex(0, math.sqrt(-x))
        else:
            raise(TypeError("Complex.sqrt() ERROR: param not float or int"))
    
    def conj(self):
        """return conjugate"""
        return Complex(self.re(), -self.im())

    def abs(self):
        """absolute value"""
        return math.sqrt(self.re()*self.re() + self.im()*self.im())


    def polar(self):
        """return tuple (r,theta) with polar coordinates"""
        x = self.re()
        y = self.im()
        if x > 0:
            theta = math.atan(y / x)
        elif x < 0 and y >= 0:
            theta = math.atan(y / x) + math.pi
        elif x < 0 and y < 0:
            theta = math.atan(y / x) - math.pi
        elif x == 0 and y > 0:
            theta = math.pi / 2.0
        elif x == 0 and y < 0:
            theta = -math.pi / 2.0
        else:
            theta = math.nan
        return (self.abs(), theta)
    
    def __str__(self):
        """get string representation. E.g. used for print(z)"""
        r = 0 if Complex._closeto(self.re(), 0) else self.re()
        i = 0 if Complex._closeto(self.im(), 0) else self.im()
        
        return "{}{:+}j".format(r, i)

    def __repr__(self):
        """get representation of object. Used from Python shell."""
        return self.__str__()

    def __eq__(self, z):
        """z1 == z2"""
        if isinstance(z, Complex):
            return Complex._closeto(self.re(), z.re()) and \
                Complex._closeto(self.im(), z.im())
        else:
            return Complex._closeto(self.re(), z) and Complex._closeto(self.im(), 0)
    
    def __add__(self, z):
        """z + a, where z is Complex and a is not"""
        if isinstance(z, Complex):
            return Complex(self.re() + z.re(), self.im() + z.im())
        # else....
        return Complex(self.re() + z, self.im())    

    def __radd__(self, z):
        """a + z, where z is Complex and a is not"""
        return self.__add__(z)

    
    def __sub__(self, z):
        """z - a, where z is Complex and a is not"""
        if isinstance(z, Complex):
            return Complex(self.re() - z.re(), self.im() - z.im())
        # else....
        return Complex(self.re() - z, self.im())
        
    def __rsub__(self, z):
        """a - z, where z is Complex and a is not"""
        if isinstance(z, Complex):
            return z - self
        # else....
        return Complex(z) - self


    def __neg__(self):
        """-z, z being Complex; unary - or negation"""
        return Complex(-self.re(), -self.im())


    def __mul__(self, z):
        """z * a, where z is Complex and a is not"""
        if isinstance(z, Complex):
            return Complex(self.re()*z.re() - self.im()*z.im(),
                           self.re()*z.im() + self.im()*z.re())
        # else....
        return self * Complex(z) 

    def __rmul__(self, z):
        """a * z, where z is Complex and a is not"""
        return self.__mul__(z)    #  * is commutative


    def __bool__(self):
        """conversion to bool, such that statement "if z:" can work"""
        return self != Complex.zero()


    
def main():
    """Demonstrate Complex code"""
    z=Complex(1,2)
    w=Complex(2,3)
    print("z={}".format(z))
    print("w={}".format(w))
    
    print("z + w: ", z + w)    # __add__
    print("-5 + w: ", -5 + w)  # __radd__
    print("z - w: ", z - w)    # __sub__
    print("10 - w; ", 10 - w)  # __rsub__
    print("z * w: ", z * w)    # __mul__
    print("z * 4: ", z * 4)    # __mul__
    print("4 * z: ", 4 * z)    # __rmul__
    
    print("Should be True:", z != w)
    print("Should be True:", z == Complex(1.0, 2.0))
    print("Should be True:", z - w == -(w - z))

    z2 = z + 5 - 2.5 * w * w * z - Complex(10, 10)
    
    print("z + 5 - 2.5 * w * w * z - Complex(10, 10)={}".format(z2))

    zz = Complex(1,2)
    print("z==zz ?", z==zz)

    # polar coords:
    z2 = 1 + Complex.jay()    # 1 + j
    print("({}).polar()={}".format(z2, z2.polar()))

    # Euler equation: e^(pi*j) + 1 == 0
    eul = Complex.exp( math.pi * Complex.jay()) + 1
    print("Euler formula: e^(pi*j) + 1 = {}".format(eul))

    # sqrt with negative numbers:
    print("sqrt(-16)={}".format(Complex.sqrt(-16)))


# call main from top program:
if __name__ == '__main__':
    # define some global variables to play with:
    z=Complex(1,2)
    w=Complex(2,3)

    main()
