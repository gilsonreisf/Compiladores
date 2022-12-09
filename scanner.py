
from tabela_de_estados import TabelaDeEstados


class Scanner:
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
    for char in self.codigoFonte:
      entrada = tabelaEstados.verificaTipoCaractere(char)
      print(entrada)
      if(entrada == '$'):
          return 'FINAL DE ARQUIVO' # Token(EOF)
      elif (tabelaEstados.verificarSeEntradaPertenceAoAlfabeto(entrada)):
        if(tabelaEstados.verificarSeProximoEstadoEValido(entrada)):
          self.lexema = self.lexema + entrada
          # self.scanner(tabelaEstados) # Como q faz recursividade nessa porra ???
        elif (tabelaEstados.verificarSeEstaEmEstadoFinal(entrada)):
          self.lexema = ''
          return entrada # Retorna token da entrada
      else:
        self.lexema = ''
        print('ENTRADA: ', entrada)
        tabelaEstados.lancarErro('2')


        
