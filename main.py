listy=[5,6,7,6.5]
print(listy)

listy.insert(2,'lol')
print(listy)

listy.pop(2)
print(listy)

listy.remove(6)
print(listy)

x=[1,2,3]
listy.extend(x)
print(listy)

listy.reverse()
print(listy)

listy.sort()
print(listy)

slownik={1: 'a',2: 2,3:'klucz'}
print(slownik)

print(slownik[1])
slownik['nowy']='wartosc'
print(slownik)

print('a={}'.format(12))

#napis=input('wprowardz liczbe: ')
#print(napis)
#if napis=='lol':
#    print('xdd')

#for i in listy:
#    print(i)

#for i in range(0,len(listy),1):
#    print(listy[i])

lista=[1,2,2,3,4,5,6,7,8,2,9]

i=0

while i < len(lista):
    if lista[i]==2:
        lista.pop(i)
    else:
        i+=1

print(lista)