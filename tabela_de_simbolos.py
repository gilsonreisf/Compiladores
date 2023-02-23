from Token import Token
from tabela_de_estados import TabelaDeEstados

class TabelaDeSimbolos:
    def __init__(self):

        self.tabela = []

        self.tabela.append(Token(classe="inicio",lexema="inicio",tipo="inicio"))
        self.tabela.append(Token(classe="varinicio",lexema="varinicio",tipo="varinicio"))
        self.tabela.append(Token(classe="varfim", lexema="varfim", tipo="varfim"))
        self.tabela.append(Token(classe="escreva",lexema="escreva", tipo="escreva"))
        self.tabela.append(Token(classe="leia", lexema="leia",tipo= "leia"))
        self.tabela.append(Token(classe="se", lexema="se",tipo= "se"))
        self.tabela.append(Token(classe="entao",lexema= "entao",tipo= "entao"))
        self.tabela.append(Token (classe="fimse",lexema= "fimse",tipo= "fimse"))
        self.tabela.append(Token(classe="fim",lexema= "fim", tipo="fim"))
        self.tabela.append(Token(classe="inteiro",lexema= "inteiro",tipo= "inteiro"))
        self.tabela.append(Token(classe="literal",lexema= "literal",tipo= "literal"))
        self.tabela.append(Token(classe="real",lexema= "real",tipo= "real"))


    def buscarToken(self, token:Token):
            for t in self.tabela:
                if(t.lexema == token.lexema):
                    return t
            return None
        

    def inserirToken(self, token:Token):
            token_encontrado = self.buscarToken(token)
            if(token_encontrado is None):
                if(token.classe == "id"):
                    self.tabela.append(token)
                return token
            else:
                return token_encontrado

    def atualizarToken(self, token: Token):
        if(token.classe == "id"):
                token_tabela_simbolos = self.buscarToken(token)
                if(token_tabela_simbolos):
                    self.tabela.remove(token_tabela_simbolos)
                    self.tabela.append(token)  
    
    def atualizaTokenParaSemantico(self, token: Token):
        for t in self.tabela:
            if t.lexema == token.lexema:
                t.tipo = token.tipo


    def imprimirTabela(self):
            print(' \n -------------------------- Tabela de Símbolos --------------------------')
            for t in self.tabela:
                print(f"Classe:{t.classe}, Lexema:{t.lexema}, Tipo:{t.tipo}")

    def construirToken(self, tabelaDeEstados: TabelaDeEstados, lexema: str, erro=False):
        if (erro) or (tabelaDeEstados.estado_atual not in tabelaDeEstados.estados_finais):
            return Token('ERROR', lexema, None)

        classe = tabelaDeEstados.retornaClasse()
        tipo = tabelaDeEstados.retornaTipo()
        if classe == 'id':
            token = self.buscarToken(Token(classe, lexema, tipo))
            if token is None:
                token = self.inserirToken(Token(classe, lexema, tipo))
            self.atualizarToken(token)
            return token
        else:
            return Token(classe, lexema, tipo)
    