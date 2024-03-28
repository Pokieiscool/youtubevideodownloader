import tkinter
import customtkinter
from pytube import YouTube

# Youtube/Pytube Library 

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:        
        finishLabel.configure(text="Download Error", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    per = str(int(percentage))
    progress.configure(text=per + '%')
    progress.update()

    progressbar.set(float(percentage) / 100)

#system settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Framework

app = customtkinter.CTk()
app.geometry("720x480")
app.title("DerpyStudios Downloader")

#UI Elements Basics
title = customtkinter.CTkLabel(app, text="Insert Youtube Link Here")
title.pack(padx=50, pady=50)

#Input

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Download

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Progress

progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)



#Post Download

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#loop
app.mainloop()

#Updated for Release v15.0.0
