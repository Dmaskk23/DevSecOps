import time, os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Замість окремого HTML файлу, повернемо простий рядок для економії часу
    return render_template ("index.html")

@app.route('/convert')
def convert():
    # Перевірка наявності секретного ключа (імітація вимог безпеки)
    api_key = os.getenv('EXCHANGE_API_KEY')
    if not api_key:
        return jsonify({"status": "ERROR", "message": "Secret EXCHANGE_API_KEY is missing!"}), 500
    
    print(f"Using API Key: {api_key[:3]}***")
    
    # Імітація затримки при зверненні до зовнішнього API курсів валют
    time.sleep(0.5)
    
    # Повертаємо умовний курс
    return jsonify({
        "status": "SUCCESS", 
        "data": {"USD_to_UAH": 38.50, "EUR_to_UAH": 41.20}
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)