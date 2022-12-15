from tabela_de_estados import TabelaDeEstados
from Tabela_de_Simbolos import Tabela_de_Simbolos
from Token import Token
from scanner import Scanner

arquivo = open("teste.txt", "r+", encoding="utf-8")
codigoFonte = arquivo.readlines()

def limpa_codigo(codigoFonte):
  novo_codigo = []
  ultimo_elemento = codigoFonte[-1]
  for i in codigoFonte:
    if(i.strip() == ultimo_elemento.strip()):
      i = i + '\n'
    nova_string = bytes(i, "utf-8").decode("unicode_escape")
    novo_codigo.append(nova_string[:][:-1])
  novo_codigo.append('$')
  return novo_codigo
  
codigoFormatado = limpa_codigo(codigoFonte)

def main(tabelaEstados: TabelaDeEstados, codigoFonte, tabelaDeSimbolos: Tabela_de_Simbolos, scanner: Scanner):
    for linha in codigoFonte:

      arrayDeCaracteres = scanner.limpa_codigo(linha)
      scanner.arrayParaIdentificarColuna = arrayDeCaracteres.copy()

      scanner.numero_da_linha += 1
      coluna = 0
      retorno = scanner.scanner(tabelaEstados, arrayDeCaracteres[0].replace(" ", ""), tabelaDeSimbolos)
      arrayDeCaracteres.pop(0)

      if(retorno['mensagem'] == 'EOF'):
        print('TOKEN - Classe: EOF, Lexema: EOF, Tipo: EOF')
        return # Final do arquivo
      while(retorno['mensagem'] != 'EOF' and len(arrayDeCaracteres) != 0):
        if(retorno['mensagem'] == 'chamar_novamente'):
          coluna += 1
          retorno = scanner.scanner(tabelaEstados, arrayDeCaracteres[0].replace(" ", ""), tabelaDeSimbolos)
          if(retorno['mensagem'] != 'TOKEN' and retorno['mensagem'] != 'TOKEN_DIRETO'):
            arrayDeCaracteres.pop(0)
          continue
        elif(retorno['mensagem'] == 'TOKEN'):
          tokenTabela = tabelaDeSimbolos.construir_token(tabelaEstados, retorno['token'].lexema)
          print('TOKEN - Classe: {}, Lexema: {}, Tipo: {}'.format(tokenTabela.classe, tokenTabela.lexema, tokenTabela.tipo))
          tabelaEstados.estado_atual = 0
          scanner.lexema = ''
          retorno = scanner.scanner(tabelaEstados, arrayDeCaracteres[0].replace(" ", ""), tabelaDeSimbolos)
          arrayDeCaracteres.pop(0)
          continue
        elif(retorno['mensagem'] == 'TOKEN_DIRETO'):
          tokenTabela = tabelaDeSimbolos.construir_token(tabelaEstados, retorno['token'].lexema)
          print('TOKEN - Classe: {}, Lexema: {}, Tipo: {}'.format(tokenTabela.classe, tokenTabela.lexema, tokenTabela.tipo))

          tabelaEstados.estado_atual = 0
          arrayDeCaracteres.pop(0)
          scanner.lexema = ''
          
          retorno = scanner.scanner(tabelaEstados, arrayDeCaracteres[0].replace(" ", ""), tabelaDeSimbolos)
          continue
        elif(retorno['mensagem']  == None): #Espaço vazio
          jaLancouErro = retorno['token'] == 'ERRO'
          ultimoTokenAntesDoErro = scanner.tratarFinalDaInstrucao(tabelaEstados, jaLancouErro)
          if(ultimoTokenAntesDoErro['mensagem'] == 'TOKEN'):
            tokenTabela = tabelaDeSimbolos.construir_token(tabelaEstados, ultimoTokenAntesDoErro['token'].lexema)
            print('TOKEN - Classe: {}, Lexema: {}, Tipo: {}'.format(tokenTabela.classe, tokenTabela.lexema, tokenTabela.tipo))
          
          tabelaEstados.estado_atual = 0
          scanner.lexema = ''
          retorno['mensagem'] = 'chamar_novamente'
          coluna += 1
          continue

        elif(retorno['mensagem']  == 'tratar_literal_comentario'):
          scanner.lexema =  scanner.lexema + ' '
          retorno['mensagem'] = 'chamar_novamente'
          continue


      ultimoTokenDaLinha = scanner.tratarFinalDaInstrucao(tabelaEstados)
      if(ultimoTokenDaLinha['mensagem'] == 'TOKEN'):
        tokenTabela = tabelaDeSimbolos.construir_token(tabelaEstados, ultimoTokenDaLinha['token'].lexema)
        print('TOKEN - Classe: {}, Lexema: {}, Tipo: {}'.format(tokenTabela.classe, tokenTabela.lexema, tokenTabela.tipo))
        tabelaEstados.estado_atual = 0
        scanner.lexema = ''

tabelaEstados = TabelaDeEstados()
tabelaDeSimbolos = Tabela_de_Simbolos()
scanner = Scanner()


main(tabelaEstados, codigoFormatado, tabelaDeSimbolos, scanner)
tabelaDeSimbolos.imprimir_tabela()