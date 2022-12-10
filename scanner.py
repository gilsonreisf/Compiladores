
from tabela_de_estados import TabelaDeEstados


class Scanner2:
  # def __init__(self, codigoFonte):
    # self.numLinha = 0
    # self.numColuna = 0
    # self.codigoFonte = codigoFonte
    # self.tamanhoDoCodigo = len(codigoFonte)
    # self.tamanhoDaLinha = len(codigoFonte[self.numLinha])
    # self.tabelaDeSimbolos = ts.TabelaDeSimbolos()
    # self.listaDeTextos = []
  def __init__(self):
    self.codigoFonte = ['a' , 'b'] + ['$'] #codigo
    self.lexema = ''


  def scanner(self, tabelaEstados: TabelaDeEstados):
    while(self.codigoFonte):
      char = self.codigoFonte[0]
      entrada = tabelaEstados.verificaTipoCaractere(char)
      if(entrada == '$'):
        if(tabelaEstados.verificarSeEstaEmEstadoFinal()):
          print('Token: ', self.lexema) # Adiciona penúltimo token na tabela de símbolos
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


        
