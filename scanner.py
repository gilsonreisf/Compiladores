
from tabela_de_estados import TabelaDeEstados
from Tabela_de_Simbolos import Tabela_de_Simbolos
from Token import Token

def construir_token(tabela_de_simbolos, tabela_de_estados, lexema):
  classe = tabela_de_estados.retornaClasse()
  tipo = tabela_de_estados.retornaTipo()
  if classe == 'id':
    token = tabela_de_simbolos.buscar_token(Token(classe, lexema, tipo))
    if token == None:
      token = Token(classe, lexema, tipo)
    
    return token
  else:
    return Token(classe, lexema, tipo)


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
    self.arrayParaIdentificarColuna = []


  def scanner(self, tabelaEstados: TabelaDeEstados, arrayDeCaracteres: list[str]):
    while(arrayDeCaracteres):
      char = arrayDeCaracteres[0]
      entrada = tabelaEstados.verificaTipoCaractere(char).strip()
      if(entrada == '$'):
        if(tabelaEstados.verificarSeEstaEmEstadoFinal()):
          print('Token: ', self.lexema) # Adiciona penúltimo token na tabela de símbolos
          self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, 
                                      token=Token(classe = self.tabelaEstados.retornaClasse(), 
                                                  lexema = self.lexema, 
                                                  tipo = self.tabelaEstados.retornaTipo()))
          #self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, token=Token(classe='EOF', lexema='EOF',tipo='NULO'))
          print('Fim de arquivo - Token EOF ')
          arrayDeCaracteres = []
          tabelaEstados.estado_atual = 0
          self.lexema = ''
          # Adiciona token na tabela de símbolos Token(EOF)
        else:
          tabelaEstados.lancarErro(self.numero_da_linha)
          arrayDeCaracteres.remove(char)
          self.lexema = ''
      elif (tabelaEstados.verificarSeEntradaPertenceAoAlfabeto(entrada)):
        if(tabelaEstados.verificarSeProximoEstadoEValido(entrada)):
          self.lexema = self.lexema + char.strip()
          arrayDeCaracteres.remove(char)
          self.scanner(tabelaEstados, arrayDeCaracteres)
        elif (tabelaEstados.verificarSeEstaEmEstadoFinal()):
          print('Token: ', self.lexema)
          self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, 
                                                token=Token(classe = self.tabelaEstados.retornaClasse(), 
                                                            lexema = self.lexema, 
                                                            tipo = self.tabelaEstados.retornaTipo()))
          tabelaEstados.estado_atual = 0
          self.lexema = ''
          # Adiciona token na tabela de símbolos
        else:
          tabelaEstados.lancarErro(self.numero_da_linha)
          arrayDeCaracteres.remove(char)
          self.lexema = ''
      elif(tabelaEstados.entradaVazia(char)):
        arrayDeCaracteres.remove(char)
        continue
      else:
        self.numero_da_coluna = self.arrayParaIdentificarColuna.index(char) + 1
        print('ERRO LÉXICO – Caracter inválido, linha {}, coluna {}'.format(self.numero_da_linha, self.numero_da_coluna) )
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
      arrayDeCaracteres = self.limpa_codigo(linha)
      self.arrayParaIdentificarColuna = arrayDeCaracteres.copy()
      self.numero_da_linha += 1
      self.scanner(tabelaEstados, arrayDeCaracteres)
