# # import requests
# # from flask import Flask, request
# # from pymessenger.bot import Bot
# #
# #
# # app = Flask(__name__)
# #
# #
# # ACCESS_TOKEN = 'EAAKqyQDZBZBPIBAOn1ODbcyFqaCNtGRTp1sxF17R9R39pVsOJeE11reJhPHykPSNv5NhZAfpCxRCopsxwWvawBPYi51h1kxuf72aoxEOyTaPU9KeEVREGD0FC0Ru5CRWZCcEWF2jUG2rZAN0qaZBMJaq2JuXEalf6lvTeyt35ql1R084ZBVGn38'
# # VERIFY_TOKEN = 'verysecrettoken'
# #
# # bot = Bot(ACCESS_TOKEN)
# #
# # get_first_last_name = requests.post('https://graph.facebook.com/<PSID>?fields=first_name,last_name&access_token=EAAKqyQDZBZBPIBAOn1ODbcyFqaCNtGRTp1sxF17R9R39pVsOJeE11reJhPHykPSNv5NhZAfpCxRCopsxwWvawBPYi51h1kxuf72aoxEOyTaPU9KeEVREGD0FC0Ru5CRWZCcEWF2jUG2rZAN0qaZBMJaq2JuXEalf6lvTeyt35ql1R084ZBVGn38')
# #
# #
# # print(get_first_last_name)
# #
#
#
# # a = [{'message': {'seq': 5464, 'text': 'Andrew sorry', 'mid': 'OInZ3ZvgbCtpS6VPGK1ATGiVJwWRDI92N2Qp2lqpiiTgGxGWyjUmBXDfgBg05WXTJz7HPb478FHJyBxHrfsZuw'}, 'sender': {'id': '2050314041686273'}, 'recipient': {'id': '1208269145995606'}, 'timestamp': 1541163042761}]
# #
# # # check = (a[0].get('message'))
# # #
# # # check_deeper = a[0]
# #
# # b = a[0]['message']['text']
# #
# # print(b)
#
# # payload = {'payload':{'template_type":"generic'},
# #     "elements":[
# #          {
# #           "title":"<TITLE_TEXT>",
# #           "image_url":"<IMAGE_URL_TO_DISPLAY>",
# #           "subtitle":"<SUBTITLE_TEXT>",
# #           "default_action": {
# #             "type": "web_url",
# #             "url": "<DEFAULT_URL_TO_OPEN>",
# #             "messenger_extensions": 'TRUE',
# #             "webview_height_ratio": "<COMPACT | TALL | FULL>"
# #           },
# #           "buttons": ['']}
# #            ],
# #            }
#
# from main_api import youtube_search
#
# test_c = {
#   "recipient":{
#     "id":"<PSID>"
#   },
#   "message":{
#     "attachment":{
#       "type":"template",
#       "payload":{
#         "template_type":"generic",
#         "elements":[
#            {
#             "title":"Welcome!",
#             "image_url":"https://petersfancybrownhats.com/company_image.png",
#             "subtitle":"We have the right hat for everyone.",
#             "default_action": {
#               "type": "web_url",
#               "url": "https://petersfancybrownhats.com/view?item=103",
#               "webview_height_ratio": "tall",
#             },
#             "buttons":[
#               {
#                 "type":"web_url",
#                 "url":"https://petersfancybrownhats.com",
#                 "title":"View Website"
#               },{
#                 "type":"postback",
#                 "title":"Start Chatting",
#                 "payload":"DEVELOPER_DEFINED_PAYLOAD"
#               }
#             ]
#           }
#         ]
#       }
#     }
#   }
# }
#
#
# curl -X POST -H "Content-Type: application/json" -d '{
#   "recipient":{
#     "id":"2050314041686273"
#   },
#   "message":{
#     "attachment":{
#       "type":"template",
#       "payload":{
#         "template_type":"generic",
#         "elements":[
#            {
#             "title":"Welcome!",
#             "image_url":" 'https://www.youtube.com/watch?v=8CdcCD5V-d8'",
#             "subtitle":"We have the right hat for everyone.",
#             "buttons":[
#               {
#                 "type":"web_url",
#                 "url":"https://www.youtube.com/watch?v=8CdcCD5V-d8",
#                 "title":"View Website"
#               },{
#                 "type":"postback",
#                 "title":"Start Chatting",
#                 "payload":"DEVELOPER_DEFINED_PAYLOAD"
#               }
#             ]
#           }
#         ]
#       }
#     }
#   }
# }' "https://graph.facebook.com/v2.6/me/messages?access_token=EAAKqyQDZBZBPIBAOn1ODbcyFqaCNtGRTp1sxF17R9R39pVsOJeE11reJhPHykPSNv5NhZAfpCxRCopsxwWvawBPYi51h1kxuf72aoxEOyTaPU9KeEVREGD0FC0Ru5CRWZCcEWF2jUG2rZAN0qaZBMJaq2JuXEalf6lvTeyt35ql1R084ZBVGn38"