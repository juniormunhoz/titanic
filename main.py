#Projeto Titanic

digito = 0
while digito != 9:
    print(" -- MENU -- \n " +
          "1) Contagem geral \n " +
          "2) Estatísticas de idade e tarifa \n " +
          "3) Frequência de Categorias \n " +
          "4) Taxa de Sobrevivência Geral e por Segmento \n " +
          "5) Análise de Composição Familiar \n " +
          "6) Estatísticas de Tarifas (Fare) por Porto de Embarque \n " +
          "7) Detalhamento de Dados Faltantes (Data Cleaning) \n " +
          "8) Perfil Etário por Classe \n " +
          "9) Sair \n ")
    while True:
        try:
            digito = int(input(" Insira sua opção: "))
            break
        except ValueError:
            print(" Valores inválidos, tente novamente.")

    match digito:
        case 1:
            print(" contagem")
            print(" -" *50)
            print()
        
        case 9:
            print(" Você escolheu sair...")
