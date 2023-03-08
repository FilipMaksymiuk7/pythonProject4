# a = 'napis\ndrugi napis'
# print(a)
# b = 5
# c = 5.5
# print(b, c)
# d = 5+3j
# print(d)
# f = c//b
# print(f)
# e = c+d
# print(e)
# g = c % b
# print(g)
# h = b**2
# print(h)
# j = pow(b,1/2)
# print(j)
#
# print('b=b+2')
# print(b)
# b+=2
# print(b)
#

# listy = ['a',4,5,6,[1,2,3],5.6]
# print(listy)
# listy.append(4)
# print(listy)
# print(listy[5])
lista =[1,2,3,]
lista2 =[4,5,6]
#dodać element na wybrane miejsce
lista.insert(2,0)
print(lista)
#dodac kilka elementow
lista.extend(lista2)
print(lista)
#usunac element z listy o danej pozycji
del lista[2]
print(lista)
#usunąć element z listy o danej wartości
lista.remove(3)
print(lista)
#odwrócić element z listy
lista.reverse()
print(lista)
#zrobić sortowanie
lista.sort()
print(lista)


#tupla =

dict = {1:'tak',0:'nie','2':'moze'}
print(dict)
print(dict[1])
dict['klucz']= 'wartosc'
print(dict)
dict.pop('klucz')
print(dict)
print(dict.keys())

print(dict.values())


print('a=%(zm)d'%{'zm':12})
# napis = 'a={},b={}'
# print(napis.format(12,12))
print('a={},b={}'.format(12,12))


#if warunek1:
    #instrukcja1
    #instrukcja2
#elif warunek2:
    #instrukcja1
    #instrukcja2
#else:
    #instrukcja1
# a=input('podaj a: ')
# b=input('podaj b: ')
# print(a)
# print(b)print(type(b))
#
# print(type(a))
# print(type(b))
# a = int(a)
# b = int(b)
# print(type(a))
# if a>b:
#     print(a)
# elif b>a:
#     print(b)
# else:
#     print('a równe b')

# if a!=b:
#     print('sa rozne')
# elif a==b:
#     print('rowne')
# else:
#     print("nie mozliwe")
#
#

# a = input('podaj a')
# b = input('podaj b')
# c = input('podaj c')
# d = input('podaj d')
# a =int(a)
# b =int(b)
# c =int(c)
# d =int(d)
#
# if(a>b)&(c>d):
#     print('a wieksze od b i c wieksze od d')
# else:
#     print('a jest mniejsze od b lub c jest mniejsze od d')
#
#

#for element in sekwencja:
    #instrukcja 1
    #instrukcja 2
#else:
#   instrukcja 1
#   instrukcja 2

for x in range(0,11,2):
    print(x)
else:
    print('koniec petli for')

# for x in lista:
#     print(x)

print(lista)
for x in range(0,len(lista)):
    print(lista[x])


#while warunek:
#   instrukcja 1
#   instrukcja 2
#else:
#   instrukcja 1
#
# licznik =0
# while licznik != len(lista):
#     print(lista[licznik])
#     licznik+=1
#
#

# liczby = [3,4,5,1,7,8]
# a = int(input('podaj a: '))
# licznik =0
# while licznik != len(liczby):
#     if a - liczby[licznik]==0:
#         print('{} - {} = 0'.format(a, liczby[licznik]))
#         break
#     licznik += 1
#
#
#

liczby = [1,2,2,2,4,5,6]
licznik =0
while licznik != len(liczby):
    if liczby[licznik]==2:
        del liczby[licznik]
        licznik-=1
    licznik+=1
print(liczby)

