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
    self.regras = Regras()
    self.scanner = Scanner("codigo.txt")
    self.tabelaEstados = TabelaDeEstados()
    self.tabelaDeSimbolos = TabelaDeSimbolos()


  def buscarProximoToken(self, listaDeTokens): 
    retornoScanner = self.scanner.SCANNER(self.tabelaEstados, self.tabelaDeSimbolos)
    if retornoScanner.classe != 'ERROR':
      listaDeTokens.append(retornoScanner)
    else:
      retornoScanner = self.scanner.SCANNER(self.tabelaEstados, self.tabelaDeSimbolos)
    #print('='*40)
    #print(retornoScanner.classe)
    #print(listaDeTokens)
  def PARSER(self):
    listaDeTokens = []
    mainAction()

    self.buscarProximoToken(listaDeTokens)
    index = 0
    token = listaDeTokens[index]

    a = token.classe.lower() # Token
    
    while True:
      # print('LINHA: ', self.scanner.linha)
      # print('COLUNA: ', self.scanner.coluna)
      # print('Token: ', token)
      # print('Pilha: ', self.pilha)
      s = self.pilha[-1]
      acao = action(s,a)
      t = acao[1:]
      if('s' in acao):
        # print('SHIFT: ', acao)
        self.pilha.append(int(t))
        self.buscarProximoToken(listaDeTokens)
        index += 1
        token = listaDeTokens[index]
        a = token.classe.lower()
        
      elif('R' in acao):
        # print('REDUCE: ', acao)

        A, B, regra = self.regras.retornaElementos(t)


        for element in B:
          desempilhar(self.pilha)

        t = self.pilha[-1]
        # print('Topo da pilha: ', t)

        self.pilha.append(int(goto(int(t),A)))
        print('Produção: ', regra)
        
      elif('a' in acao):
        print('ACCEPT')
        break
      
      else:
        sucessoPhraseRecovery = phraseRecovery(s, index, listaDeTokens, self.buscarProximoToken, self.scanner.linha, self.scanner.coluna)

        if(sucessoPhraseRecovery == False):
          index = panicMode(s, self.buscarProximoToken, listaDeTokens, index, self.scanner.linha, self.scanner.coluna)
          
        token = listaDeTokens[index]
        a = token.classe.lower()

        if (a == 'eof'):
          break