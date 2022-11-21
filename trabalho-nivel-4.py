import numpy as np
from numpy import cov, var, std, min, max, sqrt, mean
import matplotlib.pyplot as plt

x = np.array([ [0], [2], [5], [6], [7], [8], [5], [9],[8],[9] ])
y = np.array([ [0], [3], [5], [4], [6], [9], [7], [9],[7],[5]])


class RegressaoLinear:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def correlacao(self):
    covariacao = cov(self.x, self.y,bias=True)[0][1]
    variancia_x = var(self.x)
    variancia_y = var(self.y)
    return covariacao / sqrt(variancia_x * variancia_y)

  def inclinacao(self):
    stdx = std(self.x)
    stdy = std(self.y)
    return self.correlacao() * (stdy/stdx)

  def interceptacao(self):
    mediax = mean(self.x)
    mediay = mean(self.y)
    return mediay - mediax * self.inclinacao()

  def previsao(self,valor):
    intercepta = self.interceptacao()
    return (self.inclinacao() * valor) + intercepta

  def PlotaRegressao(self, titulo = "Regressão Linear", x = "Eixo X", y = "Eixo Y"):
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(titulo)

    plt.Line2D (self.x,self.y)
    x_min = min(self.x)
    x_max = max(self.x)
    x_reta = [x_min, x_max]
    y_reta = [self.previsao(x_min), self.previsao(x_max)]
    plt.plot(x_reta, y_reta,label  = "Regressão Linear", c = 'r')
    plt.axis(xmin=0 , xmax=8)
    plt.axis(ymin=0 , ymax=20)
    plt.show


plt.style.use("classic")
plt.title('Gráfico de despesas',color = 'green')
plt.xlabel('Dias',color = 'red' )
plt.ylabel('Gastos em alimentação - R$', color = 'red')
plt.axis(ymin=0 , ymax=20)
plt.axis(xmin=0 , xmax=8)
plt.plot(x, marker='o',label  = "Almoço", c = 'b')
plt.plot(y, marker='o',label  = "Jantar", c= 'y')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()

regressao = RegressaoLinear(x,y)

regressao.PlotaRegressao("Gráfico de despesas", "Dias","Gastos em alimentação - R$")

plt.title('Gráfico de despesas',color = 'green')
plt.xlabel('Dias',color = 'red' )
plt.ylabel('Gastos em alimentação - R$', color = 'red')
plt.axis(ymin=0 , ymax=20)
plt.axis(xmin=0 , xmax=8)
plt.plot(y, marker='o',label  = "jantar", c = 'y')
plt.legend(loc = 'upper left')
plt.style.use("classic")
plt.tight_layout()
plt.show()