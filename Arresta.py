class Arresta:
  def __init__(self, verticeOrigem, verticeDestino, custo):
    self.verticeDestino = verticeDestino
    self.verticeOrigem = verticeOrigem
    self.custo = custo

  def printArresta(self):
    print("  {} : {} -> {}".format(self.verticeOrigem.nome, self.verticeDestino.nome, self.custo))