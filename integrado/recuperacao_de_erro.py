from action import *
from Token import Token

class Token:
    def __init__(self, classe: str, lexema: str, tipo: str):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

def panicMode(s, index_token, tokens):
  print('Panic Mode')
  while index_token < (len(tokens) - 1):
      token = tokens[index_token]
      a = token.classe.lower()
      acao = action(s, a)
      print('TOKEN ERRO: ', a)

      if(acao[0] != 'e'):
        print('Sucesso no panic mode: ', acao)
        # t = acao[1:]
        # pilha.append(int(t))

        return index_token
      
      index_token += 1
      
def phraseRecovery(s, index_token, tokens):
  print('Phrase Recovery Mode')
  # phraseRecoveryList = ['pt_v', 'vir', 'ab_p', 'fc_p'];
  phraseRecoveryList = ['pt_v', 'vir']
  
  tokenAnterior = tokens[index_token - 1]
  tokenAtual = tokens[index_token]

  a = tokenAtual.classe.lower()
  acaoAtual = action(s, a)

  # Removendo tokens duplicados 
  if(compararTokens(tokenAnterior, tokenAtual)):
    if(a in phraseRecoveryList):
      tokens.pop(index_token)

  # Inserindo tokens faltantes 
  elif(acaoAtual[0] == 'e'):
    pt_v = action(s, 'pt_v')
    if(pt_v[0] != 'e'):
      # tokens.insert(index_token, {'classe': 'PT_V', 'lexema': ';', 'tipo': 'NULO'})
      newToken = Token('PT_V', ';', 'NULO')
      tokens.insert(index_token, newToken)





def compararTokens(token1, token2):
  return (token1.classe, token1.lexema, token1.tipo) == (token2.classe, token2.lexema, token2.tipo)
      


def printError():
  print('Print error: ')
