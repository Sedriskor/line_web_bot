from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('g1ahi5iZy4fSr/8oYFXgqDFoovc6qnixrFAUcQiqK7TKbxNDHN2SZ9q/htPCDE7CIzag/nDCPBTtyphwA1dWSwxvsyDwVQZDz64p+mubxm3xEArWSxEKx9/vdv95rXVrFhTXtobBo+sVfJWcwwcXwwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('564dcc8ae23b0d4e76d1e6c11a8e2828')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '尼供3小'

    if msg in ['hi', 'Hi']:
        r = '嗨'
    elif msg == '尼吃了嗎':
        r = '沒'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()