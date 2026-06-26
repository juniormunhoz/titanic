def display_header (file_header: list):

    '''Recebe como arguento uma lista contendo apenas os dados do cabeçalho'''

    print(file_header)

def display_n_passengers (cleaned_file_body:list):

    '''Recebe como argumento uma lista de lista ja tratada contendo apenas os dados dos passageiros '''

    passengers_num = 0

    while (passengers_num <= 0):

        passengers_num =  int(input('Informe a quantidade de passageiros a exibir: '))

        if (passengers_num > 0):

            if (passengers_num <= len(cleaned_file_body)):

                print()

                for passenger in range(0, passengers_num):

                    print(f'{passenger + 1} - {cleaned_file_body[passenger][3]}')

            else: 

                print(f'\nA quantidade de passageiros a exibir é maior que número total de passageiros ({len(cleaned_file_body)} passageiros), dessa forma será exibida o quantidade total de passageiros\n')

                for passenger in range(0, len(cleaned_file_body)):

                    print(f'{passenger + 1} - {cleaned_file_body[passenger][3]}')
                
        else: 
            
            print('\nO valor inserido deve ser maior que 0\n')

def display_file (complete_file: list):

    '''Recebe como argumento uma lista de lista de dicionarios completa '''

    for row in complete_file:

        print(row)
