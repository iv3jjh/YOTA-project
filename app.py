from flask import Flask, render_template, request, session, redirect, url_for
import os
from werkzeug.security import check_password_hash
from dotenv import load_dotenv

# Importiamo dal nostro nuovo modulo!
from database import get_db_connection, init_db

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "chiave_di_riserva")

# Esegue il controllo del DB all'avvio dell'app usando la funzione importata
init_db()

# --- ROTTA DI LOGIN ---
@app.route('/', methods=['GET', 'POST'])
def login():
    if 'nominativo' in session:
        return redirect(url_for('dashboard'))

    errore = None
    
    if request.method == 'POST':
        nominativo_inserito = request.form.get('nominativo').upper()
        password_inserita = request.form.get('password')
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT password_hash, ruolo FROM utenti WHERE nominativo_privato = %s', (nominativo_inserito,))
        utente = cur.fetchone()
        cur.close()
        conn.close()
        
        if utente and check_password_hash(utente[0], password_inserita):
            session['nominativo'] = nominativo_inserito
            session['ruolo'] = utente[1]
            return redirect(url_for('dashboard'))
        else:
            errore ="Username or password incorrect."
            return render_template('login.html', errore=errore)
            
    return render_template('login.html', errore=errore)

# --- ROTTA DELLA DASHBOARD ---
@app.route('/dashboard')
def dashboard():
    if 'nominativo' not in session:
        return redirect(url_for('login'))

    return redirect(url_for('home'))

# --- ROTTA DI LOGOUT ---
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)