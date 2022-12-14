
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


  def scanner(self, tabelaEstados: TabelaDeEstados, arrayDeCaracteres: list[str]):
    print('CODIGO: ', arrayDeCaracteres)
    while(arrayDeCaracteres):
      char = arrayDeCaracteres[0]
      entrada = tabelaEstados.verificaTipoCaractere(char).strip()
      if(entrada == '$'):
        if(tabelaEstados.verificarSeEstaEmEstadoFinal()):
          # Adiciona penúltimo token na tabela de símbolos
          #self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, 
          #                            token=Token(classe = tabelaEstados.retornaClasse(), 
          #                                        lexema = self.lexema, 
          #                                        tipo = tabelaEstados.retornaTipo()))
          print('Classe: ', tabelaEstados.retornaClasse())
          print('Lexema: ', self.lexema)
          print('Tipo: ', tabelaEstados.retornaTipo())
          print('='*15)
          #self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, token=Token(classe='EOF', lexema='EOF',tipo='NULO'))
          print('Fim de arquivo - Token EOF ')
          arrayDeCaracteres = []
          tabelaEstados.estado_atual = 0
          self.lexema = ''
          return 'FINAL DE ARQUIVO' # Adiciona último token na tabela de símbolos Token(EOF)
        else:
          print('LEXEMA 1: ', self.lexema)
          tabelaEstados.lancarErro(self.numero_da_linha)
          arrayDeCaracteres.remove(char)
          self.lexema = ''
      elif (tabelaEstados.verificarSeEntradaPertenceAoAlfabeto(entrada)):
        if(tabelaEstados.verificarSeProximoEstadoEValido(entrada)):
          self.lexema = self.lexema + char.strip()
          arrayDeCaracteres.remove(char)
          self.scanner(tabelaEstados, arrayDeCaracteres)
        elif (tabelaEstados.verificarSeEstaEmEstadoFinal()):
          #self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, 
          #                                      token=Token(classe = tabelaEstados.retornaClasse(), 
          #                                                  lexema = self.lexema, 
          #                                                  tipo = tabelaEstados.retornaTipo()))
          print('Classe: ', tabelaEstados.retornaClasse())
          print('Lexema: ', self.lexema)
          print('Tipo: ', tabelaEstados.retornaTipo())
          print('='*15)
          tabelaEstados.estado_atual = 0
          self.lexema = ''
          return entrada # Adiciona token na tabela de símbolos
        else:
          print('LEXEMA 2: ', self.lexema)
          tabelaEstados.lancarErro(self.numero_da_linha)
          arrayDeCaracteres.remove(char)
          self.lexema = ''
      elif(tabelaEstados.entradaVazia(char)):
        arrayDeCaracteres.remove(char)
        print('ENTRADA VAZIA')
        continue
      else:
        self.numero_da_coluna = arrayDeCaracteres.index(char)
        
        print('LEXEMA 3: ', self.lexema)
        print('ERRO LÉXICO – Caracter inválido, linha', self.numero_da_linha)
        print('ERRO LÉXICO – Caracter inválido, COLUNA', self.numero_da_coluna)
        self.lexema = ''
        arrayDeCaracteres.remove(char)
        tabelaEstados.estado_atual = 0


  def limpa_codigo(self, codigoFonteFormatado):
    codigo_final = []
    for line in codigoFonteFormatado:
        for caractere in line:
            codigo_final.append(caractere)
    return codigo_final

  def scannerMain(self, tabelaEstados: TabelaDeEstados, codigoFonte):
    for linha in codigoFonte:
      codigoFormatado = self.limpa_codigo(linha)
      print('-'*30)
      self.numero_da_linha += 1
      print('Linha: ', linha)
      print('NUMERO LINHA: ', self.numero_da_linha)
      self.scanner(tabelaEstados, codigoFormatado)
