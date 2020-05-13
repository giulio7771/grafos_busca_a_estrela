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
    caminho = Caminho.Caminho()
    caminho.addVertice(verticeAtual)
    caminhos.append(caminho)
    while(True):
      self.expandir(caminho)
      verticesExpandidos = self.expandir(verticeAtual, custo)
  
  def expandir2(self, verticeAtual, custo):
    arrestas = verticeAtual.obterArrestas()
    for arresta in arrestas:
      gn = arresta.obterCusto()
      hn = arresta.obterVerticeDestino().obterDistancia()
      fn = gn + hn
    return True
  
  def expandir(self, caminho):
    ultimoVertice = caminho.obterUltimoVertice()
    arrestas = ultimoVertice.obterArrestas()
    caminhos = []
    for arresta in arrestas:
      caminhoNovo = Caminho.Caminho()
      caminhoNovo.copiarDe(caminho)
      verticeDestino = arresta.obterVerticeDestino()
      caminhoNovo.addVertice(verticeDestino)
      caminhoNovo.addCusto(arresta.obterCusto())
      caminhos.append(caminhoNovo)
      print("Expansão vertice: {} | fn: {}".format(verticeDestino.nome, caminhoNovo.calculaFn()))
    return caminhos


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
      