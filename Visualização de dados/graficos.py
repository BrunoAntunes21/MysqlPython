#visualização de dados
#fazendo a importação da plataforma de criação de graficos de linha
import matplotlib.pyplot as plt
#eixo
x=[1,3,5,7,9]
#grafico
y=[2,3,5,7,9]
#eixo grafico 2
x2=[2,4,3,6,10]
#grafico 2
y2=[1,2,8,7,2]
z=[20,5,100,33,10]

titulo="grafico de barras em Python"
plt.title(titulo)
Ex="eixo x"
Ey="eixo y"
#criaçao do exios
plt.xlabel(Ex)
plt.ylabel(Ey)
plt.scatter(x,x2,label="media objetivo",color="g",marker="^",s=z)

plt.plot(y,y2,label="media alcançada",linestyle="-.")
plt.legend()
plt.show()
plt.savefig("Grafico_python.pdf",dpi=300)
