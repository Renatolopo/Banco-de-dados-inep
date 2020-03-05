dados = open('dados_indigenas_matricula_2007_2019_com_eja.txt','r')
resultado= open('dados_padronizados_ensino_medio_com_eja_2007_a_2018.csv','w')
resultado= open('dados_padronizados_ensino_medio_com_eja_2007_a_2018.csv','a')
resultado.write('NU_ANO_CENSO|ID_ALUNO|ID_MATRICULA|NU_DIA|NU_MES|NU_ANO|TP_SEXO|TP_COR_RACA|CO_UF_NASC|CO_MUNICIPIO_NASC|CO_UF_END|CO_MUNICIPIO_END|TP_ZONA_RESIDENCIAL|IN_NECESSIDADE_ESPECIAL|IN_REGULAR|IN_EJA|IN_PROFISSIONALIZANTE|TP_ETAPA_ENSINO|ID_TURMA|TP_UNIFICADA|CO_ENTIDADE|TP_DEPENDENCIA|TP_LOCALIZACAO_DIFERENCIADA|IN_EDUCACAO_INDIGENA\n')
elemento_nulo='xx'
controle=1
for linha in dados:
    linha = linha.rstrip()
    x = linha.split("|")

    if x[0]!= controle:
               controle=x[0]
               indice_localizado=[]
               arquivo_indice='indice____dados_matricula_'+x[0]+'.txt'
               indices_a_buscar=(( 'coluna=1','NU_ANO_CENSO','ANO_CENSO'),
                                  ('coluna=2','ID_ALUNO','FK_COD_ALUNO','CO_PESSOA_FISICA'),
                                  ('coluna=3','ID_MATRICULA','PK_COD_MATRICULA'),
                                  ('coluna=4','NU_DIA'),
                                  ('coluna=5','NU_MES'),
                                  ('coluna=6','NU_ANO'),
                                  ('coluna=7','TP_SEXO'),
                                  ('coluna=8','TP_COR_RACA'),
                                  ('coluna=9','CO_UF_NASC','FK_COD_ESTADO_NASC'),
                                  ('coluna=10','CO_MUNICIPIO_NASC','FK_COD_MUNICIPIO_DNASC'),
                                  ('coluna=11','CO_UF_END','FK_COD_ESTADO_END'),
                                  ('coluna=12','CO_MUNICIPIO_END','FK_COD_MUNICIPIO_END'),
                                  ('coluna=13','TP_ZONA_RESIDENCIAL','ID_ZONA_RESIDENCIAL'),
                                  ('coluna=14','IN_NECESSIDADE_ESPECIAL','ID_POSSUI_NEC_ESPECIAL'),
                                  ('coluna=15','IN_REGULAR'),
                                  ('coluna=16','IN_EJA'),
                                  ('coluna=17','IN_PROFISSIONALIZANTE'),
                                  ('coluna=18','TP_ETAPA_ENSINO','FK_COD_ETAPA_ENSINO'),
                                  ('coluna=19','ID_TURMA','PK_COD_TURMA'),
                                  ('coluna=20','TP_UNIFICADA','COD_UNIFICADA'),
                                  ('coluna=21','CO_ENTIDADE','PK_COD_ENTIDADE'),
                                  ('coluna=22','TP_DEPENDENCIA','ID_ZONA_RESIDENCIAL'),
                                  ('coluna=23','TP_LOCALIZACAO_DIFERENCIADA','ID_LOCALIZACAO_DIFERENCIADA'),
                                  ('coluna=24','IN_EDUCACAO_INDIGENA','ID_EDUCACAO_INDIGENA'))


               for indice_em_busca in indices_a_buscar:
                   indice_anterior_a_busca_por_elemento = []
                   for a in indice_localizado:
                       indice_anterior_a_busca_por_elemento.append(a)

                   for indice_buscando in indice_em_busca:

                       indice= open (arquivo_indice,'r')
                       #print(indice_em_busca)
                       contador_indice=0
                       for m in indice:
                           m=m.rstrip()
                           #print(m)
                           #int(m)
                           if m==indice_buscando:
                               indice_localizado.append(contador_indice)
                               print(x[0],'indice=',indice_em_busca[0],'localizado---posiçao=',indice_localizado)


                           contador_indice = contador_indice + 1

                   if indice_anterior_a_busca_por_elemento== indice_localizado:
                       print('indice=',indice_em_busca[0],'nao encontrado')
                       indice_localizado.append(elemento_nulo)

    linha_dados=[]
    for elemento in indice_localizado:
        if elemento== elemento_nulo:
            linha_dados.append(elemento_nulo)
        else:
            linha_dados.append(x[elemento])

    contador_elemento2=0
    while contador_elemento2!=23:
        resultado.write(str(linha_dados[contador_elemento2])+'|')
        contador_elemento2=contador_elemento2+1
    resultado.write(str(linha_dados[contador_elemento2])+'\n' )

    #print(linha_dados)
resultado.close()
indice.close()


