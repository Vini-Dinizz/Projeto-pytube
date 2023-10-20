from pytube import YouTube
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

i = 1
j = 1

while j == 1:
    i = 1
    try:
        system("cls")
        url = input("url: ")
        print("Qualidades disponiveis: 144p, 240p, 360p, 480p, 720p, 1080p.")
        qualidade = input("qualidade: ")
        ytube = YouTube(url)
        desc = ytube.description
        print(50 * "=")
        print("Quer realmente baixar este video?")
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


        while i == 1:
            system("cls")
            print("[1] Baixar video")
            print("[2] Sair")
            opção = input("Escolha a opção: ")
            if opção == "1":
                i = 0
                continue
            elif opção == "2":
                j = 0
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