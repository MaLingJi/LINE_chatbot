from flask import Flask, request, abort, send_file

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import os.path
import sys
import json
import requests

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

DIALOGFLOW_CLIENT_ACCESS_TOKEN = '15838659c7bd49d793ae9b00c9ab2c4b' #dialogflow的

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('1G23hDKeaHReGjaM9quXdjuyTLs6tTN43YvimfTxeuWSEHqRenOFGh43U0UVZftawXIYGAqdx4fWrQ7jz4bEnxDrVzod4pq5WQ27C7F31Tr46wwvYkh+NimiQtABBfTwHPJoxym3mVqmJl0AqSy9bAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('57fc53ff7d035209b3c30dc8c096b0a1')
ai = apiai.ApiAI('15838659c7bd49d793ae9b00c9ab2c4b')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # print("into callback")
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    print("\n")
    app.logger.info("Request body: " + body)
    # print("\n\nbody : " + body + "\nsignature : " + signature + "\n\n")
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# @handler.add(MessageEvent)
# def hello(event):
#     print("into hello")
#     user_id = event.source.user_id

#     # line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Hello!"))
#     # line_bot_api.push_message(user_id, TextSendMessage(text='Hello World!'))
#     if event.message.text.upper() == "IN":
#         try:
#             with open("user_id.txt", 'r') as fd:

#                 if user_id + "\n" in fd:
#                     line_bot_api.push_message(user_id, TextSendMessage(text='user id already exist.'))
#                 else:
#                     line_bot_api.push_message(user_id, TextSendMessage(text='user id record.'))
#                     with open("user_id.txt", 'a') as fd:
#                         fd.write(user_id + "\n")
#         except FileNotFoundError:
#             with open("user_id.txt", 'w') as fd:
#                 line_bot_api.push_message(user_id, TextSendMessage(text='user id record.'))
#                 fd.write(user_id + "\n")


# # 處理訊息
# # @handler.add(MessageEvent, message=TextMessage)
# @handler.add(BeaconEvent)
# def handle_message(event):
#     typ = event.type
#     print("-----------event------------")
#     print(event)

#     tds0 = int(event.beacon.dm[0:3], 16)
#     tds1 = int(event.beacon.dm[3:6], 16)
#     date = event.beacon.dm[6:8]
#     hall = int(event.beacon.dm[8:12], 16)
#     power = int(event.beacon.dm[12:14], 16)

#     if tds1 <= 40:
#         status = "正常"
#     elif tds1 <= 60:
#         status = "普通"
#     else:
#         status = "異常"

#     textc = "type : " + typ + "\nBeacon type" + event.beacon.type + "\ndm : " + event.beacon.dm + "\nTDS0 : " + str(tds0) + "\nTDS1 : " + str(tds1) + "\nHALL : " + str(hall) + "\nPOWER : " + str(power) + "\n濾芯狀況" + status + "\n淨化前:{0} >> 淨化後:{1}".format(tds0, tds1)






    
#     message = TextSendMessage(text = textc)
#     print("\n")
#     # message = ImageSendMessage(
#     #     original_content_url='http://res.cloudinary.com/demo/image/upload/w_250,h_250,c_fill,f_auto/seagull.jpg',
#     #     preview_image_url='http://res.cloudinary.com/demo/image/upload/w_250,h_250,c_fill,f_auto/seagull.jpg'
#     # )
#     line_bot_api.reply_message(event.reply_token, message)
#     # line_bot_api.push_message(event.source.userId, TextSendMessage(text='Hello World!'))


if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, port = 80)
