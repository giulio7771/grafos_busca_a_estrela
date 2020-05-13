class Caminho:
  def __init__(self):
    self.historico = []
    self.custoAcumulado = 0
  
  def addVertice(self, vertice):
    self.historico.append(vertice)

  def adicionaCusto(self, custo):
    self.custoAcumulado += custo