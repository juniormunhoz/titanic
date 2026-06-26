#Funções para carregar o arquivo

import os
import csv

def csv_file_open (path:str):

    if os.path.isfile(path):

        file_body = []
        file_header = []
        complete_file = []
        cleaned_file_body = []

        with open (path, 'r', encoding = 'utf-8') as file:

            file_reader = csv.reader(file)

            for _list in file_reader:

                any_list = []
                any_list = _list
                cleaned_list = []
                delete_list = False

                for data in any_list:

                    if (data != ''):

                        cleaned_list.append(data)
                    
                    else:

                        delete_list = True

                file_body.append(any_list)

                if (delete_list == False):

                    cleaned_file_body.append(cleaned_list)

            file_header = file_body[0]

            del file_body[0]
            del cleaned_file_body[0]

        with open (path, 'r', encoding= 'utf-8') as file:

            file_reader = csv.DictReader(file)

            for _list in file_reader:

                complete_file.append(_list)
                
        return file_header, file_body, complete_file, cleaned_file_body

    else:

        print('Arquivo não encontrado')

        return None, None, None, None

    

    



