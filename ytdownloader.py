# install py#tube by using pip install pytube
from pytube import Youtube
from sys import argv

link = argv[1]
yt = Youtube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yt.download('/Users/kp/Desktop/fela/languages/python/download')