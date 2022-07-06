#-*- coding:utf-8-*-
"""
from builtins import print

listas=["bruno","rayka","filhinha"]
lista2=[1,2,3,4]
lista3=[1,1.5,2,'alpha']
print(listas)
for item in lista3:
    print(item)

lista2.append("marmota")
print(lista2)
if 3 in lista2:
    print("está na lista")

meu_dicionario={"Nome":"bruno","idade":"24","namorada":"rayka"}

print(meu_dicionario["Nome"])

for chave in meu_dicionario:
    print(chave+":"+meu_dicionario[chave])





def leitura_de_arquivo():
    w = open("arquivo2.txt", "w")

    w.write("se fuder blume")
    arquivo2 = open("arquivo2.txt")
    w.close()
    txt2 = arquivo2.readline()
    print(txt2)


leitura_de_arquivo()

nome=input("insira o nome do arquivo para criar")
def criaçãoArquivo(nome):
    w = open(f"{nome}.txt", "w")
    w.close()

criaçãoArquivo(nome)

import random as rd
lista=[6,45,9]
#numero=rd.randint(0,100)
numero=rd.choice(lista)
print(numero)
#tratamento de exeçoes

a=2
b=0
try:
    print(a/b)
except :
    print("não é permito divisão por 0")


# list coprehension
x=[1,2,3,4,5]
y=[i**2 for i in x]
z=[i for i in x if i%2==1]

print("usando list coprehension \n {} \n {} \n numeros impares :{}".format(x,y,z))
lista=["abacate ","bola","cachorro"]
for i,nome in enumerate(lista):
    print(i,nome)
    
#filter
def pares(i):
    if i%2==0:
        return i
lista=[1,2,3,4,5,6,7,8,9]

lista_pares=filter(pares, lista)
print(list(lista_pares))

#função reduce
from functools import reduce

lista=[1,2,2,3,4,5,6,7,8,9]
def soma(x,y):
    return x+y

soma=reduce(soma, lista)
print(soma)

def escreve_arquivo():
    w=open("arquivo3.txt","w")
    
    w.close()
    
escreve_arquivo()
def escrita_arquivo():
    w=open("arquivo3.txt","w")
    w.writelines("se der certo não preciso escrever tudo aquilo \n e será que consigo escrever mais de uma linha???")
    arquivo3=open("arquivo3.txt",'w')
   

escrita_arquivo()"""    
lista1=[1,2,3,4,5]
lista2=["banana","maça","uva","mamão","abacaxi"]
    
for numero,nome in zip(lista1,lista2):
    print(numero,nome)
    
#map

"""def dobro(x):
    return x*2

valor=[1,2,3,4,5]
valor_dobrado=map(dobro, valor)
valor_dobrado=list(valor_dobrado)
print(valor_dobrado)
#funçáo lambda



valor=[1,2,38,4,5]
valor_dobrado=map(lambda i:i*2, valor)
valor_dobrado=list(valor_dobrado)
print(valor_dobrado)"""






