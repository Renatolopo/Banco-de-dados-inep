def getKey(linha):
    # chave = dia de nascimento,  mes de nascimento, ano de nascimento,  sexo, raça, municipio de nascimento
    return f'{linha[4]}/{linha[5]}/{linha[6]} {linha[7]} {linha[8]} {linha[10]}'

def getNvlinha(coluna, id_atual):
    if coluna == 'null':
        return id_atual
    else:
        return coluna

def null(linha):
    if linha[0] == 'null':
        return True
    else:
        return False
def getId(n,linha):
    ls = []
    for i in range(len(linha)):
        ls.append(n)
    return ls

def getSaida(key, saida, cont_id, ano):
    for i in range(len(saida)):
        if i != 0:#ingnora o cabeçalho do arquivo
            key2 = getKey(saida[i])
            id_atual = saida[i][0]
            ano2 = saida[i][1]
            if key == key2 and id_atual == 'null' and ano != ano2:
                saida[i] = list(map(getNvlinha, saida[i], getId(cont_id,saida[i])))
    return saida

file = open('caminho do arquivo.csv','r')
ls_file = []
ls_file = file.readlines()
file.close()

saida = []
for i in ls_file:
    linha = 'null,' + i
    linha = linha.split(',')
    saida.append(linha)

'''
coluna  descrição
0       id
1       ano da coleta
4       dia de nascimento
5       mes de nascimento
6       ano de nascimento
7       sexo
8       raça
10      municipio de nascimento

'''
cont_id = 1
for i in range(len(saida)):
    if i != 0: #ingnora o cabeçalho do arquivo
        print(f'processando ********* {cont_id}')

        if null(saida[i]):
            saida[i] = list(map(getNvlinha, saida[i], getId(cont_id,saida[i])))
            saida = getSaida(getKey(saida[i]), saida, cont_id, saida[i][1])
            cont_id+=1

file2 = open('novo arquivo.csv','w')
rm = "['']"
for i in saida:
    i = str(i)
    for j in range(len(rm)):
        i = i.replace(rm[j],"")
    file2.write(i+'\n')
file2.close()