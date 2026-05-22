from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False 

@app.route('/')
def hello():
    return jsonify({
        "статус": "ОК",
        "сообщение": "Привет! Это веб-приложение успешно работает в Docker-контейнере.",
        "автор": "Артём Фёдоров"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
