from math import *

#zad1

liczba1 = 5
liczba2 = 3

liczba3 = 2.5
liczba4 = 5.3

tekst1 = "pierwszy tekst"
tekst2 = "drugi tekst"

print(liczba1)
print(liczba2)
print(liczba3)
print(liczba4)
print(tekst1)
print(tekst2)



#zad2

a = 5
b = 100
c = 3

dodawanie = a+b
odejmowanie = a-c
mnozenie = a*c
dzielenie = b/a
potegowanie = a**c
pierwiastkowanie = sqrt(b)

print(dodawanie)
print(odejmowanie)
print(mnozenie)
print(dzielenie)
print(potegowanie)
print(pierwiastkowanie)



#zad3

d = 5

d += 1
print(d)

d -= 1
print(d)

d *= 4
print(d)

d /= 2
print(d)

d **= 2
print(d)

d %= 3
print(d)



#zad4

wynik1 = exp(10)
print(wynik1)

wynik2 = pow(log(5+sin(8)**2),1/6)
print(wynik2)

wynik3 = floor(3.55)
print(wynik3)

wynik4 = ceil(4.8)
print(wynik4)



#zad5

imie = "MATEUSZ"
nazwisko = "GRZESKIEWICZ"

print(imie.capitalize(),nazwisko.capitalize())



#zad6

piosenka = "la la la la la la turururu"
print(piosenka.count("la"))



#zad7

tekst = "dzien dobry"
print(tekst[0],tekst[10])



#zad8

print(piosenka.split())



#zad9

zmienna1 = "zdanie"
zmienna2 = 5.534
zmienna3 = 0Xff
print("%s %f %x" % (zmienna1, zmienna2, zmienna3))