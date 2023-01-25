from action import *
from Token import Token


class Token:
    def __init__(self, classe: str, lexema: str, tipo: str):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

def panicMode(s, funcaoBuscarProximoToken, listaDeTokens, index_token, linha, coluna):
  print(f'ERRO SINTÁTICO - sintaxe incorreta. Linha {linha}, coluna: {coluna -1}')
  while True:
      token = listaDeTokens[index_token]
      a = token.classe.lower()
      acao = action(s, a)

      if(acao[0] != 'e'):
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
  phraseRecoveryList = ['pt_v', 'vir', 'opa']
  
  tokenAnterior = listaDeTokens[index_token - 1]
  tokenAtual = listaDeTokens[index_token]


  a = tokenAtual.classe.lower()

    
    
  acaoAtual = action(s, a)
  if(compararTokens(tokenAnterior, tokenAtual)):
    if(a in phraseRecoveryList):
      listaDeTokens.pop(index_token)
      funcaoBuscarProximoToken(listaDeTokens)
      print(f'ERRO SINTÁTICO - Caractere "{tokenAtual.lexema}" duplicado. Linha {linha + 1}, coluna: {coluna -1}')
      return True

  elif(acaoAtual[0] == 'e'):
    pt_v = action(s, 'pt_v')
    if(pt_v[0] != 'e'):
      newToken = Token('PT_V', ';', 'NULO')
      listaDeTokens.insert(index_token, newToken)
      print(f'ERRO SINTÁTICO - Ponto e Vírgula Faltante. Linha {linha}, coluna: {coluna -1}')
      return True
  
  return False





def compararTokens(token1, token2):
  return (token1.classe, token1.lexema, token1.tipo) == (token2.classe, token2.lexema, token2.tipo)
      