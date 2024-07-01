import yt_dlp as yt

class YoutubeVideoDownloader:
    def downloadbyurl(self,url,path,quality):
        self.url = url
        self.path = path
        self.quality = quality
        
        out = {
            "format" : self.quality,
            "outtmpl" : f"{self.path}/%(title)s.%(ext)s"
        }
        
        try:
            with yt.YoutubeDL(out) as yd:
                yd.download([self.url])
                print("video downloaded successfully")
        except Exception as e:
            print(f"an error occured :- {e}")