def idRepet(id_atual, ano_atual, file):
    cont = 0
    for i in file:
        i = i.split(',')
        if id_atual == i[0] and ano_atual == i[1]:
            cont += 1
    if cont > 1:
        return True
    else:
        return False

arq = open('/home/renato/Área de Trabalho/Projeto Xakriabá/matriculas indigenas/id2_matriculas_2007_2018.csv', 'r')
file = arq.readlines()
arq.close()

repetido = []
for i in file:
    i = i.split(',')
    id_atual = i[0]
    ano_atual = i[1]
    print(f'{id_atual} \t {ano_atual}')
    if idRepet(id_atual, ano_atual, file):
        if id_atual not in repetido:
            repetido.append(id_atual)
        

print(f'id repetidos {repetido}')
print(f'foram encontrados {len(repetido)} ids repetidos')

   
   

