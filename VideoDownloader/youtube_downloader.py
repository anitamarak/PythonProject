import os
from pytube import YouTube
import ssl

class YoutubeDownloader:
   """
    A class used to download YouTube videos using the PyTube library.

    Attributes
    ----------
    url : str
        The URL of the YouTube video to download.
    slozka : str
        The name of the directory to save the downloaded video file in.
    yt : pytube.YouTube
        A PyTube YouTube object representing the video to download.

    Methods
    -------
    get_highest_resolution_stream()
        Get the highest resolution stream available for the video.
    download_video()
        Download the video to the specified directory.
    """
def __init__(self, url, slozka='Downloads'):
    """
        Constructs all the necessary attributes for the YoutubeDownloader object.

        Parameters
        ----------
        url : str
            The URL of the YouTube video to download.
        slozka : str, optional
            The name of the directory to save the downloaded video file in. Default is 'Downloads'.
        
        Raises
        ------
        ValueError
            If an invalid YouTube video URL is provided.
    """
    self.url = url
    self.slozka = os.path.join(os.getcwd(),slozka)
    os.makedirs(self.slozka, exist_ok=True)
    try:
        self.yt = YouTube(url)
    except:
        raise ValueError("Invalid YouTube video URL")

def get_highest_resolution_stream(self):
        """
        Get the highest resolution stream available for the video.

        Returns
        -------
        pytube.Stream
            A PyTube Stream object representing the highest resolution stream available.
        """
        #předchází chybám při ověřování certifikátu SSL
        ssl._create_default_https_context = ssl._create_unverified_context  
        return self.yt.streams.get_highest_resolution()
    
    #stáhne video pomocí metody get_highest_resolution_stream
def download_video(self):  
        """
        Download the video to the specified directory.

        Raises
        ------
        ValueError
            If there is an error downloading the video.
        """
        stream = self.get_highest_resolution_stream()
        soubor = self.yt.title + '.mp4'
        try:
            stream.download(output_path=self.slozka, filename=soubor)
        except:
            raise ValueError("Error downloading video")
        
    