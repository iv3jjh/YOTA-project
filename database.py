import os
import psycopg2
from werkzeug.security import generate_password_hash

def get_db_connection():
    """Crea e restituisce la connessione al database PostgreSQL"""
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

def init_db():
    """Crea le tabelle se non esistono e inserisce l'admin di base"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Crea la tabella utenti
    cur.execute('''
        CREATE TABLE IF NOT EXISTS utenti (
            nominativo_privato VARCHAR(50) PRIMARY KEY,
            password_hash TEXT NOT NULL,
            ruolo VARCHAR(20) NOT NULL
        )
    ''')
    
    # Controlla se il tuo utente admin esiste già
    cur.execute("SELECT * FROM utenti WHERE nominativo_privato = 'IV3JJH'")
    admin = cur.fetchone()
    
    # Se non c'è, lo crea con una password provvisoria
    if not admin:
        pw_hash = generate_password_hash("admin123")
        cur.execute(
            "INSERT INTO utenti (nominativo_privato, password_hash, ruolo) VALUES (%s, %s, %s)",
            ('IV3JJH', pw_hash, 'admin')
        )
        
    conn.commit()
    cur.close()
    conn.close()