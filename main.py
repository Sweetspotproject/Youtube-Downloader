from pytube import Youtube


def Download(link):
    youtubeObject = Youtube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ha ocurrido un error en la descarga de tu video")
        print("Tu descarga fue completada!!!")


link = input("Inserta el link del video: ")
Download(link)
