from tabela_de_estados import TabelaDeEstados
from Tabela_de_Simbolos import Tabela_de_Simbolos
from Token import Token

def construir_token(tabela_de_simbolos, tabela_de_estados, lexema):
  classe = tabela_de_estados.retornaClasse()
  tipo = tabela_de_estados.retornaTipo()
  print('_'*20)
  print(tipo)
  print('_'*20)
  if classe == 'id':
    token = tabela_de_simbolos.buscar_token(Token(classe, lexema, tipo))
    if token == None:
      token = Token(classe, lexema, tipo)
    tabela_de_simbolos.inserir_token(token)
    return token
  else:
    token = Token(classe, lexema, tipo)
    tabela_de_simbolos.inserir_token(token)
    return token

class Scanner:
    def __init__(self, codigo_fonte):
        self.numero_da_coluna = 0
        self.numero_da_linha = 0
        self.codigo_fonte = codigo_fonte + ['$']
        print(self.codigo_fonte)
        self.tamanho_do_codigo = len(codigo_fonte)
        self.tamanho_da_linha = len(codigo_fonte[self.numero_da_linha])
        self.lista_de_textos = []
        self.lexema = ''
        self.Tabela_de_Simbolos = Tabela_de_Simbolos()
        self.tabela_de_estados = TabelaDeEstados()

    def scanner(self):
        self.lexema = ""
        caractere_invalido = False
        self.tabela_de_estados = TabelaDeEstados()
        while(self.numero_da_linha < self.tamanho_do_codigo):
            self.tamanho_da_linha = len(self.codigo_fonte[self.numero_da_linha])
            while(self.numero_da_coluna < self.tamanho_da_linha - 1):
                char = self.codigo_fonte[self.numero_da_linha][self.numero_da_coluna]

                if char == '$':
                    return Token(classe='EOF', lexema='EOF', tipo='NULO')
                elif (char in self.tabela_de_estados.alfabeto):
                    estado = self.tabela_de_estados.verificaTipoCaractere(char)
                    if (self.tabela_de_estados.verificarSeProximoEstadoEValido(estado)):
                        self.lexema = self.lexema + char
                        self.numero_da_coluna = self.numero_da_coluna + 1
                    else:
                        if(self.tabela_de_estados.verificarSeEstaEmEstadoFinal()):
                            token = construir_token(self.Tabela_de_Simbolos, self.tabela_de_estados, self.lexema)
                            self.lexema = ""
                            if(token.classe == 'Comentário'):
                                self.tabela_de_estados = TabelaDeEstados()
                            else:
                                return token
                        else:
                            self.tabela_de_estados.lancarErro(self.numero_da_linha + 1)
                            caractere_invalido = True
                            self.lexema = ""
                            self.numero_da_coluna = self.numero_da_coluna + 1
                else:
                    print(f"Erro Léxico -- Caractere Inválido na linha: {self.numero_da_linha + 1}") 
                    self.numero_da_coluna = self.numero_da_coluna + 1
                    caractere_invalido = True   
                    self.tabela_de_estados.estado_atual = 0
                    self.lexema = ""

            self.numero_da_coluna = 0
            self.numero_da_linha = self.numero_da_linha + 1

            if(self.tabela_de_estados.verificarSeEstaEmEstadoFinal()):
                token = construir_token(self.Tabela_de_Simbolos, self.tabela_de_estados, self.lexema)
                self.lexema = ""
                if(token.classe == 'Comentário'):
                    self.tabela_de_estados = TabelaDeEstados()
                else:
                    return token
            else:
                if not(caractere_invalido):
                    self.tabela_de_estados.lancarErro(self.numero_da_linha + 1)
                    self.lexema = ""
                    caractere_invalido = False
                
