"""
Python script to get details of a Youtube video.
"""


import os
from pytube import YouTube


input_url = input("Enter URL of YouTube video: ")

yt = YouTube(input_url)


#Get details of the video
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")
print("Rating of video: ", yt.rating)
print("Highest Resolution stream available: ", yt.streams.get_highest_resolution())
print("Lowest Resolution stream available: ", yt.streams.get_lowest_resolution())