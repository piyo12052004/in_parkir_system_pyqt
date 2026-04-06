import psycopg2

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="app_parkir_local",
        user="",
        password=""  # ganti sesuai kamu
    )
    return conn