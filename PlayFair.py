import re
import string

def criptografar(chave, texto):
    chave = chave.replace('j', 'i')
    lista_letras_nao_repetidas = []
    lista_alfabeto = list(string.ascii_lowercase)
    lista_alfabeto.remove('j')
    for letra in chave:
        if letra in lista_letras_nao_repetidas:
            pass
        else:
            lista_letras_nao_repetidas.append(letra)
    for letra in lista_alfabeto:
        if letra in lista_letras_nao_repetidas:
            pass
        else:
            lista_letras_nao_repetidas.append(letra)
    
    matriz = [lista_letras_nao_repetidas[0:5],
              lista_letras_nao_repetidas[5:10],
              lista_letras_nao_repetidas[10:15],
              lista_letras_nao_repetidas[15:20],
              lista_letras_nao_repetidas[20:25]]
    lista_palavras_duplas = []
    lista_texto = []
    for i, letra in enumerate(texto):
        if texto[i] == texto[i-1] and i != 0:
            lista_texto.append('x')
        else:
            pass
        lista_texto.append(letra)
    if len(lista_texto) % 2 != 0:
        lista_texto.append('x')
    x = 0
    for i,letra in enumerate(lista_texto):
        if x == 1:
            x = 0
            lista_palavras_duplas.append(lista_texto[i-1:i+1])
        else:
            x += 1
    texto_criptografado = []
    for letras in lista_palavras_duplas:
        for i, item in enumerate(matriz):
            if letras[0] in item and letras[1] in item:
                index = item.index(letras[1])
                coluna_1 = index
                coluna_2 = index + 1
                linha_1 = i
                linha_2 = i
                break
            try:
                coluna_1 = item.index(letras[0])
            except:
                pass
            if letras[1] in item:
                linha_1 = i
            try:
                coluna_2 = item.index(letras[1])
            except:
                pass
            if letras[0] in item:
                linha_2 = i
        if coluna_2 == coluna_1:
            linha_2 += 1
            linha_1 += 1
            if linha_1 > 4:
                linha_1 = 0
            if linha_2 > 4:
                linha_2 = 0
        texto_criptografado.append(matriz[linha_2][coluna_2])
        texto_criptografado.append(matriz[linha_1][coluna_1])
    return ''.join(texto_criptografado)

def verificar_apenas_letra(texto):
    resultado = False
    pattern = '^[a-z]*$'
    state = bool(re.match(pattern, texto))
    if len(texto) == 0:
        pass
    elif state:
        resultado = True
    else:
        pass
    if resultado:
        pass
    else:
        print('Sua chave deve contem apenas letras sem espaço e não deve ser vazia')
    return resultado
    
while(1):
    escolha = int(input('Você deseja 1 - criptografar ou 2 - Sair\n'))
    if escolha == 1:
        palavra_chave = input('Insira sua chave para criptografar(Deve conter apenas letras sem espaço):\n').lower()
        resultado = verificar_apenas_letra(palavra_chave)
        if resultado:
            palavra_criptografar = input('Insira uma palavra para ser criptografada:\n').lower()
            resultado = verificar_apenas_letra(palavra_criptografar)
            if resultado:
                palavra_criptografada = criptografar(palavra_chave, palavra_criptografar)
                print(palavra_criptografada)
    elif escolha == 2:
        break
    else:
        print('Essá fucao não está disponível')


# In[ ]:




