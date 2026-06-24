#Funções para carregar o arquivo

import os
import csv

def csv_file_open (path:str):

    if os.path.isfile(path):

        file_body = []
        file_title = []

        with open(path, 'r', encoding = 'utf-8') as file:

            file_reader = csv.reader(file)

            linha = 0

            for i in file_reader:

                if (linha == 0):

                    file_title.append(i)

                else:

                    file_body.append(i)

                linha += 1

        return file_title, file_body

    else:

        print('Arquivo não encontrado')
    

    



