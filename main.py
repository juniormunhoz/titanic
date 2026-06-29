#Projeto Titanic

import os
import importacao
import analise_titanic
import visualizacao

def main():
    path = os.getcwd()
    path = os.path.join(path, "train.csv")
    file_header, file_body, complete_file, cleaned_file_body = importacao.csv_file_open(path)
    
    if file_header != None:

        digito = 0
        
        while digito != 12:
            print("\n -- MENU -- \n " +
                  "1) Contagem geral \n " +
                  "2) Estatísticas de idade e tarifa \n " +
                  "3) Frequência de Categorias \n " +
                  "4) Taxa de Sobrevivência Geral e por Segmento \n " +
                  "5) Análise de Composição Familiar \n " +
                  "6) Estatísticas de Tarifas (Fare) por Porto de Embarque \n " +
                  "7) Detalhamento de Dados Faltantes (Data Cleaning) \n " +
                  "8) Perfil Etário por Classe \n " +
                  "9) Exibir cabeçalho \n " +
                  "10) Exibir quantidade x de informações dos passageiros \n " +
                  "11) Listar todos os dados de forma organizada \n " +
                  "12) Sair \n ")
            while True:
                try:
                    digito = int(input(" Insira sua opção: "))
                    break
                except ValueError:
                    print(" Valores inválidos, tente novamente.")

            match digito:
                case 1:
                    print()
                    analise_titanic.contagem_geral(file_body)
                    print()
                    print(" -" *50)

                case 2 :
                    print()
                    analise_titanic.idades(cleaned_file_body)
                    print()
                    analise_titanic.valores_pas(cleaned_file_body)
                    print()
                    print(" -" *50)

                case 4:
                    print()
                    analise_titanic.taxa_sobrevivencia(file_body)
                    print()
                    print(" -" *50)

                case 5:
                    print()
                    analise_titanic.estatistica_familia(cleaned_file_body)
                    print()
                    print(" -" *50)

                case 6:
                    print()
                    analise_titanic.tarifas_por_portos(file_body)
                    print()
                    print(" -" *50)

                case 7:
                    print()
                    analise_titanic.distinct_values(cleaned_file_body)
                    print()
                    print(" -" *50)

                case 8 :
                    print()
                    analise_titanic.perfil_classe(cleaned_file_body)
                    print()
                    print(" -" *50)

                case 9:
                    print()
                    visualizacao.display_header(file_header)
                    print()
                    print(" -" *50)

                case 10:
                    print()
                    visualizacao.display_n_passengers(cleaned_file_body)
                    print()
                    print(" -" *50)
                    
                case 11:
                    print()
                    visualizacao.display_file(complete_file)
                    print()
                    print(" -" *50)
                    
                    
                    
                    
                
                case 12:
                    print(" Você escolheu sair...")

    else:
        print(" Reinicie e tente novamente.")

    
if __name__ == "__main__":
    main()
    
        
