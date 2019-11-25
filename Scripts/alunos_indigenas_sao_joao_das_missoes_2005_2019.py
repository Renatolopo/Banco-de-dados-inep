
contador_de_resultado_geral=0
contador_de_arquivos_analisados=0
dados = open('dados_matricula_2005_2019.txt', 'r')
resultado= open('dados_indigenas_matricula_2005_2019.txt', 'w')
resultado= open('dados_indigenas_matricula_2005_2019.txt', 'a')

for linha in dados:
    linha = linha.rstrip()

    ##################################################################################
    ##################################################################################
    ##################################################################################


    if linha == "dados_matricula_2005.txt": # 2005 precisa de antençao especial#
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[2] == "3162450":  # codigo do municipio de missoes
                if x[33] == "s" or  x[33] == "S" :# codigo de instituiçao indigena //33=ESC_T_IN
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2006.txt":## semelhante a 2005, porem com 2 info a mais
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[2] == "3162450":  # codigo do municipio de missoes
                if x[33] == "s" or  x[33] == "S" :# codigo de instituiçao indigena //33=ESC_T_IN
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2007.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[43] == "3162450":  # codigo do municipio de missoes
                if x[53] == "1" or x[54] == "1":  # codigo de instituiçao indigena
                    #if x[36] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2008.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[43] == "3162450":  # codigo do municipio de missoes
                if  x[55] == "1":  # codigo de instituiçao indigena
                    #if x[36] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2009.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[44] == "3162450":  # codigo do municipio de missoes
                if  x[56] == "1":  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2010.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[44] == "3162450":  # codigo do municipio de missoes
                if x[56] == "1" :  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2011.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[47] == "3162450":  # codigo do municipio de missoes
                if x[60] == "1":  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2012.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[58] == "3162450":  # codigo do municipio de missoes
                if x[72] == "1":  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2013.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[70] == "3162450":  # codigo do municipio de missoes
                if x[84] == "1":  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2014.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[70] == "3162450":  # codigo do municipio de missoes
                if x[84] == "1":  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2015.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[78] == "3162450":  # codigo do municipio de missoes
                if x[92] == "1":  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2016.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[77] == "3162450":  # codigo do municipio de missoes
                if x[91] == "1":  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2017.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[77] == "3162450":  # codigo do municipio de missoes
                if x[91] == "1":  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    if linha == "dados_matricula_2018.txt":
        arquivo = open(linha, 'r')
        contador_de_linhas = 0
        for linha2 in arquivo:
            linha2 = linha2.rstrip()
            x = linha2.split("|")
            print('arquivo_em_processamento=', contador_de_arquivos_analisados, ' *** linhas_analisadas=',
                  contador_de_linhas, ' *** resultados_encontrados=', contador_de_resultado_geral)
            contador_de_linhas = contador_de_linhas + 1

            if x[77] == "3162450":  # codigo do municipio de missoes
                if x[91] == "1":  # codigo de instituiçao indigena
                    #if x[] == "":  # codigos de etapa de ensino

                        contador_de_resultado_geral = contador_de_resultado_geral + 1
                        resultado.write(linha2 + '\n')

    contador_de_arquivos_analisados=contador_de_arquivos_analisados+1


dados.close()
resultado.close()
arquivo.close()

print('EXIT SUSSESS')
print('EXIT SUSSESS')
print('EXIT SUSSESS')
