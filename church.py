#!/usr/bin/python

zero = lambda f: lambda x:x
suc = lambda n: lambda f: lambda x: f(n(f)(x))
add = lambda n: lambda m: lambda f: lambda x: n(f)(m(f)(x))
mul = lambda n: lambda m: lambda f: lambda x: n(m(f))(x)
exp = lambda n: lambda m: lambda f: lambda x: (n)(m)(f)(x)

#Dwie funkcje zmieniajace liczby w liczebniki Churcha i odwrotnie

def IntToChurch (x):
        if x == 0:
                return zero
        else:
                return suc(IntToChurch(x-1))

ChurchToInt = lambda x: x(lambda i: i+1)(0)

#Funkcja do wypisywania kodu i wyniku

def myprint(x):
        print (x, ' = ',eval(x))
        return

#--------------------------------------------------------------
#Przyklady

myprint('ChurchToInt(zero)')
myprint('ChurchToInt(suc(exp(IntToChurch(4))(add(zero)(suc(suc(zero))))))')
