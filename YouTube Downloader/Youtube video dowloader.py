from pytube import YouTube
link = input("enter the link of youtube video: ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download("Video scaricati")
print("download completato!")