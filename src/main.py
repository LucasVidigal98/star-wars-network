from Graph import Graph
import os


def read_data_dir():
    files = os.listdir('..' + os.path.sep + 'data')
    return files


def selecet_network(files):
    print('Selecione a rede a ser Estudada! ')
    index = 0
    for file in files:
        print(str(index) + '-' + file)
        index += 1

    try:
        selected_index = int(input('> '))
    except:
        print('Utilize um número para a seleção !')
        exit(1)

    while selected_index > index:
        print('Opção inválida')
        try:
            selected_index = int(input('> '))
        except:
            print('Utilize um número para a seleção !')
            exit(1)

    return selected_index


def centrality_menu(G):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Selecione a centralidade para ranquear os top 20 vértices mais centrais !')
        print('1- Centralidade por grau')
        print('2- Closeness')
        print('3- Betweeness')
        print('4- Centralidade por Auto vetor')
        print('0 - Sair')
        try:
            option = int(input('Selecione a opção > '))
        except:
            print('Utilize um número inteiro para a opção !')
            continue

        if option == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            G.centrality_ranking(G.degree_centrality(), 'Grau')
            input('Enter para continuar ...')
        elif option == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            G.centrality_ranking(G.closeness(), 'Closeness')
            input('Enter para continuar ...')
        elif option == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            G.centrality_ranking(G.betweeness(), 'Betweeness')
            input('Enter para continuar ...')
        elif option == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            G.centrality_ranking(G.eigenvector(), 'Autovetor')
            input('Enter para continuar ...')
        elif option == 0:
            return
        else:
            print('Opção inválida')


def menu(G):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Rede Carregada com sucesso!')
    while True:
        print('1- Averiguar Características básicas')
        print('2- Plotar rede')
        print('3- Plotar distribuição de graus')
        print('4- Ranking centralidade')
        print('0- Sair')
        try:
            option = int(input('Selecione a opção > '))
        except:
            print('Utilize um número inteiro para a opção !')
            continue

        if option == 0:
            exit(1)
        elif option == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            G.get_info()
            input('Enter para continuar ...')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif option == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            G.draw_graph()
        elif option == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            G.degreehistogram()
        elif option == 4:
            centrality_menu(G)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('Opção inválida !')


files = read_data_dir()
index = selecet_network(files)
G = Graph(files[index])
menu(G)
