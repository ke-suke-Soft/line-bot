from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
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
