import Vertice
import Caminho

class Grafo:
  def __init__(self, verticeOrigemNome, verticeDestinoNome):
    self.vertices = []
    self.verticeOrigemNome = verticeOrigemNome
    self.verticeDestinoNome = verticeDestinoNome
  
  def aEstrela(self):
    verticeAtual = self.obterVerticePorNome(self.verticeOrigemNome)
    verticeDestino = self.obterVerticePorNome(self.verticeDestinoNome)
    caminhos = []
    custo = 0
    while(verticeAtual.nome != verticeDestino.nome):
      verticesExpandidos = self.expandir(verticeAtual, custo)
  
  def expandir(self, verticeAtual, custo):
    arrestas = verticeAtual.obterArrestas()
    for arresta in arrestas:
      gn = arresta.obterCusto()
      hn = arresta.obterVerticeDestino().obterDistancia()
      fn = gn + hn
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
      