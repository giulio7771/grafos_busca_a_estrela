import Vertice

class Grafo:
  def __init__(self, verticeOrigemNome, verticeDestinoNome):
    self.vertices = []
    self.verticeOrigemNome = verticeOrigemNome
    self.verticeDestinoNome = verticeDestinoNome
  
  def aEstrela(self):
    verticeAtual = self.obterVerticePorNome(self.verticeOrigemNome)
    print("Vertice Expandido: {}".format(verticeAtual.nome))
    return True

  def addVertice(self, vertice):
    self.vertices.append(vertice)

  def obterVerticePorNome(self, nome):
    for i in self.vertices:
      if i.nome == nome:
        return i
    vertice =  Vertice.Vertice(nome)
    self.addVertice(vertice)
    return vertice

  def printGrafo(self):
    for i in self.vertices:
      print("Vertice: {} : {}".format(i.nome, i.distancia))
      i.printVertice()
      