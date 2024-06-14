# install py#tube by using pip install pytube
from pytube import YouTube
from sys import argv
import urllib.error

link = argv[1]
try:
    yt = YouTube(link)

    print("Title: ", yt.title)

    print("View: ", yt.views)
    
    print("Length of the video (in seconds):", yt.length)

    yd = yt.streams.get_highest_resolution()

    yt.download('/Users/kp/Desktop/fela/languages/python/download')
except urllib.error.HTTPError as e:
    if e.code == 410:  # HTTP Error 410: Gone
        print("Video is private or unavailable:", link)
    else:
        print("Error occurred while processing the video:", e)