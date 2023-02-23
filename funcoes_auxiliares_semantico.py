def inicia_arquivo_objeto(programa_objeto, temporarias):
    objeto_final = ''
    objeto_final += '#include <stdio.h> \n'
    objeto_final += 'typedef char literal[256]: \n'
    objeto_final += 'void main(void) \n'
    objeto_final += '{\n' 
    objeto_final += '/*----Variaveis temporarias----*/\n'
    objeto_final += temporarias + '\n'
    objeto_final += '/*------------------------------*/ \n'
    objeto_final += programa_objeto
    #objeto_final += '\n}'
    with open('PROGRAMA.C', 'w') as f:
        f.write(objeto_final)