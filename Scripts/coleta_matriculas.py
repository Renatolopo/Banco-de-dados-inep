arquivo = open('/home/renato/Área de Trabalho/Projeto Xakriabá/Matriculas/MATRICULA_SUDESTE2018.txt','r',encoding="ISO-8859-1") #MATRICULA_SUDESTE
resultado= open('/home/renato/Área de Trabalho/Projeto Xakriabá/matriculas indigenas/matriculas sao joao das missoes 2018_1ano.txt','w', encoding="ISO-8859-1")
resultado= open('/home/renato/Área de Trabalho/Projeto Xakriabá/matriculas indigenas/matriculas sao joao das missoes 2018_1ano.txt','a',encoding="ISO-8859-1")

contador=0
contador2=0

for linha in arquivo:
    linha=linha.rstrip()
    x = linha.split("|")
    print('codogo do municipi0 x[77]=',x[77],'** ',contador2,' analisados ate o momento ***',contador,'encontrados **   x[91]=',x[91])
    print(contador2,' * ',contador)
    if contador2 == 0:
        resultado.write(linha + '\n')


    contador2=contador2+1

    if x[77]=="3162450":                          #CODIGO DO MINICIPIO DE JANUARIA  3135209
       if x[91]=="1":                            #CODIGO DE INSTITUIÇAO DE ENSINO INDIGENA x[91] em januaria nao tem alunos estudando em instituiçoes de estudo indigena
           if (x[67]=="25"):       #CODIGO DE ETAPA DE ENSINO x[67] 6 16

            contador=contador+1
            resultado.write(linha+'\n')



arquivo.close()
resultado.close()
print('EXIT SUSSESS')
print('foram encontradas ',contador,' resultados')