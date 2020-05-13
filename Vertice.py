class Vertice:

  def __init__(self, nome, distancia = None):
    self.nome = nome
    self.distancia = distancia
    self.arrestas = []
  
  def setDistancia(self, distancia):
    self.distancia = distancia
  
  def addArresta(self, arresta):
    self.arrestas.append(arresta)
  
  def printVertice(self):
    for i in self.arrestas:
      i.printArresta()
