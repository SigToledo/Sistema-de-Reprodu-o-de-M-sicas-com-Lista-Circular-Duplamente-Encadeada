from ListaMusicas import ListaMusicas

def main_menu():
    playlist = ListaMusicas()  # Instancia uma nova lista de músicas.
    while True:
        # Exibe o menu principal no console.
        print("\nMENU PRINCIPAL")
        print("1 - Adicionar nova música")
        print("2 - Avançar para a próxima música")
        print("3 - Retroceder para a música anterior")
        print("4 - Listar todas as músicas")
        print("5 - Tocar Playlist")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")  # Solicita ao usuário para escolher uma opção.
        if opcao == "1":
            titulo = input("Digite o título da música: ")
            artista = input("Digite o nome do artista: ")
            duracao = int(input("Digite a duração da música (em minutos): "))
            playlist.adicionar_musica(titulo, artista, duracao)
            print("Música adicionada com sucesso!")
        elif opcao == "2":
            playlist.proxima_musica()
            print("Avançado para a próxima música.")
        elif opcao == "3":
            playlist.musica_anterior()
            print("Retrocedido para a música anterior.")
        elif opcao == "4":
            musicas = playlist.listar_musicas()
            print("Músicas na lista de reprodução:")
            for musica in musicas:
                print(musica)
        elif opcao == "5":
            print("Iniciando a reprodução da playlist:")
            current_track = playlist.head
            while True:
                print("\nTocando agora:")
                print(f"{current_track.titulo} - {current_track.artista} ({current_track.duracao} min)")
                print("\nOpções de reprodução:")
                print("P - Próxima música")
                print("V - Música anterior")
                print("S - Sair da reprodução")

                opcao_reproducao = input("Escolha uma opção de reprodução: ").upper()
                if opcao_reproducao == "P":
                    current_track = current_track.proximo
                elif opcao_reproducao == "V":
                    current_track = current_track.anterior
                elif opcao_reproducao == "S":
                    print("Encerrando a reprodução.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
