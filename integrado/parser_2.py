from goto import *
from action import *
from funcoes_auxiliares_sintatico import *
from recuperacao_de_erro import *
from regras import Regras
from scanner import Scanner
from tabela_de_estados import TabelaDeEstados
from tabela_de_simbolos import TabelaDeSimbolos



class Parser2:
  def __init__(self):
    self.pilha = [0]


  def buscarProximoToken(self, scanner: Scanner, tabelaEstados: TabelaDeEstados, tabelaDeSimbolos: TabelaDeSimbolos, listaDeTokens): 
    retornoScanner = scanner.SCANNER(tabelaEstados, tabelaDeSimbolos)
    listaDeTokens.append(retornoScanner)


  def PARSER(self):
    listaDeTokens = []
    mainAction()
    regras = Regras()
    scanner = Scanner("codigo.txt")
    tabelaEstados = TabelaDeEstados()
    tabelaDeSimbolos = TabelaDeSimbolos()
    self.buscarProximoToken(scanner, tabelaEstados, tabelaDeSimbolos, listaDeTokens)
    index = 0
    token = listaDeTokens[index]

    a = token.classe.lower() # Token
    
    while True:
      print('-'*50)
      print('Token: ', token)
      print('Pilha: ', self.pilha)
      s = self.pilha[-1]
      acao = action(s,a)
      t = acao[1:]
      if('s' in acao):
        print('SHIFT: ', acao)
        self.pilha.append(int(t))
        self.buscarProximoToken(scanner, tabelaEstados, tabelaDeSimbolos, listaDeTokens)
        index += 1
        token = listaDeTokens[index]
        a = token.classe.lower()

      elif('R' in acao):
        print('REDUCE: ', acao)

        A, B, regra = regras.retornaElementos(t)


        for element in B:
          desempilhar(self.pilha)

        t = self.pilha[-1]
        print('Topo da pilha: ', t)

        self.pilha.append(int(goto(int(t),A)))
        print('Produção: ', regra)
        
      elif('a' in acao):
        print('ACCEPT')
        break

      else:
        # index = panicMode(s, index, listaDeTokens)
        phraseRecovery(s, index, listaDeTokens)
        token = listaDeTokens[index]
        a = token.classe.lower()
