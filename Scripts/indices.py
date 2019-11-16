arquivo = open('/home/renato/Área de Trabalho/Projeto Xakriabá/indces escolas indigenas/ind.txt','r') #MATRICULA_SUDESTE
resultado= open('/home/renato/Área de Trabalho/Projeto Xakriabá/indces escolas indigenas/indice_Turmas 2008.txt','w')
resultado= open('/home/renato/Área de Trabalho/Projeto Xakriabá/indces escolas indigenas/indice_Turmas 2008.txt','a')

contador=0
contador2=0
n=0
for linha in arquivo:
    linha=linha.rstrip()
    x = linha.split("|")
    while n!=-1:


                     contador=contador+1
                     resultado.write(x[n]+'\n')
                     n=n+1



arquivo.close()
resultado.close()
print('EXIT SUSSESS')
print('foram encontradas ',contador,' resultados')