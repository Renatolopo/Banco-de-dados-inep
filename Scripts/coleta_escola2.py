arquivo_escola= open ('/home/renato/Área de Trabalho/escolas indigenas/escola sao joao das missoes 2017.CSV','r',encoding='ISO-8859-1')
zzz='Turmas ind. 2017.txt'      #nome do arquivo para grafico
exp_grafico= open(zzz,'w')
exp_grafico= open(zzz,'a')
exp_grafico.write('\n')

for linha2 in arquivo_escola:
  linha2=linha2.rstrip()
  z = linha2.split("|")
 # zz=z[2]+'/home/renato/Área de Trabalho/TURMAS2017.txt'


 # resultado= open(zz,'w')
  #resultado= open(zz,'a')
  contador=0
  arquivo = open('/home/renato/Área de Trabalho/TURMAS2017.txt','r',encoding='ISO-8859-1')
  for linha in arquivo:
    linha=linha.rstrip()
    x = linha.split("|")

    if x[68]==z[1]: #CODIGO DA INSTITUIÇAO DE ENSINO

             contador=contador+1
             resultado.write(linha+'\n')


  print('co_instituiçao= ',z[1],' **no_instituiçao= ',z[2],' **alunos 3ano medio= ',contador)
  s=','+str(contador)
  exp_grafico.write(z[2]+s+'\n')
  arquivo.close()
  resultado.close()


exp_grafico.close()
print('EXIT SUSSESS')