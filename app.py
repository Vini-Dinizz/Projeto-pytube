from pytube import YouTube, Playlist
from os import system
from time import sleep

def baixar_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(res=qualidade).first()
        print(20 * "=")
        print("Baixando video...")
        print(20 * "=")
        video.download("./midias")
        print("Concluido")
        print(20 * "=")
        sleep(5)
    except:
        print("Ocorreu algum problema. Tente novamente.")
        sleep(5)


def baixar_audio(url):
    try:
        audio = YouTube(url)
        print(20 * "=")
        print("Baixando audio...")
        audio.streams.get_audio_only().download("./midias", audio.title + ".mp3")
        print(20 * "=")
        print("Concluido")
        print(20 * "=")
    except:
        print("Ocorreu um erro. Tente novamente.")
        sleep(3)
    
def baixar_playlist(url):
    try:
        playlist = Playlist(url)
        for url in playlist:
            video_playlist = YouTube(url)
            stream_playlist = video_playlist.streams.get_highest_resolution()
            print("baixando playlist...")
            stream_playlist.download(output_path="playlist")
            print("Concluido")
            sleep(3)
    except:
        print("Ocorreu um problema. Tente novamente")
        sleep(3)


i = 1
j = 1

while j == 1:
    i = 1
    try:
        system("cls")
        print("Você deseja:")
        print("[1] Baixar video")
        print("[2] Baixar audio")
        print("[3] Baixar playlist")
        print("[4] Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            system("cls")
            url = input("url: ")
            print("Qualidades disponiveis: 144p, 240p, 360p, 480p, 720p, 1080p.")
            qualidade = input("qualidade: ")
            ytube = YouTube(url)
            desc = ytube.description
            print(50 * "=")
            print("Quer realmente baixar?")
            print(f"Titulo: {ytube.title}")
            print(f"Autor: {ytube.author}")
            print(f"Descrição: {desc}")
            print(f"Qualidade: {qualidade}")
            n = input("Digite s para sim, e n para não: ")
            if n == "s":
                baixar_video(url)
            elif n == "n":
                continue
            else:
                print(20 * "=")
                print("Digite uma das opções")
                sleep(5)
                continue

        elif escolha == "2":
            system("cls")
            url = input("url: ")
            ytube = YouTube(url)
            desc = ytube.description
            print(50 * "=")
            print("Quer realmente baixar?")
            print(f"Titulo: {ytube.title}")
            print(f"Autor: {ytube.author}")
            print(f"Descrição: {desc}")
            n = input("Digite s para sim, e n para não: ")
            if n == "s":
                baixar_audio(url)
            elif n == "n":
                continue
            else:
                print(20 * "=")
                print("Digite uma das opções")
                sleep(5)
                continue

        elif escolha == "3":
            system("cls")
            url = input("url: ")
            playlist = Playlist(url)
            print("Deseja realmente baixar?")
            numero = input("Digite s para sim, e n para não: ")
            if numero == "s":
                baixar_playlist(url)
            elif numero == "n":
                continue
            else:
                print(20 * "=")
                print("Digite uma das opções")
                sleep(3)
                continue

        elif escolha == "4":
            print("Saindo...")
            sleep(2)
            break

        else:
            print(20 * "=")
            print("Digite uma das opções")
            sleep(3)
            continue


        while i == 1:
            system("cls")
            print("[1] Menu")
            print("[2] Sair")
            opção = input("Escolha a opção: ")
            if opção == "1":
                i = 0
                continue
            elif opção == "2":
                j = 0
                print("Saindo...")
                sleep(2)
                break
            else:
                print("Digite uma das opções")
                sleep(2)
                continue

    except:
        print("Ocorreu algum erro. Tente novamente.")
        sleep(5)
        system("cls")
        continue