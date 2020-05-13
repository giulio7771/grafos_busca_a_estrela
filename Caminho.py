class Caminho:
  def __init__(self):
    self.historico = []
    self.custoAcumulado = 0
  
  def addVertice(self, vertice):
    self.historico.append(vertice)

  def addCusto(self, custo):
    self.custoAcumulado += custo
  
  def calculaFn(self):
    ultimoVertice = self.obterUltimoVertice()
    hn = ultimoVertice.obterDistancia()
    fn = self.custoAcumulado + hn
    return fn
  
  def setHistorico(self, historico):
    self.historico = historico

  def obterUltimoVertice(self):
    return self.historico[len(self.historico) - 1]

  def copiarHistorico(self):
    historico = []
    for i in self.historico:
      historico.append(i)
    return historico
  
  def obterCustoAcumulado(self):
    return self.custoAcumulado
  
  def copiarDe(self, caminho):
    self.historico = caminho.copiarHistorico()
    self.custoAcumulado = caminho.obterCustoAcumulado()
  
  def printCaminho(self):
    print("Caminho encontrado com custo: {}".format(self.custoAcumulado))
    for vertice in self.historico:
      print("  vertice {}".format(vertice.obterNome()))


