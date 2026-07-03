from flask import Flask
import os
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env (utile quando lavori in locale sul PC)
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "chiave_di_riserva")

@app.route('/')
def home():
    return "<h1>🚀 Sistema DYM Manager Online!</h1><p>Il server Flask è connesso e funzionante.</p>"

if __name__ == '__main__':
    # In locale girerà sulla porta 5000, su Render deciderà lui
    app.run(debug=True, port=5000)
