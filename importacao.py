#Funções para carregar o arquivo

import os
import csv

def csv_file_open (path: str):
    """
    Esta função abre um arquivo csv e extrai seu cabecalho, corpo e conteúdo estruturado.
    Retorna uma tupla contendo file_header, uma lista de listas com o nome das colunas, file_body, uma lista de listas com linhas de dados
    dos passageiros, complete_file, lista de listas de dicionários, onde as chaves são as colunas.
    
    Args:
        path (string) = Caminho do arquivo
    
    Returns:
        file_body (list) = Lista de listas que contem todas as informações dos passageiros, sem o cabeçalho. Caso arquivo não exista, retorna None.
        file_header (list) = Lista de listas que contem o cabeçalho.
        complete_file (list) = Lista de listas de dicionários, que contém todas as informações do arquivo, ordenadas pelas colunas.
    
    """
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
    
        
    

if __name__ == "__main__":
    path = r"E:\UTFPR\Algoritimos\atividade\Projeto 1\train.csv"
    print(csv_file_open(path)[2])
    


