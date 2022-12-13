class Token:
    def __init__(self, classe: str, lexema: str, tipo: str):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

    def __str__(self) -> str:
        return f"Classe: {self.classe}, Lexema: {self.lexema}, Tipo: {self.tipo}"
        
    def __repr__(self) -> str:
        return f"Classe: {self.classe}, Lexema: {self.lexema}, Tipo: {self.tipo}"