#Funções para carregar o arquivo

import os
import csv

def csv_file_open (path:str):

    if os.path.isfile(path):

        file_body = []
        file_header = []
        complete_file = []

        with open (path, 'r', encoding = 'utf-8') as file:

            file_reader = csv.reader(file)

            line = 0

            for row1 in file_reader:

                if (line == 0):

                    file_header.append(row1)

                else:

                    file_body.append(row1)

                line += 1

        with open (path, 'r', encoding= 'utf-8') as file:

            file_reader = csv.DictReader(file)

            for row2 in file_reader:

                complete_file.append(row2)

        return file_header, file_body, complete_file

    else:

        print('Arquivo não encontrado')

        return None, None, None
    

    



