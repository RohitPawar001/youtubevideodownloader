import yt_dlp as yt

class YoutubeDownload:
    def downloadbytitle(self,title,path,quality):
        self.title = title
        self.path = path
        self.quality = quality
        
        out_ydl = {
            "format":self.quality,
            "outtmpl":f"{self.path}/%(title)s.%(ext)s",
            
        }
        
        with yt.YoutubeDL(out_ydl) as yd:
            search_results = yd.extract_info(f"ytsearch:{self.title}",download =False)
            results = search_results.get("entries",[None])[0]
            
            if results:
                url = results.get("webpage_url")
                title = results.get("title")
                
                if url:
                    print(f"downloading {self.title}")
                    try:
                        yd.download([url])
                    except Exception as e:
                        print(f"error downloading: {e}")
                else:
                    print("url not found, hrrs we got")
                    print(results)
            else:
                print(f"we cant find the video you are looking for {self.title}")