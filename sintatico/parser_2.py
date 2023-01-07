# (1) Seja a o primeiro símbolo de w$;
# (2) while { /*Repita indefinidamente*/
# (3) seja s o estado no topo da pilha;
# (4) if (ACTION [s,a] = shift t ) {
# (5) empilha t na pilha;
# (6) seja a o próximo símbolo da entrada;
# (7) }else if (ACTION [s,a] = reduce A-> β ) {
# (8) desempilha símbolos | β | da pilha;
# (9) faça o estado t agora ser o topo da pilha;
# (10) empilhe GOTO[t,A] na pilha;
# (11) imprima a produção A-> β ;
# (12) }else if (ACTION [s,a] = accept ) pare; /* a análise terminou*/
# (13) else chame uma rotina de recuperação do erro;

from goto import *
from action import *
from funcoes_auxiliares_sintatico import *
from recuperacao_de_erro import *
from regras import Regras
import json



class Parser2:
  def __init__(self):
    self.pilha = [0]



  def PARSER(self):
    mainAction()
    with open("tokens.json", "r") as f:
      listaDeTokens = json.load(f)
    regras = Regras()


    index = 0
    token = listaDeTokens[index]

    a = token['classe'].lower() # Token
    
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
        index += 1
        token = listaDeTokens[index]
        a = token['classe'].lower()

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
        a = token['classe'].lower()
