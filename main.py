class NoMusica:
    """
    Classe para representar um nó na lista circular duplamente encadeada.
    Cada nó armazena detalhes de uma música e tem referências para o nó anterior e o próximo.
    """

    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo  # Título da música
        self.artista = artista  # Artista da música
        self.duracao = duracao  # Duração da música em minutos
        self.anterior = None  # Referência para o nó anterior na lista
        self.proximo = None  # Referência para o próximo nó na lista


class ListaMusicas:
    """
    Classe para gerenciar a lista circular duplamente encadeada de músicas.
    Permite adicionar músicas, navegar pela lista e listar todas as músicas.
    """

    def __init__(self):
        self.cabeca = None  # Início da lista
        self.cauda = None  # Fim da lista

    def adicionar_musica(self, titulo, artista, duracao):
        """
        Adiciona uma nova música ao final da lista.
        """
        novo_no = NoMusica(titulo, artista, duracao)  # Cria um novo nó com os detalhes da música
        if not self.cabeca:  # Se a lista está vazia
            self.cabeca = novo_no
            self.cauda = novo_no
            novo_no.proximo = novo_no  # A lista é circular
            novo_no.anterior = novo_no
        else:  # Se a lista não está vazia
            novo_no.anterior = self.cauda
            novo_no.proximo = self.cabeca
            self.cauda.proximo = novo_no
            self.cabeca.anterior = novo_no
            self.cauda = novo_no

    def proxima_musica(self):
        """
        Avança para a próxima música na lista.
        """
        if self.cabeca:
            self.cabeca = self.cabeca.proximo  # Atualiza a cabeça para o próximo nó

    def musica_anterior(self):
        """
        Retrocede para a música anterior na lista.
        """
        if self.cabeca:
            self.cabeca = self.cabeca.anterior  # Atualiza a cabeça para o nó anterior

    def listar_musicas(self):
        """
        Lista todas as músicas na lista.
        """
        musicas = []
        if self.cabeca:
            atual = self.cabeca
            while True:
                musicas.append(f"{atual.titulo} - {atual.artista} ({atual.duracao} min)")
                atual = atual.proximo
                if atual == self.cabeca:
                    break
        return musicas


def menu_principal():
    """
    Função para executar o menu principal do sistema de reprodução de músicas.
    Permite ao usuário adicionar músicas, navegar entre elas e listar todas as músicas.
    """
    lista_musicas = ListaMusicas()  # Cria uma instância da lista de músicas
    opcoes = {
        '1': "Adicionar nova música",
        '2': "Listar todas as músicas",
        '3': "Próxima música",
        '4': "Música anterior",
        '0': "Sair"
    }

    while True:
        print("\nMenu Principal - Sistema de Reprodução de Músicas")
        for key, value in opcoes.items():  # Mostra as opções disponíveis no menu
            print(f"{key}. {value}")

        escolha = input("Escolha uma opção: ")  # Pede ao usuário para escolher uma opção

        if escolha == '1':  # Opção de adicionar nova música
            titulo = input("Digite o título da música: ")
            artista = input("Digite o artista da música: ")
            duracao = int(input("Digite a duração da música (em minutos): "))
            lista_musicas.adicionar_musica(titulo, artista, duracao)
            print("Música adicionada com sucesso!")

        elif escolha == '2':  # Opção de listar todas as músicas
            musicas = lista_musicas.listar_musicas()
            if musicas:
                print("\nLista de Músicas:")
                for musica in musicas:
                    print(musica)
            else:
                print("A lista de músicas está vazia.")

        elif escolha == '3':  # Opção de avançar para a próxima música
            if lista_musicas.cabeca:
                lista_musicas.proxima_musica()
                print(f"Avançado para a próxima música: {lista_musicas.cabeca.titulo} - {lista_musicas.cabeca.artista}")
            else:
                print("Não há próxima música, a lista está vazia.")

        elif escolha == '4':  # Opção de retroceder para a música anterior
            if lista_musicas.cabeca:
                lista_musicas.musica_anterior()
                print(
                    f"Retornando para a música anterior: {lista_musicas.cabeca.titulo} - {lista_musicas.cabeca.artista}")
            else:
                print("Não há música anterior, a lista está vazia.")

        elif escolha == '0':  # Opção de sair do sistema
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")

# Para executar o menu, descomente a linha abaixo após revisão.
menu_principal()