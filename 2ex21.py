import os

nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''

def escreveArq(caminho, arquivo, linha_arq):
    file: str = ''
    tipo: str = ''
    enc: str = ''
    caminho_arquivo = caminho + arquivo
    if (os.path.exists(caminho) and os.path.isdir(caminho)):
        tipo = 'w'
        enc = 'utf-8'
        if (os.path.exists(caminho_arquivo)):
            tipo = 'a'
        with open(caminho_arquivo, tipo, encoding=enc) as file:
            file.write(linha_arq)
        

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq
    dir = '/tmp/exercicios/'
    arq = 'ex21.txt'
    linha: str = ''

    linha = nm + ';' + str(nt1) + ';' + str(nt2) + ';' + str(nt3) + ';' + str(nt4) + ';' + str(vlr_med) + '\n'
    escreveArq(dir, arq, linha)
   

def med(n1, n2, n3, n4):
    media: float = 0.0
    media = (n1 + n2 + n3 + n4) / 4
    return media

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))
    valor_media = med(nota1, nota2, nota3, nota4)
    print(f'A média do aluno {nome} é: {valor_media:.2f}')
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def main():
    pastas: str = ''

    pastas = '/tmp/exercicios'
    os.makedirs(pastas, exist_ok=True)
    os.chmod(pastas, 0o744)

    contador = 0
    while contador < 5:
        entrada()
        contador += 1


if (__name__ == '__main__'):
    main()