from tabela_de_estados import TabelaDeEstados
from Tabela_de_Simbolos import Tabela_de_Simbolos
from Token import Token
class Scanner:
  def __init__(self, codigoFonte):
    self.numero_da_coluna = 0
    self.numero_da_linha = 0
    self.codigoFonte = codigoFonte
    self.lexema = ''
    self.Tabela_de_Simbolos = Tabela_de_Simbolos()
    self.arrayParaIdentificarColuna = []


def construir_token(self, tabela_de_simbolos, tabela_de_estados, lexema):
  classe = tabela_de_estados.retornaClasse()
  tipo = tabela_de_estados.retornaTipo()
  if classe == 'id':
    token = tabela_de_simbolos.buscar_token(Token(classe, lexema, tipo))
    if token == None:
      token = tabela_de_simbolos.inserir_token(Token(classe, lexema, tipo))

    return token
  else:
    return Token(classe, lexema, tipo)

  def scanner(self, tabelaEstados: TabelaDeEstados, arrayDeCaracteres: str, finalDaInstrucao = False):
    char = arrayDeCaracteres
    entrada = tabelaEstados.verificaTipoCaractere(char).strip()
    if(entrada == '$'):
      if (tabelaEstados.verificarSeEstaEmEstadoFinal()):
        #self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, 
        #                                      token=Token(classe = tabelaEstados.retornaClasse(), 
        #                                                  lexema = self.lexema, 
        #                                                  tipo = tabelaEstados.retornaTipo()))
        print('TOKEN - Classe: {}, Lexema: {}, Tipo: {}'.format(tabelaEstados.retornaClasse(), self.lexema, tabelaEstados.retornaTipo()))
        tabelaEstados.estado_atual = 0
        self.lexema = ''
        return 'TOKEN'
      else:
        tabelaEstados.lancarErro(self.numero_da_linha)
        self.lexema = ''
        print('TOKEN - Classe: EOF, Lexema: EOF, Tipo: EOF')
        #self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, token=Token(classe='EOF', lexema='EOF',tipo='NULO'))
      return 'EOF'
    if (tabelaEstados.verificarSeEntradaPertenceAoAlfabeto(entrada)):
      if(tabelaEstados.verificarSeProximoEstadoEValido(entrada)):
        self.lexema = self.lexema + char.strip()
        # arrayDeCaracteres.remove(char)
        # self.scanner(tabelaEstados, arrayDeCaracteres)
        # continue
        return 'chamar_novamente'
      elif (tabelaEstados.verificarSeEstaEmEstadoFinal()):
        #self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, 
        #                                      token=Token(classe = tabelaEstados.retornaClasse(), 
        #                                                  lexema = self.lexema, 
        #                                                  tipo = tabelaEstados.retornaTipo()))
        print('TOKEN - Classe: {}, Lexema: {}, Tipo: {}'.format(tabelaEstados.retornaClasse(), self.lexema, tabelaEstados.retornaTipo()))
        tabelaEstados.estado_atual = 0
        self.lexema = ''
        return 'TOKEN'
      else:
        tabelaEstados.lancarErro(self.numero_da_linha)
        self.lexema = ''
    elif(tabelaEstados.entradaVazia(char)):
      return
    else:
      self.numero_da_coluna = self.arrayParaIdentificarColuna.index(char) + 1
      print('ERRO LÉXICO – Caracter inválido, linha {}, coluna {}'.format(self.numero_da_linha, self.numero_da_coluna))
      self.lexema = ''
      tabelaEstados.estado_atual = 0
    if (tabelaEstados.verificarSeEstaEmEstadoFinal()):
      #self.Tabela_de_Simbolos.inserir_token(self.Tabela_de_Simbolos, 
      #                                      token=Token(classe = tabelaEstados.retornaClasse(), 
      #                                                  lexema = self.lexema, 
      #                                                  tipo = tabelaEstados.retornaTipo()))
      print('TOKEN - Classe: {}, Lexema: {}, Tipo: {}'.format(tabelaEstados.retornaClasse(), self.lexema, tabelaEstados.retornaTipo()))
      tabelaEstados.estado_atual = 0
      self.lexema = ''
      return 'TOKEN'
    else:
      tabelaEstados.lancarErro(self.numero_da_linha)
      self.lexema = ''
      return



  def limpa_codigo(self, codigoFonteFormatado):
    codigo_final = []
    for line in codigoFonteFormatado:
        for caractere in line:
            codigo_final.append(caractere)
    return codigo_final

  def scannerMain(self, tabelaEstados: TabelaDeEstados, codigoFonte):
    for linha in codigoFonte:
      finalDaInstrucao = False
      print('-'*30)
      arrayDeCaracteres = self.limpa_codigo(linha)
      self.arrayParaIdentificarColuna = arrayDeCaracteres.copy()

      self.numero_da_linha += 1
      coluna = 0
      retorno = self.scanner(tabelaEstados, arrayDeCaracteres[0].replace(" ", ""))
      print('Retorno 1: ', retorno)
      if(retorno != 'TOKEN'):
        arrayDeCaracteres.pop(0)



      if(retorno == 'EOF'):
        return # Final do arquivo
      while(retorno != 'EOF' and len(arrayDeCaracteres) != 0):
        if(retorno == 'chamar_novamente'):
          coluna += 1
          retorno = self.scanner(tabelaEstados, arrayDeCaracteres[0].replace(" ", ""))
          if(retorno != 'TOKEN'):
            arrayDeCaracteres.pop(0)
          print('Retorno 2: ', retorno)
        elif(retorno == 'TOKEN'):
          retorno = self.scanner(tabelaEstados, arrayDeCaracteres[0].replace(" ", ""))
          print('Retorno 3: ', retorno)
          arrayDeCaracteres.pop(0)
        elif(retorno == None):
          arrayDeCaracteres.pop(0)


      finalDaInstrucao = True
      retorno = self.scanner(tabelaEstados, '', True)
      




    