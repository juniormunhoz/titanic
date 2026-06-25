def display_header (file_header: list):
    """
    Este procedimento recebe como argumento uma lista contendo apenas os dados do cabeçalho do arquivo train.csv e 
    imprime o cabeçalho da planilha.

    Args:
        file_header = []
    """

    print(f'\nOpção escolhida: Exibir Cabeçalho\n\n{file_header}')


def display_n_passengers (file_body:list):
    """
    Este procedimento recebe como argumento uma lista contendo os dados dos passageiro 
    e imprime a quantidade de passageiros que o usuário inserir.
    
    Args:
        file_body = []
    
    """
    passengers_num = 0

    print('\nOpção escolhida: Exibir nomes dos primeiros passageiros\n')

    while (passengers_num <= 0):

        passengers_num =  int(input('Informe a quantidade de passageiros a exibir: '))

        if (passengers_num > 0):

            print('')

            for passenger in range(0, passengers_num):

                print(f'{passenger + 1} - {file_body[passenger][3]}')

        else: 
            
            print('\nO valor inserido deve ser maior que 0\n')


def display_file (complete_file: list):
    """
    Este procedimento recebe como argumento uma lista com os dados completos do arquivo.csv 
    e imprime o arquivo todo.
    
    Args:
        complete_file = []
    
    """

    print('\nOpção escolhida: Exibir todos os dados\n')

    for row in complete_file:

        print(row)
