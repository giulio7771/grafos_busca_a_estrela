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
      caminhoEscolhido = self.caminhoMenorFn(caminhos)
      (chegada, novosCaminhos) = self.expandir(caminhoEscolhido)
      if (chegada):
        return novosCaminhos
      caminhos = self.agruparCaminhos(caminhos, novosCaminhos)

  def agruparCaminhos(self, caminhos1, caminhos2):
    for caminho in caminhos2:
      caminhos1.append(caminho)
    return caminhos1

  def caminhoMenorFn(self, caminhos):
    melhorCaminho = None
    melhorFn = None
    #idx = 0
    #i = 0
    for caminho in caminhos:
      fn = caminho.calculaFn()
      if (melhorFn == None or fn < melhorFn):
        melhorFn = fn
        melhorCaminho = caminho
        #idx = i
      #i += 1
    caminhos.remove(melhorCaminho)
    return melhorCaminho
  
  def expandir(self, caminho):
    ultimoVertice = caminho.obterUltimoVertice()
    arrestas = ultimoVertice.obterArrestas()
    caminhos = []
    print("-----Expandindo {} vertices------".format(len(arrestas)))
    print("Patindo do vertice {} ".format(ultimoVertice.obterNome()))
    for arresta in arrestas:
      caminhoNovo = Caminho.Caminho()
      caminhoNovo.copiarDe(caminho)
      verticeDestino = arresta.obterVerticeDestino()
      caminhoNovo.addVertice(verticeDestino)
      caminhoNovo.addCusto(arresta.obterCusto())
      caminhos.append(caminhoNovo)
      print("Expansão vertice: {} | fn: {}".format(verticeDestino.nome, caminhoNovo.calculaFn()))
      if (verticeDestino.obterNome() == self.verticeDestinoNome):
        return [True, caminhoNovo]
    return [False, caminhos]


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
      