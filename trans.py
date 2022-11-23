from flask import Flask, jsonify, request
from googletrans import Translator


app = Flask(__name__)
translator = Translator()


@app.route('/translator')
def trans():
    param1 = request.args.get('word', default='hello', type=str)
    param2 = request.args.get('lang', default='th', type=str)
    lang = translator.detect(param1).lang
    result = translator.translate(text=param1, src=lang, dest=param2)
    return jsonify({'result':str(result.text)})

if __name__ == "__main__":
    app.run(debug=True)