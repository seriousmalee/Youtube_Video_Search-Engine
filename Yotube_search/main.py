from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

#Api key
DEVELOPER_KEY= "AIzaSyB43CdT3qGIGvBH_AYKhnoW4jfkec4y6-c"
YOUTUBE_API_NAME = "youtube"
YOUTUBE_API_VER=    "v3"


def youtube_search(keyword,max_result = 5):
    youtube= build(YOUTUBE_API_NAME,YOUTUBE_API_VER,developerKey= DEVELOPER_KEY)
    try:
        search_respon = youtube.search().list(q=keyword,
                                              part="id,snippet",maxResults=max_result).execute()
        videos=[]
        for search_result in search_respon.get("items",[]):
            if search_result["id"]["kind"]== "youtube#video":
                video = {"title":
                         search_result["snippet"]["title"],"description":
                         search_result["snippet"]["description"],"video_id":
                         search_result["id"]["videoId"],"thumbnail":
                         search_result["snippet"]["thumbnails"]["default"]["url"]
                         }
                videos.append(video)
                return videos
    except HttpError as e:
        print("HTTP hatası {0}:{1}".format(e.resp.status,e.content))


#anahtar kelime
keyword = input("Aramak istediğin kelimeyi giriniz")
results = youtube_search(keyword)

#sonuç

for video in results:
    print("Başlık:",video["title"])
    print("Açıklama:",video["description"])
    print("Video ID:",video["video_id"])
    print("Thumbnail URL:",video["thumbnail"])
    print("-----------------------------------")







