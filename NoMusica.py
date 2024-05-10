class NoMusica:
    """
    Representa um nó em uma lista circular duplamente encadeada de músicas.
    Armazena informações sobre a música e mantém referências para os nós anterior e próximo.
    """
    def __init__(self, titulo, artista, duracao):
        # Inicialização das propriedades do nó com informações específicas da música.
        self._titulo = titulo  # Título da música.
        self._artista = artista  # Artista da música.
        self._duracao = duracao  # Duração da música em minutos.
        self._anterior = None  # Inicializa a referência ao nó anterior como None.
        self._proximo = None  # Inicializa a referência ao próximo nó como None.

    # Getters e Setters para cada atributo para controle de acesso e modificação.
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def artista(self):
        return self._artista

    @artista.setter
    def artista(self, value):
        self._artista = value

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, value):
        self._duracao = value

    @property
    def anterior(self):
        return self._anterior

    @anterior.setter
    def anterior(self, value):
        self._anterior = value

    @property
    def proximo(self):
        return self._proximo

    @proximo.setter
    def proximo(self, value):
        self._proximo = value
