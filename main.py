from flask import Flask

from app.routes.login_routes import login
from config import Config

app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
app.secret_key = "super_secret_key"
app.config.from_object(Config)

app.register_blueprint(login)

app.run(host = "0.0.0.0", debug = True, port = "5000")