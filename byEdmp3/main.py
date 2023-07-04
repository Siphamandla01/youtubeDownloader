import tkinter
import customtkinter
import os
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink,on_progress_callback=on_progress)
        if combobox.get() == "Mp3":
            video = ytObject.streams.filter(only_audio=True).first()
            title.configure(text=ytObject.title, text_color="white")
            finishLabel.configure(text="")
            downloaded_file = video.download()
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
            finishLabel.configure(text = "Downloaded!")
        else:
            ytLink = link.get()
            ytObject = YouTube(ytLink,on_progress_callback=on_progress)
            video = ytObject.streams.get_highest_resolution()
            title.configure(text=ytObject.title, text_color="white")
            finishLabel.configure(text="")
            video.download()
            finishLabel.configure(text = "Downloaded!")
            
    except:
         finishLabel.configure(text = "Link is invalid, please check link and try again", text_color="red")
    

'''
def downloadmp4():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink,on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text = "Downloaded!")
    except:
         finishLabel.configure(text = "Link is invalid, please check link and try again", text_color="red")
         '''

def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completetion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completetion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    
    #Update progress bar
    progressBar.set(float(percentage_of_completetion / 100))

#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Please insert a youtube link here")
title.pack(padx=20,pady=20)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=450, height=40, textvariable=url_var)
link.pack()

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack()

#Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=20,pady=20)

#drop down menu
combobox = customtkinter.CTkComboBox(app,values=["Mp3", "Mp4"])
combobox.pack(padx=10, pady=5)

#download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=20, pady=10)

#mp4 download
#download = customtkinter.CTkButton(app, text="Download mp4", command=downloadmp4)
#download.pack(padx=20, pady=10)

#Run app
app.mainloop()