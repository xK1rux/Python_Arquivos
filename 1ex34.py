import os

valor: int = 0
dir: str = ''
arq: str = ''
arquivo: str = ''

def grava(c, rslt):
    global dir, arq, arquivo
    dir = '/tmp/exercicios/'
    arq = 'ex34.txt'
    file: str = '' 
    tipo: str = ''
    enc: str = ''
    linha: str = ''

    linha = str(rslt) + '\n'
    arquivo = dir + arq
    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        enc = 'utf-8'
        if c > 0:
            if (os.path.exists(arquivo)):
                tipo = 'a'
            with open(arquivo, tipo, encoding=enc) as file:
                file.write(linha)
    else:
        print('Diretório inválido.')

def multi(vlr, tab):
    res = vlr * tab
    return res

def main():
    pastas: str = ''

    pastas = '/tmp/exercicios'
    os.makedirs(pastas, exist_ok=True)
    os.chmod(pastas, 0o744)

    global valor
    valor = int(input('Digite um valor entre 1 e 10: '))
    if valor < 1 or valor > 10:
        print('Valor inválido. Digite um valor entre 1 e 10.')
        return
    else:
        contador = 0
        while contador < 10:
            contador += 1
            result = multi(valor, contador)
            grava(contador, result)


if (__name__ == '__main__'):
    main()