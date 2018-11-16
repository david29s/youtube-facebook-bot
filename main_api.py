import main_tts
from googleapiclient.discovery import build

DEVELOPER_KEY = 'AIzaSyA5f6jpo4TDJzYLUqVdKTphOlab8UnU_x4'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

voice_to_text_result = main_tts.result_text


def youtube_search(query=voice_to_text_result):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=query,
    part='id,snippet',
    maxResults=10
  ).execute()

  print(search_response.get('items', []))

  elements = []

  for search_result in search_response.get('items', []):
    print(search_result)
    if search_result['id']['kind'] == 'youtube#video':
        #print(search_result)

        elements.append(
                          {
                           "title":search_result['snippet']['title'] ,
                           "image_url": search_result['snippet']['thumbnails']['default']['url'],
                           "subtitle":search_result['snippet']['description'],
                           "buttons":[
                             {
                               "type":"web_url",
                               "url":"https://www.youtube.com/watch?v={}".format(search_result['id']['videoId']),
                               "title":"WATCH"
                             },
                           ]
                         }
    )

  print(len(elements), elements)
  return elements


