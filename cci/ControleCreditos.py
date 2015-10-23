from cih.TelaCreditos import *

class Creditos:
    def __init__(self):
        self.posicao = [0,0] # posicao onde sera impresso o background ((0,0) e o topo superior esquerdo)
        self.imprimeCreditos = ImprimeCreditos()
        return

    def mostraCreditos(self,numero, controle):

        if controle.evento.keys[4]: # se a tecla ESC for pressionada
            if numero == 0:
                controle.opcao = 1 # retorna a opcao correspondente no loop principal (controle)
            if numero == 1:
                controle.opcao = 5 # retorna a opcao correspondente no loop principal (controle)

        self.imprimeCreditos.imprimirJanelaCreditos(controle,self.posicao)


        pygame.display.update() # atualiza a imagem
