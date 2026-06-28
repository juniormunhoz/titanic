# 1 - Contagem Geral
def contagem_geral (file_body: list):
    """
    Conta utilizando um loop for uma lisata de lista de passageiros usando o campo name.
    """
    contador = 0
    for row in range (0, len(file_body)):
        if file_body[row][3] != "":
            contador += 1
    print(f"A Contagem geral de passageiros contabilizou {contador} passageiros.")

#Atividades 2 Enzo
def idades(cleaned_file_body: list):
    maior = float(cleaned_file_body[0][5])
    menor = float(cleaned_file_body[0][5])
    soma = 0

    for linha in cleaned_file_body:
        idade = float(linha[5])
        soma += idade

        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade

    media = soma / len(cleaned_file_body)

    print(f'A maior idade registrada no Titanic é igual a {maior}')
    print(f'A menor idade registrada no Titanic é igual a {menor}')
    print(f'A média aproximada das idades registradas no Titanic é igual a {media:.2f}')

def valores_pas(cleaned_file_body: list):
    maior = float(cleaned_file_body[0][9])
    menor = float(cleaned_file_body[0][9])
    soma = 0

    for linha in cleaned_file_body:
        valor = float(linha[9])
        soma += valor

        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    media = soma / len(cleaned_file_body)

    print(f'O maior valor aproximado da passagem do Titanic custou {maior:.2f}')
    print(f'O menor valor da passagem do Titanic custou {menor:.2f}')
    print(f'A média aproximada dos valores das passagens foi {media:.2f}')
'''    
cabecalho, corpo, dicionario, cleaned_file_body = importacao.csv_file_open('train.csv')
valores_pas(cleaned_file_body)  
'''
# 3 - Frequencia de Categorias
def distinct_values (file_body: list):

    '''
    Calcula a quantidade de valores distintos na coluna selecionada pelo usuario

    Parametros de Entrada:

    file_body -> Lista de listas contendo os dados do arquivo
    '''

    values_found = []
    distinct_values_num = 0

    print('Colunas disponiveis para verificação:\n\n1 - PassengerId\n2 - Survived\n3 - Pclass\n4 - Name\n5 - Sex\n6 - Age\n7 - SibSp\n8 - Parch\n9 - Ticket\n10 - Fare\n11 - Cabin\n12 - Embarked\n')

    while True:
        
        try:

            column = int(input('Informe o índice da coluna a ser analisada: '))

            if (column > 0) and (column <= len(file_body[0])): 

                break

            else: 

                print('\nNão existe coluna correspondente com o índice informado\n')

        except ValueError:

            print('\nEntrada inválida, digite apenas números inteiros.\n')

    match column:

        case 1:

            for row in range (0, len(file_body)):

                if (file_body[row][0] != ''):

                    if (file_body[row][0] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][0])

        case 2:
            
            for row in range (0, len(file_body)):

                if (file_body[row][1] != ''):

                    if (file_body[row][1] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][1])

        case 3:

            for row in range (0, len(file_body)):

                if (file_body[row][2] != ''):

                    if (file_body[row][2] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][2])

        case 4:

            for row in range (0, len(file_body)):

                if (file_body[row][3] != ''):

                    if (file_body[row][3] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][3])

        case 5:

            for row in range (0, len(file_body)):

                if (file_body[row][4] != ''):

                    if (file_body[row][4] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][4])

        case 6:

            for row in range (0, len(file_body)):

                if (file_body[row][5] != ''):

                    if (file_body[row][5] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][5])

        case 7:

            for row in range (0, len(file_body)):

                if (file_body[row][6] != ''):

                    if (file_body[row][6] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][6])

        case 8:

            for row in range (0, len(file_body)):

                if (file_body[row][7] != ''):

                    if (file_body[row][7] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][7])

        case 9:

            for row in range (0, len(file_body)):

                if (file_body[row][8] != ''):

                    if (file_body[row][8] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][8])

        case 10:

            for row in range (0, len(file_body)):

                if (file_body[row][9] != ''):

                    if (file_body[row][9] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][9])

        case 11:

            for row in range (0, len(file_body)):

                if (file_body[row][10] != ''):

                    if (file_body[row][10] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][10])

        case 12:

            for row in range (0, len(file_body)):

                if (file_body[row][11] != ''):

                    if (file_body[row][11] not in values_found):

                        distinct_values_num += 1
                        values_found.append(file_body[row][11])

    print(f'\nExistem {distinct_values_num} valores distintos na coluna analisada.')

#Atividade 5 Enzo
def estatistica_familia (cleaned_file_body : list) :
    #Esta função analisa a 7º e 8º coluna da matriz (respectivamente, SibSp e Parch), calcula e printa quantas pessoas viajaram sozinho ou em grupo, além da média
    sozinho = 0
    grupo = 0
        
    for linha in cleaned_file_body :
        irmaos = float(linha[6])
        parentes = float(linha[7])
        if irmaos >= 1 :
            if parentes >= 1 :
                grupo += 1
            else :
                grupo += 1
        else :
            if parentes >= 1 :
                grupo += 1
            else :
                sozinho += 1

    soma = 0
    contador = 0

    for linha1 in cleaned_file_body :
        parente = float(linha1[7])
        soma += parente
        contador += 1
    media = soma / contador

    print(f'{sozinho} das pessoas registradas viajaram sozinhas no Titanic')
    print(f'{grupo} das pessoas registradas viajaram em grupo no Titanic')
    print(f'\nA média aproximada de parentes que os passageiros levaram a bordo é igual a {media:.2f}')


# 6 - Estatísticas de Tarifas (Fare) por Porto de Embarque
def tarifas_por_portos (file_body: list):
    """
    Cruza informações de valores de tarifa por portos, calculando a tarifa
    média paga em cada porto de embarque e identificando qual porto teve a
    passagem mais cara e qual teve a passagem mais barata.

    Linhas sem valor de Fare ou sem valor de Embarked são ignoradas.
    Passagens com Fare igual a 0 são contabilizadas separadamente,
    não entram no cálculo da média e não são consideradas na busca pela
    passagem mais barata(são tratadas como passagens gratuitas).

    file_body > Lista de listas contendo os dados do arquivo.
    """

    portos_encontrados = []
    soma_tarifas = []
    contagem_pagantes = []
    contagem_gratis = []

    maior_tarifa_individual = None
    porto_maior_tarifa_individual = None
    menor_tarifa_individual = None
    porto_menor_tarifa_individual = None

    for row in range (0, len(file_body)):
        porto = file_body[row][11]
        tarifa_texto = file_body[row][9]
        if (porto != '') and (tarifa_texto != ''):
            tarifa = float(tarifa_texto)
            if porto in portos_encontrados:
                indice_porto = portos_encontrados.index(porto)
            else:
                portos_encontrados.append(porto)
                soma_tarifas.append(0)
                contagem_pagantes.append(0)
                contagem_gratis.append(0)
                indice_porto = len(portos_encontrados) - 1
                
            if tarifa == 0:
                contagem_gratis[indice_porto] += 1
            else:
                soma_tarifas[indice_porto] += tarifa
                contagem_pagantes[indice_porto] += 1
                if (maior_tarifa_individual == None) or (tarifa > maior_tarifa_individual):
                    maior_tarifa_individual = tarifa
                    porto_maior_tarifa_individual = porto
                if (menor_tarifa_individual == None) or (tarifa < menor_tarifa_individual):
                    menor_tarifa_individual = tarifa
                    porto_menor_tarifa_individual = porto

    medias_por_porto = []

    for indice in range (0, len(portos_encontrados)):
        if contagem_pagantes[indice] > 0:
            medias_por_porto.append(soma_tarifas[indice] / contagem_pagantes[indice])
        else:
            medias_por_porto.append(0)

    total_gratis = 0

    for indice in range (0, len(contagem_gratis)):
        total_gratis += contagem_gratis[indice]
    print('\nTarifa média por porto de embarque:\n')

    for indice in range (0, len(portos_encontrados)):
        print(f'Porto {portos_encontrados[indice]}: R$ {medias_por_porto[indice]:.2f} (com base em {contagem_pagantes[indice]} passageiros pagantes)')
        if contagem_gratis[indice] > 0:
            print(f'   -> {contagem_gratis[indice]} passageiro(s) com passagem gratuita neste porto')

    if total_gratis > 0:
        print(f'\nObservação: havia {total_gratis} passagem(ns) gratuita(s) no total (Fare = 0), não consideradas nas médias nem na busca pela passagem mais barata.')

    print('\nPassagem individual mais cara e mais barata:\n')
    print(f'A passagem mais cara custou R$ {maior_tarifa_individual:.2f}, paga por um passageiro embarcado no porto {porto_maior_tarifa_individual}.')
    print(f'A passagem mais barata (excluindo gratuitas) custou R$ {menor_tarifa_individual:.2f}, paga por um passageiro embarcado no porto {porto_menor_tarifa_individual}.')

    # 7 - Detalhamento de dados faltantes
def data_cleaning (file_header: list, file_body: list):

    '''
       Imprime uma tabela com o nome das colunas e a quantidade de dados sem valor atribuido em cada uma, 
       além de analises detalhadas do percentual de passageiros sem a informação de cabine.

      Parametros de entrada:

       file_header -> Lista contendo o cabeçalho do arquivo.
       file_body -> Lista de listas contendo os dados a serem analisados.
    '''

    passengers_num = 0
    passenger_for_class = [0, 0, 0]
    no_cabin_info_for_class = [0, 0, 0]

    print('\n***** Quantidade de dados sem valor atribuido por coluna: *****\n')

    for column in range (0, len(file_header)):

        empty_data = 0

        for row in range (0, len(file_body)):

            if (file_body[row][column] == ''):

                empty_data += 1

        print(f'Coluna {column}: {file_header[column]} - {empty_data} dados sem valor atribuido')

    print('\n***** Analise detalhada dos passageiros sem a informação de cabine: *****\n')

    for row1 in range (0, len(file_body)):

        passengers_num += 1

        if (file_body[row1][10] == ''):

            no_cabin_info_for_class[(int(file_body[row1][2]) - 1)] = (no_cabin_info_for_class[(int(file_body[row1][2]) - 1)] + 1)

        match (file_body[row1][2]):

            case '1':

                passenger_for_class[0] = (int(passenger_for_class[0]) + 1)

            case '2':

                passenger_for_class[1] = (int(passenger_for_class[1]) + 1)

            case '3':

                passenger_for_class[2] = (int(passenger_for_class[2]) + 1)

    no_cabin_info_all = (no_cabin_info_for_class[0] + no_cabin_info_for_class[1] + no_cabin_info_for_class[2])

    print(f'Percentual de passageiros sem a informação de cabine:\n\n{((no_cabin_info_all * 100) / passengers_num):.2f} % dos passageiros não possui informação de cabine.')

    print(f'\nPercentual de passageiros sem a informação de cabine por classe:\n\n{((no_cabin_info_for_class[0] * 100) / (passenger_for_class[0])):.2f} % dos passageiros da 1° Classe não possui informação de cabine.\n{((no_cabin_info_for_class[1] * 100) / passenger_for_class[1]):.2f} % dos passageiros da 2° Classe não possui informação de cabine.\n{((no_cabin_info_for_class[2] * 100) / passenger_for_class[2]):.2f} % dos passageiros da 3° Classe não possui informação de cabine.')
