import tkinter as tk
import pytube
from pytube import YouTube
from youtube_downloader import YoutubeDownloader
import threading
import os
import requests
import time


class Window:
    def downloading(self):
        """ Downloads a YouTube video when the user clicks the 'Download' button. Checks for an internet connection,
        verifies the video link, creates a YoutubeDownloader object, and downloads the video on a separate thread.

        Args:
            None

        Returns:
            None
        """

         # zkontroluje zda je uživatel připojen k internetu
        try:
            requests.get("http://www.google.com", timeout=5)
        except requests.ConnectionError:
            self.error_label.config(text="No internet connection, close the window and reconnect")
            return
        

        url = self.link.get()
        
        try:
            yt = YouTube(url)
        except pytube.exceptions.VideoUnavailable:
            #když video není již k dispozici
            self.error_label.config(text="Video unavailable for download") 
            return
        except:
            self.error_label.config(text="This is not a link from https://www.youtube.com/")
            return
        
        downloader = YoutubeDownloader(url)

       
        
        try:
            #blokování tlačítka ke stahování dalšího videa
            self.download_button.config(state="disabled") 
            self.download_thread = threading.Thread(target=downloader.download_video)
            self.download_thread.start()

            #kontroluje připojení k internetu stále při stahování
            while self.download_thread.is_alive():
                time.sleep(5)
                try:
                    requests.get("http://www.google.com", timeout=5)
                except requests.ConnectionError:
                    self.error_label.config(text="Internet connection lost")
                    self.download_thread._stop()
                    break

        except:
            #když dojde k chybě
            self.error_label.config(text="Error downloading video") 
            #odblokuje tlačítko 
            self.download_button.config(state="normal") 
            return
        
        self.error_label.config(text="Video download successfully")
        self.download_button.config(state="normal")

    #metoda k vytvoření grafického okna
    def __init__(self):
        """Creates a graphical window with an input field, an error label, and a download button. The user can insert a 
        YouTube link and click the download button to initiate the download.

        Args:
            None

        Returns:
            None
        """
        root = tk.Tk()
        displaywindow = tk.Canvas(root, width=400, height=200, relief='raised')
        displaywindow.pack()
        label1 = tk.Label(root, text= 'Insert a link from YouTube')
        label1.config(font=('times new roman', 20))
        displaywindow.create_window(200, 25, window=label1)
        self.link = tk.Entry(root)
        self.link.config(width=50)
        displaywindow.create_window(200, 100, window=self.link)

        self.error_label = tk.Label(root, text="")
        self.error_label.config(fg="red")
        displaywindow.create_window(200, 120, window=self.error_label)

        self.download_button = tk.Button(text="Download", command=self.downloading, bg='black', fg='white', font=('times new roman', 12))
        displaywindow.create_window(200, 180, window=self.download_button)

        root.mainloop()

        
    
