arquivo  = open('/home/renato/Área de Trabalho/Projeto Xakriabá/Relacionados/dados_indigenas_matricula_2007_2019_com_eja-1.txt', 'r')  #arquivo de entrada
resultado = open('/home/renato/Área de Trabalho/Projeto Xakriabá/Matriculas/matriculas13a16rascunho.txt','w') #saida
resultado = open('/home/renato/Área de Trabalho/Projeto Xakriabá/Matriculas/matriculas13a16rascunho.txt','a')
resultado.write('NU_ANO_CENSO|ID_ALUNO|ID_MATRICULA|NU_DIA|NU_MES|NU_ANO|TP_SEXO|TP_COR_RACA|CO_UF_NASC|CO_MUNICIPIO_NASC|CO_UF_END|CO_MUNICIPIO_END|TP_ZONA_RESIDENCIAL|IN_NECESSIDADE_ESPECIAL|IN_REGULAR|IN_EJA|IN_PROFISSIONALIZANTE|TP_ETAPA_ENSINO|ID_TURMA|TP_UNIFICADA|CO_ENTIDADE|TP_DEPENDENCIA|TP_LOCALIZACAO_DIFERENCIADA|IN_EDUCACAO_INDIGENA\n')
for linha in arquivo:
    linha = linha.rstrip()
    x = linha.split('|')
    if x[0] == '2013':
        resultado.write(x[0] + '|' + x[2] +'|'+x[1] + '|'+ x[3] + '|' + x[4] + '|' + x[5] + '|' + x[11]+ '|' + x[12]+ '|'+ x[15] + '|'+ x[17]+ '|'+ x[18]+ '|'+ x[20]+ '|' + x[21]+ '|' + x[36]+ '|'+' .'+ '|'+'. '+ '|'+' .'+ '|'  +x[62]+ '|'+x[63]+ '|' +x[65]+ '|' +x[67]+ '|' +x[73]+ '|' +x[83]+ '|' +x[84]+ '\n' )
    if x[0] == '2014':
        resultado.write(x[0] + '|' + x[2] +'|'+x[1] + '|'+ x[3] + '|' + x[4] + '|' + x[5] + '|' + x[13]+ '|' + x[14]+ '|'+ x[17] + '|'+ x[18]+ '|'+ x[19]+ '|'+ x[20]+ '|' + x[21]+ '|' + x[36]+ '|'+' .'+ '|'+'. '+ '|'+' .'+ '|'  +x[62]+ '|'+x[64]+ '|' +x[66]+ '|' +x[68]+ '|' +x[73]+ '|' +x[83]+ '|' +x[84]+ '\n' )
    if x[0] == '2015':
        resultado.write(x[0] + '|' + x[2] +'|'+x[1] + '|'+ x[3] + '|' + x[4] + '|' + x[5] + '|' + x[14]+ '|' + x[16]+ '|'+ x[18] + '|'+ x[19]+ '|'+ x[20]+ '|'+ x[21]+ '|' + x[22]+ '|' + x[37]+ '|'+x[64]+ '|'+x[65]+ '|'+x[66]+ '|'  +x[67]+ '|'+x[69]+ '|' +x[71]+ '|' +x[73]+ '|' +x[80]+ '|' +x[91]+ '|' +x[92]+ '\n' )
    if x[0] == '2016':
        resultado.write(x[0] + '|' + x[2] +'|'+x[1] + '|'+ x[3] + '|' + x[4] + '|' + x[5] + '|' + x[14]+ '|' + x[16]+ '|'+ x[18] + '|'+ x[19]+ '|'+ x[20]+ '|'+ x[21]+ '|' + x[22]+ '|' + x[37]+ '|'+x[64]+ '|'+x[65]+ '|'+x[66]+ '|'  +x[67]+ '|'+x[68]+ '|' +x[70]+ '|' +x[72]+ '|' +x[79]+ '|' +x[90]+ '|' +x[91]+ '\n' )


   arquivo.close()
resultado.close()
print("Finalizado!")
Fazenda São Geraldo, S/N Km 06 - 39480-000 - Januária /MG