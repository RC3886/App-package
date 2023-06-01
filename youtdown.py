import time
from pytube import YouTube


class YoutubeDownloader:                # class with a link as an attribute
    def __init__(self, link=None):
        self.link = link

    def download(self):
        youtube_mode = True
        while youtube_mode:
            user_input = input("Enter a video link or press 0 to go back to the menu. ")
            if user_input == "0":
                break
            else:
                self.link = user_input
                yt = YouTube(self.link)
                yd = yt.streams.get_highest_resolution()
                start_time = time.time()
                print("Please wait while the video is being downloaded.")
                yd.download("E:\\Downloads")
                end_time = time.time()
                print(f"The video was downloaded within {end_time-start_time} seconds")




"""
class YoutubeDownloader:                # class with a link as an attribute
    def __init__(self, link):
        self.link = link

    def resolution(self):
        yt = YouTube(self.link)
        streams = yt.streams
        resolutions = set()             # empty set that will be filled with results, no duplicates
        for stream in streams:
            resolution = stream.resolution
            if resolution is None:
                resolution = "Unknown"  # changing None result to "Unknown"
            resolutions.add(resolution)
        for res in resolutions:
            print("Resolution:", res)

    def download(self):
        YouTube(self.link).streams[0].download()

    def show_streams(self):
        yt = YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0&ab_channel=officialpsy')
        print(yt.streams)


youtubedownloader = YoutubeDownloader("https://www.youtube.com/watch?v=9bZkp7q19f0&ab_channel=officialpsy")
youtubedownloader.resolution()
youtubedownloader.show_streams()
# youtubedownloader.download()
"""