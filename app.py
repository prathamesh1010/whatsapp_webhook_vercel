from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        verify_token = "prathamesh10"  # <-- your token
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token == verify_token:
            return challenge
        return "Error, invalid token", 403

    if request.method == 'POST':
        data = request.json
        print("Received webhook data:", data)
        return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(debug=True)
