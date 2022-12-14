class TabelaDeEstados:
  def __init__(self):

    self.letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    self.digitos = ['0','1','2','3','4','5','6','7','8','9']

    self.simbolos = ['"', '.', '_', '{', '}', '<', '>', '=', '-', '+', '*', '/', '(', ')', ';', ',', ':', '\\']

    self.espacos_vazios = [' ', '\n', '\t']

    self.alfabeto = self.letras + self.digitos + self.simbolos + self.espacos_vazios

    self.tabela_de_estados = {

          0: {'D':1, '"':7, 'L':10, '{':12, '$':15, '<':16, '>':26, '=':28, '+':18, '-':18, '*':18, '/':18, '(':19, ')':20, ';':21, ',':22, ' ': 0, '\n': 0, '\t': 0},       

          1: {'D':1, '.':2, 'E':4, 'e':4},

          2: {'D':3},      

          3: {'D':3, 'E':4, 'e':4},     

          4: {'D':6, '+':5, '-':5},

          5: {'D':6},

          6: {'D':6},

          7: {'qualquerCoisa': 8, '"': 9},

          8: {'qualquerCoisa': 8, '"': 9},    

          9: {},

          10: {'D':11, 'L':11, '_':11},

          11: {'D':11, 'L':11, '_':11},

          12: {'qualquerCoisa': 13, '}': 14},

          13: {'qualquerCoisa': 13, '}': 14},

          14: {},

          15: {},

          16: {'-': 17, '>': 25, '=': 24},

          17: {},

          18: {},

          19: {},

          20: {},

          21: {},

          22: {},

          23: {},

          24: {},

          25: {},

          26: {'=': 27},

          27: {},

          28: {},

        }


    self.estados_finais = {
      1:"Num",
      3:"Num",
      6:"Num",
      9:"Lit",
      10:"id",
      11:"id",
      14:"Comentário",
      15:"EOF",
      16:"OPR",
      17:"ATR",
      18:"OPA",
      19:"AB_P",
      20:"FC_P",
      21:"PT_V",
      22:"VIR",
      23:"ERRO",
      24:"OPR",
      25:"OPR",
      26:"OPR",
      27:"OPR",
      28:"OPR",
    }

    self.estados_não_finais = {
      0:"Caracter inválido",
      2:"Num incompleto",
      4:"Num incompleto",
      5:"Num incompleto",
      7:"Literal incompleto",
      8:"Literal incompleto",
      12:"Comentário incompleto",
      13:"Comentário incompleto",
    }

    self.estado_atual = 0


  def irParaProximoEstado(self, char):
    try:
      self.estado_atual = self.tabela_de_estados[self.estado_atual][char]
    except KeyError:
      raise KeyError

  def verificarSeComentarioOuLiteral(self):
    estadosDeLiteral = [7, 8]
    estadosDeComentario = [12, 13]
    if((self.estado_atual in estadosDeLiteral) or (self.estado_atual in estadosDeComentario)):
      return True
    else: 
      return False


  def lancarErro(self, linha, coluna):
    print('ERRO LÉXICO – {}, linha {}, coluna {}'.format(self.estados_não_finais[self.estado_atual], linha, coluna))

  def verificaTipoCaractere(self, char):
    estadosDeDigitos = [1, 3]
    estadosDeLiteral = [7, 8]
    estadosDeComentario = [12, 13]

    if((self.estado_atual in estadosDeLiteral) and char != '"') or ((self.estado_atual in estadosDeComentario) and char != '}'): #Tratamento para comentário e literal
      return 'qualquerCoisa'
          
    if (char in self.letras):
      if(self.estado_atual in estadosDeDigitos):
        return 'E'
      return 'L'
    elif (char in self.digitos):
          return 'D'
    return char

  def verificarSeEntradaPertenceAoAlfabeto(self, char):
    if (char in self.alfabeto):
      return True
    else: 
      return False

  def retornaClasse(self):
    return self.estados_finais[self.estado_atual]

  def retornaTipo(self):
    classe = self.retornaClasse()

    if classe == 'Num':
      if self.estado_atual == 1:
        return 'inteiro'
      elif (self.estado_atual == 3) or (self.estado_atual == 6):
        return 'real'
    elif classe == 'Lit':
      return 'literal'
    elif classe == 'id':
      return 'NULO'
    elif classe == 'ERRO':
      return 'NULO'
    else:
      return 'NULO'
