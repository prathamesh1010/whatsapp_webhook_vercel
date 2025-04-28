from flask import Flask, request, Response

app = Flask(__name__)
VERIFY_TOKEN = 'prathamesh10'

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    if (request.args.get('hub.mode') == 'subscribe' and
        request.args.get('hub.verify_token') == VERIFY_TOKEN):
        print('Webhook verified!')
        return request.args.get('hub.challenge'), 200
    return Response(status=403)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.get_json()
    print('Received:', data)
    return Response(status=200)

if __name__ == '__main__':
    app.run(port=3000)