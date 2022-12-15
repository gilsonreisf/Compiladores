from tabela_de_estados import TabelaDeEstados
from Tabela_de_Simbolos import Tabela_de_Simbolos
from Token import Token

class Scanner:
  def __init__(self):
    self.numero_da_coluna = 0
    self.numero_da_linha = 0
    self.lexema = ''
    self.arrayParaIdentificarColuna = []


  def scanner(self, tabelaEstados: TabelaDeEstados, arrayDeCaracteres: str, tabelaDeSimbolos: Tabela_de_Simbolos):
    char = arrayDeCaracteres
    entrada = tabelaEstados.verificaTipoCaractere(char).strip()
    if(entrada == '$'):
      if (tabelaEstados.verificarSeEstaEmEstadoFinal()):
        newToken = Token(tabelaEstados.retornaClasse(), self.lexema, tabelaEstados.retornaTipo())
        return {'mensagem': 'TOKEN', 'token': newToken}
      return {'mensagem': 'EOF', 'token': Token(classe='EOF', lexema='EOF',tipo='NULO')}
    if (tabelaEstados.verificarSeEntradaPertenceAoAlfabeto(entrada)):
      if(tabelaEstados.verificarSeProximoEstadoEValido(entrada)):
        self.lexema = self.lexema + char.strip()
        return {'mensagem': 'chamar_novamente', 'token': None}
      elif(tabelaEstados.verificarSeEFinalDefinitivo(entrada)):
          newToken = Token(tabelaEstados.retornaClasse(), self.lexema, tabelaEstados.retornaTipo())
          return {'mensagem': 'TOKEN_DIRETO', 'token': newToken}
      elif (tabelaEstados.verificarSeEstaEmEstadoFinal()):
        newToken = Token(tabelaEstados.retornaClasse(), self.lexema, tabelaEstados.retornaTipo())
        return {'mensagem': 'TOKEN', 'token': newToken}
      else:
        tabelaEstados.lancarErro(self.numero_da_linha, self.numero_da_coluna)
        return {'mensagem': None, 'token': None}
    elif(tabelaEstados.entradaVazia(char)):
      if (tabelaEstados.verificarSeEstaEmEstadoFinal()):
        newToken = Token(tabelaEstados.retornaClasse(), self.lexema, tabelaEstados.retornaTipo())
        return {'mensagem': 'TOKEN', 'token': newToken}
      elif(tabelaEstados.verificarSeComentarioOuLiteral()):
        return {'mensagem': 'tratar_literal_comentario', 'token': None}

      else:
        return {'mensagem': 'chamar_novamente', 'token': None}
    else:
      self.numero_da_coluna = self.arrayParaIdentificarColuna.index(char) + 1
      print('ERRO LÉXICO – Caracter inválido, linha {}, coluna {}'.format(self.numero_da_linha, self.numero_da_coluna))
      return {'mensagem': None, 'token': None}



  def tratarFinalDaInstrucao(self, tabelaEstados: TabelaDeEstados):
    if (tabelaEstados.verificarSeEstaEmEstadoFinal()):
      newToken = Token(tabelaEstados.retornaClasse(), self.lexema, tabelaEstados.retornaTipo())
      return {'mensagem': 'TOKEN', 'token': newToken}
    else:
      tabelaEstados.lancarErro(self.numero_da_linha, self.numero_da_coluna)
      self.lexema = ''
      return {'mensagem': None, 'token': None}




  def limpa_codigo(self, codigoFonteFormatado):
    codigo_final = []
    for line in codigoFonteFormatado:
        for caractere in line:
            codigo_final.append(caractere)
    return codigo_final
