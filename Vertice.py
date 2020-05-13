class Vertice:

  def __init__(self, nome, distancia = None):
    self.nome = nome
    self.distancia = distancia
    self.arrestas = []
  
  def obterNome(self):
    return self.obterNome

  def obterDistancia(self):
    return self.distancia
  
  def setDistancia(self, distancia):
    self.distancia = distancia
  
  def addArresta(self, arresta):
    self.arrestas.append(arresta)
  
  def obterArrestas(self):
    return self.arrestas
  
  def printVertice(self):
    for i in self.arrestas:
      i.printArresta()
