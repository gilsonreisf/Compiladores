from action import *
from Token import Token


class Token:
    def __init__(self, classe: str, lexema: str, tipo: str):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

def panicMode(s, funcaoBuscarProximoToken, listaDeTokens, index_token, linha, coluna):
  print(f'*************** Panic Mode: linha {linha}, coluna: {coluna}')
  while True:
      token = listaDeTokens[index_token]
      a = token.classe.lower()
      acao = action(s, a)

      if(acao[0] != 'e'):
        print('******* Sucesso no panic mode: ', acao)
        return index_token

      if(a == 'eof'):
        print('Fim de arquivo')
        return index_token
      
      
      val = funcaoBuscarProximoToken(listaDeTokens)
      if val == 1:
        index_token += 1
      else:
        index_token = index_token



def phraseRecovery(s, index_token, listaDeTokens: list, funcaoBuscarProximoToken, linha, coluna):
  #print(f'############### Phrase Recovery Mode:')
  # phraseRecoveryList = ['pt_v', 'vir', 'ab_p', 'fc_p'];
  phraseRecoveryList = ['pt_v', 'vir']
  
  tokenAnterior = listaDeTokens[index_token - 1]
  tokenAtual = listaDeTokens[index_token]


  a = tokenAtual.classe.lower()

    
    
  acaoAtual = action(s, a)
  # Removendo tokens duplicados 
  if(compararTokens(tokenAnterior, tokenAtual)):
    if(a in phraseRecoveryList):
      listaDeTokens.pop(index_token)
      funcaoBuscarProximoToken(listaDeTokens)
      #print('####### Sucesso no phrase recovery: ', acaoAtual)
      return True

  # Inserindo tokens faltantes 
  elif(acaoAtual[0] == 'e'):
    pt_v = action(s, 'pt_v')
    if(pt_v[0] != 'e'):
      newToken = Token('PT_V', ';', 'NULO')
      
      print(f'Erro sintático -- Ponto e Vírgula Faltante em  linha {linha}, coluna: {coluna}')
      
      listaDeTokens.insert(index_token, newToken)
      #print('############### Sucesso no phrase recovery: ', pt_v)
      return True
  
  return False





def compararTokens(token1, token2):
  return (token1.classe, token1.lexema, token1.tipo) == (token2.classe, token2.lexema, token2.tipo)
      


def printError():
  print('Print error: ')
