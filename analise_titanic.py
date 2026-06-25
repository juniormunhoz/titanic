#Funções do projeto titanic

#Função 4 - Taxa de Sobrevivência Geral e por Segmento

def taxa_sobrevivencia(file_body):
    """
    Este procedimento recebe uma lista de listas, file_body, e faz verificações de taxa de sobrevivência.
    Taxa Geral: Porcentagem total de sobreviventes em relação ao total de passageiros.
    Por Sexo: Compara a taxa de sobrevivência entre male (homens) e female (mulheres)
    Por Classe: Calcula qual a porcentagem de sobreviventes em cada Pclass (1ª, 2ª e 3ª classe).

    Args:
        file_body = []


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
    
