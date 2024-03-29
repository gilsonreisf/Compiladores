from goto import *
from action import *
from funcoes_auxiliares_sintatico import *
from recuperacao_de_erro import *
from regras import Regras
from scanner import Scanner
from tabela_de_estados import TabelaDeEstados
from tabela_de_simbolos import TabelaDeSimbolos
from semantico import *
from semantico import Semantico
from funcoes_auxiliares_semantico import *


class Parser2:
  def __init__(self):
    self.pilha = [0]
    self.regras = Regras()
    self.scanner = Scanner("codigo.txt")
    self.tabelaEstados = TabelaDeEstados()
    self.tabelaDeSimbolos = TabelaDeSimbolos()
    self.Semantico = Semantico('', '', 0)
    
    


  def buscarProximoToken(self, listaDeTokens): 
    retornoScanner = self.scanner.SCANNER(self.tabelaEstados, self.tabelaDeSimbolos)
    if retornoScanner.classe != 'ERROR':
      listaDeTokens.append(retornoScanner)
      return 1
    else:
      retornoScanner = self.buscarProximoToken(listaDeTokens)
      return 0
    
  def PARSER(self):
    listaDeTokens = []
    mainAction()

    self.buscarProximoToken(listaDeTokens)
    index = 0
    token = listaDeTokens[index]

    a = token.classe.lower()
    
    while True:
      s = self.pilha[-1]
      acao = action(s,a)
      t = acao[1:]
      
      if('s' in acao):
        self.pilha.append(int(t))
        
        self.Semantico.pilha_semantica.append(token)
        
        val = self.buscarProximoToken(listaDeTokens)
        index += 1
        token = listaDeTokens[index]
        a = token.classe.lower()

      elif('R' in acao):

        A, B, regra = self.regras.retornaElementos(t)
        
        taux = t
      
        for element in B:
            desempilhar(self.pilha)
            

            
        t = self.pilha[-1]
        
        self.pilha.append(int(goto(int(t),A)))
      
        #print('Produção: ', regra)
        
        var_semantico = self.Semantico.ativa_semantico(taux, A, B, token, self.tabelaDeSimbolos)
        
        for i in range(len(B)):
            desempilhar(self.Semantico.pilha_semantica)
        
        self.Semantico.pilha_semantica.append(var_semantico)
        
        #print(f' ============== {self.Semantico.pilha_semantica}')
        
      elif('a' in acao):
        print('ACCEPT')
        print(self.tabelaDeSimbolos.imprimirTabela())
        #print(self.Semantico.programa_objeto)
        inicia_arquivo_objeto(self.Semantico.programa_objeto, self.Semantico.variaveis_temporarias)
        break
      
      else:
        sucessoPhraseRecovery = phraseRecovery(s, index, listaDeTokens, self.buscarProximoToken, self.scanner.linha2, self.scanner.coluna2)
        if(sucessoPhraseRecovery == False):
          index = panicMode(s, self.buscarProximoToken, listaDeTokens, index, self.scanner.linha, self.scanner.coluna)
          
        token = listaDeTokens[index]
        a = token.classe.lower()

        if (a == 'eof'):
          break