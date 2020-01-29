arquivo = open('/home/renato/Área de Trabalho/Projeto Xakriabá/Matriculas/MATRICULA_SUDESTE2009.txt','r',encoding="ISO-8859-1") #MATRICULA_SUDESTE
resultado= open('/home/renato/Área de Trabalho/Projeto Xakriabá/matriculas indigenas/matriculas sao joao das missoes 2019_EJA.txt','w', encoding="ISO-8859-1")
resultado= open('/home/renato/Área de Trabalho/Projeto Xakriabá/matriculas indigenas/matriculas sao joao das missoes 2019_EJA.txt','a',encoding="ISO-8859-1")

contador=0
contador2=0

for linha in arquivo:
    linha=linha.rstrip()
    x = linha.split("|")
    print('codigo do municipi0 x[44]=',x[44],'** ',contador2,' analisados ate o momento ***',contador,'encontrados **   x[56]=',x[56])
    print(contador2,' * ',contador)
    if contador2 == 0:
        resultado.write(linha + '\n')


    contador2=contador2+1

    if x[44]=="3162450":                          #CODIGO DO MINICIPIO DE JANUARIA  3135209
       if x[56]=="1":                            #CODIGO DE INSTITUIÇAO DE ENSINO INDIGENA x[91] em januaria nao tem alunos estudando em instituiçoes de estudo indigena
           if (x[35]=="3"):       #CODIGO DE ETAPA DE ENSINO x[67] 6 16

            contador=contador+1
            resultado.write(linha+'\n')



arquivo.close()
resultado.close()
print('EXIT SUSSESS')
print('foram encontradas ',contador,' resultados')