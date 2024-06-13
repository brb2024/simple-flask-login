import os

class Config:
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "templates")
    STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "static")
    DIRECCION_BD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "database", "bd.sqlite3")