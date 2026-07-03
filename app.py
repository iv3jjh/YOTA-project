from flask import Flask
import os
import psycopg2
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env (solo per il PC locale)
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "chiave_di_riserva")

# Funzione per collegarsi al database
def get_db_connection():
    # Prende l'indirizzo dalla variabile d'ambiente (che sia locale o su Render)
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

@app.route('/')
def home():
    try:
        # Prova a connettersi e a chiedere la versione del database
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        
        # Chiude la connessione
        cur.close()
        conn.close()
        
        return f"<h1>🚀 Sistema DYM Manager Online!</h1><p>✅ Database connesso con successo: {db_version[0]}</p>"
    
    except Exception as e:
        return f"<h1>🚀 Sistema DYM Manager Online!</h1><p>❌ Errore di connessione al DB: {e}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
