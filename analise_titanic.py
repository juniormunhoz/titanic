#Funções do projeto titanic

# 1 - Contagem Geral
def contagem_geral (file_body: list):
    """
    Este procedimento recebe uma lista de listas contendo todas as informações de todos os passageirosdo arquivo "train.csv".
    Contabiliza quantos passageiros existem utilizando o campo "name" e imprime essa informação na tela.
    
    Args:
        file_body (list) = Lista de listas contendo todas as informações de todos os passageirosdo arquivo "train.csv".
        
    """
    contador = 0
    for row in range (0, len(file_body)):
        if file_body[row][3] != "":
            contador += 1
    print(f" A Contagem geral de passageiros contabilizou {contador} passageiros.")

# 2 - Estatísticas de Idade e Tarifa
def idades(cleaned_file_body: list):
    """
    Este procedimento recebe uma lista de listas já tratada e filtrada sem as linhas com células vazia.
    Faz operações para descobrir a maior e menor idade e a média aproximada de idades registradas no Titanic.
    
    Args:
        cleaned_file_body (list) = Lista de listas tratada e filtrada sem as linhas com células vazias.
        
    """

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

    print(f' A maior idade registrada no Titanic é igual a {maior}')
    print(f' A menor idade registrada no Titanic é igual a {menor}')
    print(f' A média aproximada das idades registradas no Titanic é igual a {media:.2f}')

def valores_pas(cleaned_file_body: list):
    """
    Este procedimento recebe uma lista de listas já tratada e filtrada sem as linhas com células vazia.
    Faz operações para descobrir a maior e a menor tarifa paga e a média aproximada de tarifas registradas no Titanic.
    
    Args:
        cleaned_file_body (list) = Lista de listas tratada e filtrada sem as linhas com células vazias.

    """
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

    print(f' O maior valor aproximado da passagem do Titanic custou {maior:.2f}')
    print(f' O menor valor da passagem do Titanic custou {menor:.2f}')
    print(f' A média aproximada dos valores das passagens foi {media:.2f}')

# 3 - Frequencia de Categorias
def distinct_values (file_body: list):
    """ 
    Este procedimento recebe uma lista de listas contendo todas as informações de todos os passageiros do arquivo "train.csv".
    O procedimento lista as colunas disponíveis para verificação e, após informada pelo usuário, verifica a quantidade de valores distintos na coluna informada.
    
    Args:
        file_body (list) = Lista de listas contendo todas as informações de todos os passageiros do arquivo "train.csv".
        
    """

    values_found = []
    distinct_values_num = 0

    print(' Colunas disponiveis para verificação:\n\n1 - PassengerId\n2 - Survived\n3 - Pclass\n4 - Name\n5 - Sex\n6 - Age\n7 - SibSp\n8 - Parch\n9 - Ticket\n10 - Fare\n11 - Cabin\n12 - Embarked\n')

    while True:
        
        try:

            column = int(input(' Informe o índice da coluna a ser analisada: '))

            if (column > 0) and (column <= len(file_body[0])): 

                break

            else: 

                print('\n Não existe coluna correspondente com o índice informado\n')

        except ValueError:

            print('\n Entrada inválida, digite apenas números inteiros.\n')

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

    print(f'\n Existem {distinct_values_num} valores distintos na coluna analisada.')

# 4 - Taxa de Sobrevivência Geral e por Segmento
def taxa_sobrevivencia(file_body: list):
    """
    Este procedimento recebe uma lista de listas contendo todas as informações de todos os passageiros do arquivo "train.csv".
    Faz verificações de taxa de sobrevivência.
    Taxa Geral: Porcentagem total de sobreviventes em relação ao total de passageiros.
    Por Sexo: Compara a taxa de sobrevivência entre male (homens) e female (mulheres)
    Por Classe: Calcula qual a porcentagem de sobreviventes em cada Pclass (1ª, 2ª e 3ª classe).

    Args:
        file_body (list) = Lista de listas contendo todas as informações de todos os passageirosdo arquivo "train.csv".

    """
    vivos_geral = 0
    male = [0,0] #[total, sobreviventes]
    female = [0,0] #[total, sobreviventes]
    c_classes = [0,0,0]
    vivos_classes = [0,0,0]


    for linha in file_body:
        #Contagem geral
        if linha[1] == "1":
            vivos_geral += 1

        #Contagem homens e mulheres
        if linha[4] == "male":
            male[0] += 1
            if linha[1] == "1":
                male[1] += 1
        elif linha[4] == "female":
            female[0] += 1
            if linha[1] == "1":
                female[1] += 1
                
        #Contagem por classe
        if linha[2] == "1":
            c_classes[0] += 1
            if linha[1] == "1":
                vivos_classes[0] += 1
        elif linha[2] == "2":
            c_classes[1] += 1
            if linha[1] == "1":
                vivos_classes[1] += 1
        elif linha[2] == "3":
            c_classes[2] += 1
            if linha[1] == "1":
                vivos_classes[2] += 1

    print(f" Na contagem geral, apenas {(vivos_geral/len(file_body)) * 100:.2f}% dos passageiros sobreviveram, o que corresponde a {vivos_geral} passageiros.\n" +
          f" Dentre os {male[0]} homens, apenas {(male[1]/male[0]) * 100:.2f}% sobreviveram, o que corresponde a {male[1]} homens.\n" +
          f" Dentre as {female[0]} mulheres, apenas {(female[1]/female[0]) *100:.2f}% sobreviveram, o que corresponde a {female[1]} mulheres.")
    
    for i in range(len(c_classes)):
        print(f" Dentre os {c_classes[i]} da {i+1}° classe, apenas {(vivos_classes[i]/c_classes[i]) *100:.2f}% sobreviveram, o que corresponde a {vivos_classes[i]} passageiros.")

# 5 - Análise de Composição Familiar
def estatistica_familia (cleaned_file_body : list) :
    """
    Este procedimento recebe uma lista de listas já tratada e filtrada sem as linhas com células vazia.
    Analisa e faz operações utilizando as colunas SibSp e Parch para verificar se o passageiro viajava sozinho ou em grupo.
    Verifica também a quantidade média de parentes que tinham a bordo do Titanic.

    Args:
        cleaned_file_body (list) = Lista de listas tratada e filtrada sem as linhas com células vazias.
    
    """

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
    Este procedimento recebe uma lista de listas contendo todas as informações de todos os passageiros do arquivo "train.csv".
    Utiliza as colunas Fare e Embarked para calcular:
    Qual porto de embarque teve a tarifa mais cara e mais barata dentre todos os portos.
    A tarifa média paga em cada porto de embarque.
    
    Linhas sem valor de Fare ou sem valor de Embarked são ignoradas.
    Passagens com Fare igual a 0 são contabilizadas separadamente,
    não entram no cálculo da média e não são consideradas na busca pela
    passagem mais barata(são tratadas como passagens gratuitas).
    
    Args:
        file_body (list) = Lista de listas contendo todas as informações de todos os passageirosdo arquivo "train.csv".
    
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
    print('\n Tarifa média por porto de embarque:\n')

    for indice in range (0, len(portos_encontrados)):
        print(f' Porto {portos_encontrados[indice]}: R$ {medias_por_porto[indice]:.2f} (com base em {contagem_pagantes[indice]} passageiros pagantes)')
        if contagem_gratis[indice] > 0:
            print(f'   -> {contagem_gratis[indice]} passageiro(s) com passagem gratuita neste porto')

    if total_gratis > 0:
        print(f'\n Observação: havia {total_gratis} passagem(ns) gratuita(s) no total (Fare = 0), não consideradas nas médias nem na busca pela passagem mais barata.')

    print('\n Passagem individual mais cara e mais barata:\n')
    print(f' A passagem mais cara custou R$ {maior_tarifa_individual:.2f}, paga por um passageiro embarcado no porto {porto_maior_tarifa_individual}.')
    print(f' A passagem mais barata (excluindo gratuitas) custou R$ {menor_tarifa_individual:.2f}, paga por um passageiro embarcado no porto {porto_menor_tarifa_individual}.')

# 7 - Detalhamento de dados faltantes
def data_cleaning (file_header: list, file_body: list):
    """
    Este procedimento recebe uma lista de listas contendo todas as informações de todos os passageiros do arquivo "train.csv" e uma lista contendo apenas os dados do cabeçalho do arquivo.
    Faz uma análise de dados faltantes, imprimindo uma tabela com o nome das colunas e a quantidade de dados sem valor atribuído em cada uma.
    Além de análises detalhadas de percentual de passageiros sem informação de cabine.
    
    Args:
        file_header (list) = Lista contendo os dados do cabeçalho do arquivo "train.csv".
        file_body (list) = Lista de listas contendo todas as informações de todos os passageirosdo arquivo "train.csv".
    
    """

    passengers_num = 0
    passenger_for_class = [0, 0, 0]
    no_cabin_info_for_class = [0, 0, 0]

    print('\n ----- Quantidade de dados sem valor atribuido por coluna: ----- \n')

    for column in range (0, len(file_header)):

        empty_data = 0

        for row in range (0, len(file_body)):

            if (file_body[row][column] == ''):

                empty_data += 1

        print(f' Coluna {column}: {file_header[column]} - {empty_data} dados sem valor atribuido')

    print('\n ----- Analise detalhada dos passageiros sem a informação de cabine: ----- \n')

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

    print(f' Percentual de passageiros sem a informação de cabine: \n\n{((no_cabin_info_all * 100) / passengers_num):.2f} % dos passageiros não possui informação de cabine.')

    print(f'\n Percentual de passageiros sem a informação de cabine por classe: \n\n{((no_cabin_info_for_class[0] * 100) / (passenger_for_class[0])):.2f} % dos passageiros da 1° Classe não possui informação de cabine.\n{((no_cabin_info_for_class[1] * 100) / passenger_for_class[1]):.2f} % dos passageiros da 2° Classe não possui informação de cabine.\n{((no_cabin_info_for_class[2] * 100) / passenger_for_class[2]):.2f} % dos passageiros da 3° Classe não possui informação de cabine.')

# 8 - Perfil etário por classe
def perfil_classe (cleaned_body_file: list):
    """
    Este procedimento recebe uma lista de listas já tratada e filtrada sem as linhas com células vazia.
    Realiza operações para descobrir a idade média de cada classe.
    Verifica se os passageiros da primeira classe eram mais velhos que os da segunda classe por exemplo.
    
    Args:
        cleaned_body_file (list) = Lista de listas tratada e filtrada sem as linhas com células vazias.
    
    """
    #Listas de contagem por classe
    idade_classe = [0,0,0]
    contagem_classe = [0,0,0]
    idade_media = [0,0,0]
    idade_minima = [999,999,999]
    idade_maxima = [0,0,0]

    for linha in cleaned_body_file:
        idade = float(linha[5])
        if linha[2] == "1":
            idade_classe[0] += idade
            contagem_classe[0] += 1
            
            if idade_minima[0] > idade:
                idade_minima[0] = idade

            if idade_maxima[0] < idade:
                idade_maxima[0] = idade
        
        elif linha[2] == "2":
            idade_classe[1] += idade
            contagem_classe[1] += 1

            if idade_minima[1] > idade:
                idade_minima[1] = idade
                
            if idade_maxima[1] < idade:
                idade_maxima[1] = idade
        
        elif linha[2] == "3":
            idade_classe[2] += idade
            contagem_classe[2] += 1

            if idade_minima[2] > idade:
                idade_minima[2] = idade
                
            if idade_maxima[2] < idade:
                idade_maxima[2] = idade
        
    for i in range(len(idade_classe)):
        idade = idade_classe[i]/contagem_classe[i]
        idade_media[i] = idade
        print(f"\n {i+1}° Classe")
        print(f" Idade média: {idade_media[i]:.2f} ano(s).")
        print(f" Idade mínima: {idade_minima[i]:.2f} ano(s).")
        print(f" Idade máxima: {idade_maxima[i]:.2f} ano(s).") 

    #Cálculo maior e menor idade
    maior_idade = idade_media[0]
    menor_idade = idade_media[0]
    classe_menor, classe_maior = 0, 0
    for i in range(len(idade_media)):
        if idade_media[i] > maior_idade:
            maior_idade = idade_media[i]
            classe_maior = i
        if idade_media[i] < menor_idade:
            menor_idade = idade_media[i]
            classe_menor = i
    
    print(f"\n A classe com pessoas mais velhas era a {classe_maior+1}° classe com média de idade de {maior_idade:.2f} ano(s).")
    print(f" A classe com pessoas mais novas era a {classe_menor+1}° classe com média de idade de {menor_idade:.2f} ano(s).")
        
