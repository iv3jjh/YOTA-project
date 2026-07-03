from flask import Flask, render_template, request
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "chiave_di_riserva")

def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

# Aggiungiamo methods=['GET', 'POST'] per permettere al form di inviare dati
#@app.route('/', methods=['GET', 'POST'])
#def home():
  #  if request.method == 'POST':
        # Qui cattureremo i dati inviati dal form
   #     nominativo_inserito = request.form.get('nominativo')
    #    password_inserita = request.form.get('password')
        
        # Per ora stampiamo solo un messaggio di test
     #   return f"<h1>Test Login</h1><p>Hai provato ad accedere come: {nominativo_inserito}</p>"
    
    # Se il metodo è GET (l'utente sta solo visitando la pagina), mostriamo l'HTML
render_template('fpage.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
