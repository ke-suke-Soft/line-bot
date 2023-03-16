from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE Developers ConsoleでアクセストークンとChannel Secretを設定し、Webhook URLを指定する
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証に必要な値を取得する
    signature = request.headers['X-Line-Signature']

    # リクエストボディを取得する
    body = request.get_data(as_text=True)

    # LINE Developers Consoleで設定したWebhookの認証を行う
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
