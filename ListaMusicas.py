from NoMusica import NoMusica

class ListaMusicas:
    """
    Gerencia uma lista circular duplamente encadeada de músicas.
    Permite adicionar músicas, navegar para frente e para trás e listar todas as músicas.
    """
    def __init__(self):
        self.head = None  # Cabeça da lista, aponta para o nó atual.
        self.start = None  # Ponto de início da lista, mantém a referência ao primeiro nó adicionado.

    def adicionar_musica(self, titulo, artista, duracao):
        new_node = NoMusica(titulo, artista, duracao)  # Cria um novo objeto NoMusica.
        if not self.head:
            # Se a lista está vazia, estabelece o novo nó como head e start.
            self.head = self.start = new_node
            new_node.proximo = new_node.anterior = new_node
        else:
            # Insere o novo nó no final da lista.
            tail = self.start.anterior
            tail.proximo = new_node
            new_node.anterior = tail
            new_node.proximo = self.start
            self.start.anterior = new_node

    def proxima_musica(self):
        if self.head:
            self.head = self.head.proximo  # Move a cabeça para o próximo nó.

    def musica_anterior(self):
        if self.head:
            self.head = self.head.anterior  # Move a cabeça para o nó anterior.

    def listar_musicas(self):
        musicas = []
        if self.start:
            current = self.start
            while True:
                tocando = "->" if current == self.head else "  "
                musicas.append(f"{tocando} {current.titulo} - {current.artista} ({current.duracao} min)")
                current = current.proximo
                if current == self.start:
                    break
        return musicas
