from flask import current_app
import sqlite3

class LoginServices:

    def __init__(self):
        self.dir_bd = current_app.config["DIRECCION_BD"]

    def crear_tablas(self):
        con = sqlite3.connect(self.dir_bd)
        cursor = con.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuario_login(
                id_usuario INTEGER PRIMARY KEY NOT NULL,
                usuario TEXT NOT NULL UNIQUE,
                pass TEXT NOT NULL
            );
        """)

        con.commit()
        con.close()

    def agregar_usuario(self, nombre, passw):
        con = sqlite3.connect(self.dir_bd)
        cursor = con.cursor()

        try:
            cursor.execute("""
                INSERT INTO usuario_login (usuario, pass) VALUES (?, ?)
            """, (nombre, passw))

            con.commit()
        except sqlite3.DatabaseError as e:
            print(e)
        finally:
            con.close()

    def obtener_usuario(self, usuario, passw):
        con = sqlite3.connect(self.dir_bd)
        cursor = con.cursor()
        usuario_log = ""

        try:
            cursor.execute("""
                SELECT * FROM usuario_login WHERE usuario = ? AND pass = ?;
            """, (usuario, passw))
            
            usuario_log = cursor.fetchall()
            print(usuario)
        except sqlite3.DatabaseError as e:
            print(e)
        finally:
            con.close()

        return usuario_log

