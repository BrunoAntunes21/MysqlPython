#box
"""import matplotlib.pyplot as plt

import random as rd
vetor=[]
for i in range(10):
    num_aleatorio=rd.randint(0,10)
    vetor.append(num_aleatorio)
plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()"""

entrada=open("dados_utilizados_e_codigo_fonte (1)/16s_bacteria.fasta").read()
saida=open("dados_utilizados_e_codigo_fonte (1)/18s_humano.html","w")
cont={}
for x in ['A','T','C','G']:
    for y in['A','T','C','G']:
        cont[x+y]=0
entrada=entrada.replace("\n","")
for k in range(len(entrada)-1):
    cont[entrada[k]+entrada[k+1]]+=1

print(cont)
#html
saida.write("<div>")
i=1
for k in cont:
    transparencia=cont[k]/max(cont.values())
    saida.write("<div style='width:100px;border:1px solid #111;height:100px; float:left;background-color:rgba(0,0,01,"+str(transparencia)+"')></div>")
    if i%4==0:
        saida.write("<div style='clear:both'></div>")
    i+=1

saida.close()