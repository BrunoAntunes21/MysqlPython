# grafico comparativo do crescimento da população brasileira 80-2016
import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()
x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.xlabel("Anos")
plt.ylabel("Centenas de Milhoes")
plt.title("crescimento da população ao longo do tempo")
plt.plot(x,y,color="k",linestyle="--")
plt.bar(x, y, label="Crescimento populacional", color="#e4e4e4")
#plt.scatter(x,y,marker="D",color="b")
plt.show()
#plt.savefig("População_Brasileira.png",dpi=320)