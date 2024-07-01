from url import YoutubeVideoDownloader
from title import YoutubeDownload


def main():
    print("WELCOME")
    while True:
        option = input("Do you want audio/video from YouTube? (y/n)").lower()
        if option == "y":
            try:
                choice = int(input("Do you want to download by (1) title or (2) URL?"))
                if choice in [1, 2]:
                    if choice == 1:
                        title = input("Enter the title of the video to download: ")
                        path = input("Enter the path to save the video (e.g., c:\\folder\\..): ")
                        quality = input("Choose the quality of the video (worst/best): ")
                        if quality.lower() in ["worst", "best"]:
                            download = YoutubeDownload()
                            download.downloadbytitle(title, path, quality)
                        else:
                            print("Please enter a valid quality (worst/best).")
                                       
                    elif choice == 2:
                        url = input("Enter the url of the video to download: ")
                        path = input("Enter the path to save the video (e.g., c:\\folder\\..): ")
                        quality = input("Choose the quality of the video (worst/best): ")
                        if quality.lower() in ["worst", "best"]:
                            download = YoutubeVideoDownloader()
                            download.downloadbyurl(url, path, quality)
                        else:
                            print("Please enter a valid quality (worst/best).")
                            
                    else :
                        print("please enter valid choice")
                        
                else:
                    print("Please enter a valid choice (1 or 2).")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif option == "n":
            print("THANK YOU")
            break
        else:
            print("Please enter a valid option (y/n).")
            

if __name__ == "__main__":
    main()