from scanner import Scanner
from tabela_de_estados import TabelaDeEstados
from tabela_de_simbolos import TabelaDeSimbolos

def main():
  tabelaEstados = TabelaDeEstados()
  tabelaDeSimbolos = TabelaDeSimbolos()
  scanner = Scanner("codigo.txt")

  while True:      
    token = scanner.SCANNER(tabelaEstados, tabelaDeSimbolos)
    print(token)

    if token.classe == 'EOF':
        break
  

if __name__ == "__main__":
  main()