from flask import Flask
from flask import jsonify
# json形式のファイルを使う部品

app = Flask(__name__)

@app.route("/")
def hello():
# json形式のデータは{}でかこう
    data = {
        "name": "Mito",
        "age": 43,
        "message": "Hello API"    
    }
    return jsonify(data)
# json形式のデータを返す
# 順不同で表示される

if __name__ == "__main__":
    app.run(debug=True)
