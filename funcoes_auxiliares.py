import string

def verifica_digito(character : str):
    digitos = ['0','1','2','3','4','5','6','7','8','9']
    if character in digitos:
        return True
    else:
        return False

def verifica_se_letra(character : str):
    
    if (character in string.ascii_lowercase) or (character in string.ascii_uppercase):
        return True
    else:
        return False
    

def verifica_existencia_caractere(character : str):
    if (character != None) and not(character.isspace()):
        return True
    else:
        return False

def removerQuebraDeLinha(txt: str):
    txt.replace('\n', '')