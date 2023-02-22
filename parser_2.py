from goto import *
from action import *
from funcoes_auxiliares_sintatico import *
from recuperacao_de_erro import *
from regras import Regras
from scanner import Scanner
from tabela_de_estados import TabelaDeEstados
from tabela_de_simbolos import TabelaDeSimbolos
from semantico import *


class Parser2:
  def __init__(self):
    self.pilha = [0]
    self.regras = Regras()
    self.scanner = Scanner("codigo.txt")
    self.tabelaEstados = TabelaDeEstados()
    self.tabelaDeSimbolos = TabelaDeSimbolos()
    self.programa_objeto = ''


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
        val = self.buscarProximoToken(listaDeTokens)
        index += 1
        token = listaDeTokens[index]
        a = token.classe.lower()
        #tipo = token.tipo
        #lexema = token.lexema
        
        #print(f' Classe: {a} \n Tipo: {tipo} \n Lexema {lexema}')
      elif('R' in acao):

        A, B, regra = self.regras.retornaElementos(t)
        
        for element in B:
            desempilhar(self.pilha)
        #print("=_"*20)
        #print(f"Redução: -----> {t}")
        #print("=_"*20)
        t = self.pilha[-1]
        print(self.pilha[-1])
        self.pilha.append(int(goto(int(t),A)))
        
        print('Produção: ', regra)
        
        self.programa_objeto += str(semantico(t, token, A, B, self.tabelaDeSimbolos))

        

        

        

        
        #self.programa_objeto += semantico(t, token, A, B)
        
        
        
        #print(self.tabelaDeSimbolos.imprimirTabela())
        #print('=='*20)
        #print(f'A: {A} \n B: {B} \n Regra: {regra}')
        #print(f'Token: {token}')
        #print(f't: {t}')
        #print('=='*20)
        
      elif('a' in acao):
        print('ACCEPT')
        print(self.programa_objeto)
        #print(self.tabelaDeSimbolos.imprimirTabela())
        #inicia_programa_objeto()
        #escreve_string_no_objeto
        break
      
      else:
        sucessoPhraseRecovery = phraseRecovery(s, index, listaDeTokens, self.buscarProximoToken, self.scanner.linha2, self.scanner.coluna2)
        if(sucessoPhraseRecovery == False):
          index = panicMode(s, self.buscarProximoToken, listaDeTokens, index, self.scanner.linha, self.scanner.coluna)
          
        token = listaDeTokens[index]
        a = token.classe.lower()

        if (a == 'eof'):
          break