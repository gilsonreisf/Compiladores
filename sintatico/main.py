from scanner import Scanner
from tabela_de_estados import TabelaDeEstados
from tabela_de_simbolos import TabelaDeSimbolos
from parser_1 import Parser


def main():
  tabelaEstados = TabelaDeEstados()
  tabelaDeSimbolos = TabelaDeSimbolos()
  scanner = Scanner("../lexico/codigo.txt")
  # parser = Parser()

  while True:      
    token = scanner.SCANNER(tabelaEstados, tabelaDeSimbolos)
    # parser.PARSER(token)
    print(token)

    if token.classe == 'EOF':
        break
  

if __name__ == "__main__":
  main()