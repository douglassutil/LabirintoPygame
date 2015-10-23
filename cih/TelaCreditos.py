__author__ = 'Douglas'
from cdp.Componentes import *

class ImprimeCreditos:
    def __init__(self):
        self.creditosImagem = Imagens("backcreditos").criaImagens((632,632)) # file recebe o local da imagem que sera utilizada


    def imprimirJanelaCreditos(self,controle,posicao):
        controle.screen.fill(0) #limpar a tela
        controle.screen.blit(self.creditosImagem,posicao) # printar a tela