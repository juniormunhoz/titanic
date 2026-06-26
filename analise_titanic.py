def contagem_geral (file_body: list):
    """
    Conta utilizando um loop for uma lisata de lista de passageiros usando o campo name.
    """
    contador = 0
    for row in range (0, len(file_body)):
        if file_body[row][3] != "":
            contador += 1
    print(f"A Contagem geral de passageiros contabilizou {contador} passageiros.")

def distinct_values (cleaned_file_body: list):

    values_found = []
    distinct_values_num = 0
    aux = 0

    print('Colunas disponiveis para verificação:\n\n1 - PassengerId\n2 - Survived\n3 - Pclass\n4 - Name\n5 - Sex\n6 - Age\n7 - SibSp\n8 - Parch\n9 - Ticket\n10 - Fare\n11 - Cabin\n12 - Embarked\n')

    while True:
        
        try:

            column = int(input('Informe o índice da coluna a ser analisada: '))

            if (column > 0) and (column < 13):

                break

            else: 

                print('\nNão existe coluna correspondente com o índice informado\n')

        except ValueError:

            print('\nEntrada inválida, digite apenas números inteiros.\n')

    match column:

        case 1:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][0] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][0])

        case 2:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][1] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][1])

        case 3:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][2] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][2])

        case 4:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][3] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][3])

        case 5:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][4] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][4])

        case 6:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][5] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][5])

        case 7:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][6] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][6])

        case 8:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][7] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][7])

        case 9:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][8] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][8])

        case 10:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][9] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][9])

        case 11:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][10] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][10])

        case 12:

            for row in range (0, len(cleaned_file_body)):

                if (cleaned_file_body[row][11] not in values_found):

                    distinct_values_num += 1
                    values_found.append(cleaned_file_body[row][11])

    print(f'\nExistem {distinct_values_num} valores distintos na coluna analisada.')
