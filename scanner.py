
from tabela_de_estados import TabelaDeEstados
from Tabela_de_Simbolos import Tabela_de_Simbolos
from Token import Token

class Scanner:
  def __init__(self, codigoFonte):
    self.numero_da_coluna = 0
    self.numero_da_linha = 0
    self.codigoFonte = codigoFonte
    self.tamanhoDoCodigo = len(codigoFonte)
    self.tamanhoDaLinha = len(codigoFonte[self.numero_da_linha])
    self.lista_de_textos = []
    self.lexema = ''
    self.Tabela_de_Simbolos = Tabela_de_Simbolos()

    self.codigoFonte = ['a' , 'b'] + ['$'] #codigo
                    #codigo fonte  +  EOF fixo


  def scanner(self, tabelaEstados: TabelaDeEstados):
    while(self.codigoFonte):
      char = self.codigoFonte[0]
      entrada = tabelaEstados.verificaTipoCaractere(char)
      if(entrada == '$'):
        if(tabelaEstados.verificarSeEstaEmEstadoFinal()):
          print('Token: ', self.lexema) # Adiciona penúltimo token na tabela de símbolos
          self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, 
                                      token=Token(classe = self.tabelaEstados.retornaClasse(), 
                                                  lexema = self.lexema, 
                                                  tipo = self.tabelaEstados.retornaTipo()))
          #self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, token=Token(classe='EOF', lexema='EOF',tipo='NULO'))
          print('Fim de arquivo - Token EOF ')
          self.codigoFonte = []
          tabelaEstados.estado_atual = 0
          self.lexema = ''
          return 'FINAL DE ARQUIVO' # Adiciona último token na tabela de símbolos Token(EOF)
        else:
          linhaFake = '1'
          self.lexema = ''
          tabelaEstados.lancarErro(linhaFake)
          self.codigoFonte.remove(char)
      elif (tabelaEstados.verificarSeEntradaPertenceAoAlfabeto(entrada)):
        if(tabelaEstados.verificarSeProximoEstadoEValido(entrada)):
          self.lexema = self.lexema + entrada
          self.codigoFonte.remove(char)
          self.scanner(tabelaEstados)
        elif (tabelaEstados.verificarSeEstaEmEstadoFinal()):
          print('Token: ', self.lexema)
          self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, 
                                                token=Token(classe = self.tabelaEstados.retornaClasse(), 
                                                            lexema = self.lexema, 
                                                            tipo = self.tabelaEstados.retornaTipo()))
          tabelaEstados.estado_atual = 0
          self.lexema = ''
          return entrada # Adiciona token na tabela de símbolos
        else:
          linhaFake = '1'
          self.lexema = ''
          tabelaEstados.lancarErro(linhaFake)
          self.codigoFonte.remove(char)

      else:
        linhaFake = '1'
        print('ERRO LÉXICO – Caracter inválido, linha', entrada)
        self.lexema = ''
        self.codigoFonte.remove(char)
        tabelaEstados.estado_atual = 0

  def construir_token(tabela_de_estados, lexema, classe, tipo):
    token = Token(classe = tabela_de_estados.retornaClasse(), 
                  lexema = lexema, 
                  tipo = 
                  )
        
