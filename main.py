import Grafo
import Vertice
import Arresta

def app():
  grafo = None
  distancias = readFile("distancias.txt")
  mapa = readFile("mapa.txt")

  mapa_linhas = mapa.split("\n")
  for i in mapa_linhas:
    values = i.split(" ")
    if grafo == None:
      grafo = Grafo.Grafo(values[0], values[1])
    else:
      verticeOrigem = grafo.obterVerticePorNome(values[0])
      verticeDestino = grafo.obterVerticePorNome(values[1])
      arresta = Arresta.Arresta(verticeOrigem, verticeDestino, values[2])
      verticeOrigem.addArresta(arresta)
      #arrestaInversa = Arresta.Arresta(verticeDestino, verticeOrigem, values[2])
      #verticeDestino.addArresta(arrestaInversa)

  distancias_linhas = distancias.split("\n")
  for i in distancias_linhas:
    values = i.split(" ")
    vertice = grafo.obterVerticePorNome(values[0])
    vertice.setDistancia(values[1])

  caminho = grafo.aEstrela()
  caminho.printCaminho()

def readFile(path):
  file = open(path, 'r')
  txt = file.read()
  file.close()
  return txt

app()
